#Python program to print odd numbers in a List
#cach1:loop
txt = input("nhap mang so nguyen cach nhau boi dau phay:")
arr = [int(i) for i in txt.split(',')]
newArr = []
for i in arr:
    if i % 2 != 0:
        newArr.append(i)
print(newArr)
#cach2: list comprehension
result = [i for i in arr if i % 2 != 0]
print(result)
#cach3:fliter()
result2 = filter(lambda x : x % 2 != 0, arr)
print(list(result2))