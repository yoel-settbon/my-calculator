import os

def save_history(result):
    try:
        with open("calculs_historique.txt", "a") as file:
            file.write(result + "\n")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement dans le fichier : {e}")
        
def Menu():
    try:
        print ("you want to do a operation with one or two operators ?")
        print ("1. One operator")
        print ("2. Two operators")
        print ("3. Show history")
        print ("4. Quit")
        choice = input("Do your choice 1, 2 or 3 : ")
        os.system("cls")
        if choice == "1":
            print ("So, you choose to do a operation with one operator : ")
            return calcul()
        elif choice  == "2":
            print ("So, you choose to do a operation with 3 numbers, pick three numbers : ")
            return multiple_operators()
        elif choice  == "3":
            print ("You're gonna see the history of your calculations : ")
            with open("calculs_historique.txt", "r") as file:
                for line in file:
                    print(line.strip())
        elif choice  == "4":
            print ("Goodbye ! See you soon !")
        else:
            print("No you've making a mistake, pick a number between 1 and 3 : ")
            return Menu()
    except KeyboardInterrupt:
        print("\nYou're already leaving. Goodbye, see you soon!")
        exit()

def multiple_operators():
    try:
        a = float(input("Pick you're first number : "))
        operator = input("Pick an operator : ( +, *, -, / ) ")
        if operator != "/" and operator != "*" and operator != "+" and operator != "-":
            print("You've making a mistake, pick an operator between +, *, -, / : ")
            return multiple_operators()
        b = float(input("Pick you're second number : "))
        operator_ = input("Pick an operator : ( +, *, -, / ) ")
        c = float(input("Pick you're third number : "))
        if operator == "+" and operator_ == "+" :
            result=f"The result is : {a + b + c}"
            print(result)
            save_history(f"Operation: {a} + {b} + {c} = {a + b + c}")
            return Menu()
        elif operator == "+" and operator_ == "-" :
            result=f"The result is : {a + b - c}"
            print(result)
            save_history(f"Operation: {a} + {b} - {c} = {a + b - c}")
            return Menu()
        elif operator == "-" and operator_== "+" :
            result=f"The result is : {a - b + c}"
            print(result)
            save_history(f"Operation: {a} - {b} + {c} = {a - b + c}")
            return Menu()
        elif operator == "-" and operator_ == "-" :
            result=f"The result is : {a - b - c}"
            print(result)
            save_history(f"Operation: {a} - {b} - {c} = {a - b - c}")
            return Menu()  
        elif operator == "*" and operator_ == "*" :
            result=f"The result is : {a * b * c}"
            print(result)
            save_history(f"Operation: {a} * {b} * {c} = {a * b * c}")
            return Menu()
        elif operator == "*" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a * b / c}"
            print(result)
            save_history(f"Operation: {a} * {b} / {c} = {a * b / c}")
            return Menu()
        elif operator == "/" and operator_ == "*" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b * c}"
            print(result)
            save_history(f"Operation: {a} / {b} * {c} = {a / b * c}")
            return Menu()
        elif operator == "*" and operator_ == "+" :
            result=f"The result is : {a * b + c}"
            print(result)
            save_history(f"Operation: {a} * {b} + {c} = {a * b + c}")
            return Menu()
        elif operator == "*" and operator_ == "-" :
            result=f"The result is : {a * b - c}"
            print(result)
            save_history(f"Operation: {a} * {b} - {c} = {a * b - c}")
            return Menu()
        elif operator == "+" and operator_ == "*" :
            result=f"The result is : {b * c + a}"
            print(result)
            save_history(f"Operation: {b} * {c} + {a} = {b * c + a}")
            return Menu()
        elif operator == "-" and operator_ == "*" :
            result=f"The result is : {b * c - a}"
            print(result)
            save_history(f"Operation: {b} * {c} - {a} = {b * c - a}")
            return Menu()
        elif operator == "/" and operator_ == "/" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            elif c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b / c}"
            print(result)
            save_history(f"Operation: {a} / {b} / {c} = {a / b / c}")
            return Menu()
        elif operator == "/" and operator_ == "+" :
            if b  == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b + c}"
            print(result)
            save_history(f"Operation: {a} / {b} + {c} = {a / b + c}")
            return Menu()
        elif operator == "/" and operator_ == "-" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b - c}"
            print(result)
            save_history(f"Operation: {a} / {b} - {c} = {a / b - c}")
            return Menu()
        elif operator == "+" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {b / c + a}"
            print(result)
            save_history(f"Operation: {b} / {c} + {a} = {b / c + a}")
            return Menu()
        elif operator == "-" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {b / c - a}"
            print(result)
            save_history(f"Operation: {b} / {c} - {a} = {b / c - a}")
            return Menu()
        elif operator == "/" and operator_ == "*" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b * c}"
            print(result)
            save_history(f"Operation: {a} / {b} * {c} = {a / b * c}")
            return Menu()
        elif operator == "+" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators() 
            result=f"The result is : {b / c + a}"
            print(result)
            save_history(f"Operation: {b} / {c} + {a} = {b / c + a}")
            return Menu()
        elif operator == "-" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {b / c - a}"
            print(result)
            save_history(f"Operation: {b} / {c} - {a} = {b / c - a}")
            return Menu()
        elif operator == "*" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators() 
            result=f"The result is : {a * b / c}"
            print(result)
            save_history(f"Operation: {a} * {b} / {c} = {a * b / c}")
            return Menu()
    except KeyboardInterrupt:
        print("\nOperation interrupted. Returning to main menu...")
        return Menu()

def calcul():
    try:
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
            result=f"The result is : {a + b}"
            print(result)
            save_history(f"Operation: {a} + {b} = {a + b}")
            return Menu()
        elif choice == "2":
            print ("So, you choose to do a substraction, pick two numbers : ")
            a = float(input("Pick you're first number : "))
            b = float(input("Pick you're second number : "))
            result=f"The result is : {a - b}"
            print(result)
            save_history(f"Operation: {a} - {b} = {a - b}")
            return Menu()
        elif choice  == "3":
            print ("So, you choose to do a multiplication, pick two numbers : ")
            a = float(input("Pick you're first number : "))
            b = float(input("Pick you're second number : "))
            result=f"The result is : {a * b}"   
            print(result)
            save_history(f"Operation: {a} * {b} = {a * b}")
            return Menu()
        elif choice  == "4":
            print ("So, you choose to do a division, pick two numbers : ")
            a = float(input("Pick you're first number : "))
            b = float(input("Pick you're second number : "))
            if b == 0:
                print("you can't divide by 0 : ")
                return calcul()
            result=f"The result is : {a / b}"
            print(result)
            save_history(f"Operation: {a} / {b} = {a / b}")
            return Menu()
        elif choice  == "5":
            print ("So, you choose to do a percentage, pick two numbers : ")       
            a = float(input("Pick you're first number : "))
            b = float(input("Pick you're second number : "))
            result=f"The result is : {a % b}"
            print(result)
            save_history(f"Operation: {a} % {b} = {a % b}")
            return Menu()
        elif choice  == "6":
            print ("So you're back to the main menu.")
            return Menu()
        else:
            print("You've making a mistake, pick a number between 1 and 6 : ")
            return calcul()
    except KeyboardInterrupt:
        print("\nOperation interrupted. You're back to the main menu.")
        return Menu()

Menu()
