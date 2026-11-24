"""Assignment 3 - Question 38
Remove duplicate list elements.
Run this file directly in VS Code.
"""

items = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(items))
print(unique)
