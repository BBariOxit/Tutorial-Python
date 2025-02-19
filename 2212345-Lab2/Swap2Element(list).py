txt = input("nhap mot mang cac so cach nhau bang dau phay:")
arr = [int(i) for i in txt.split(',')]
#CACH1:hoan doi truc tiep
arr[2], arr[3] = arr[3], arr[2]
#CACH2:temp
temp = arr[2]
arr[2] = arr[3]
arr[3] = temp