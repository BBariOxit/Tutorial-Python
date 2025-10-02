#Remove empty tuples from a list 
a = [(1, 2), (), (3, 4), (), (5,)]
#cach1:list comprehension
result = [i for i in a if i]
print(result)
#cach2:filter()
result2 = list(filter(lambda x : x,a))
print(result2)
#cach3:filter() với none
result3 = list(filter(None, a))
print(result3)
#cach4:itertools.compress()
import itertools
b = [bool(i) for i in a]
result4 = list(itertools.compress(a,b))
print(result4)
#cach5:loop
c = []
for i in a:
    if i:
        c.append(i)
print(c)