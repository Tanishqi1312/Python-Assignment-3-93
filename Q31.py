"""Assignment 3 - Question 31
Insert element at specified list position.
Run this file directly in VS Code.
"""

items = [10, 20, 40]
position = int(input("Index to insert at: "))
value = int(input("Value: "))
items.insert(position, value)
print(items)
