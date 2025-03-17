#Python Program to Check if a String is Palindrome or Not
# a = "malayalam"
a = str(input("nhap chuoi :"))
#cach1:two pointer
i , j = 0 , len(a) - 1
check = True
while i < j:
    if a[i] != a[j]:
        check = False
        break
    i +=1
    j -=1
if check:
    print("day la mot chuoi doi xung")
else:
    print("day ko la mot chuoi doi xung")
#cach2:slicing
if a == a[::-1]:
    print("day la mot chuoi doi xung")
else:
    print("day ko la mot chuoi doi xung")
#cach3:reversed()
b = "".join(reversed(a))
if a == b:
    print("day la mot chuoi doi xung")
else:
    print("day ko la mot chuoi doi xung")
#cach4:recursion(De quy), chua toi uu
def CheckDoiXung(a,i,j):
    if i >= j:
        return True
    if a[i] != a[j]:
        return False 
    return CheckDoiXung(a, i+1, j-1)
if CheckDoiXung(a,0, len(a)-1):
    print("day la mot chuoi doi xung")
else:
    print("day ko la mot chuoi doi xung")
#cach5:recursion(De quy),toi uu
def CheckDoiXung2(a):
    if len(a) <= 1:
        return True
    if a[0] != a[-1]:
        return False
    return CheckDoiXung2(a[1:-1])
if CheckDoiXung2(a):
    print("day la mot chuoi doi xung")
else:
    print("day ko la mot chuoi doi xung")
#cach6:loop
c = ""
for i in a:
    c = i + c
if a == c:
    print("day la mot chuoi doi xung")
else:
    print("day ko la mot chuoi doi xung")