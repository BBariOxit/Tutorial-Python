txt = input("nhap mot chuoi bat ky:")

def Check(txt):
    if(txt[:2] == "Is"):
        return txt
    else:
        return "Is" + txt
    
print("chuoi sau khi them Is (neu da co se khong them):", Check(txt))