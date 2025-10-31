from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path as needed

img = Image.open('img_1.jpg')
extract_text = pytesseract.image_to_string(img)
print(extract_text)