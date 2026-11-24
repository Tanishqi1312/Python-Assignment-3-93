"""Assignment 3 - Question 4
Reverse string without built-in reverse.
Run this file directly in VS Code.
"""

text = input("Enter a string: ")
reversed_text = ""
for ch in text: reversed_text = ch + reversed_text
print(reversed_text)
