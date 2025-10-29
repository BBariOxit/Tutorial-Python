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
# using try ... except  
try:
    val3 = d[k]
except KeyError:
    val3 = "N/A"
print(val3)