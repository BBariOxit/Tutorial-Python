operator = input("enter an operator(+ - * /):")
num1 = float(input("enter the 1st number:"))
num2 = float(input("enter the 2nd number:"))

#if operator != "+" and operator != "-" and operator != "*" and operator != "/":
#    print(f"{operator} is not valid operator")
if operator not in ["+", "-", "*", "/"]:
    print(f"{operator} is not valid operator")
elif operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(round(result),3)