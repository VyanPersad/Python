from readFunction import read_from_file
import matplotlib.pyplot as plt
import numpy as np

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\MERCH SALES VISION GAMIN NOV 2025.csv'

df = read_from_file(filepath=file_path, test=0)

model_no = df['Item Description'].str.split(' ').str[1]
day = df['Item Delivery Date'].str.split('/').str[0]
#print(model_no)
Model_No_df = df.assign(Model_No=model_no, Day=day)
edited_df = Model_No_df[['Product Category','Item Number','Brand','Model_No','Day']]
#print(edited_df)
samsung_df=edited_df[(edited_df['Brand']=='SAMSUNG') & (edited_df['Product Category']=='Vision')]
print(samsung_df)

samsung_count = samsung_df['Model_No'].value_counts()
print(samsung_count)