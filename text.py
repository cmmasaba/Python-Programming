# an illustration python operatons with texts
# text is represented as str

text = 'Paris rabbit got your back :)! Yay!'

# raw strings are also supported, for example when you don't characters
# prefaced by \ to be treated as special characters
# raw strings must have an even number of \ characters

print(r'C:\home\games')  # raw strings represented by r before quotes

# string literals can span multiple lines when using triple-quotes """.."""
# or '''...'''

print("""
Usage: foo [OPTIONS]
     -h                 Display this usage message
     -H process         Process to start
""")

# CONCATENATION AND QUITTING

print(3 * ('hello' + ' world\n'))

# INDEXING fist index has index 0, last character has index -1
print(f'First character of {text} is {text[0]}')

# SLICING, can be used to get a substring of a string

print(text[2:4])
print(text[:5])  # omitted first index defaults to zero
print(text[2:])  # omitted second index defaults to size of sting
print(text[:])  # always equal to the string

# python strings are immutable, assigning an index position results in error
# strings also have methods associated with them
print(f'\n{text = }')
print(f'{text.capitalize() = }')  # first character of string is put in Titlecase
print(f'{text.casefold() = }')  # casefolds the string to allow caseless matching
print(f'{text.count("ari", 0,9) = }') # return non-overlapping substrings in the range
print(f'{text.encode(encoding="utf-8", errors="strict") = }') # encode string to bytes
print(f'{text.isalnum() = }')  # True if it is alphanumerics &  has at least 1 char
print(f'{text.isascii() = }')  # True all characters are ASCII/string is empty
print(f'{text.islower() = }')  # check if string is lower case
print(f'{text.isnumeric() = }')
print(f'{text.isupper() = }')  # check if string is upper case
print(f'{text.lower() = }')  # copy of string lowercased
print(f'{text.upper() = }')  # convert to uppercase

# str.formart(*args, **kwargs) to format the string
# str.find(sub, start, end) to find the location of substring sub
# str.isdecimal() True if all characters are decimal and there is at least 1 char
# str.isdigit() return True if all characters are digits
# str.isspace() True if string only contains whitespace
# str.istitle() True if string is titlecased
# str.join(iterable) string which concatenation of all string in iterable
# str.lstrip([chars]) return copy os string with leading characters removed
# str.partition(sep) split the string at the 1st occurence of sep
# str.removeprefix(prefix) returns string[len(prefix):]
# str.removesuffix(suffix) return string[:-len(suffix)]
# str.replace(old, new, count) replace old with new
# str.rstrip(chars) remove trailing characters
# str.split(sep) return a list of words in the string using sep as delimiter
# str.splitlines() list of lines in the string
# str.strip(chars) leading and trailing whitespace removed
# str.swapcase() convert uppercase to lowercase and vice versa

