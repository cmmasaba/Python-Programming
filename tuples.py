"""The tuple sequence type and its operations

   A tuple is comma-separated values enclosed by 
   parentheses
   Tuples are immutable, but you create a tuple 
   of mutable objects like lists
   Differences between tuples and lists
   Tuples often contain heterogenous elememts that
   are accessed by unpacking or indexing the tuple
   Lists often contain homogeneous elements that
   are accessed by iterating over the list
"""
t = 12, 34, 56, 79  # tuple packing
u = t, 'boy', 'girl', 'hello!'
print(f'{t=}')
print(f'{u=}')
empty =()
singleton = ('Collins',)
print(f'{len(empty)} {empty=}')
print(f'{len(singleton)} {singleton=}')
