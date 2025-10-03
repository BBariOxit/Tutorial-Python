#Input: keys = ['a','b','c'], vals = [1,2,3] → {'a':1,'b':2,'c':3}
#Output:{"a":1,"b":2,"c":3}
keys = ['a','b','c']
vals = [1,2,3]
result = dict(zip(keys, vals))
print(result)

# Đầu vào: ['a','b','c'] + [1,2,3]
# zip (iterator) → tạo tuần tự:
# yield ('a',1)
# yield ('b',2)
# yield ('c',3)
# dict(zip(...)) → đọc lần lượt các cặp ở trên, chèn vào bảng băm:
# Chèn 'a':1 → {'a':1}
# Chèn 'b':2 → {'a':1,'b':2}
# Chèn 'c':3 → {'a':1,'b':2,'c':3}