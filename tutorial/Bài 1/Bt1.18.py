txt = input("nhap 3 bat ky cach nhau boi dau phay:")
list = txt.split(',')
# print(list)
a,b,c = list
print(a,b,c)

def TinhTong3So(a,b,c):
    Tong = int(a) + int(b) + int(c)
    if(a == b ==c ):   
        Tong *= 3
    return Tong

print("tong ba so(neu 3 so co gia tri bang nhau thi tong x3) la: ",TinhTong3So(a,b,c))