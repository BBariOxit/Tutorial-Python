txt = input("nhap mot loat cac so tu 0 - 9 cach nhau boi dau phay:")
number = input("nhap mot so ma ban muon dem so lan xuat hien trong list tren:")
list = txt.split(',')

def CountNumberInList(Ds,n):
    # lenght = len(list)
    count = 0
    for i in Ds:
        if(i == n):
            count += 1
    return count

print(f"so lan xuat hien cua so {number} la:",CountNumberInList(list,number))
