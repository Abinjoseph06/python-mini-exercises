"""Checks whether an integer is even or odd."""

try:
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
except ValueError:
    print("Please enter a valid integer.")
