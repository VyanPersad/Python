from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from io import StringIO
import os

pdf_path =r"C:\Users\Vyan\Downloads\AUG_2025_TCL"
dest_file = open('test.csv', 'a')
all_tables = []
cleaned_tables = []
output_string = StringIO()
for file in os.listdir(pdf_path):

    with open(os.path.join(pdf_path, file), 'rb') as pdf:

        parser = PDFParser(pdf)
        document = PDFDocument(parser)
        resourceMngr = PDFResourceManager()
        device = TextConverter(resourceMngr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(resourceMngr, device)

        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            text = output_string.getvalue()
            print(text)
    
        output_string.getvalue()
     
    print(output_string)
