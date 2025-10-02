#Python Program to Print all Odd Numbers in a Range
start = int(input("nhap so bat dau:"))
end = int(input("nhap so ket thuc:"))
#cach1:loop
arr = []
for i in range(start, end +1):
    if i %2 !=0:
        arr.append(i)
print(arr)
#cach2:list comprehension
result = [i for i in range(start, end + 1) if i % 2 != 0]
print(result)