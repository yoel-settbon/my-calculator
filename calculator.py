import os     # import the os module to clear the console
import time   # import the time module to use the sleep function

def delete_history():
    # function to delete the history of all the calculs
    try:
        with open("calculs_history.txt", "w") as file:
            file.write("")
    except Exception as e:
    # if there is an error, it will return an error message
        print(f"Error deleting to files : {e}")
def save_history(result):
    # function to save the history of all the calculs, and write them in text file
    try:
        with open("calculs_history.txt", "a") as file:
            file.write(result + "\n")
    except Exception as e:
        print(f"Error saving to files : {e}")
        
def Menu():
    # function to display the main menu of the calculator
    try:
        print ("Choose what you want to do ?")
        print ("1. One operator")
        print ("2. Two operators")
        print ("3. Show history")
        print ("4. Delete history")
        print ("5. Quit")
        choice = input("Choose what you want to do : ")
        os.system("cls")
    # after you've picked a number, the menu will be clear
        if choice == "1":
            print ("So, you chose to do a operation with one operator : ")
            return calcul()
        elif choice  == "2":
            print ("So, you chose to do an operation with 3 numbers, pick three numbers : ")
            return multiple_operators()
        elif choice  == "3":
            print ("This is the history of your calculations : ")
            with open("calculs_history.txt", "r") as file:
                for line in file:
                    print(line.strip())
            return Menu()
        elif choice  == "4":
            print ("Your history has been deleted : ")
            delete_history()
            return Menu()
        elif choice  == "5":
            print ("Goodbye ! See you soon !")
            time.sleep(2)
            os.system("cls")
        else:
        # if you've picked a number that is not in the menu, it will return an error message
            print("No you've made a mistake, pick a number between 1 and 5 : ")
            return Menu()
    except KeyboardInterrupt:
        # you can quit the program by pressing ctrl + c
        print("\nYou're already leaving. Goodbye, see you soon!")
        time.sleep(2)
        os.system("cls")
        exit()

def multiple_operators():
    # function to do an operation with 3 numbers and 2 operators
    try:
        try:

            a = float(input("Pick your first number : "))
        except ValueError:
            # if your choice is not a number, you will go back to the previous step
            print("You've made a mistake, pick a number : ")
            return multiple_operators()
        operator = input("Pick an operator : ( +, *, -, / ) ")
        if operator != "/" and operator != "*" and operator != "+" and operator != "-":
        # if you've picked an operator that is not in the list, you will go back to the previous step
            print("You've made a mistake, pick an operator between +, *, -, / : ")
            return multiple_operators()
        try:
            b = float(input("Pick your second number : "))
        except ValueError: 
            print("You've made a mistake, pick a number : ")
            return multiple_operators()
        operator_ = input("Pick an operator : ( +, *, -, / ) ")
        try :
            c = float(input("Pick your third number : "))
        except ValueError:
            print("You've made a mistake, pick a number : ")
            return multiple_operators()
        if operator == "+" and operator_ == "+" :
        # all the conditions to calculs with 2 operators, with priority, impossible calculs
            result=f"The result is : {a + b + c}"
            print(result)
            save_history(f" {a} + {b} + {c} = {a + b + c}")
            return Menu()
        elif operator == "+" and operator_ == "-" :
            result=f"The result is : {a + b - c}"
            print(result)
            save_history(f" {a} + {b} - {c} = {a + b - c}")
            return Menu()
        elif operator == "-" and operator_== "+" :
            result=f"The result is : {a - b + c}"
            print(result)
            save_history(f" {a} - {b} + {c} = {a - b + c}")
            return Menu()
        elif operator == "-" and operator_ == "-" :
            result=f"The result is : {a - b - c}"
            print(result)
            save_history(f" {a} - {b} - {c} = {a - b - c}")
            return Menu()  
        elif operator == "*" and operator_ == "*" :
            result=f"The result is : {a * b * c}"
            print(result)
            save_history(f" {a} * {b} * {c} = {a * b * c}")
            return Menu()
        elif operator == "*" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a * b / c}"
            print(result)
            save_history(f" {a} * {b} / {c} = {a * b / c}")
            return Menu()
        elif operator == "/" and operator_ == "*" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b * c}"
            print(result)
            save_history(f" {a} / {b} * {c} = {a / b * c}")
            return Menu()
        elif operator == "*" and operator_ == "+" :
            result=f"The result is : {a * b + c}"
            print(result)
            save_history(f" {a} * {b} + {c} = {a * b + c}")
            return Menu()
        elif operator == "*" and operator_ == "-" :
            result=f"The result is : {a * b - c}"
            print(result)
            save_history(f" {a} * {b} - {c} = {a * b - c}")
            return Menu()
        elif operator == "+" and operator_ == "*" :
            result=f"The result is : {b * c + a}"
            print(result)
            save_history(f" {b} * {c} + {a} = {b * c + a}")
            return Menu()
        elif operator == "-" and operator_ == "*" :
            result=f"The result is : {b * c - a}"
            print(result)
            save_history(f" {b} * {c} - {a} = {b * c - a}")
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
            save_history(f" {a} / {b} / {c} = {a / b / c}")
            return Menu()
        elif operator == "/" and operator_ == "+" :
            if b  == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b + c}"
            print(result)
            save_history(f" {a} / {b} + {c} = {a / b + c}")
            return Menu()
        elif operator == "/" and operator_ == "-" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b - c}"
            print(result)
            save_history(f" {a} / {b} - {c} = {a / b - c}")
            return Menu()
        elif operator == "+" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {b / c + a}"
            print(result)
            save_history(f" {b} / {c} + {a} = {b / c + a}")
            return Menu()
        elif operator == "-" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {b / c - a}"
            print(result)
            save_history(f" {b} / {c} - {a} = {b / c - a}")
            return Menu()
        elif operator == "/" and operator_ == "*" :
            if b == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {a / b * c}"
            print(result)
            save_history(f" {a} / {b} * {c} = {a / b * c}")
            return Menu()
        elif operator == "+" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators() 
            result=f"The result is : {b / c + a}"
            print(result)
            save_history(f" {b} / {c} + {a} = {b / c + a}")
            return Menu()
        elif operator == "-" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators()
            result=f"The result is : {b / c - a}"
            print(result)
            save_history(f" {b} / {c} - {a} = {b / c - a}")
            return Menu()
        elif operator == "*" and operator_ == "/" :
            if c == 0:
                print("you can't divide by 0 : ")
                return multiple_operators() 
            result=f"The result is : {a * b / c}"
            print(result)
            save_history(f" {a} * {b} / {c} = {a * b / c}")
            return Menu()
    except KeyboardInterrupt:
        print("\nOperation interrupted. You're back to the main menu.")
        return Menu()

