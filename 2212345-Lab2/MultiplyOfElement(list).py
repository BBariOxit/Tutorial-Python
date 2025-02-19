txt =input("nhap mang so nguyen cach nhau boi dau phay:")
arr = [int(i) for i in txt.split(',')]
#CACH1:loop
result1 = 1
for i in arr:
    result1 *= i
print(result1)
#CACH2:math.prod()
import math
result2 = math.prod(arr)
print(result2)
#CACH3:reduce() va mul()
from functools import reduce
import operator
result3 = reduce(operator.mul,arr)
print(result3)