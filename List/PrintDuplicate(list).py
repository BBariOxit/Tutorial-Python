#Program to print duplicates from a list of integers in Python
a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
#cach1:set
s = set()
b = []
for i in a:
    if i in s:
        b.append(i)
    else:
        s.add(i)
print(b)
#cach2:nested loop
arr = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j] and a[i] not in arr:
            arr.append(a[i])
print(arr)
#cach3:dict
d = {}

for n in a:
    d[n] = d.get(n, 0) + 1

# Find duplicates by filtering numbers with count > 1
dup = [n for n, c in d.items() if c > 1]

print(dup)