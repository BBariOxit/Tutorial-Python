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

# Đầu vào: {"x":10,"y":20,"z":30}
# d.items() → tạo tuần tự:  
# yield ('x',10)
# yield ('y',20)    
# yield ('z',30)
# dict comprehension → đọc lần lượt các cặp ở trên, đảo ngược k,v rồi chèn vào bảng băm:
# Đọc ('x',10) → chèn 10:'x' → {10:'x'}
# Đọc ('y',20) → chèn 20:'y' → {10:'x',20:'y'}
# Đọc ('z',30) → chèn 30:'z' → {10:'x',20:'y',30:'z'}
# Kết quả cuối cùng: {10:'x',20:'y',30:'z'}