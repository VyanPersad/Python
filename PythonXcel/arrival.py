from calendar import Month

from readFunction import read_from_file
import pandas as pd
import datetime as dt

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\Arriving_Soon.xlsx'

df = read_from_file(filepath=file_path, test=0)

filter_df = df[['STATUS', 'RWT', 'ETA', 'CONTAINER#', 'SUPPLIER', 'DESCRIPTIONS']]

date = pd.to_datetime(filter_df['ETA'], errors='coerce')

filter_df['ETA'] = date.dt.date
filter_df['Month'] = date.dt.month.astype('Int64')
filter_df['Year'] = date.dt.year.astype('Int64')

search_terms = 'TV|SoundBar|Audio|Speaker|Home Theater|Projector|Monitor|Display|Screen|Mini-System'

test = filter_df[
    (filter_df['Year'] >= 2026)
    &
    (filter_df['DESCRIPTIONS'].str.contains(search_terms, case=False, na=False))
    ]
test = test.sort_values(by='Month', ascending=True)
print(test)
