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
Product_List = TY_df[['Sku', 'Brand','Description']]
Product_List['Model'] = Product_List['Description'].str.split(' ', n=1, expand=True)[0]
Product_List['Description'] = Product_List['Description'].str.split(' ', n=2, expand=True)[2]

print(Product_List)
