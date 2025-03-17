#Python Program to Add Two Matrices
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#cach1:numpy
import numpy as np
a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b1 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
result = a1 + b1
print(result)
#cach2:list comprehension
# c = [[a[i][j] + b[i][j] for j in range(3)]for i in range(3)]
result2 = [[a[i][j] + b[i][j] for j in range(len(a[0]))]for i in range(len(a))]
# result2 = [[int(i) for i in j] for j in c] #neu numpy thi dung cach nay de doi tu intnumpy64 thanh int
print(result2)
#cach3:zip()
result3 = [[x + y for x, y in zip(rowA,rowB)] for rowA , rowB in zip(a,b)]
print(result3)
#cach4: nested loop
result4 = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result4[i][j] = a[i][j] + b[i][j]
print(result4)
