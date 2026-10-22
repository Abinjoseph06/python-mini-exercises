"""Counts how often each word appears in a sentence."""
import re
from collections import Counter

def count_words(sentence):
    words = re.findall(r"\\b[\\w']+\\b", sentence.lower())
    return dict(Counter(words))

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    for word, count in count_words(text).items():
        print(f"{word}: {count}")
