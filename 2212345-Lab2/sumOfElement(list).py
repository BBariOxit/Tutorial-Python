txt = input("nhap mang so cach nhau boi dau phay:")
arr = [int(i) for i in txt.split(',')]
#CACH1:sum()
result = sum(arr)
print(result)
#CACH2:loop
total = 0
for i in arr:
    total += i
print(total)
