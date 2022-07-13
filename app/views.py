from app import app

from flask import render_template, request, redirect, jsonify, make_response, send_from_directory, abort

import os

from werkzeug.utils import secure_filename

from pdf2docx import Converter
import subprocess

@app.route ("/")
def index():
	print(app.config["DB_NAME"])
	return render_template("public/index.html")

@app.route ("/profile")
def profile():
	return render_template("public/profile.html")

@app.route ("/json", methods=["POST"])
def json():
	if request.is_json:
		req = request.get_json()
		response = {
			"message": "JSON received",
			"name": req.get("name")
		}
		res = make_response(jsonify(response),200)

		return res

	else:
		res = make_response(jsonify({"message": "No JSON received"}),400)
		return res

def allowed_format(filename):
	if not "." in filename:
		return False

	ext = filename.rsplit(".", 1)[1]

	if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
		return True
	else:
		return False

def allowed_filesize(filesize):

	if request.content_length <= app.config["MAX_FILESIZE"]:
        	return True
	else:
                return False

def convert_pdf_to_doc(input_file, output_file):

	cv = Converter(input_file)
	cv.convert(output_file)
	cv.close()
	print("Output saved")

def convert_to_pptx(input_file):
	subprocess.run(["pdf2pptx", input_file])
	print("pptx created")

@app.route ("/upload", methods=["GET", "POST"])
def upload():
	if request.method == "POST":
		if request.form.get('submit_button') == 'convert to .doc':

			if not  allowed_filesize(request.content_length):
				print("File exceeded maximum size")
				return redirect(request.url)
			pdf = request.files["pdf"]

			if pdf.filename == "":
				print("File must have a filename")
				return redirect(request.url)

			if not allowed_format(pdf.filename):
				print("That file extension is not allowed")

			else:
				filename = secure_filename(pdf.filename)
				pdf.save(os.path.join(app.config["PDF_UPLOADS"], filename))
				print('File uploaded')
				input_path = os.path.join(app.config["PDF_UPLOADS"], filename)
				output_file = filename.split(".")[0]+".doc"
				output_path = os.path.join(app.config["CLIENT_DOCS"], output_file)
				convert_pdf_to_doc(input_path, output_path)
				print("File converted to doc")

				return redirect("/get-doc/{}".format(output_file))
			return render_template("public/upload.html")

		elif request.form.get('submit_button') == 'convert to .pptx':
			pdf = request.files["pdf"]
			filename = secure_filename(pdf.filename)
			input_path = os.path.join(app.config["PDF_UPLOADS"], filename)
			output_file = filename.split(".")[0]+".pptx"
			output_path = os.path.join(app.config["CLIENT_DOCS"], output_file)
			convert_to_pptx(input_path)
			print("File converted to pptx")
			return redirect("/get-doc/{}".format(output_file))
			return render_template("public/upload.html")

		else:
			return redirect(request.url)
	elif  request.method == 'GET':
		return render_template("public/upload.html")

@app.route ("/get-doc/<doc_name>")
def get_doc(doc_name):
	try:
		return send_from_directory(app.config["CLIENT_DOCS"],
		filename=doc_name, as_attachment=True)

	except FileNotFoundError:
		abort(404)
