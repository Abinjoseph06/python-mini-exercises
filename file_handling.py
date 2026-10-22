"""Writes text to a file and reads it back."""
from pathlib import Path

FILE_PATH = Path("sample.txt")

if __name__ == "__main__":
    message = "Python file handling is working!\n"
    FILE_PATH.write_text(message, encoding="utf-8")
    content = FILE_PATH.read_text(encoding="utf-8")
    print("File content:")
    print(content, end="")
