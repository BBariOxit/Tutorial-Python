a = int((input("nhap mot so nguyen bat ky:")))
print(type(a))
num = input("nhap mot list cac so nguyen tuy y cach nhau bang dau phay:")
list = num.split(',')
print(list)
def CheckNum(listOfNum,a):
    for x in listOfNum:
        if(a == int(x)):
            return True
    return False

if(CheckNum(list,a)):
    print("so ban nhap co trong list")
else:
    print("so ban nhap khong co trong list")
