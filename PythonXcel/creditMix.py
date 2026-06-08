from readFunction import read_from_file
import pandas as pd
import datetime as dt

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\CreditMixReport_Month.xlsx'

df = read_from_file(filepath=file_path,test=0, sheet=4)
df = df[['itemno','itemdescr1','datedel','Department','Brand','quantity'
]]
total_item_df = []
day = df['datedel'].dt.day
month = df['datedel'].dt.month
df = df.assign(day=day, month=month)
df = df[(df['Department'] == 'VISION')&(df['itemno'] == '10612F')]
df['total_quantity'] = df.groupby(['itemno','itemdescr1','Brand'])['quantity'].transform('sum')
df= df.drop_duplicates(subset=['itemno'])
print(df)