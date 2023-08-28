"""String input and output operations in Python.
"""

import math

# output can be written using print(), expressions statements and using write()

# formatted string literals
year = 2023
action = 'learning Python'
print(f'In the year {year} I was {action}')
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

# str() method is used to return representation of an object in a  human
# readable way. Whereas repr() return the representation of an object
# which can be read by the interpreter, or it will force an error if there
# is no equivalent syntax. For objects that have no particular human
# friendly representation, str() return same output as repr()

s = 'Hello, World.'
print(f'{str(s)=}')
print(f'{repr(s)=}')
x = 100 * 3.25
y = 400 * 400
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'Hello, World\n'
print(f'{hello}')

# formatted string literals
# passing an integer after :. specifies number of decimal places
print(f'The value of pi is approximately {math.pi:.16f}.')

# passing an integer after : specifies how wide the characters should be
table = dict(
        Sjoerd=4127,
        Jack=4098,
        Dcab=7679
        )
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# other modifiers can be used to convert the value before it is formatted
# !a applies ascii(), !s applies str() and !r applies repr()
animals = 'eels'
print(f'My tank is full of {animals!a}')
print(f'My tank is full of {animals!r}')
print(f'My tank is full of {animals!s}')

# the string format() method
print('{} and {}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('{food} is {description}'.format(food='spam', description='horrible'))
print('The story of {0}, {1} and {other}.'.format('Bill', 'Manfred',
      other='Georg'))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'
        .format(**table))
names = ['Collins', 'Brian', 'Wayne']
print('The names are {}, {} and {}'.format(*names))

# manual string formatting
print('Numbers and their squares and cubes:')
for x in range(1, 11):
    print(repr(x).rjust(2),  repr(x*x).rjust(3), end = ' ')
    print(repr(x*x*x).rjust(4))
# repr.rjust(n) right justifies the value in a column of width n and pads
# it with spaces on the left
# alternatives are repr.ljust(n) and repr.center(n)
# repr.zfill(n) pads a numeric string on the left with zeroes
