#Kiểm tra xem phần tử có tồn tại trong list không
txt = input("nhap mot mang bat ky cach nhau bang dau phay:")
arr = [int(i) for i in txt.split(',')]
n = int(input("nhap so bat ky ma ban muon ktra xem trong mang co khong:"))
#CACH1:dung in
def Check1(arr,n):
    if n in arr:
        print(f"so {n} co trong mang")
    else:
        print(f"so {n} khong co trong mang")
print(arr)
Check1(arr,n)
#CACH2:su dung any()
def Check2(arr,n):
    result = any(i == n for i in arr)
    if result:
        print(f"so {n} co trong mang")
    else:
        print(f"so {n} khong co trong mang")
print(arr)
Check2(arr,n)
#CACH3: su dung count()
def Check3(arr,n):
    result = arr.count(n)
    if result >= 1:
        print(f"so {n} co trong mang")
    else:
        print(f"so {n} khong co trong mang")
print(arr)
Check3(arr,n)
#CACH4 sd vong lap
def Check4(arr,n):
    result = False
    for i in arr:
        if n == i:
            result = True
    if result:
        print(f"so {n} co trong mang")
    else:
        print(f"so {n} khong co trong mang")
print(arr)
Check4(arr,n)