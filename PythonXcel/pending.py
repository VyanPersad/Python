from readFunction import read_from_file
import datetime as dt
import pandas as pd

this_yr = dt.datetime.now().year
curr_mon = dt.datetime.now().month
last_mon = curr_mon - 1
next_mon = curr_mon + 1


file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\Raw_Data\Raw_Data\Reportes Courts.xls'
df = read_from_file(filepath=file_path, test=0)
major_Filter = df[
                  (df['Department'].str.contains('VIDEO', na=False)) |
                  (df['Department'].str.contains('AUDIO', na=False)) |
                  (df['Department'].str.contains('GAMING', na=False))
                  ]

grouped_df = major_Filter[['Class', 'Brand', 'Code Courts', 'Model','Description','PO','Expected Delivery Date','Pending']]

date_df = grouped_df[
    (grouped_df['Expected Delivery Date'].dt.year == this_yr) 
    & 
    ((grouped_df['Expected Delivery Date'].dt.month == curr_mon)
    |
    (grouped_df['Expected Delivery Date'].dt.month == last_mon)
    |
    (grouped_df['Expected Delivery Date'].dt.month == next_mon))
    ]
print(date_df.head(10))

file_path_2 = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\Arriving_Soon.xlsx'
df_2 = read_from_file(filepath=file_path_2, test=0)
filter_df = df_2[['STATUS', 'RWT', 'ETA', 'CONTAINER#', 'SUPPLIER', 'DESCRIPTIONS']].copy()
date = pd.to_datetime(filter_df['ETA'], format='%d-%b-%Y',errors='coerce')

filter_df['ETA'] = date.dt.date
filter_df['Month'] = date.dt.month.astype('Int64')
filter_df['Year'] = date.dt.year.astype('Int64')

search_terms = 'TV|SoundBar|Audio|Speaker|Home Theater|Projector|Monitor|Display|Screen|Mini-System|Gaming|Console|PS5'

arrival_df = filter_df[
    (filter_df['Year'] >= 2026)
    &
    (filter_df['DESCRIPTIONS'].str.contains(search_terms, case=False, na=False))
    &
    (filter_df['Month'] >= last_mon)
    ]

arrival_df = arrival_df.sort_values(by='Month', ascending=True)
print(arrival_df.head(10))

'''
with open("test_output.txt", 'w') as file:
    for row in arrival_df.to_string(index=False):
        file.write(row)
        '''