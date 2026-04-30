from readFunction import read_from_file
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import seaborn as sns

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\BuyerSalesHistory.csv'

df = read_from_file(filepath=file_path, test=0)

mons = ['April','May','June','July','August','September','October','November','December','January','February','March']

TY_df = df[(df['Year'] == 'This Year')]
LY_df = df[(df['Year'] == 'Last Year')]

Brand_List = TY_df['Brand'].unique().tolist()
#Product_List = TY_df[['Sku', 'Brand','Description']]
#Product_List['Model'] = Product_List['Description'].str.split(' ', n=1, expand=True)[0]
#Product_List['Description'] = Product_List['Description'].str.split(' ', n=2, expand=True)[2]

product_dist = TY_df.groupby('Brand').sum().reset_index()

Total = product_dist['Year to Date'].sum()

product_dist_by_mon = TY_df[['Brand', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March','Year to Date']].groupby('Brand').sum()

#product_dist_by_mon = ((product_dist_by_mon/Total)*100).round(2)
#product_dist_by_mon = product_dist_by_mon.reset_index().#sort_values(by='Year to Date', ascending=False)
replotdata = TY_df[['Sku', 'Brand', 'Cash Price', 'Year to Date']].nlargest(100, 'Year to Date')

stripplotdata = TY_df[['Sku', 'Brand', 'Description', 'Cash Price','Year to Date']].nlargest(100, 'Year to Date')

#sns.stripplot(x='Brand', y='Cash Price', data=stripplotdata)
#sns.swarmplot(x='Brand', y='Cash Price', data=stripplotdata)
#sns.relplot(x='Cash Price', y='Year to Date', data=replotdata, #hue='Brand', size='Year to Date', sizes=(20, 200), alpha=0.7)
#plt.show()

Sales_df = TY_df.iloc[:, np.r_[0,2, 10:22]].groupby(TY_df.columns[2]).sum().reset_index()

print(Sales_df)