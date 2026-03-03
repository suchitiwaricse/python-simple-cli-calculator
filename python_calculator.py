
"""
Project 1: Simple CLI Calculator
Internship Project Submission
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def display_menu():
    print("\n========== SIMPLE CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=======================================")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values only.")
                continue

            if choice == "1":
                result = add(num1, num2)
                operation = "Addition"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == "4":
                result = divide(num1, num2)
                operation = "Division"

            print(f"{operation} Result: {result}")

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
