#Cloning or Copying a List 
#=====================SHALLOW COPY====================
#cach1:copy()
a = [[1, 2], [3, 4], [5, 6]]
b = a.copy()
print(b)
#cach2:list slicing
c = a[:]
print(c)
#cach3:list()
d = list(a)
print(d)
#list comprehension
e = [i for i in a]
print(e)
#=====================DEEP COPY=======================
#copy.deepcopy()
import copy
f = copy.deepcopy(a)
print(f)
