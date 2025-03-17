#Python program to find Cumulative sum of a list
#cach1:itertools.accumulate()
import itertools
l = [1, 2, 3, 4]
result = list(itertools.accumulate(l))
print(result)
#cach2:numpy.cumsum()
import numpy
result2 = numpy.cumsum(l)
print(result2)
#cach3:loop
total = 0
arr = []
for i in l:
    total += i
    arr.append(total)
print(arr)
#cach4:List Comprehension
result3 = [sum(l[:i+1]) for i in range(len(l))]
print(result3)
#cach5:generator
def Generator(l):
    total = 0
    for i in l:
        total += i
        yield total
result4 = list(Generator(l))
print(result4)
