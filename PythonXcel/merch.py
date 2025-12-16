from readFunction import read_from_file
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\MERCH SALES VISION GAMIN NOV 2025.csv'
support_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\supported.csv'
df = read_from_file(filepath=file_path, test=0)
support_df = read_from_file(filepath=support_path, test=0)
#print(support_df)
brand = 'SAMSUNG'
prod_category = 'Vision'
mod_num = ''
start_day = 24
end_day = 30
rebate = 0.00
'''
items =[
    {'Brand':brand, 'Model Number':mod_num, 'Start Day':start_day, 'End Day':end_day,'Rebate':rebate},
]
'''
'''
items =[('TCL','V55V6C-A',14,16,25),
        ('TCL','V55V6C-A',18,19,25),
        ('TCL','V55V6C-A',21,23,25),
        ('TCL','V55V6C-A',28,30,25)]
'''

total_item_df = []
model_no = df['Item Description'].str.split(' ').str[1]
day = df['Item Delivery Date'].str.split('/').str[0].astype('Int64')
#print(model_no)
Model_No_df = df.assign(Model_No=model_no, Day=day)
edited_df = Model_No_df[['Product Category','Item Number','Item Description','Item Description 2','Brand','Model_No','Day']]
#print(edited_df)
for item in support_df.values:
    item_df=edited_df[
        (edited_df['Brand']== item[0]) & 
        (edited_df['Model_No']== item[1]) &
        (edited_df['Day'] >= item[2]) & 
        (edited_df['Day'] <= item[3])
    ]
    total_item_df.append(item_df)

#print(total_item_df)
#samsung_count = item_df['Model_No'].value_counts()
#samsung_count = item_df.groupby(['Item Number','Model_No']).size().sort_values(ascending=False)
#total_item_df['Item Description_'] = edited_df['Item Description'].str.cat(edited_df##['Item Description 2'], sep=' ')
total_item_df = pd.concat(total_item_df)
item_count = total_item_df.groupby(['Model_No','Brand','Item Number']).size().reset_index(name='Count').sort_values(by='Count',ascending=False)
item_count['Total Rebate'] = '$ '+(item_count['Count']*item[4]).astype(str)+'.00'
print(item_count)