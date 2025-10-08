#Input: d={"a":1,"b":2,"c":4,"d":5}
#Output: {"b":2,"c":4}
d = {"a":1,"b":2,"c":4,"d":5}
result = {k: v for k, v in d.items() if v % 2 == 0}
print(result) 
