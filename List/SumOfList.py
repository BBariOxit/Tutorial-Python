txt = input("nhap day so nguyen cach nhau boi dau phay:")
Ds = list(txt.split(','))

def TongCuaMang(Ds):
    Tong = 0
    for i in Ds:
        Tong += int(i)
    return Tong
print("Tong cua mang la:",TongCuaMang(Ds))

#cach2: sumsum
# arr = [2,3,5,7,4]
# print("tong cua mang:",sum(arr))

#cach3:enumerateenumerate
# list1 = [12, 3, 4, 15]
# s=0
# for i,a in enumerate(list1): 
#     s+=a 
# print(s)