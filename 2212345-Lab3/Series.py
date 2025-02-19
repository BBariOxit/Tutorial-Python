#How to create a series from a list, numpy array and dict?
import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist,myarr))
ser1 = pd.Series(mydict)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mylist)
print(ser1.head())
print(ser2.head())
print(ser3.head())