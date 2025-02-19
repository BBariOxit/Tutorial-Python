#Những cách khác nhau để xóa danh sách trong Python
#CACH: clear()
arr1 = [1,2,3,4]
arr1.clear()
print(arr1)
#CACH2: reassigning
arr2 = [2,3,4,5,5]
arr2 = []
print(arr2)
#CACH3: del
arr3 = [1,2,3,4,5]
del arr3[:]
print(arr3)