#Chương trình Python để tìm số lớn thứ hai trong một danh sách
txt =input("nhap mang so nguyen cach nhau boi dau phay:")
arr = [int(i) for i in txt.split(',')]
#CACH1:loop
max1 = max2 = float('-inf')
for i in arr:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max2 = i
print(max2)
#CACH2:sort() hoac sorted
# arr.sort(reverse= True)
newArr = sorted(arr, reverse = True)
print(newArr[1])
#CACH3:heapq.nlargest()
import heapq
newArr = heapq.nlargest(3,arr)
print(newArr[1])



