from flask import Flask, render_template, request, redirect
from PIL import Image
import pytesseract
import os
import io
from pdf2image import convert_from_path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def ocr_text():
    files = request.files.getlist('file')
    limit = request.form.get('limit')
    text = ""
    for file in files:
        if file.filename.endswith(('pdf','jpg','jpeg','png','tiff')):
            if file.filename.endswith('pdf'):
                pages = convert_from_path(file, 500, first_page=0, last_page=int(limit))
                for page in pages:
                    img_io = io.BytesIO()
                    page.save(img_io, 'JPEG')
                    img_io.seek(0)
                    image = Image.open(img_io)
                    text += pytesseract.image_to_string(image)
            else:
                image = Image.open(file)
                text += pytesseract.image_to_string(image)
    return text
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)