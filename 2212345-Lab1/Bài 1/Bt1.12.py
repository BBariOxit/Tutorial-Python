import calendar
import os
def XuatLichThang():
    year = int(input("nhap nam ma ban muon:"))
    month = int(input("nhap thang (1-12):"))
    if(1 <= month <= 12):
        os.system('cls')
        print("\n", calendar.month(year,month))
    else:  
        print("thang ban nhap khong ton tai!, vui long nhap lai")
XuatLichThang(); 

