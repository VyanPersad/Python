import pandas as pd
import numpy as np
import os


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
        xlFile = pd.ExcelFile(filepath, engine='openpyxl')  
        sheetName = xlFile.sheet_names[sheet]
        dataFrame = xlFile.parse(f'{sheetName}')
        if (test == 0):
            print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the numbe rof rows.')
        elif (test == 1):
            print(dataFrame.head(n))

        return dataFrame

def testFunc(dataFrame, test=0, n=5):
    if (test == 0):
        print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
    elif (test == 1):
        print(dataFrame.head(n)) 

def makeFolder(folderpath):
    if os.path.exists(folderpath):
        return print("Path Exists")
    else:
        os.makedirs(folderpath)
        print("Path does not exist creating....")