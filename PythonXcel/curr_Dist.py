from readFunction import read_from_file
import pandas as pd
from xlsxwriter import Workbook
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\STOCK QUERY FILE.xlsx'

df = read_from_file(filepath=file_path, test=0, sheet=5)

#print(df)
Loc_Name = df['LocationName'].unique()
 
Loc_Name = df[
    (df['LocationName'].str.startswith('O') == False)
    &
    (df['SKU'].str.startswith('T') == False)
    &
    (df['SKU'].str.startswith('O') == False)
]

Loc_Name = Loc_Name['Model No.']

table = Loc_Name.pivot_table(index='SKU', 
                       columns='LocationName', 
                       values='StockOnHand', 
                       aggfunc=sum,
                       fill_value=0,
                       margins=True,
                       margins_name='Total'
                       )
to_print = r'Data\Current_Dist.xlsx'
with pd.ExcelWriter(to_print, engine='xlsxwriter') as writer:
    table.to_excel(writer, sheet_name='CurrDist')

    max_row = table.shape[0]
    max_col = table.shape[1]

    wrkbook = writer.book
    worksheet = writer.sheets['CurrDist']
    worksheet.autofilter(0, 0, max_row, max_col)

    header_format = wrkbook.add_format({
        'bold': True,
        'rotation': 90,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })

    for col_num, value in enumerate(table.columns.values):
        worksheet.write(0, col_num + 1, value, header_format)

