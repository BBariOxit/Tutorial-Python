#CACH1:normalnormal
# txt = input("nhap day so nguyen cach nhau boi dau phay:")
# Ds = list(txt.split(','))
# Dsnew = []
# for i in Ds:
#     Dsnew.append(int(i))
# def MaxCuaMang(Dsnew):
#     a = 0
#     for i in Dsnew:
#         if(i > a):
#             a = i
#     return a
# print(f"phan tu lon nhat cua mang {Ds} la:", MaxCuaMang(Dsnew))

#CACH2:arr[i]
def laregest(arr,n):
    max = arr[0]
    for i in range(1,n):
        if(arr[i] > max):
            max = arr[i]
    return max
arr = [2,4,56,243]
n = len(arr)
print("phan tu lon nhat cua mang la:",laregest(arr,n))

#CACH3:Maxax()
def MaxItem(arr):
    return max(arr)
print("phan tu lon nhat cua mang la:",MaxItem(arr))

#CACH4:sort()
def MaxItem2(arr):
    arr2 = sorted(arr)
    return arr2[-1]
print("phan tu lon nhat cua mang la:",MaxItem2(arr))

#CACH5:reduce
from functools import reduce
def MaxItem3(arr):
    return reduce(max, arr)
print("phan tu lon nhat cua mang la:",MaxItem3(arr))

#CACH6:operator.gt()
import operator
def MaxItem4(arr):
    max = 0
    for i in arr:
        if(operator.gt(i,max)):
            max = i
    return max
print("phan tu lon nhat cua mang la:",MaxItem4(arr))

#CACH7:lambda
txt = max(arr, key=lambda x: x)
print("phan tu lon nhat cua mang la:",txt)