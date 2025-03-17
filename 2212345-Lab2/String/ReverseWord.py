#Reverse Words in a Given String in Python
#CACH1:split() va join()
a = "Hello World Python"
result = " ".join(a.split()[::-1])
print(result)
#CACH2:loop
b = a.split()
result2= ""
for i in reversed(b):
    result2 += i +" "
print(result2.strip())
#CACH3:stack
stack = []
for i in b:
    stack.append(i)
result3 = ""
while stack:
    result3 += stack.pop() + " "
print(result3.strip())
#CACH4:Recursion
def DaoTu(a):
    if not a:
        return ""
    return a[-1] + " " + DaoTu(a[:-1])
result4 =DaoTu(a.split()).strip()
print(result4)