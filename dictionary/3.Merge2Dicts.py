# Input: d1={"a":1,"b":2}; d2={"b":20,"c":3}
# Output: {"a":1,"b":20,"c":3}
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

# Using dictionary unpacking
result = {**d1, **d2}
print(result)
# Giải thích:
# **d1 → giải nén các cặp key-value trong d1:
# **d1 → "a":1, "b":2
# **d2 → giải nén các cặp key-value trong d2:
# **d2 → "b":20, "c":3
# Kết hợp lại:
# {**d1, **d2} → {"a":1, "b":2, "b":20, "c":3}
# Chèn vào bảng băm:
# Chèn "a":1 → {"a":1}
# Chèn "b":2 → {"a":1,"b":2}
# Chèn "b":20 → {"a":1,"b":20} (ghi đè "b":2)
# Chèn "c":3 → {"a":1,"b":20,"c":3}
# Kết quả cuối cùng:
# {"a":1,"b":20,"c":3}

# Using the union operator
result2 = d1 | d2
print(result2)

# Using the update() method
d3 = d1.copy()
d3.update(d2)
print(d3)

