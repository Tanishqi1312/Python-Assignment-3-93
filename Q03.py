"""Assignment 3 - Question 3
Count vowels and consonants separately.
Run this file directly in VS Code.
"""

text = input("Enter a string: ").lower()
vowels = sum(ch in "aeiou" for ch in text)
consonants = sum(ch.isalpha() and ch not in "aeiou" for ch in text)
print("Vowels:", vowels, "Consonants:", consonants)
