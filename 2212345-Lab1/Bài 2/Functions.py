import os
import math

#HAM CAC CHUC NANG
#1. Tính (a+b), a/b, a^b
def TinhToanCoBan(a,b):
    Tong = a + b
    Chia = a / b
    LuyThua = a ** b
    print(f"Tong cua {a} va {b} la:",Tong)
    print(f"Thuong cua {a} va {b} la: {Chia}")
    print(f"a^b la: {LuyThua}")

#2. Tính diện tích hình tròn khi biết bán kính
def TinhSHinhTron(n):
    S = (math.pi)*(n**2)
    return S

#3. Xuất tất cả các số nguyên tố trong 1 khoảng
def KtraSoNguyenTo(num):
    if(num < 1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def TimDaySoNguyenTo(start, end):
    ListOfNum = []
    for i in range(start, end +1):
        if(KtraSoNguyenTo(i)):
            ListOfNum.append(i)
    return ListOfNum

#4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
def KtraSoFibonacci(num):
    a,b = 0,1
    while b < num:
        a,b = b, a + b
    return b == num   #neu b == num thi se ss de tra ve true or false

#5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
#dung de quy
def FindFibonacciRescusive(n):
    if n <= 0:  
        return 0
    elif n == 1:  
        return 1
    else:  
        return FindFibonacciRescusive(n - 1) + FindFibonacciRescusive(n - 2)  #F(3) = F(2) + F(1)
    
# FindFibonacciRescusive(4)
# ├── FindFibonacciRescusive(3)
# │   ├── FindFibonacciRescusive(2)
# │   │   ├── FindFibonacciRescusive(1) => 1
# │   │   └── FindFibonacciRescusive(0) => 0
# │   └── FindFibonacciRescusive(1) => 1
# ├── FindFibonacciRescusive(2)
# │   ├── FindFibonacciRescusive(1) => 1
# │   └── FindFibonacciRescusive(0) => 0


#khong dung de quy
def FindFibonacciNonRecursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a,b = 0 , 1
    for i in range(2, n + 1):
        a,b = b, a + b
    return b

#6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
#dung de quy
def SumOfFibonacciRescusive(n):
    if n <= 0:
        return 0
    return FindFibonacciRescusive(n) + SumOfFibonacciRescusive(n - 1)

# SumOfFibonacciRescusive(4) = FindFibonacciRescusive(4) + SumOfFibonacciRescusive(3)
# FindFibonacciRescusive(4) = 3 (như đã tính ở trên)
# SumOfFibonacciRescusive(3) = FindFibonacciRescusive(3) + SumOfFibonacciRescusive(2)
# FindFibonacciRescusive(3) = 2
# SumOfFibonacciRescusive(2) = FindFibonacciRescusive(2) + SumOfFibonacciRescusive(1)
# FindFibonacciRescusive(2) = 1
# SumOfFibonacciRescusive(1) = FindFibonacciRescusive(1) + SumOfFibonacciRescusive(0)
# FindFibonacciRescusive(1) = 1, SumOfFibonacciRescusive(0) = 0
# Cộng dần kết quả:
# SumOfFibonacciRescusive(1) = 1 + 0 = 1
# SumOfFibonacciRescusive(2) = 1 + 1 = 2
# SumOfFibonacciRescusive(3) = 2 + 2 = 4
# SumOfFibonacciRescusive(4) = 3 + 4 = 7


def SumOfNFibonacciNonRescusive(n):
    if n <= 0:
        return 0
    a,b = 0,1
    total = a
    for i in range(n):
        total += b
        a,b = b, a+b 
    return total      

#7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
def TongSQRTCuaNSoNguyen(n):
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n +1 ):
        total += math.sqrt(i)
    return total

#8. Giải phương trình bậc 2: ax2 + bx + c=0
#delta  = b^2 - 4ac
#delta = 0 , pt co 1 nghiem kep
#delta > 0  , pt co 2 nghiem phan biet
#delta < 0 , pt vo nghiem

