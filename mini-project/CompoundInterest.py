principle = 0
rate = 0
time = 0

while principle <= 0:
# while true:
    principle = float(input("enter the principle amount:"))
    if principle <=0:
        print("the principle can't be less than or equal to zero")
    elif principle < 1000:
        print("you are a fucking poor guy :)))")
#   else:
#       break

while rate <= 0:
# while true:
    rate = float(input("enter the interest rate:"))
    if rate <=0:
        print("interest rate can't be less than or equal to zero")
#   else:
#       break

while time <= 0:
# while true:
    time = int(input("enter the time in years:"))
    if time <=0:
        print("time can't be less than or equal to zero")
#   else:
#       break
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years:{total:.3f}")