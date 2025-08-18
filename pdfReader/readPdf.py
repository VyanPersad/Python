import pdfplumber, os, re

pdf_path =r"C:\Users\Vyan\Downloads\PDF_297161_68367377.pdf"
dest_file = open('test.csv', 'a')
all_tables = []
cleaned_tables = []
calc_tables = []
bounding_box = (0,210,612,625)
for file in os.listdir(pdf_path):

    with pdfplumber.open(os.join(pdf_path, file)) as pdf:

            table_settings = {
                "vertical_strategy":"explicit",
                "explicit_vertical_lines":[0, 45, 330, 465, 545, 612],
                "horizontal_strategy":"text",
                "text_tolerance":2,
                "min_words_horizontal":1,
            }
            pg = pdf.pages[0]
            pg_crp = pg.crop(bounding_box)
            #pg_crp.to_image().debug_tablefinder(table_settings=table_settings).show()
            all_tables = pg_crp.extract_tables(table_settings=table_settings)

    for table in all_tables:    
        for row in table:
            cleaned_row=[]
            cleaned_item = ''
            for item in row:
                if item is not None:
                    cleaned_item = re.sub(r'\(cid:\d+\)','',item).strip() 
                    cleaned_item = cleaned_item.replace('US$','')  
                #if "/" in cleaned_item:
                #   cleaned_item = cleaned_item.split('/')
                if cleaned_item != '':
                    cleaned_row.append(cleaned_item) 
            if cleaned_row != [] and len(cleaned_row)>1:
                cleaned_row[0:1] = cleaned_row[0].split(' ', maxsplit=1)
                cleaned_row[2:3] = cleaned_row[2].split('/', maxsplit=1)
                cleaned_row[3:4] = cleaned_row[3].split(' ', maxsplit=1)
                cleaned_row[5:6] = cleaned_row[5].split(' ', maxsplit=1)
                for item in cleaned_row:
                    if item == '': 
                        cleaned_row.remove(item)
                cleaned_tables.append(cleaned_row)        

    for row in cleaned_tables:
        print(row)

    for row in cleaned_tables:
        dest_file.write(f"{",".join(row)}\n")

dest_file.close()
