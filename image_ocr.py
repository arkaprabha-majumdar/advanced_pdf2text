import easyocr

reader = easyocr.Reader(['en'])

def image_ocr(image):
    return reader.readtext(image)