import pdfplumber, os, re

pdf_path =r"C:\Users\Vyan\Downloads\AUG_2025_TCL"
dest_file = open('test.csv', 'a')
all_tables = []
cleaned_tables = []
inv_tables=[]
calc_tables = []
Servicio_bBox = (475,25,550,75)
bounding_box = (0,210,612,625)
for file in os.listdir(pdf_path):

    with pdfplumber.open(os.path.join(pdf_path, file)) as pdf:
            ser_table_settings = {
                "vertical_strategy":"explicit",
                #This defines the vertical lines to be used to split the text into columns.
                #TThe left and right bounds of the text.
                "explicit_vertical_lines":[480, 540],
                "horizontal_strategy":"text",
                "text_tolerance":15,
                "min_words_horizontal":1,
            }
            table_settings = {
                "vertical_strategy":"explicit",
                "explicit_vertical_lines":[0, 25,45, 330, 465, 545, 612],
                "horizontal_strategy":"text",
                "text_tolerance":1,
                "min_words_horizontal":1,
            }
            pg = pdf.pages[0]
            pg_crp = pg.crop(bounding_box)
            #pg_crp.to_image().debug_tablefinder(table_settings=table_settings).show()
            ser_Crop = pg.crop(Servicio_bBox)
            #ser_Crop.to_image().debug_tablefinder(table_settings=ser_table_settings).show()
            all_tables = pg_crp.extract_tables(table_settings=table_settings)
            rwt_No=ser_Crop.extract_table(table_settings=ser_table_settings)[0]
            rwt_No = "".join(rwt_No)
            #all_tables.insert(0,rwt_No)
            #print(rwt_No)
            #print(all_tables)

    for table in all_tables:   
        for row in table:
            cleaned_row=[]
            cleaned_row_qty = []
            cleaned_item = ''
            for item in row:
                if item is not None:
                    cleaned_item = re.sub(r'\(cid:\d+\)','',item).strip() 
                    cleaned_item = cleaned_item.replace('US$','')  
                #if "/" in cleaned_item:
                #   cleaned_item = cleaned_item.split('/')
                if cleaned_item != '':
                    cleaned_row.append(cleaned_item) 
                    
            if cleaned_row !=[]:
                if len(cleaned_row)>2:
                    cleaned_row[0:1] = cleaned_row[0].split(' ', maxsplit=1)
                    cleaned_row[2:3] = cleaned_row[2].split('/', maxsplit=1)
                    for item in cleaned_row:
                        if item == '': 
                            cleaned_row.remove(item)
                    cleaned_row.append(round(float(cleaned_row[4])*10,2))
                    cleaned_row.append(round((cleaned_row[5]*-1.125)/(0.25-1),0))
                    cleaned_row.insert(0,rwt_No)
                    cleaned_tables.append(cleaned_row)
                
                elif len(cleaned_row)==2:
                    cleaned_row_qty = cleaned_row[0] 
                    inv_tables.append(cleaned_row_qty)

#print(cleaned_tables)
print(len(inv_tables))
print(len(cleaned_tables))

for n in range(0, len(cleaned_tables),1):
    row=cleaned_tables[n]
    dest_file.write(','.join(map(str, row)) + ','+str(inv_tables[n])+'\n')

dest_file.close()
