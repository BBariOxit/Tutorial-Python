#Count occurrences of an element in a list in Python
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
#cach1:count()
print(a.count(2))
#cach2:loop
total = 0
for i in a:
    if i == 2:
        total += 1
print(total)
#cach3:loop voi function
# n = int(input("nhap so ma ban muon tim sl:"))
def DemSLElement(n):
    total1 = 0
    for i in a:
        if i == n:
            total1 += 1
    return total1
print(DemSLElement(2))
#cach4:countnOf() form operator
import operator
result = operator.countOf(a,2)
print(result)
#cach5:counter form Collections
import collections
result2 = collections.Counter(a)
print(result2[2])