from readFunction import read_from_file
import pandas as pd
from xlsxwriter import Workbook
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime as dt

curr_date = dt.datetime.now().strftime('%d.%m.%Y')

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

table = Loc_Name.pivot_table(
                       index='SKU', 
                       columns='LocationName', 
                       values='StockOnHand', 
                       aggfunc=sum,
                       fill_value=0,
                       margins=True,
                       margins_name='Total'
                       )

to_print = r'Data\Combined_Current_Distribution_{curr_date}.xlsx'
with pd.ExcelWriter(to_print, engine='xlsxwriter') as writer:
    table.to_excel(writer, sheet_name='CurrDist')

    max_row = table.shape[0]
    max_col = table.shape[1]

    wrkbook = writer.book
    worksheet = writer.sheets['CurrDist']
    worksheet.autofilter(0, 0, max_row, max_col)

    red_fill = wrkbook.add_format({
        'bg_color': '#FFC7CE',
        'font_color': '#9C0006'
    })

    header_format = wrkbook.add_format({
        'bold': True,
        'rotation': 90,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })

    cond_format = {
        'type':     'cell',
        'criteria': '>',
        'value':    1,
        'format':   red_fill
    }

    for col_num, value in enumerate(table.columns.values):
        worksheet.write(0, col_num + 1, value, header_format)
        worksheet.conditional_format(1, col_num + 1, max_row, max_col, cond_format)

