import os
from readFunction import*

folderpath = ""
combinedFile = []

for file in os.listdir(folderpath):
    os.oath.join(folderpath, file)
    dataframe = read_from_file
    combinedFile.append(dataframe)

combinedFile.to_excel(f'{folderpath}/combinedFile.xlsx', index=False)

