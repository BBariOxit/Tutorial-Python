#Python program to print even numbers in a list
#cach1:loop
import random as rd
n = int(input("nhap so luong nguyen:"))
def NhapMangTDong(n):
    arr = []
    for i in range(n):
        num = rd.randint(1,100)
        arr.append(num)
    return arr
arr = NhapMangTDong(n)
print("list:",arr)
newArr = []
for i in arr:
    if i % 2 == 0:
        newArr.append(i)
print(newArr)
#cach2:list comprehension
result = [i for i in arr if i % 2 == 0]
print(result)
#cach3:filter()
result = filter(lambda x : x % 2 == 0, arr)
print(list(result))
#cach4: