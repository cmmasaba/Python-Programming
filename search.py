def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Searches for letters in a supplied phrase."""
    search_letters = set(letters)
    found = search_letters.intersection(set(phrase))
    return found


found = search_for_letters('sky', 'k')
print('Letters found in phrase: ')
for letter in found:
    print('\t', letter)
