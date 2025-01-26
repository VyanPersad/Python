import pandas as pd

def readCols(dataFrame, colName1, colName2):
    dF = dataFrame[[colName1, colName2]]
    return dF