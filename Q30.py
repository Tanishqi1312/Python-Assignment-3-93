"""Assignment 3 - Question 30
Count even and odd list elements.
Run this file directly in VS Code.
"""

numbers = [1, 2, 3, 4, 5, 6, 7]
even = sum(n % 2 == 0 for n in numbers)
odd = sum(n % 2 != 0 for n in numbers)
print("Even:", even, "Odd:", odd)
