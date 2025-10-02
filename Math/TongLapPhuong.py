n = int(input("nhap so n:"))
def TongLapPhuongNSo(n):
    result = 0
    for i in range(1, n +1):
        result += i**3
    return result

print(f"tong binh phuong cua {n} so tu nhien dau tien la:", TongLapPhuongNSo(n))