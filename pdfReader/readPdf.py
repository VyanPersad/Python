import pdfplumber, os

pdf_path =r"C:\Users\Vyan\Downloads\PDF_297161_68367377.pdf"
#dest_file = open('test.csv', 'a')
all_tables = []
cleaned_tables = []
bounding_box = (0,210,612,625)
#for file in os.listdir(pdf_path):

with pdfplumber.open(pdf_path) as pdf:

        table_settings = {
            "vertical_strategy":"explicit",
            "explicit_vertical_lines":[0, 45, 330, 465, 545, 612],
            "horizontal_strategy":"text",
            "text_tolerance":2,
            "min_words_horizontal":1,
        }
        pg = pdf.pages[0]
        pg_crp = pg.crop(bounding_box)
        pg_crp.to_image().debug_tablefinder(table_settings=table_settings).show()
        tables = pg_crp.extract_tables(table_settings=table_settings)
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

print(cleaned_tables)    
#for row in cleaned_tables:
#   dest_file.write(f"{",".join(row)}\n")

#dest_file.close()
