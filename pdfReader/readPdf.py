import pdfplumber, os

pdf_path =r"C:\Users\Vyan\Downloads\AUG_2025_TCL"
dest_file = open('test.csv', 'a')
all_tables = []
cleaned_tables = []
for file in os.listdir(pdf_path):

    with pdfplumber.open(os.path.join(pdf_path, file)) as pdf:

        table_settings = {
            "vertical_strategy":"text",
            "horizontal_strategy":"text",
            "text_tolerance":10,
            "min_words_horizontal":1,
        }
        pg = pdf.pages[0]

        tables = pg.extract_tables(table_settings=table_settings)
        [2,3,4,6,9]
        #print(tables) 
        for table in tables:
            #print(table)
            all_tables.append(table)
 
'''
for table in all_tables:
    for row in table:
        for i in range(len(row)):
            for item in row:
                if item == '' or item is None or item == ' ':
                    row.remove(item)
        if row is not None:
            print(row)
'''
for table in all_tables:    
    for row in table:
        cleaned_row=[]
        for item in row:
            if item != '':
                cleaned_row.append(item)
        if cleaned_row != []:
            cleaned_tables.append(cleaned_row)        
    
for row in cleaned_tables:
    dest_file.write(f"{",".join(row)}\n")

dest_file.close()
