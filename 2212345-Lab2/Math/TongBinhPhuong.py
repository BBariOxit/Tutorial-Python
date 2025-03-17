n = int(input("nhap so n:"))
def TongBinhPhuongNSo(n):
    result = 0
    for i in range(1, n +1):
        result += i**2
    return result

print(f"tong binh phuong cua {n} so tu nhien dau tien la:", TongBinhPhuongNSo(n))
