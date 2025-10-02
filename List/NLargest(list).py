#Chương trình Python để tìm N phần tử lớn nhất từ ​​một danh sách
txt =input("nhap mang so nguyen cach nhau boi dau phay:")
arr = [int(i) for i in txt.split(',')]
n = int(input("nhap so n:"))
#CACH1:lap n lan
def NSoLonNhat(arr,n):
    arrCopy = arr.copy()
    newArr =[]
    for i in range(0,n):
        max1 = float('-inf')
        for j in arrCopy:
            if j > max1:
                max1 = j
        arrCopy.remove(max1)
        newArr.append(max1)
    print(newArr)
NSoLonNhat(arr,n)
#CACH2:numpy.argsort()
import numpy as np
def NSoLonNhat2(arr,n):
    arr2 = np.array(arr)
    return arr2[np.argsort(arr2)[-n:]]
NSoLonNhat2(arr,n)
#CACH3:sort()