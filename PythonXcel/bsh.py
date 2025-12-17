from readFunction import read_from_file
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\BuyerSalesHistory.csv'

df = read_from_file(filepath=file_path, test=0)
#brand = input("Enter Brand Name: ")
#`sku = input("Enter Sku: ")
mons = ['April','May','June','July','August','September','October','November','December','January','February','March']
'''
for index, row in df[['Sku', 'Brand','Description','Year','Cash Price','April','May','June','July','August','September','October','November','December','January','February','March']].iterrows():
    if row['Year'] == 'This Year' and row['Brand'] == brand and row['Sku'] == sku:
        print(row['Sku'], row['Brand'], row['Description'].split('-',maxsplit=1)[0].replace(' ',""), f"{'$ '}{round(row['Cash Pric``e'],2)}")
        
        print(row['Sku'], [row[mon] for mon in mons])
'''
x_vals = []
y_vals = []

filtered_df = df[(df['Year'] == 'This Year')
                & 
                (df['Cash Price'] < 70000)
                &
                (df['Brand']== 'TCL') |
                (df['Brand']== 'SAMSUNG') | 
                (df['Brand']== 'LG') | 
                (df['Brand']== 'WESTINGHOUSE')]

grouped_df = filtered_df.groupby('Brand')

for brand_name, grouped_by_df in grouped_df:
    x_vals = grouped_by_df['Sku'].tolist()
    y_vals = grouped_by_df['Cash Price'].tolist()

    plt.scatter(x_vals, y_vals, label=brand_name)

plt.legend(title="Brand")
y_formatter = ScalarFormatter()
y_formatter.set_scientific(False)
plt.gca().yaxis.set_major_formatter(y_formatter)
plt.xticks([])
plt.xlabel("Sku")
plt.ylabel("Cash Price ($)")
plt.ylim(0, 20000)
plt.grid('both')
plt.show()