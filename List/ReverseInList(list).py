#Đảo ngược list trong Python
#CACH1: sd arr.reverse()
arr1 = [1,2,3,4,5]
arr1.reverse()
# print(f"===={arr1}====")
print(arr1)
#CACH2: list slicing
arr2 = [1,2,3,4,5]
newArr2 = arr2[::-1]
# print(f"===={arr2}====")
print(newArr2)
#CACH3: reverse(arr)
arr3 = [1,2,3,4,5]
rel = list(reversed(arr3))
# print(f"===={arr3}====")
print(rel)
#CACH4: loop va insert()
arr4 = [1,2,3,4,5]
newArr4 = []
for i in arr4:
    newArr4.insert(0,i)
# print(f"===={arr4}====")
print(newArr4)
#CACH5: sd loop in place
arr5 = [1,2,3,4,5]
start , end = 0, 4
def Swap(start,end,arr):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
# print(f"===={arr5}====")
print(Swap(start,end,arr5))
#CACH5:list comprehension
arr6 =[1,2,3,4,5]
newArr6 = [arr6[i]for i in range(len(arr6)-1,-1,-1)]
print(newArr6)

