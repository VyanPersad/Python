from readFunction import read_from_file
import pandas as pd
import datetime as dt

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\STOCK QUERY FILE.xlsx'
curr_date = dt.datetime.now().strftime('%d.%m.%Y')


df = read_from_file(filepath=file_path, sheet=3, test=0)
#print(df)

stor_List = df['LocationName'].unique()
sku_list = df['SKU'].unique().tolist()

code_filter = df[
    (df['SKU'].str.startswith('T') == False)
    |
    (df['SKU'].str.startswith('O') == False)
    |
    (df['SKU'].str.startswith('R') == False)
]
category_filter = code_filter[
    (code_filter['SKU'].str.startswith(('1','2')))
]  
brnd_fltr = category_filter[
    (category_filter['Brand'] == 'SAMSUNG') 
    | 
    (category_filter['Brand'] == 'LG')
]

table = brnd_fltr.pivot_table(
                       index=['SKU','Brand','PosDescription'], 
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

to_print = fr'Data\Inv_Rpt_{curr_date}.xlsx'
with pd.ExcelWriter(to_print, engine='xlsxwriter') as writer:
    table.to_excel(writer, sheet_name='Summary')

    max_row = table.shape[0]
    max_col = table.shape[1]

    wrkbook = writer.book
    worksheet = writer.sheets['Summary']
    worksheet.autofilter(0, 0, max_row, max_col)

    header_format = wrkbook.add_format({
        'font_size': 8,
        'bold': True,
        'rotation': 90,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })

    index_format = wrkbook.add_format({
        'font_size': 8,
        'bold': True,
        'align': 'left',
        'valign': 'vcenter',
        'border': 1
    })

    col_format = wrkbook.add_format({
        'font_size': 8,
        'bold': False, 
        'align': 'left'
    })

    worksheet.set_column(0,0, 15, col_format)
    worksheet.set_column(1,1, 15, col_format)
    worksheet.set_column(2,2, 70, col_format)

    worksheet.write(0,0, 'SKU', index_format)
    worksheet.write(0,1, 'Brand', index_format)
    worksheet.write(0,2, 'PosDescription', index_format)   

    for col in range (3, max_col):
        worksheet.set_column(col, col, 15, col_format)
        worksheet.write(0, col, table.columns[col], header_format)

print('Report generated successfully!')