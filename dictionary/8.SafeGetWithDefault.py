# Input: d={"id":7}; k="name"
# Output: "N/A"
d = {"id":7}
k = "name"
val = d.get(k, "N/A")
print(val)
# using if ... else
if k in d:
    val2 = d[k]
else:
    val2 = "N/A"
print(val2)
