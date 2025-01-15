import os

def save_to_history(calculation):
    with open("calculator_history.txt", "a") as file:
        file.write(calculation + "\n")

def show_history():
    try:
        with open("calculator_history.txt", "r") as file:
            content = file.read()
            if content.strip():
                print("History:")
                print(content)
            else:
                print("No history available.")
    except FileNotFoundError:
        print("No history available.")

def clear_history():
    with open("calculator_history.txt", "w") as file:
        file.write(" ")

def calculator():
    while True:
        print("\nMenu:")
        print("1. Perform a calculation")
        print("2. View history")
        print("3. Clear history")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        os.system('cls')
        
        if choice == "1":
            # Perform a calculation
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/" and num2 != 0:
                result = num1 / num2
            else:
                print("Invalid operator or division by zero.")
                continue
            
            calculation = f"{num1} {operator} {num2} = {result}"
            print(f"Result: {result}")
            save_to_history(calculation)
        
        elif choice == "2":
            # View history
            show_history()
        
        elif choice == "3":
            print("History successfully cleaned !")
            clear_history()

        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the calculator
calculator()