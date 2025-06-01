import os
import pandas as pd
from readFunction import*
from writeFunctions import*

folderpath = r'Data'
combinedFile = pd.DataFrame()

rowCount = 0
with pd.ExcelWriter(f'combinedFile.xlsx', engine='openpyxl') as writer:
    for file in os.listdir(folderpath):
        filepath = os.path.join(folderpath, file)
        dataframe = read_from_file(filepath, test=0, n=5, col_Names = [], sheet = 0)
        dataframe.to_excel(writer, sheet_name='combinedFile', startrow=rowCount, index=False)
        rowCount = len(dataframe)+2    

