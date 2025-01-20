def menu():
    print("1 - calculate with 2 terms")
    print("2 - calculate with 3 terms")
    print("3 - Quit")

    while True:
        try:
            user_input = int(input("choose an option : 1, 2 or 3 "))
        except ValueError:
            print("incorrect entry")
            menu()

        if user_input == 1:
            print("first option")
            calculator()

        elif user_input == 2:
            print("second option")
            plusieurs_terme()
    
        elif user_input == 3:
            print("Quit")
            break
  
        else:
            print("error")


def calculator():

    while True:
        try:
            first_term = float(input("number 1 : "))
            break
        except:
            ValueError
            print("incorrect entry")

    operator = input("choose an operator : '+', '-', '*' or '/' : ")

    while True:
        try:
            second_term = float(input("number 2 : "))
            break
        except:
            ValueError
            print("incorrect entry")

    print(first_term, operator, second_term)

    if operator == "+":
        print(first_term + second_term)

    elif operator == "-":
        print(first_term - second_term)

    elif operator == "*":
        print(first_term * second_term)

    elif operator == "/":
        try:
            first_term / second_term
            print(first_term / second_term)
        except ZeroDivisionError:
            print("invalid operation")
            print("cannot divide by zero")

    else:
        print("invalid operation")


def plusieurs_terme():

    first_number = int(input("enter a number : "))
    operator1 = input("choose an operation : ")
    second_number = int(input("enter a second number : "))
    operator2 = input("choose an other operation : ")
    third_number = int(input("enter a third number : "))

    if operator1 == "*" and operator2 == "+":
        print(first_number * second_number + third_number)
    elif operator1 == "*" and operator2 == "-":
        print(first_number * second_number - third_number)
    elif operator1 == "*" and operator2 == "*":
        print(first_number * second_number * third_number)
    elif operator1 == "*" and operator2 == "/":
        if third_number == 0:
            print("invalid operation")
        else:
            print(first_number * second_number / third_number)
    elif operator1 == "+" and operator2 == "+":
        print(first_number + second_number + third_number)
    elif operator1 == "+" and operator2 == "-":
        print(first_number + second_number - third_number)
    elif operator1 == "+" and operator2 == "*":
        print(first_number + second_number * third_number)
    elif operator1 == "+" and operator2 == "/":
        if third_number == 0:
            print("invalid operation")
        else:
            print(first_number + second_number / third_number)

    elif operator1 == "/" and operator2 == "+":
        if second_number == 0:
            print("invalid operation")
        else:
            print(first_number / second_number + third_number)
    elif operator1 == "/" and operator2 == "-":
        if second_number == 0:
            print("invalid operation")
        else:
            print(first_number / second_number - third_number)
    elif operator1 == "/" and operator2 == "/":
        if second_number == 0 or third_number == 0:
            print("invalid operation")
        else:
            print(first_number / second_number / third_number)
    elif operator1 == "/" and operator2 == "*":
        if second_number == 0:
            print("invalid operation")
        else:
            print(first_number / second_number * third_number)

    elif operator1 == "-" and operator2 == "-":
        print(first_number - second_number - third_number)
    elif operator1 == "-" and operator2 == "+":
        print(first_number - second_number + third_number)
    elif operator1 == "-" and operator2 == "*":
        print(first_number - second_number * third_number)
    elif operator1 == "-" and operator2 == "/":
        if third_number == 0:
            print("invalid operation")
        else:
            print(first_number - second_number / third_number)
    else:
        print("wrong entry")

menu()