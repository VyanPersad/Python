import os 
import csv

filePath = 'env'

def getFileName(file):
    lastDot = file.rfind('.')
    #Note the position of the :
    #If the index comes after then the string before is printed
    #If the index comes before then the string after is printed
    #The ':' indicates what will be printed up until the index   
    fileName = file[:lastDot]

    return fileName

def writetoTXT(fileName, filelistName='File_List.txt'):
    file = open(filelistName, 'a')
    file.write(f'{fileName}\n')

def writeFolderContents(filepath):
    dirInfo = []
    for root, folder, files in os.walk(filePath):
        dirInfo.append((root, folder, files)) 
    # The output would be and array of arrays
    # [[root],[folder],[files]] 
    # Note the dirInfo[0] is the first entry into the array  
    # that is the contents of the filePath
    # Essentially you may not need to use any number but 0
    # as there would only be one of this term. 
    # all other terms may have more and would have more thna one entry.
    # ROOT - difInfo[0][0]
    # FOLDER - difInfo[0][1][i]
    # FILES - difInfo[0][2][i]
    return dirInfo
