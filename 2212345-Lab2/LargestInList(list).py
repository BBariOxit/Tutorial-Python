#Chương trình Python để tìm số lớn nhất trong danh sách
txt =input("nhap mang so nguyen cach nhau boi dau phay:")
arr = [int(i) for i in txt.split(',')]
#CACH1:max()
result1 = max(arr)
print(result1)
#CACH2:loop
result2 = arr[0]
for i in arr:
    if i > result2:
        result2 = i
print(result2)
#CACH3:reduce()
from functools import reduce
result3 = reduce(lambda x,y: x if x > y else y,arr)
print(result3)
#CACH4:sort() hoac sorted()
arr.sort()
# newArr = sorted(arr)
result4 = arr[-1]
print(result4)
