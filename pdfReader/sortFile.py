import pandas as pd

csv_path=r"C:\Users\Vyan\Documents\GitHub\Python\pdfReader\test.csv"
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
    filtered_df = df[df['Model'] == search_val] 
    sum = filtered_df['QTY'].sum()
    selected_cols.append(filtered_df[['RWT_No','Model','Brand','QTY']])
    selected_cols.append(sum)     

for df in selected_cols:
    print(df)

