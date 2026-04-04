from readFunction import read_from_file
import pandas as pd
from xlsxwriter import Workbook
import matplotlib.pyplot as plt
import datetime as dt

curr_date = dt.datetime.now().strftime('%d.%m.%Y')

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\STOCK QUERY FILE.xlsx'

df = read_from_file(filepath=file_path, test=0, sheet=5)

Loc_Name = df['LocationName'].unique()
 
Loc_Name = df[
    (df['SKU'].str.startswith('T') == False)
    &
    (df['SKU'].str.startswith('O') == False)
    ]

table = Loc_Name.pivot_table(
                       index=['SKU','PosDescription'], 
                       columns='LocationName', 
                       values='StockOnHand', 
                       aggfunc='sum',
                       fill_value=0,
                       margins=True,
                       margins_name='Total'
                       )

locs =[tot for tot in table.columns if tot != 'Total']
loc_rnk = table.iloc[:-1][locs].sum().sort_values(ascending=False).index
table = table[list(loc_rnk) + ['Total']]

index_count = len(table.index.names)
print(index_count)

to_print = fr'Data\Combined_Current_Distribution_{curr_date}.xlsx'
with pd.ExcelWriter(to_print, engine='xlsxwriter') as writer:
    table.to_excel(writer, sheet_name='Summary')

    max_row = table.shape[0]
    max_col = table.shape[1]

    wrkbook = writer.book
    worksheet = writer.sheets['Summary']
    worksheet.autofilter(0, 0, max_row, max_col)

    gray_fill = wrkbook.add_format({
        'bold': True,
        'bg_color': "#BFBFBF",
        'font_color': "#000000",
        'align': 'center',
    })

    header_format = wrkbook.add_format({
        'bold': True,
        'rotation': 90,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })

    index_format = wrkbook.add_format({
        'bold': True,
        'align': 'left',
        'valign': 'vcenter',
        'border': 1
    })

    col_format = wrkbook.add_format({
        'bold': False, 
        'align': 'left'
    })

    cell_format = wrkbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })

    cond_format = {
        'type':     'cell',
        'criteria': '>',
        'value':    1,
        'format': gray_fill
    }

    worksheet.set_column(0,0, 20, col_format)
    worksheet.set_column(1,1, 70, col_format)

    worksheet.write(0,0, 'SKU', index_format)
    worksheet.write(0,1, 'PosDescription', index_format)   

    for col_num, value in enumerate(table.columns.values):
        worksheet.write(0, 0, value, index_format)
        worksheet.write(0, 1, value, index_format)

        worksheet.conditional_format(1, col_num + index_count, max_row, col_num + index_count, cond_format)

print("File writing completed")