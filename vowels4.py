"""
Using sets to find vowels present in a string while avoiding duplicates
"""

vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for letter in sorted(found):
    print(letter)
