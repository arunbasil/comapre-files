import pandas as pd

import numpy as np
# create DataFrame
dfmay = pd.read_excel('files/excel/May_Report.xlsx')
dfjune = pd.read_excel('files/excel/June_Report.xlsx')

# DF equals returns True of False
# print(dfmay.equals(dfjune))

# Used to compare cel by cell and return True or False
comparevalues = dfmay.values == dfjune.values
print(comparevalues)

#
rows, cols = np.where(comparevalues == False)

for item in zip(rows, cols):
    dfmay.iloc[item[0], item[1]] = ' {} --> {} '.format(dfmay.iloc[item[0], item[1]], dfjune.iloc[item[0], item[1]])

dfmay.to_excel('files/excel/output.xlsx', index=False, header=True)
