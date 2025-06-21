def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiply(a,b):
    return a * b

def menu():
    menu =  ["1. Addition",
            "2. Subtraction",
            "3. Division",
            "4. Multiplication"]
    for menus in menu:
        print(menus)

def main():
    print("Welcome to Calculator.")
    menu()

    user = input("Enter operation (+, -, /, *): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if user == "+":
        print("Result:", add(a, b))
    elif user == "-":
        print("Result:", subtract(a, b))
    elif user == "/":
        print("Result:", divide(a, b))
    elif user == "*":
        print("Result:", multiply(a, b))
    else:
        print("Invalid operation.")

main()