num = int(input("nhap so nguyen duong:"))
# #CACH1
GiaiThua = 1
for i in range(1,num+1):
    GiaiThua *= i
print(f"giai thua cua so {num} la: {GiaiThua}")
#CACH2
def TinhGiaiThua(num):
    # return 1 if (num==0 or num==1) else num * TinhGiaiThua(num-1)
    if(num==1 or num==0):
        return 1
    else:
        num * TinhGiaiThua(num-1)
print(f"giai thua cua {num} la:", TinhGiaiThua(num))
#CACH3
import math
def TinhGiaiThua2(num):
    return (math.factorial(num))
print(f"giai thua cua {num} la:", TinhGiaiThua2(num))
# CACH4
import numpy
x = numpy.prod([i for i in range(1,num+1)])
print(x)
