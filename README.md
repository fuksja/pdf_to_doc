<h1 align="center"> pdf_to_doc</h1>


[pdf_to_doc]( https://github.com/fuksja/pdf_to_doc) is a project to construct a simple web page, allowing a user to easily convert a pdf document into editable doc one.

## Contents
- [Author](#author)
- [Requirements and limitations](#requirements)
- [Getting started](#getting-started)
- [Time frame](#time-frame)
- [Documentation](#documentation)
- [License and copyright notice](#license)

## Author
- [Basia Lewicka aka fuksja](https://github.com/fuksja)

## Requirements and Limitations

Stakeholder requirements: there is a need for a tool for fast and automated conversion of not editable pdf documents to editable .doc format.

General description of fuctionality: user goes to the upload page, uploads a pdf file, conversion takes place and user receives doc file as output.

EDIT: added new functionality: conversion to .pptx format. User uploads file and chooses whether to convert to .doc or .pptx  

### Assumptions: 
- the project will only be using open source software and will be open software licensed  
- no conversion of encrypted files for now  
- all pages converted as default
- custom max file size limitation 
- no special security features
- simple conversion from pdf to .pptx as images put in slides, no strings OCRed

### Limitations:

- english language version for now
- no security features, user profiles, login option, session control, simple file input and output for now
- for conversion to doc format:  
    limitations derived from conversion method and library [pdf2doc](https://pypi.org/project/pdf2docx/):
    - text based files  
    - language from left to right  
    - no rotation possible
    - no 1:1 layout conversion achievable
- for conversion to .pptx format: 
    limitations derived from conversion method and library [pdf2pptx](https://pypi.org/project/pdf2pptx/):
    - each original file page rendered as a PNG image and input into a Powerpoint slide
    - slides not editable, no OCR - but may be presented as slides

## Getting started

- chosen language/method: Python3 and flask
- chosen method of file conversion: 
    - pdf2docx 0.5.3 library: https://pypi.org/project/pdf2docx/
    - pdf2pptx 1.0.5 library: https://pypi.org/project/pdf2pptx/

## Time frame
First part of the project completed in June 2022. Second part, with addition of .pptx feature completed in July. Project will be updated in the future.

## Documentation

This github repository serves as projects documentation.

## License and copyright notice
This project uses GPLv3 license and MIT license. Part of this project is derived from other software, created by other programmers, community or made in different way also under the  GNU General Public License v3.0:

[Source of pdf2docx library used for file conversion to .doc](https://github.com/dothinking/pdf2docx)  
[License](https://github.com/dothinking/pdf2docx/blob/master/LICENSE)

[Source of pdf2pptx library used for file conversion to .pptx](https://github.com/kevinmcguinness/pdf2pptx)  
[License](https://github.com/kevinmcguinness/pdf2pptx/blob/master/LICENSE)  
