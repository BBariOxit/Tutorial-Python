#Convert a Panda module Series to Python list and it’s type
import pandas as pd
ds= pd.Series([1,2,3,4,5,6])
print("==============SERIES=================")
print(ds)
print(type(ds))
print("===============LIST==================")
print(ds.tolist())
print(type(ds.tolist()))