import pdfplumber

pdf_path =r"C:\Users\Vyan\Downloads\PDF_296429_68297599.pdf"

with pdfplumber.open(pdf_path) as pdf:
    all_tables=[]

    for page in pdf.pages:
        #text = page.extract_text()
        #print(text)
        tables = page.extract_tables()
        for table in tables:
            print(table)

    table_settings = {
        "vertical_strategy":"text",
        "horizontal_strategy":"text",
        "text_tolerance":10,
        "min_words_horizontal":3,
    }
    pg = pdf.pages[0]

    tables = pg.extract_tables(table_settings=table_settings)
    [2,3,4,6,9]
    print(tables[0][15]) 
 

