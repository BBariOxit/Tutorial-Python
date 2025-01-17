#Cach 1
num1 = 1 
num2 = 2
print("tong 2 so la",num1 + num2) 
#cach 2
def Add(a,b):
    return a + b
print("Tong 2 so la",Add(num1,num2))
#cach 3
import operator
Tong = operator.add(num1, num2)
print("tong 2 so la :", Tong)
#cach 4
Add_number = lambda x,y:x+y 
num1 = 1 
num2 = 2
Tong2 = Add_number(num1,num2)
print("tong 2 so la :", Tong2)
#cach 5
def CongBangDeQuy(x, y):
    if y == 0:
        return x
    else:
        return CongBangDeQuy(x + 1, y - 1)
    
print(f"tong 2 so {num1} va {num2} la:",CongBangDeQuy(num1,num2))