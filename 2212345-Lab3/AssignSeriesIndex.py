# How to assign name to the series’ index?
import numpy as np
import pandas as pd
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser.name = 'alphabets'
print(ser.head())