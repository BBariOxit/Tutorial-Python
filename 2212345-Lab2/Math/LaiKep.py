p = int(input("nhap tien goc:"))
t = int(input("nhap thoi gian:"))
r = int(input("nhap lai suat:"))
def LaiKep(p,t,r):
    # A = p *((1+(r/100))**t)
    A = p * (pow((1 + r / 100), t))
    Lai = A - p
    print("tien lai kep la:",Lai)
LaiKep(p,t,r)