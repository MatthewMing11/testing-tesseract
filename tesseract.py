import pytesseract
from pdf2image import convert_from_path

#update paths if downloaded in other locations
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pages = convert_from_path("Sample Discharge Summary_0.pdf",
                          poppler_path=r"C:\Program Files\poppler-26.02.0\Library\bin")

for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page)
    print(f"Page {i+1}")
    print(text)
