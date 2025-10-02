a = str(input("nhap so nguyen bat ky:"))
b = int(a)
# Ds = []
# for i in a:
#     Ds.append(int(i))

def KtraSoAmstrong(a,b):
    result = 0
    n = len(a)
    for i in a:
        result += (int(i)**n)
    if(result == b):
        print("day la so Amstrong")
    else:
        print("day ko la so Amstrong")

KtraSoAmstrong(a,b)