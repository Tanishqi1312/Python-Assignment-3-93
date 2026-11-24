"""Assignment 3 - Question 33
Delete list element using remove().
Run this file directly in VS Code.
"""

items = [10, 20, 30, 20]
value = int(input("Value to remove: "))
if value in items: items.remove(value)
else: print("Value not found.")
print(items)
