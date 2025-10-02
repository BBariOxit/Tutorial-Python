#How to convert the index of a series into a column of a dataframe?
import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist,myarr))
ser1 = pd.Series(mydict)
# print(ser1)
df = ser1.to_frame(name = 'value').reset_index()
print(df)