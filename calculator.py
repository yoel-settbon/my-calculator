import os
def Menu():
    print ("you want to do a operation with one or two operators ?")
    print ("1. One operator")
    print ("2. Two operators")
    print ("3. Quit")
    choice = input("Do your choice : ")
    os.system("cls")
    if choice == "1":
        print ("So, you choose to do a operation with one operator : ")
        return calcul()
    elif choice  == "2":
        print ("So, you choose to do a operation with 3 numbers, pick three numbers : ")
        return multiple_operators()
    elif choice  == "3":
        print ("Goodbye ! See you soon !")
def multiple_operators():
        a = float(input("Pick you're first number : "))
        operator = input("Pick an operator : ( +, *, -, / ) ")
        if operator != "/" and operator != "*" and operator != "+" and operator != "-":
                print("You've making a mistake, pick an operator between +, *, -, / : ")
                return multiple_operators()
        b = float(input("Pick you're second number : "))
        operator_ = input("Pick an operator : ( +, *, -, / ) ")
        if operator != "/" and operator != "*" and operator != "+" and operator != "-":
                print("You've making a mistake, pick an operator between +, *, -, / : ")
                return multiple_operators()
        c = float(input("Pick you're third number : "))
        if operator == "+" and operator_ == "+" :
            print(f"The result is : {a + b + c}")
            return Menu()
        elif operator == "+" and operator_ == "-" :
            print(f"The result is : {a + b - c}")
            return Menu()
        elif operator == "-" and operator_== "+" :
            print(f"The result is : {a - b + c}")
            return Menu()
        elif operator == "-" and operator_ == "-" :
            print(f"The result is : {a - b - c}")
            return Menu()  
        elif operator == "*" and operator_ == "*" :
            print(f"The result is : {a * b * c}")
            return Menu()
        elif operator == "*" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print(f"The result is : {a * b / c}")
            return Menu()
        elif operator == "/" and operator_ == "*" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print(f"The result is : {a / b * c}")
            return Menu()
        elif operator == "*" and operator_ == "+" :
            print(f"The result is : {a * b + c}")
            return Menu()
        elif operator == "*" and operator_ == "-" :
            print(f"The result is : {a * b - c}")
            return Menu()
        elif operator == "+" and operator_ == "*" :
            print(f"The result is : {b * c + a}")
            return Menu()
        elif operator == "-" and operator_ == "*" :
            print(f"The result is : {b * c - a}")
            return Menu()
        elif operator == "/" and operator_ == "/" :
            if b or c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print(f"The result is : {a / b / c}")
            return Menu()
        elif operator == "/" and operator_ == "+" :
            if b  == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print(f"The result is : {a / b + c}")
            return Menu()
        elif operator == "/" and operator_ == "-" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print(f"The result is : {a / b - c}")
            return Menu()
        elif operator == "+" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print (f"The result is : {b / c + a}")
            return Menu()
        elif operator == "-" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print(f"The result is : {b / c - a}")
            return Menu()
        elif operator == "/" and operator_ == "*" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print(f"The result is : {a / b * c}")
            return Menu()
        elif operator == "+" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators() 
            print(f"The result is : {b / c + a}")
            return Menu()
        elif operator == "-" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            print(f"The result is : {b / c - a}")
            return Menu()
        elif operator == "*" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators() 
            print(f"The result is : {a * b / c}")
            return Menu()
def calcul():
    print ("Pick your opperation : ")
    print ("1. Addition")
    print ("2. Substraction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Percentage")
    print ("6. Return to the main menu")
    choice = input("Pick an opperation : ")
    os.system("cls")
    if choice == "1":
        print ("So, you choose to do a addition, pick two numbers : ")
        a = float(input("Pick you're firt number : "))
        b = float(input("Pick tou're second number : "))
        print(f"The result is : {a + b}")
        return Menu()
    elif choice == "2":
        print ("So, you choose to do a substraction, pick two numbers : ")
        a = float(input("Pick you're first number : "))
        b = float(input("Pick you're second number : "))
        print(f"The result is : {a - b}")
        return Menu()
    elif choice  == "3":
        print ("So, you choose to do a multiplication, pick two numbers : ")
        a = float(input("Pick you're first number : "))
        b = float(input("Pick you're second number : "))
        print(f"The result is : {a * b}")   
        return Menu()
    elif choice  == "4":
        print ("So, you choose to do a division, pick two numbers : ")
        a = float(input("Pick you're first number : "))
        b = float(input("Pick you're second number : "))
        if b == 0:
            print("you can't divide by 0 : ")
            return calcul()
        print(f"The result is : {a / b}")
        return Menu()
    elif choice  == "5":
        print ("So, you choose to do a percentage, pick two numbers : ")       
        a = float(input("Pick you're first number : "))
        b = float(input("Pick you're second number : "))
        print(f"The result is : {a % b}")
        return Menu()
    elif choice  == "6":
        return Menu()
    else:
        print("No you've making a mistake, pick a number between 1 and 6 : ")
        return calcul()
Menu()