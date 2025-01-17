a = int(input("nhap mot so nguyen bat ky: "))

def KetQua(a):
    if(a > 17):
        return (a - 17)*2
    else:
        return abs(a - 17)
    
print(KetQua(a))