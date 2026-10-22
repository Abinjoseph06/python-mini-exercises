"""A simple calculator using functions."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Simple Calculator")
    try:
        a = float(input("Enter first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))
        operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
        if operator not in operations:
            print("Invalid operation.")
            return
        print("Result:", operations[operator](a, b))
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
