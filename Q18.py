"""Assignment 3 - Question 18
Find longest word in a sentence.
Run this file directly in VS Code.
"""

words = input("Enter a sentence: ").split()
print("Longest word =", max(words, key=len) if words else "No words entered")
