"""
Transforming a list using list methods
"""

phrase = "Don't panic!"
plist = list(phrase)
print(plist)
target = ['o', 'n', 't', 'a', 'p']
found = []
for letter in phrase:
    print(letter)
    if letter in target:
        if letter not in found:
            found.append(letter)
        else:
            plist.remove(letter)
    else:
        plist.remove(letter)
plist.insert(1, plist.pop())
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, ' ')
new_phrase = ''.join(plist)
print(new_phrase)
