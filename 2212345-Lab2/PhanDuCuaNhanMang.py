arr = [100, 10, 5, 25, 35, 14]
n = int(input("nhap so n:"))
length = len(arr)
def Remain(arr,n):
    total = 1
    for i in arr:
       total *= i
    return total % n
print("phan du cua phep nhan cac phan tu trong mang la:",Remain(arr,n))