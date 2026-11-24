"""Assignment 3 - Question 12
Find first and last occurrence using string methods.
Run this file directly in VS Code.
"""

text = input("Enter a string: ")
ch = input("Character to find: ")
print("First occurrence index:", text.find(ch))
print("Last occurrence index:", text.rfind(ch))
