#Python program to print all even numbers in a range
start = int(input("nhap so bat dau:"))
end = int(input("nhap so ket thuc:"))
#cach1:loop
arr = []
for i in range(start, end +1):
    if i %2 ==0:
        arr.append(i)
print(arr)
#cach2:list comprehension
result = [i for i in range(start, end + 1) if i % 2 == 0]
print(result)
#cach3:range with step
newArr = []
for i in range(2,end + 1, 2):
    newArr.append(i)
print(newArr)
