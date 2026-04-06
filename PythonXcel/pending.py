from readFunction import read_from_file
import datetime as dt
import streamlit as st
import pandas as pd

this_yr = dt.datetime.now().year
print(this_yr)
curr_mon = dt.datetime.now().month
print(curr_mon)

file_path = r'C:\Users\Vyan\Documents\GitHub\Python\PythonXcel\Data\Reportes Courts.xlsx'

df = read_from_file(filepath=file_path, test=0)

vision_Filter = df[df['Department'].str.contains('VISION', na=False)]
audio_Filter = df[df['Department'].str.contains('AUDIO', na=False)]
gaming_Filter = df[df['Department'].str.contains('GAMING', na=False)]

major_Filter = df[
                  (df['Department'].str.contains('VISION', na=False)) |
                  (df['Department'].str.contains('AUDIO', na=False)) |
                  (df['Department'].str.contains('GAMING', na=False))
                  ]

grouped_df = major_Filter[['Class', 'Brand', 'Code Courts', 'Model','Description','Expected Delivery Date','Pending']]

'''
date_df = grouped_df[
    (grouped_df['Expected Delivery Date'].dt.year == this_yr) 
    & 
    (grouped_df['Expected Delivery Date'].dt.month == curr_mon)]
'''

st.dataframe(grouped_df, height=800)
st.set_page_config(layout="wide")