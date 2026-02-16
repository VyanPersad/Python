from readFunction import read_from_file
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
from MerchMath import marginOnCost

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\BuyerSalesHistory.csv'

def calcDisc(cP, sP, margin):
    disc =sP-((cP/(1-margin))*1.125)
    return disc

df = read_from_file(filepath=file_path, test=0)

df = df.rename(columns=
              {'Stock On Hand':'Stock', 'Average Weighted Cost': 'Cost', 'Cash Price': 'Price'}
              )
df['Cost'] = df['Cost'].round(2)
df['Margin'] = df.apply(lambda row: marginOnCost(row['Cost'], row['Price'],VAT=12.5), axis=1).round(2)

df['Disc'] = np.where(df['Margin'] > 0.25, calcDisc(df['Cost'], df['Price'], .25), 0).round(-2)

df['Now Price'] = df['Price'] - df['Disc'].round(-2)
df['Now Price'] =df['Now Price'].round(0)

df['New Mrgn'] = df.apply(lambda row: marginOnCost(row['Cost'], row['Now Price'], VAT=12.5), axis=1).round(2)

df['Price'] = df['Price'].round(3)
df_filtered = df[
    (df['Year'] == 'This Year') &
    (df['Brand'] == 'SAMSUNG') &
    (df['Margin'] > 0.25) &
    (df['Stock'] > 10)
]
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df_filtered[['Sku', 'Brand', 'Description', 'Cost', 'Price', 'Margin', 'Disc',
'Now Price', 'New Mrgn', 'Stock']].sort_values(by='Stock', ascending=False))