"""Assignment 3 - Question 49
Demonstrate tuple immutability and create modified tuple.
Run this file directly in VS Code.
"""

items = (1, 2, 3)
try:
    items[0] = 99
except TypeError as error:
    print("Tuples are immutable:", error)
modified = items + (4,)
print("New tuple:", modified)
