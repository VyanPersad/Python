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
        print(row['Sku'], row['Brand'], row['Description'].split('-',maxsplit=1)[0].replace(' ',""), f"{'$ '}{round(row['Cash Price'],2)}")
        
        print(row['Sku'], [row[mon] for mon in mons])
'''
'''
The code above allows for the reading of a csv file and the filtering of data based on user full brand and sku. They Could facilitate the searching specific columns in the CSV file iterating each of those and the details of the that matches the user input. 

For the code above it is important to note that we don't lewd the entire data free from the CSV we in this essence create a second data where we stipulate the column names as defined by the existing CSV file that we wish to load and it is from this we further filter the details indicating by the Col which column we wish to filter and the subsequent filter term.

For the code below however is slightly different approach is taken in that we create a filtered data frame that is filtered based on the user input. It highlights all the various columns to which we intend to search on the accompanying search term which will then be to make the filtered data frame This filtered data frame is then further processed by using the group by function which essentially allows for grouping by in this instance the column name of brand and this is then to make a scatterplot.
'''
x_vals = []
y_vals = []
'''
The next step is to use another filtered data to select the data we wish to use for a scatter plot. In it we specify the specific column names and the conditions to which we are to map them too. For instance we want the Brand Column to be equal to certain specific brands at the same time we wish the search criteria be several different brands. As such we use a combination of equal to and or to refine the search criteria to include more than one criteria.
'''
filtered_df = df[(df['Year'] == 'This Year')
                & 
                (df['Cash Price'] < 70000)
                &
                (df['Brand']== 'TCL') |
                (df['Brand']== 'SAMSUNG') | 
                (df['Brand']== 'LG') | 
                (df['Brand']== 'WESTINGHOUSE')]
'''
Note how the specific columns that are searched along their conditions and are recombined into an array and this constitutes the new filtered data frame. In this instance we can safely say that what we are doing is recreating a filtered data frame with the columns yeah cash price and and specifically we are reading from the original data free defined by DF.
'''
grouped_df = filtered_df.groupby('Brand')
'''
The grouped by dataframe utilizes the group by function within Python to better sort the given the specific column name this goes a long way in helping to better organize the data and make it readable once plotted.
'''
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