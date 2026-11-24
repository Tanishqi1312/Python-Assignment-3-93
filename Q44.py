"""Assignment 3 - Question 44
Demonstrate copy() versus direct assignment.
Run this file directly in VS Code.
"""

original = [1, 2, 3]
direct = original
copied = original.copy()
original.append(4)
print("Original:", original)
print("Direct assignment:", direct)
print("copy():", copied)
