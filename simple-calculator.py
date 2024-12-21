    #Basic Python calculator

operator = input("Choose an operator (+ - * / )")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "":
    print("Please choose an Operator!!!")
else:
    print(f"{operator} is not a valid operator")
