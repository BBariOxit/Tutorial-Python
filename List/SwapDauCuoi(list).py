#hoán đổi phần tử đầu tiên và cuối cùng trong một danh sách
txt = input("Nhap mang cac so cach nhau boi dau phay:")
arr = [int(i) for i in txt.split(',')]

#CACH1
def Swap1(arr): 
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr
print(arr)

#CACH2
def Swap2(arr):
    temp = arr[0]
    arr[0] = arr[len(arr)-1]
    arr[len(arr)-1] = temp
    return arr
print(Swap2(arr))

#CACH3:sdung tuple
def Swap3(arr):
    tpl = arr[-1] , arr[0]
    arr[0] , arr[-1] = tpl
    return arr
print(Swap3(arr))

#CACH4:operator *,unpacking
def Swap4(arr):
    start, *middle, end = arr
    arr = [end, *middle, start]
    return arr
print(Swap4(arr))

#CACH5:slicing
def Swap5(arr):
    if len(arr)>2:
        arr = arr[-1:] + arr[1:-1] + arr[:1]
    return arr
print(Swap5(arr))