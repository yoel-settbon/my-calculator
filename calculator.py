import os
def calcul():
    print ("Pick your opperation : ")
    print ("1. Addition")
    print ("2. Substraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Percentage")
    print ("6. Operation with 3 numbers")
    print ("7. Quit")
    choice = input("Pick an opperation : ")
    os.system("cls")
    if choice == "1":
        print ("So, you choose to do a addition, pick two numbers : ")
        a = float(input("Pick you're firt number : "))
        b = float(input("Pick tou're second number : "))
        print(f"The result is : {a + b}")
    elif choice == "2":
        print ("So, you choose to do a substraction, pick two numbers : ")
        a = float(input("Pick you're first number : "))
        b = float(input("Pick you're second number : "))
        print(f"The result is : {a - b}")
    elif choice  == "3":
        print ("So, you choose to do a multiplication, pick two numbers : ")
        a = float(input("Pick you're first number : "))
        b = float(input("Pick you're second number : "))
        print(f"The result is : {a * b}")
    elif choice  == "4":
        print ("So, you choose to do a division, pick two numbers : ")
        a = float(input("Pick you're first number : "))
        b = float(input("Pick you're second number : "))
        if b == 0:
            print("you can't divide by 0 : ")
            return calcul()
        print(f"The result is : {a / b}")
    elif choice  == "5":
        print ("So, you choose to do a percentage, pick two numbers : ")       
        a = float(input("Pick you're first number : "))
        b = float(input("Pick you're second number : "))
        print(f"The result is : {a % b}")
    elif choice  == "6":
        print ("So, you choose to do a operation with 3 numbers, pick three numbers : ")
        a = float(input("Pick you're first number : "))
        operator = input("Pick an operator : ( +, *, -, / ) ")
        b = float(input("Pick you're second number : "))
        operator_ = input("Pick an operator : ( +, *, -, / ) ")
        c = float(input("Pick you're third number : "))
        if operator == "+" and operator_ == "+" :
            print(f"The result is : {a + b + c}")
        elif operator == "+" and operator_ == "-" :
            print(f"The result is : {a + b - c}")
        elif operator == "-" and operator_== "+" :
            print(f"The result is : {a - b + c}")
        elif operator == "-" and operator_ == "-" :
            print(f"The result is : {a - b - c}")
        elif operator == "*" and operator_ == "*" :
            print(f"The result is : {a * b * c}")
        elif operator == "*" and operator_ == "/" :
            print(f"The result is : {a * b / c}")
        elif operator == "/" and operator_ == "*" :
            print(f"The result is : {a / b * c}")
        elif operator == "*" and operator_ == "+" :
            print(f"The result is : {a * b + c}")
        elif operator == "*" and operator_ == "-" :
            print(f"The result is : {a * b - c}")
        elif operator == "+" and operator_ == "*" :
            print(f"The result is : {b * c + a}")
        elif operator == "-" and operator_ == "*" :
            print(f"The result is : {b * c - a}")
        elif operator == "/" and operator_ == "/" :
            print(f"The result is : {a / b / c}")
        elif operator == "/" and operator_ == "+" :
            print(f"The result is : {a / b + c}")
        elif operator == "/" and operator_ == "-" :
            print(f"The result is : {a / b - c}")
        elif operator == "+" and operator_ == "/" :
            print (f"The result is : {b / c + a}")
        elif operator == "-" and operator_ == "/" :
            print(f"The result is : {b / c - a}")
    elif choice  == "7":
        print("Have a nice day, see you later ! ")
    else:
        print("No you've making a mistake, pick a number between 1 and 6 : ")
        return calcul()
calcul()