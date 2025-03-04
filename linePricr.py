import pandas as pd

def read_from_file(filepath, test=0, n=5, col_Names = [], sheet = 0):
    filetype = filepath.split('.')[1]
    #This will read the csv and display the first 5 rows of the data.
    if (filetype == 'csv'):
        if (col_Names == []):
            dataFrame = pd.read_csv(filepath)
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell python to use the ; as the spearator.
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
            elif (test == 1):
                print(dataFrame.head(n))
        elif (col_Names != []):
            dataFrame = pd.read_csv(filepath, names=col_Names)
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell python to use the ; as the spearator.
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
            elif (test == 1):
                print(dataFrame.head(n))

        return dataFrame

    elif (filetype == 'xlsx'):
        xlFile = pd.ExcelFile(filepath)  
        sheetName = xlFile.sheet_names[sheet]
        dataFrame = xlFile.parse(f'{sheetName}')
        if (test == 0):
            print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the numbe rof rows.')
        elif (test == 1):
            print(dataFrame.head(n))

        return dataFrame

xl_src = 'Vision Audio Bank Noms_MAR_2025.xlsx'

priceList = read_from_file(xl_src, test=1, n=5,sheet=0)
'''col_Names=["PRODUCT CODE", "BRAND", "Model", "WAS PRICE"]'''

priceList_mod = priceList[["PRODUCT CODE", "Class", "BRAND", "Model", "WAS PRICE"]]
priceList_mod['WAS PRICE'] = priceList_mod['WAS PRICE'].astype(float).round(2)
priceList_mod = priceList_mod.sort_values(by='WAS PRICE', ascending=True)
print(priceList_mod.head(5))

search_term = r'32'
search = priceList_mod[priceList_mod['Class'].str.contains(search_term, case=False, na=False)]
print(search)