def calcul():
    # menu to do a calcul with one operator
    try:
        print ("Pick your opperation : ")
        print ("1. Addition")
        print ("2. Substraction")
        print ("3. Multiplication")
        print ("4. Division")
        print ("5. Return to the main menu")
        choice = input("Pick an opperation : ")
        os.system("cls")
        if choice == "1":
            print ("So, you chose to do an addition, pick two numbers : ")
            try:
                a = float(input("Pick your firt number : "))
            except ValueError:
                print("You've made a mistake, pick a number : ")
                return calcul()
            try:
                b = float(input("Pick your second number : "))
            except ValueError:
                print("You've made a mistake, pick a number : ")
                return calcul()
            result=f"The result is : {a + b}"
            print(result)
            save_history(f" {a} + {b} = {a + b}")
            return Menu()
            # when you have the result you go back to the main menu
        elif choice == "2":
            print ("So, you chose to do a substraction, pick two numbers : ")
            try:
                a = float(input("Pick your firt number : "))
            except ValueError:
                print("You've made a mistake, pick a number : ")
                return calcul()
            try:
                b = float(input("Pick your second number : "))
            except ValueError:
                print("You've made a mistake, pick a number : ")
                return calcul()
            result=f"The result is : {a - b}"
            print(result)
            save_history(f" {a} - {b} = {a - b}")
            return Menu()
        elif choice  == "3":
            print ("So, you chose to do a multiplication, pick two numbers : ")
            try:
                a = float(input("Pick your firt number : "))
            except ValueError:
                print("You've made a mistake, pick a number : ")
                return calcul()
            try:
                b = float(input("Pick your second number : "))
            except ValueError:
                print("You've made a mistake, pick a number : ")
                return calcul()
            result=f"The result is : {a * b}"   
            print(result)
            save_history(f" {a} * {b} = {a * b}")
            return Menu()
        elif choice  == "4":
            print ("So, you chose to do a division, pick two numbers : ")
            try:
                a = float(input("Pick your firt number : "))
            except ValueError:
                print("You've made a mistake, pick a number : ")
                return calcul()
            try:
                b = float(input("Pick your second number : "))
            except ValueError:
                print("You've made a mistake, pick a number : ")
                return calcul()
            if b == 0:
                print("you can't divide by 0 : ")
                return calcul()
            result=f"The result is : {a / b}"
            print(result)
            save_history(f" {a} / {b} = {a / b}")
            return Menu()
        elif choice  == "5":
            print ("So you're back to the main menu.")
            return Menu()
        else:
            print("You're making a mistake, pick a number between 1 and 5 : ")
            return calcul()
    except KeyboardInterrupt:
        print("\nOperation interrupted. You're back to the main menu.")
        return Menu()

Menu()