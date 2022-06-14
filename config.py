import os

class Config(object):
	DEBUG = False
	TESTING = False

	SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "")
	DB_NAME = "production-db"
	UPLOADS = "/home/upload"
	SESSION_COOKIE_SECURE = True
	PDF_UPLOADS = "/var/www/p2d/app/app/static/img/uploads"
	CLIENT_DOCS = "/var/www/p2d/app/app/static/img/client/doc"
	ALLOWED_EXTENSIONS = ["PDF"]
	MAX_FILESIZE = 3000000
class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG = True
	DB_NAME = "development-db"
	UPLOADS = "/home/upload"

	SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
	TESTING = True
	DB_NAME = "development-db"
	UPLOADS = "/home/upload"

	SESSION_COOKIE_SECURE = False
