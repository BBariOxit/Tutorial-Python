# Input: n=6
# Output: {1:"odd",2:"even",3:"odd",4:"even",5:"odd",6:"even}
# cach 1:loop
n = int(input("nhap so n:"))
d = {}
for i in range(1, n +1):
    if i % 2 == 0:
        d[i] = "even"
    else:
        d[i] = "odd"
print(d)

#cach2: dict comprihension
result = {k: ("even" if k % 2 == 0 else "odd") for k in range(1, n +1)}
print(result)