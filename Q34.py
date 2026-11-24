"""Assignment 3 - Question 34
Delete list element using pop().
Run this file directly in VS Code.
"""

items = [10, 20, 30, 40]
index = int(input("Index to remove: "))
if -len(items) <= index < len(items): print("Removed:", items.pop(index))
else: print("Invalid index.")
print(items)
