"""Finds the largest number in a list."""

def find_largest(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == "__main__":
    values = [12, 45, 7, 89, 23]
    print("Numbers:", values)
    print("Largest:", find_largest(values))
