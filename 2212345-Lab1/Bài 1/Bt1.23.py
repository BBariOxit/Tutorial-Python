txt = input("nhap vao mot chuoi bat ky:")
n = int(input("nhap vao so lan ma ban muon nhan ban 2 ky tu dau:"))

def NhanBan(txt,n):
    result = ""
    for i in range(n):
        result = result + txt[:2]
    return result

print("chuoi sau khi nhan ban 2 ky tu dau la:",NhanBan(txt,n))

