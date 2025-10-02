txt = input("nhap mot chuoi bat ky:")
n = int(input("nhap so ban sao ban muon tao:"))

def NhanBan(txt,n):
    result = ""
    for i in range(n):
        result = result + txt
    return result

print("ket qua sau khi nhan ban:", NhanBan(txt,n))