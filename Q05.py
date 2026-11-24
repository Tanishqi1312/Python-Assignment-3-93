"""Assignment 3 - Question 5
Check palindrome string.
Run this file directly in VS Code.
"""

text = input("Enter a string: ")
clean = text.replace(" ", "").lower()
print("Palindrome" if clean == clean[::-1] else "Not palindrome")
