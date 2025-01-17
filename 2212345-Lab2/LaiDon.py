p = int(input("nhap tien goc:"))
t = int(input("nhap thoi gian:"))
r = int(input("nhap lai suat:"))
def LaiSuat(p,t,r):
    si = (p * t * r)/100
    print('lai don la:',si)
    return si
LaiSuat(p,t,r)