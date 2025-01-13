def counting(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "You can not divide by zero"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "You can not use % with zero"

# Ask the user to enter inputs
num1 = float(input("Enter you first number : "))
operator = input("Enter the operator : (+, -, *, /, %): ")
num2 = float(input("Enter the second number : "))

# Call the function with the inputs asked to the user
result = counting(num1, operator, num2)
print("Result:", result)