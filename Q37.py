"""Assignment 3 - Question 37
Find second-largest list element.
Run this file directly in VS Code.
"""

numbers = [10, 5, 8, 20, 20, 15]
unique = sorted(set(numbers), reverse=True)
print("Second largest:", unique[1] if len(unique) >= 2 else "Not available")
