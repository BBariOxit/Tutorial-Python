txt =input("nhap mang so nguyen cach nhau boi dau phay:")
arr = [int(i) for i in txt.split(',')]
#CACH1:min()
result1 = min(arr)
print(result1)
#CACH2:loop
result2 = arr[0]
for i in arr:
    if i < result2:
        result2 = i
print(result2)
#CACH3:sort() hoac sorted()
arr.sort()
# newArr = sorted(arr)
result3 = arr[0]
print(result3)