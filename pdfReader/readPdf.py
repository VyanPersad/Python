import pdfplumber, os, re, math

pdf_path =r"C:\Users\Vyan\Downloads\Servicio_GIS\AUG_2025_TCL"
dest_file = open('AUG_TCL.csv', 'a')

cleaned_tables = []
inv_tables=[]
brand_tables=[]

Servicio_bBox = (475,25,550,75)
bounding_box = (0,210,605,625)
'''
This first defines the area of the PDF that will be looked at to extract the data for the tables. 

The Dimension specified for the bounding box Represent the left boundary the upper boundary the right boundary and the lower boundary of the area to be selected. Essentially the 475 stipulate the left boundary or specifically the distance from the left boundary where the rectangle will start the 25 stipulates the upper boundary or the distance from the top of the document The 550 stipulates the right hand boundary of the bounding box from the left hand side of the document and the 75 stipulates the lower edge of the bounding box as measured from the top of the document. Essentially in this the upper left hand corner of the document would be the 00 origin point.
'''
for file in os.listdir(pdf_path):
    try:
        if file.endswith('.pdf'):
            print(f"Processing file: {file}")
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
                    "text_tolerance":2,
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
    except Exception as e:
        continue
        '''
        The code below now begins the process of iterating through all the tables now 4 every rule in the table we I want to extract certain pieces of information.

        Given the nature of what was extracted a fair of cleaning is required and so the next few lines of code perform those operations over all the characters within the row wherever we see certain combinations of text and symbols they are replaced with blanks Where we see commas or possibly dashes they are also replaced with blanks.
        '''
    for table in all_tables:   
        for row in table:
            cleaned_row=[]
            cleaned_row_qty = []
            brand_Arr=[]
            cleaned_item = ''
            for item in row:
                if item is not None:
                    cleaned_item = re.sub(r'\(cid:\d+\)','',item).strip() 
                    cleaned_item = cleaned_item.replace('US$','')  
                    cleaned_item = cleaned_item.replace(' - ','')
                    cleaned_item = cleaned_item.replace(',','')
                #if "/" in cleaned_item:
                #   cleaned_item = cleaned_item.split('/')
                if cleaned_item != '':
                    cleaned_row.append(cleaned_item) 
            '''
            The Bro that is being clean is temporarily assigned the variable of Clean item then a cleaned item is subsequently reattached to a new array known as clean going forward this array with the cleaned roofs will be the array that is used for the rest of the operations.

            So long as the clean room is not empty which is to say that it has a particular value we can that by using citizen selection criteria we can further clean and further the individual columns of the rule and make replacements as needed as well as performing mathematical calculations to get the values we want for the final table.

            It is important to note I went to forming mathematical competitions we have to ensure that the values that are read from the table are in the appropriate numerical format this case we had to convert it to a float.
            '''        
            if cleaned_row !=[]:
                try:
                    if len(cleaned_row)>2:
                        '''
                        The notation listed below is very specific and can save you quite a lot of time. What is happening here is that the first term is being spit into two parts the first part being zero and the second part being the one. From this we then indicate which of the two elements we require by the of the term in the aarray.

                        Similarly we do it for the third element in the which would have an index of 2 and we wish to split that into three of which we will take the third and further split that using the / as a delimiter.
                        '''
                        cleaned_row[0:1] = cleaned_row[0].split(' ', maxsplit=1)
                        cleaned_row[2:3] = cleaned_row[2].split('/', maxsplit=1)
                        for item in cleaned_row:
                            if item == '': 
                                cleaned_row.remove(item)
                        
                        cleaned_row.append(round(float(cleaned_row[4].replace(',', '').strip())*10,2))
                        cleaned_row.append(round(((math.ceil(((cleaned_row[5]*-1.125)/(0.25-1))/100))*100)-1,0))
                        cleaned_row.insert(0,rwt_No)
                        cleaned_tables.append(cleaned_row)
                    
                    elif len(cleaned_row)==2:
                        cleaned_row_qty = cleaned_row[0] 
                        brand_Arr = [cleaned_row[1].split()[0]]
                        brand_tables.append(brand_Arr)
                        inv_tables.append(cleaned_row_qty)
                
                    print(cleaned_row)
                except Exception as e:
                    print(f"Error processing row {rwt_No}: {e}")
                            

print(len(inv_tables))
print(len(cleaned_tables))
print(len(brand_tables))

dest_file.write('RWT_No,Model,Item_Desc,UPC,Courts_Code,US_Unit_Price,EST_Landed_TTD,EST_Price_w_Mrgn25,QTY,Brand\n')
for n in range(0, len(cleaned_tables),1):
    row=cleaned_tables[n]
    dest_file.write(','.join(map(str, row)) +','+str(inv_tables[n])+','+str(brand_tables[n][0])+'\n')


dest_file.close()

'''
We use the plumber library opening a PDF file and then we define the table settings. These settings done so we can specifically tell the library how we want the data to be read Moving across horizontally or are we moving across horizontally and chopping the data vertically in this we want the data to be defined by a series of vertical lines as we want to split the data into by setting it to explicit we can then go on to specify the points at which we want the vertical lines to be drawn in this instance 480 and 540 taking note to remember that the leftmost boundary of the document is zero. 

Next point is the horizontal strategy We know for a fact that the data we are extracting will be largely in the text format so we indicate text however when it comes to text tolerance and minimum widths in the horizontal there may be a certain amount of trial and error to properly determine which of the numerical settings gives us the result that we want at this point it is a good time to print the The contents of the table to console so you can see where the split is occurring and how the library is interpreting the data that is being read.

Depending on the table and the bounding box that is used we can specify any number of vertical lines explicitly so that we have greater granular control over where the data is split and subsequently the specific columns that are created and the data that is put into the resective tables.

After this we specify which of the pages of the document we wish to have this acted on as it is with many things in Python the pages are stored as elements of an array therefore indicating the zeroth term of the array Will give us the first page of the document.

By using the crop function we can now crop the document to the specific bonding box this helps because it narrows down the area over which the software on the library has to act reducing the detection of terms that could potentially be misread.

We then call the extract tables function the Specifically cropped areas and this extracts the data and puts it into the form of a table. It is at this point where we specify the table settings we previously talked about earlier that would help in chopping the data up as needed.
'''