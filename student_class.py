"""Demonstrates a class, object, and instance methods."""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")

    def has_passed(self):
        return self.marks >= 40

if __name__ == "__main__":
    student = Student("Anu", 82)
    student.display()
    print("Passed:", student.has_passed())
