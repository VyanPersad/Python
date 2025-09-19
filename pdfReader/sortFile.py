import pandas as pd

csv_path=r"C:\Users\Vyan\Documents\GitHub\Python\pdfReader\final.csv"
unique_vals = []
selected_cols = []

#'RWT_No,Model,Item_Desc,UPC,Courts_Code,US_Unit_Price,EST_Landed_TTD,EST_Price_w_Mrgn25,QTY,Brand'
 
df = pd.read_csv(csv_path, on_bad_lines='skip')

for col in df.columns:
    unique_vals = df['Model'].unique()    

#print(len(unique_vals))
#print(unique_vals)

for n in range(len(unique_vals)):
    search_val = unique_vals[n]
    filtered_qty = df[df['Model'] == search_val]
    sum = filtered_qty['QTY'].sum()
    filtered_df = df[df['Model'] == search_val].iloc[0]
    filtered_df['Tot_QTY'] = sum   
    selected_cols.append(filtered_df[['Model','Brand','Tot_QTY','EST_Landed_TTD','EST_Price_w_Mrgn25']])
      

final_df = pd.DataFrame(selected_cols)
print(final_df)

