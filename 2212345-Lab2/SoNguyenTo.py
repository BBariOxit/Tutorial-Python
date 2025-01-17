import math
a = int(input("nhap khoang bat dau:"))
b = int(input("nhap khoang ket thuc:"))

def KtraSoNguyenTo(n):
    if (n < 1):
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def TimSoNguyenTo(a,b):
    Ds = []
    for i in range(a, b + 1):
        if(KtraSoNguyenTo(i)):
            Ds.append(i)
    return Ds

print("day so nguyen to la:", TimSoNguyenTo(a,b))
