"""Classes in Python."""

from dataclasses import dataclass

# class syntax
class Foo:
	"""A simple class."""
	i = 12345
	def f(self):
		return "Hello, World"

# class instantiation
x = Foo()

# attribute reference
print(x.i)
print(x.f())

# class instantiation automatically calls the __init__(self) method if defined
class Complex:
    """Complex numbers."""
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

x = Complex(2, 3)
print(x.r, x.i)

# class and instance variables
class Dog:

    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(f"{d.kind = }, {e.kind = }")
print(f"{d.name = }. {e.name = }")

# mutable objects like lists and dictionaries should not be used a
# class variable since a single list would be share by all instances
class Dog:

    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('sit')
print(f"{d.tricks = }")  # unexpectedly shared by all dogs

# correct syntax

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


# bundling named data items together

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

collins = Employee('collins', 'computer technician', 1000)


# Generators
class Reverse:

    def __init__(self, data):
        self.data = data

    def reverse(self):
        for index in range(len(self.data)-1, -1, -1):
            yield self.data[index]

    def print(self):
        for char in self.reverse():
            print(char, end='')
        print()

rev = Reverse('engineer')
rev.print()

# Generator expressions, similar to list comprehensions but use parentheses
# suited when the generator is used right away by the enclosing function
print(sum(i*i for i in range(20)))
xvec = [10, 20, 30]
yvec = [4, 5, 6]
print(sum(x * y for x, y in zip(xvec, yvec)))
data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
