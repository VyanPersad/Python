import pandas as pd
import numpy as np
import html5lib
import os

def write_to_csv(dataFrame, destpath, file_name):
    return dataFrame.to_csv(f'{destpath}/{file_name}.csv', index=False)

#This will only be used for outputting an Excel file with one sheet.
def write_to_xl(dataFrame, destpath, file_name, sheet_name = '1'):
    return dataFrame.to_excel(f'{destpath}/{file_name}.xlsx', sheet_name=sheet_name, index=False)

#If you had to output a file that had multiple sheets you would probably use the function below.
def write_to_xl_mul(dataFrame, destpath, file_name, sheet_name = '1'):
    folderpath = f'{destpath}/{file_name}.xlsx'
    if os.path.exists(folderpath):
        with pd.ExcelWriter(f'{destpath}/{file_name}.xlsx', engine='openpyxl',mode='a') as writer:
            dataFrame.to_excel(writer, sheet_name, index=False)
        return print("Path Exists")
    else:
        with open(folderpath, 'w') as file:
            print("Path does not exist creating....")
            dataFrame.to_excel(f'{destpath}/{file_name}.xlsx', sheet_name=sheet_name, index=False)
