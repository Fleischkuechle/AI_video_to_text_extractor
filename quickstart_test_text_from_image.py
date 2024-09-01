try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os

self_filepath=os.path.dirname(os.path.abspath(__file__))
tesseract_exe_rel_path=r"\tesseract_ocr\tesseract.exe"

tesseract_path=self_filepath+tesseract_exe_rel_path

image_name:str='quickstart_test.png'

image_path:str=os.path.join(self_filepath,image_name)
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = tesseract_path
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open(image_path)))

# French text image to string
print(pytesseract.image_to_string(Image.open(image_path), lang='fra'))

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open(image_path)))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open(image_path)))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open(image_path)))