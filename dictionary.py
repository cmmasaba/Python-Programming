"""Dictionaries in python
    
    Store key-value pairs.
    Dictionaries are indexed by keys
    list(d) will list all keys of pairs in d
    depending on insertion order
    sorted(d) will sort the keys in d
    membership can be tested using the in or not in
    keywords
    dict() can be used to create dictionary from a
    sequence of key-value pairs
"""
tel = {'jack':4098, 'sape':3143}
tel['guido'] = 5009
print(f'{tel=}')
del tel['sape']
print(list(tel))
print(sorted(tel))
print(f'{"jack" in tel}')
print(f'{"collins" not in tel}')
# dict comprehensions
names = ['collins', 'hellen', 'alice']
ages = [23, 18, 12]
name_ages = {names[i]:ages[i] for i in range(3)}
print(f'{name_ages=}')
