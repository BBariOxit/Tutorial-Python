#Python program to print all positive numbers in a range
# txt = input("nhap cac so am duong bat ky cach nhau bang dau phay:")
# arr = [int(i) for i in txt.split(',')]
start = int(input("nhap start:"))
end = int(input("nhap end:"))
#cach1:loop
newArr = []
for i in range(start, end + 1):
    if i > 0:
        newArr.append(i)
print(newArr)
#cach2:list comprehension
result = [i for i in range(start, end + 1) if i > 0]
print(result)
#cach3:filter
result2 = list(filter(lambda x : x > 0, range(start,end+1)))
print(result2)
