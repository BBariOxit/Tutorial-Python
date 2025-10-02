#Chương trình Python để chia mảng và đưa phần đầu xuống cuối
#cach1:tu lam
arr = [1,2,3,4,5,6,7,8]
n = len(arr)
print(arr)
k = int(input("nhap so phan tu can cat o dau:"))
def New(arr,n,k):
    arrNew1 = []
    arrNew2 = []
    for i in range(k):
        arrNew1.append(arr[i])
    for i in range(k,n):
        arrNew2.append(arr[i])
    return arrNew2 + arrNew1
    # print(arrNew1)
    # print(arrNew2)
print("mang sau khi doi la:",New(arr,n,k))

#cach2:dich chuyen
arr2 = [1,2,3,4,5,6,7,8]
n = len(arr2)
print(arr2)
k = int(input("nhap so phan tu can cat o dau:"))
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
        arr[n-1] = x

splitArr(arr2,n,k)
print(arr2)

# cach3:
arr3 = [1,2,3,4,5,6,7,8]
n = len(arr3)
print(arr3)
k = int(input("nhap so phan tu can cat o dau:"))
def splitArr2(arr,k):
    return arr[k:]+arr[:k]
print(splitArr2(arr3,k))

# cach4:extend
arr4 = [1,2,3,4,5,6,7,8]
n = len(arr4)
print(arr4)
k = int(input("nhap so phan tu can cat o dau:"))
a = arr4[:k]
b = arr4[k:]
b.extend(a)
print(b)

#cach5:list comprehension
def split_and_add(arr, n):
    return [arr[(i + n) % len(arr)] for i in range(len(arr))]
arr = [12, 10, 5, 6, 52, 36]
n = 2
result = split_and_add(arr, n)
print(*result)