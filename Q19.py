"""Assignment 3 - Question 19
Count frequency of each character.
Run this file directly in VS Code.
"""

text = input("Enter a string: ")
frequency = {}
for ch in text: frequency[ch] = frequency.get(ch, 0) + 1
for ch, count in frequency.items(): print(repr(ch), count)
