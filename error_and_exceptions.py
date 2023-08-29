"""Errors and exceptions in Python.
"""

import sys

# handling exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("That was no valid number. Try again...")
    except KeyboardInterrupt:
        print("Ending...")
        break
    except (RuntimeError, NameError, TypeError):
        # multiple exceptions can be named in a parenthesized tuple
        pass
    finally:
        print("Thanks for playing :)")


# a class in an except clause is compatible with an exception if the
# same class or a base class of the exception. An except clause listing
# a derived class is not compatible with a base class.
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')
# if except B was first it would print B, B, B

# an exception may contain arguments
# except clause may also specify a variable after the exception name
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst)) # inst is bound to the exception raised
    print(inst.args)  # args is an attribute that contains arguments given
    print(inst)  # builtin exceptions contain __str__() that prints all args


try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)}")
    raise  # re-raise a catch all Exception after printing it to allow caler to
           # handle it as well

# try...except statement can have an optional else clause
# when present, it must follow all except clauses
# the else clause is useful for code that must be executed in case no exception
# is raised

# the raise statement allows programmers to force a specific exception to occur
s = input("Enter your name: ")
raise NameError(s)

# exceptions have an attribute add_note(note) that allows adding additional 
# error information to be printed
try:
    raise TypeError("Bad type")
except Exception as e:
    e.add_note("Add sone information")
    raise
