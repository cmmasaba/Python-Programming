"""Techniques to loop over dictionaries & sequences
"""

import math

knights = dict(gallahad='the pure', robin='the brave')
for key, value in knights.items():
    print(key, value)
print()
cities = ['Nairobi', 'Kampala', 'Dar es Salaam', 'Kigali']
countries = ['Kenya', 'Uganda', 'Tanzania', 'Rwanda']

# retrieving the index and value at the same time
for index, value in enumerate(cities):
    print(f'{index=} {value=}')
print()
# looping over two sequences at the same time
for city, country in zip(cities, countries):
    print(f"Where is {city}? It is in {country}.")
print()
# looping over a sequence in reverse, first specify it in
# forward direction and call the reverse function
for i in reversed(range(1, 20, 4)):
    print(i)
print()
fruit_basket = ['apple', 'mango', 'grapes', 'banana', 'mango', 'orange']
# looping over a sorted sequence
for i in sorted(fruit_basket):
    print(i)
print()
# looping over a sorted sequence and removing duplicates
for i in sorted(set(fruit_basket)):
    print(i)
print()
# recommended to create a new list instead of modifying a list
# while iterating over it
raw_data = [50.2, float('NaN'), 47.9, 23.7, 42.1, float('NaN')]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
