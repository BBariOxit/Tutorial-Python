#How to combine many series to form a dataframe?
import numpy as np
import pandas as pd
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
#CACH1
df = pd.concat([ser1, ser2], axis=1)
#CACH2
df2 = pd.DataFrame({'col1': ser1, 'col2': ser2})
print(df.head())
print(df2.head())