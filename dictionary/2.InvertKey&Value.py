#Input: d = {"x":10,"y":20,"z":30}
#Output:{10:"x",20:"y",30:"z"}
d = {"x":10,"y":20,"z":30}
result = {v: k for k,v in d.items()}
print(result)

#zip
result2 = dict(zip(d.values(), d.keys()))
print(result2)

#vong lap
inv = {}
for k,v in d.items():
    inv[v] = k
print(inv)