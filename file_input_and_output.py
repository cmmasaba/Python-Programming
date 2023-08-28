"""File input and output operations in Python.
"""

import json

# open(filename, mode, encoding="encoding")
# modes can be w for write, r for read and a for append
# r+ opens a file for both reading and writing
# default mode of file opening is r

with open('text', 'w', encoding='utf-8') as f:
    f.write('File operations in Python')

with open('text') as f:
    line = f.read()
    print(line)

# file objects methods
# f.read(size) reads some quantity of data and returns it as a string/bytes
# size is optional. If omitted the entire file contents are read
# f.read returns an empty string if end of file has been reached
# f.readline() reads a single line from a file object. A newline character is
# left at the end of the string except when the line doesn't end in a new line
# f.readlines() reads all the lines of s ile into a list
with open('text') as f:
    print(f.read(10))
    print(f.readline())

# a memory efficient an fast way of looping over the contents os file is
# looping over a file object
with open('text') as f:
    for line in f:
        print(line)


# f.write(string) writes the 'string' into a file and return number of
# characters written

# other object types need to be converted either to a string in text mode
# or to bytes in binary mode
with open('text', 'a') as f:
    value = ('the value is', 43)
    s = str(value)
    f.write(s)

# f.tell()
# f.seek(offset, whence)
# the above two methods are best used in binary mode

with open('text2', 'w') as f:
    cities = ['Nairobi', 'New York', 'London']
    countries = ['Kenya', 'USA', 'Britain']
    data2 = {cities[i]:countries[i] for i in range(3)}
    print(json.dumps(cities))
    json.dump([cities, countries, data2], f)

with open('text2') as f:
    print(json.load(f))
