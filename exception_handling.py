"""Demonstrates exception handling for division."""

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero."

if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
