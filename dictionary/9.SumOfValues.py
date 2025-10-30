# Input: d={"a":1,"b":5,"c":2}
# output: 8
d = {"a": 1, "b": 5, "c": 2}
result = sum(d.values())
print(result)
#cach2
result2 = 0
for value in d.values():
    result2 += value
print(result2)