def GiaiPTBac2(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm."
            else:
                return "Phương trình vô nghiệm."
        else:
            return f"Phương trình bậc nhất có nghiệm: x = {-c / b}"
    
    delta = (b**2)- 4 * (a*c)
    if(delta > 0):
        x1 = (-b + (math.sqrt(delta))/(2*a))
        x2 = (-b - (math.sqrt(delta))/(2*a))
        return f"co 2 nghiem phan biet la: x1={x1}, x2={x2}"
    elif (delta == 0):
        return "co 1 nghiem kep la:", -b/(2*a)
    else:
        return "vo nghiem"
    
#Tính n!
def TinhNGiaiThua(n):
    total = n
    for i in range(n - 1,0,-1):
        total *= i
    return total

# print("10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)")
def inTamGiac(n):
    # kq = []
    # for i in range(n):
    #     row = " " * n
    #     kq.append(row)
    #     kq[i][0] = "*"
    #     kq[i][i] = "*"
    # for j in range(0,n-1):  
    #     kq[n-1][j] ="*"
    # for row in kq:
    #     print(' '.join(row))
    # return kq

    for i in range(n):
        for j in range(i + 1):
            if j == 0 or i == j or i == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

#11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
#Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất
#ra màn hình 1:2:50.

def DoiGioPhutGiay(n):
    # h = int(n / 3600)
    # p = int((n % 3600) / 60) 
    # s = int(n % 60)
    h = n // 3600
    p = (n % 3600) // 60 
    s = n % 60
    print(f"{h}:{p}:{s}")

def NhapMangSoNguyen():
    n = int(input("nhap so luong so nguyen ma ban muon nhap:"))
    DsNumbs = [];
    for i in range(1,n + 1):
        nums = int(input(f"nhap so nguyen thu {i}:"))
        DsNumbs.append(nums)
    return DsNumbs


def XuatSoLeKhongChiaHetCho5(Ds):
    DsNew = []
    for i in Ds:
        if (i % 2 != 0 and i % 5 != 0):
            DsNew.append(i)
    return DsNew

def XuatAllFibonacci(Ds):
    DsNew = []
    for i in Ds:
        if KtraSoFibonacci(i):
            DsNew.append(i)
    return DsNew
    
def XuatAllSoNguyenTo(Ds):
    DsNew = []
    for i in Ds:
        if(KtraSoNguyenTo(i)):
            DsNew.append(i)
    return DsNew

def TinhTBSoLe(Ds):
    DsNew = []
    for i in Ds:
        if(i % 2 != 0):
            DsNew.append(i)
    TBinh = 0 
    for i in DsNew:
        TBinh += i
    return TBinh

def TinhTichSoLeKoChiaHetCho3(Ds):
    DsNew = []
    for i in Ds:
        if(i % 2 != 0 and i % 3 != 0):
            DsNew.append(i)
    Tich = 1
    for i in DsNew:
        Tich *= i
    return Tich


def HoanVi2ViTri(a,b,Ds):
    if(a < 0 or b < 0 or a >= len(Ds) or b >= len(Ds)):
        print("vui long nhap lai so cho hop le:")
    else:
        Ds[a], Ds[b] = Ds[b], Ds[a]
    return Ds

def DaoDS(Ds):
    NewDs = Ds[::-1]
    return NewDs
    
def LaySoLonThu2(Ds):
    numMax = max(Ds)
    # newDs = [i for i in Ds if i != numMax] 
    newDs = []
    for i in Ds:
        if i != numMax:
            newDs.append(i)
    SoLonNhi = max(newDs)
    # newDs2 = [i for i in newDs if i == SoLonNhi]
    newDs2 = []
    for i in newDs:
        if i == SoLonNhi:
            newDs2.append(i)
    return newDs2

def TongAllCacChuSo(Ds):
    TongAll = 0
    for num in Ds:
        newNum = str(num)
        Tong = 0
        for num2 in newNum:
            Tong += int(num2)
        TongAll += Tong
    return TongAll   

def DemSoLanXH(Ds,n):
    count = 0
    # count = Ds.count(n)
    for i in Ds:
        if i == n:
            count +=1
    return count

def TimCacSoXHNLan(ds,n):
    newDs = []
    for i in ds:
        if ds.count(i) == n:
            newDs.append(i)
    newDs2 = list(set(newDs))
    return newDs2

def TimCacSoXHNhieuLanNhat(Ds):
    Max = 0
    newDs =[]
    for i in Ds:
        if Ds.count(i) > Max:
            Max = Ds.count(i)
    for i in Ds:
        if Ds.count(i) == Max:
            newDs.append(i)
    newDs2 = list(set(newDs))
    return newDs2