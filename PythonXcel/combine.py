import os
import pandas as pd
from readFunction import*
from writeFunctions import*

folderpath = r'Data\Sales_data\Month'
combinedFile = pd.DataFrame()
fileName = 'month'
rowCount = 0
with pd.ExcelWriter(f'{fileName}.xlsx', engine='openpyxl') as writer:
    for file in os.listdir(folderpath):
        filepath = os.path.join(folderpath, file)
        dataframe = read_from_file(filepath, test=0, n=5, col_Names = [], sheet = 0)
        dataframe.to_excel(writer, sheet_name=f'{fileName}File', startrow=rowCount, index=False)
        rowCount = rowCount + len(dataframe)+2    

'''
So this simply combines multiple files into one data set and outputs it onto 1 sheet In an entirely new Excel file.

The the basic explanation of it is that it uses Pandas accelerator to read the file name using the Open PYXL engine.

The read from file is a custom function that takes the file path and allows the user to output the detail from the data frame using the test attribute if it is set to zero Then it will output the default number of N which is set to 5 if it is set to one however then it will output the entire dataframe.

The function is the two excel function which allows for the writing of the data frame to an Excel file. It allows the user to specify the sheet name as well as the rule position that the data frame is to be written in the particular new combined excel file It is important at this point to ensure that you have a row count that continually updates based on the length of the data theme that was previously being written This will ensure that the new data frame is written directly below the previous data and that there is a gap between the two. In this instance the plus two at the end of the row count is there to that there is a gap of two rules between the data frames.
'''
