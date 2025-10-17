# Input: d={"a":1,"b":None,"c":0,"d":None}
# Output: {"a":1,"c":0}
d = {"a":1,"b":None,"c":0,"d":None}
result = {k: v for k,v in d.items() if v is not None}
print(result)   

