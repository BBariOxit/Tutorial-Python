n = int(input("nhap so nguyen bat ki:"))

def KtraFibonacci(n):
    a,b = 0,1
    while b < n:
        a,b =b, a+b
    return b ==  n

if(KtraFibonacci(n)):
    print(f"so {n} la so fibonacci")
else:
    print(f"so {n} ko la so fibonacci")