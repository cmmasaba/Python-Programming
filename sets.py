"""Sets in Python

    Unordered collection with no duplicate elements
    Commonly used for membership testing and
    eliminating duplicate entries
"""

fruit_basket = {'apple', 'orange', 'banana', 'mango', 'pear', 'apple'}
print(f'{fruit_basket=}')
print(f'{"orange" in fruit_basket=}')
print(f'{"pineapple" in fruit_basket=}')

# set methods
a = set('abracadabra')
b = set('alacazam')
print(f'Set {a=} and Set {b=}')
print(f'Letters in a but not in b {a-b=}')
print(f'{a.difference(b)=}')
print(f'Letters in a or b or both {a|b=}')
print(f'{a.union(b)=}')
print(f'Letters in both a and b {a&b=}')
print(f'{a.intersection(b)=}')
print(f'Letters in a or b but not both {a^b=}')

# set comprehensions is also possible
a = {x for x in 'abracadrabra' if x not in 'abc'}
