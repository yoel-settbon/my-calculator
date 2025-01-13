def calcul():
    print("Welcome to the calculator")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    choice = input("Choose an opperation : ")
    if choice == "1":
        a = float(input("Choose you're firt number : "))
        b = float(input("Choose tou're second number : "))
        print(f"The result is : {a + b}")
    elif choice == "2":
        a = float(input("Choose you're first number : "))
        b = float(input("Choose you're second number : "))
        print(f"The result is : {a - b}")
    elif choice == "3":
        a = float(input("Choose you're first number : "))
        b = float(input("Choose you're second number : "))
        print(f"The result is : {a * b}")
    elif choice == "4":
        a = float(input("Choose you're first number : "))
        b = float(input("Choose you're second number : "))
        print(f"The result is : {a / b}")
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid choise")
calcul()