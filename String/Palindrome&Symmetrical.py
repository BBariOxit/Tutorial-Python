#Python program to check whether the string is Symmetrical or Palindrome
a = "amaama"
#cach1:slicing
ChiaDoi = len(a) // 2
sym = a[:ChiaDoi] == a[ChiaDoi:] if len(a) % 2 == 0 else a[:ChiaDoi] == a[ChiaDoi+1:]
pal = a == a[::-1]
print("============Cach1============")
print(f"'{a}' la chuoi symmetrical" if sym else "'{a}' ko la chuoi symmetrical")
print(f"'{a}' la chuoi palindrome" if pal else "'{a}' ko la chuoi palindrome")
#cach2:2 pointer
checkPal = True
i, j =0 ,len(a) -1 
while i < j:
    if a[i] != a[j]:
        checkPal = False
        break
    i += 1 
    j -= 1

checkSym = True
for i in range(ChiaDoi):
    if len(a) % 2 ==0:
        if a[i] != a[i + ChiaDoi]:
            checkSym = False
            break
    else:
        if a[i] != a[i + ChiaDoi + 1]:
            checkSym = False
            break
print("============Cach2============")
print(f"'{a}' la chuoi symmetrical" if checkSym else "'{a}' ko la chuoi symmetrical")
print(f"'{a}' la chuoi palindrome" if checkPal else "'{a}' ko la chuoi palindrome")
#cach3: de quy(recursion)
def CheckPalindrome(a, i=0):
    if i >= len(a) // 2:
        return True
    return a[i] == a[-(i + 1)] and CheckPalindrome(a, i +1)

def CheckSymmetrical(a, ChiaDoi , i = 0):
    if i >= ChiaDoi:
        return True
    if len(a) % 2 ==0:
        return a[i] == a[i + ChiaDoi] and CheckSymmetrical(a, ChiaDoi, i + 1)
    else:
        return a[i] == a[i + ChiaDoi + 1] and CheckSymmetrical(a, ChiaDoi, i + 1)
print("============Cach3============")
print(f"'{a}' la chuoi symmetrical" if CheckSymmetrical(a, ChiaDoi) else "'{a}' ko la chuoi symmetrical")
print(f"'{a}' la chuoi palindrome" if CheckPalindrome(a) else "'{a}' ko la chuoi palindrome")
#CACH4: reversed()
checkPal2 = list(a) == list(reversed(a))
checkSym2 = a[:ChiaDoi] == a[ChiaDoi:] if len(a) % 2 == 0 else a[:ChiaDoi] == a[ChiaDoi+1:]
print("============Cach4============")
print(f"'{a}' la chuoi symmetrical" if checkPal2 else "'{a}' ko la chuoi symmetrical")
print(f"'{a}' la chuoi palindrome" if checkSym2 else "'{a}' ko la chuoi palindrome")