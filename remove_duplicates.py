"""Removes duplicate values while preserving their original order."""

def remove_duplicates(values):
    return list(dict.fromkeys(values))

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 3, 5, 1]
    print("Original:", numbers)
    print("Without duplicates:", remove_duplicates(numbers))
