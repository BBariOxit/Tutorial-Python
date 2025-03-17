#Python program to print positive numbers in a list
txt = input("nhap cac so am duong bat ky cach nhau bang dau phay:")
arr = [int(i) for i in txt.split(',')]
#cach1:loop
NewArr = []
for i in arr:
    if i > 0:
        NewArr.append(i)
print(NewArr)
#cach2: list comprehension
result = [i for i in arr if i > 0]
print(result)
#cach3:filter()
result2 = list(filter(lambda x : x > 0,arr))
print(list(result2))