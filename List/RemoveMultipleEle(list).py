#Remove Multiple Elements from List in Python
# txt = input("nhap cac so am duong bat ky cach nhau bang dau phay:")
# arr = [int(i) for i in txt.split(',')]
#cach1:loop
a = [1,2,3,4,5,6,7,8,9]
a1 = [2,4,6,8]
result = []
for i in a:
    if i not in a1:
        result.append(i)
print(result)
#cach2:list comprehension
b = [1,2,3,4,5,6,7,8,9]
b1 = [2,4,6,8] 
result2 = [i for i in b if i not in b1]
print(result2)
#cach3:remove()
c = [1,2,3,4,5,6,7,8,9]
c1 = [2,4,6,8] 
for i in c1:
    while i in c:
        c.remove(i)
print(c)
#cach4:filter()
d = [1,2,3,4,5,6,7,8,9]
d1 = [2,4,6,8] 
result3 = list(filter(lambda x : x not in d1,d))
print(result3)