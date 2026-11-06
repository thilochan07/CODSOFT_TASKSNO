"""
Task 2: Simple Calculator
CodSoft Python Programming Internship
Author: Thilochan P
"""

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ValueError("Error: Modulus by zero is not allowed.")
    return a % b

def power(a, b): return a ** b

def display_menu():
    print("\n===============================")
    print("       PYTHON CALCULATOR       ")
    print("===============================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Exit")
    print("===============================")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("[!] Invalid input. Please enter a valid numerical value.")

def main():
    print("Welcome to Professional CLI Calculator!")
    while True:
        display_menu()
        choice = input("Select operation (1-7): ").strip()
        
        if choice == "7":
            print("\nThank you for using Python Calculator! Goodbye! 👋")
            break
            
        if choice in ["1", "2", "3", "4", "5", "6"]:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            try:
                if choice == "1":
                    res = add(num1, num2)
                    op = "+"
                elif choice == "2":
                    res = subtract(num1, num2)
                    op = "-"
                elif choice == "3":
                    res = multiply(num1, num2)
                    op = "*"
                elif choice == "4":
                    res = divide(num1, num2)
                    op = "/"
                elif choice == "5":
                    res = modulus(num1, num2)
                    op = "%"
                elif choice == "6":
                    res = power(num1, num2)
                    op = "^"
                
                # Print integer cleanly if whole number
                res_formatted = int(res) if res.is_integer() else f"{res:.4f}"
                n1_fmt = int(num1) if num1.is_integer() else num1
                n2_fmt = int(num2) if num2.is_integer() else num2
                
                print(f"\n[RESULT]: {n1_fmt} {op} {n2_fmt} = {res_formatted}")
            except ValueError as e:
                print(f"\n[!] {e}")
        else:
            print("[!] Invalid option. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
