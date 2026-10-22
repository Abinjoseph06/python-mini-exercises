"""Reverses a string."""

def reverse_string(text):
    return text[::-1]

if __name__ == "__main__":
    value = input("Enter text: ")
    print("Reversed:", reverse_string(value))
