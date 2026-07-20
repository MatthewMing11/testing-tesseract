import pytesseract
from pdf2image import convert_from_path

#update paths if downloaded in other locations
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pages = convert_from_path("Sample Discharge Summary_0.pdf",
                          poppler_path=r"C:\Program Files\poppler-26.02.0\Library\bin")

total_text=""
for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page)
    total_text+=text
    print(f"Page {i+1}")
    print(text)
print(total_text)
total_text_list=total_text.split("\n")
data_dict={}
for text in total_text_list:
    if ":" in text:
        entry=text.split(":")
        field_name=entry[0]
        field_value=entry[1].strip()
        data_dict[field_name]=field_value
print(data_dict)
#clean up name
data_dict["Patient Name"]= " ".join(reversed(data_dict["Patient Name"].split(",")))

import csv
fields=["Patient Name","Patient Number","Date Admitted","Date Discharged","Symptoms","Type of Discharge","Condition on Discharge","Prognosis","Disposition","Physical Activity","Dietary Instructions","By"]
with open("output.csv","w") as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerow({field: data_dict[field] for field in fields})
        
