#Sort the values of first list using second list in Python
a = ['a', 'b', 'c', 'd']
b = [3, 1, 4, 2]
#cach1:zip() và sorted()
result = [i for _, i in sorted(zip(b,a))]
print(result)
#cach2:numpy.argsort()
import numpy
result2 = [a[i] for i in numpy.argsort(b)]
print(result2)
#cach3: pandas
import pandas as pd
df = pd.DataFrame({'a': a, 'b': b})
sorted_a = df.sort_values('b')['a'].tolist()
print(sorted_a)
