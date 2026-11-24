"""Assignment 3 - Question 7
Count digits, alphabets and special characters.
Run this file directly in VS Code.
"""

text = input("Enter a string: ")
digits = sum(ch.isdigit() for ch in text)
alphabets = sum(ch.isalpha() for ch in text)
special = sum(not ch.isalnum() and not ch.isspace() for ch in text)
print("Digits:", digits, "Alphabets:", alphabets, "Special:", special)
