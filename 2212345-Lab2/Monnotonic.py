txt = input("nhap mang ktra(cach nhau bang dau phay):")
newArr = [int(x) for x in txt.split(',')]
#cach1:duyet qua tung phan tu trong mang
print(type(newArr[1]))
def KtraMonotonic(arr):
    inc = dec = True
    for i in range(1,len(arr)):
        if arr[i] < arr[i - 1]:
            inc = False
        elif arr[i] > arr[i - 1]:
            dec = False
    return inc or dec

def KtraMonotonic2(arr):
    inc = dec = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            inc = False
        elif arr[i] < arr[i + 1]:
            dec = False
    return inc or dec

#cach2:list comprehension
def KtraMonotonic3(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or \
           all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

print(KtraMonotonic(newArr))
print(KtraMonotonic2(newArr))
print(KtraMonotonic3(newArr))