"""Assignment 3 - Question 6
Count uppercase and lowercase characters.
Run this file directly in VS Code.
"""

text = input("Enter a string: ")
upper = sum(ch.isupper() for ch in text)
lower = sum(ch.islower() for ch in text)
print("Uppercase:", upper, "Lowercase:", lower)
