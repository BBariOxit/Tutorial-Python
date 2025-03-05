#Sum of number digits in List in Python
#cach1:LOOP
arr = [123,456, 789]
def TongCacChuSo(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
result = [TongCacChuSo(i) for i in arr]
print(result)
#cach2:list comprehension
result2 = [sum(int(j) for j in str(i)) for i in arr]
print(result2)
#cach3:map()
def TongCacChuSo2(n):
    return sum(int(i) for i in str(n))
result3 = list(map(TongCacChuSo2,arr))
print(result3)