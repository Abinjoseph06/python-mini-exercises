"""Calculates a grade from a mark out of 100."""

def calculate_grade(mark):
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    if mark >= 40:
        return "E"
    return "F"

if __name__ == "__main__":
    try:
        mark = float(input("Enter mark (0-100): "))
        print("Grade:", calculate_grade(mark))
    except ValueError as error:
        print("Error:", error)
