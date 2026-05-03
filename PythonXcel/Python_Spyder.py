# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from readFunction import read_from_file


file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\BuyerSalesHistory.csv'
file_path2 = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\Inventory_V.xlsx'

df = read_from_file(filepath=file_path, test=0)
df2 = read_from_file(filepath=file_path2, sheet = 1 ,test=0)
df2 = df2.rename(columns={'SKU':'Sku', 'BRAND':'Brand', 'DESC':'Description'})

TY_df = df[(df['Year'] == 'This Year')]
LY_df = df[(df['Year'] == 'Last Year')]

merged_df = TY_df.merge(df2, on='Sku', how='outer')
print(merged_df)
