from calendar import Month

from readFunction import read_from_file
import pandas as pd
import datetime as dt

from writeFunctions import write_to_csv

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\Arriving_Soon.xlsx'
arrival_list = 'arrivals'

df = read_from_file(filepath=file_path, test=0)

filter_df = df[['STATUS', 'RWT', 'ETA', 'CONTAINER#', 'SUPPLIER', 'DESCRIPTIONS']]

date = pd.to_datetime(filter_df['ETA'], errors='coerce')
curr_mon = dt.datetime.now().month

filter_df['ETA'] = date.dt.date
filter_df['Month'] = date.dt.month.astype('Int64')
filter_df['Year'] = date.dt.year.astype('Int64')

search_terms = 'TV|SoundBar|Audio|Speaker|Home Theater|Projector|Monitor|Display|Screen|Mini-System|Gaming|Console|PS5'

test = filter_df[
    (filter_df['Year'] >= 2026)
    &
    (filter_df['DESCRIPTIONS'].str.contains(search_terms, case=False, na=False))
    #&
    #(filter_df['Month'] >= curr_mon)
    ]
test = test.sort_values(by='Month', ascending=True)
#print(test)

write_to_csv(test, r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data', arrival_list)
