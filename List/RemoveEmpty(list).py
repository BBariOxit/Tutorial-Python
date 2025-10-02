#Remove empty Lists from List
#cach1:loop
arr = [[1, 2], [], [3, 4], [], [5]]
result = []
for i in arr:
    if i:
        result.append(i)
print(result)
#cach2:list comprehension
result2 = [i for i in arr if i]
print(result2)
#cach3:filter()
result3 = list(filter(lambda x : x, arr))
print(result3)