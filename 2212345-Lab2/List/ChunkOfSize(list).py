#Break a List into Chunks of Size N in Python
a = [1, 2, 3, 4, 5, 6, 7, 8]
n = int(input("nhap so n:"))
#cach1:list comprehension
result = [a[i:i+n] for i in range(0, len(a), n)]
print(result)
#cach2:slicing
b = []
for i in range(0, len(a), n):
    b.append(a[i:i+n])
print(b)
#cach3:itertools.islice
import itertools
it = iter(a)
result2 = [list(itertools.islice(it,n)) for i in range((len(a) + n -1) // n)]
print(result2)
#cach4:numpy.array_split
import numpy
Nhom = len(a) // n + (len(a) % n != 0)
chunk = numpy.array_split(a,Nhom)
result4 = [list(map(int, i)) for i in chunk]
print(result4)
#cach5:geneator
def DSChunk(a,n):
    for i in range(0, len(a), n):
        yield a[i:i+n]
print(list(DSChunk(a,n)))

