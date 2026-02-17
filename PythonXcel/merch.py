import os
from readFunction import read_from_file
from writeFunctions import write_to_xl, write_to_xl_mul
import pandas as pd

support_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\JAN DELIVERED SALES 2026.xlsx'
#df = read_from_file(filepath=support_path, test=0)
df = read_from_file(filepath=support_path, test=0)

#print(df)
#items =[(brand, model no, start day, end day, rebate amount)]
items = [('SAMSUNG','UN50CU7090PXPA',19,31,95),
        ('SAMSUNG','QN65Q7FAAPXPA',19,31,171)
        ]

brand = df['Item Description'].str.split(' ').str[0]
model_no = df['Item Description'].str.split(' ').str[1]
day = df['Item Delivery Date'].str.split('/').str[0].astype('Int64')
month = df['Item Delivery Date'].str.split('/').str[1].astype('Int64')

Model_No_df = df.assign(Brand=brand, Model_No=model_no, Day=day, Month=month)

edited_df = Model_No_df[['Product Category','Item Number','Item Description','Item Description 2','Brand','Model_No','Item Delivery Date','Day','Month']]
#print(edited_df)

total_item_df = []
for item in items:
    item_df=edited_df[
        (edited_df['Brand']== item[0]) & 
        (edited_df['Model_No']== item[1]) &
        (edited_df['Day'] >= item[2]) & 
        (edited_df['Day'] <= item[3])
    ]
    total_item_df.append(item_df)

#print(total_item_df)

total_item_df = pd.concat(total_item_df)
item_count = total_item_df.groupby(['Model_No','Brand','Item Number']).size().reset_index(name='Count').sort_values(by='Count',ascending=False)

for item in items:
    item_count.loc[item_count['Model_No'] == item[1], 'Total Rebate'] = '$ '+(item_count['Count']*item[4]).astype(str)+'.00'

print(item_count)
total_rebate = item_count['Total Rebate'].str.replace('$ ','').str.replace('.00','').astype('Int64').sum()
print('Total Rebate: $', total_rebate)
'''
The above lines of code show how a particular column can be slit into multile columns and assigned to a specific variable. In this case the item description column can be split into two columns formatted as a string as indicated by the dot string method. This produces a split that is loaded into an array. It is important to note that by using the dot split method and specifying the delimiter the function works by splitting in details of the item description column into the number of columns that are ultimately delimited bt the indicated delimiter. Thus the output of is stored as an array with each of the split terms constituting a member of the arr As such we would cycle through the end using 0 as the first two and then other tubes to determine which of the values we wish to keep.

When working with numbers however we have to go the additional step and convert it back into that of a number hence we cast using the astype method, With integer 64 as we know that these two variables are to be whole numbers.
'''

'''
Using these entirely data can be built but it seemed that I'm matching to columns from the original data frame allowing you to keep the original data intact and then add it on this extra information gives you extra flexibility when sorting or possibly plotting graphs.
'''
#write_to_xl_mul(edited_df, r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\Sales_data', #'Edited_Merch_Sales_Vision', sheet_name='Edited Data')
'''
samsung_count = item_df['Model_No'].value_counts()
samsung_count = item_df.groupby(['Item Number','Model_No']).size().sort_values(ascending=False)
total_item_df['Item Description_'] = edited_df['Item Description'].str.cat(edited_df['Item Description 2'], sep=' ')
'''