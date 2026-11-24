"""Assignment 3 - Question 32
Append five elements to list.
Run this file directly in VS Code.
"""

items = [1, 2, 3]
for i in range(5):
    items.append(int(input(f"Enter element {i+1}: ")))
print(items)
