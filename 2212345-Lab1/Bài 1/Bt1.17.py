print("KIEM TRA XEM SO BAN NHAP CO NAM TRONG KHOANG 100 DON VI SO VOI 1000 HOAC 2000 KHONG")
a = int(input("nhap mot so bat ky de kiem tra:"))

def CheckNumber(a):
    return (abs(1000 - a) <= 100) or (abs(2000 - a) <= 100)

# def CheckNumber(a):
#     if((abs(1000 - a) <= 100) or (abs(2000 - a) <= 100)):
#         return "true"
#     else:
#         return "false"
print(CheckNumber(a))