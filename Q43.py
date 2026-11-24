"""Assignment 3 - Question 43
Find index of an element in list.
Run this file directly in VS Code.
"""

items = [10, 20, 30, 40]
value = int(input("Element to find: "))
print("Index:", items.index(value) if value in items else "Not found")
