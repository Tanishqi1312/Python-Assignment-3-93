"""Assignment 3 - Question 2
Count vowels.
Run this file directly in VS Code.
"""

text = input("Enter a string: ").lower()
print("Vowel count =", sum(ch in "aeiou" for ch in text))
