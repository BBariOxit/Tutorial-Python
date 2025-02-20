#Python program to print negative numbers in a list
txt = input("nhap cac so am duong bat ky cach nhau bang dau phay:")
arr = [int(i) for i in txt.split(',')]
#cach1:loop
newArr = []
for i in arr:
    if i < 0:
        newArr.append(i)
print(newArr)
#cach2:list compreehsion
result = [i for i in arr if i < 0]
print(result)
#cach3:filter()
result2 = list(filter(lambda x : x < 0 , arr))
print(result2)
#cach4:map()
result3 = list(map(lambda x : x if x < 0 else None, arr))
result3 = [i for i in result3 if i is not None]
print(result3)