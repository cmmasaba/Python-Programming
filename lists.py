"""Lists in Python and related operations
lists are comma-separated values which can be of same type of different type"""

from collections import deque
from math import pi


squares1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f'Square of 1 to 10 {squares1}')

# lists can also be indexed and sliced
print('Square of 5 is', squares1[4])
print('Square of 10 is', squares1[-1])
print('Square of 1, 2 and 3 is', squares1[:3])

# lists also support concatenation
squares2 = [121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
print(f'Squares of 11 to 20 {squares2}')
squares3 = squares1 + squares2
print(f'Squares of 1 to 20 {squares3}')

# assignment to a list/slice is possible is possible
squares3[-4:] = [17, 18, 19, 20]
squares3[:] = []

# list methods
# list.append(x) adds x to the end of list
# list.extend(iterable) appends all items from iterable to list
# list.insert(i, x) inserts x at position before index i
# list.remove(x) remove first item whose value equals x
# list.pop(i) remove the item at index i and return it
# list.clear() remove all elements from the list
# list.index(x[,start[,end]])
# list.count(x) returns number of times x appears in the list
# list.sort(*,key=None, reverse=False) sort the list in-place
# list.reverse() reverse the elements of the list
# list.copy() return shallow copy of the list

# using lists as stacks
stack = [1, 2, 3, 4, 5, 6, 7]
stack.append(8)
stack.append(9)
print(stack)
stack.pop()
stack.pop()

# using lists as queue
queue = deque(['Collins', 'Frandel', 'Aineah'])
queue.append('Raul')
queue.append('Bryan')
queue.append('Antonne')
queue.popleft()
queue.popleft()
print(queue)

# list comprehensions
# conists of brackets containing an expression, followed by a for clause
# then zero or more for or if clauses.
sqaures = [x**2 for x in range(10)]
combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x>=0])
print([abs(x) for x in vec])
number_square = [(x, x**2) for x in range(10)]
print(f'{number_square=}')
round_pi = [str(round(pi,i)) for i in range(10)]
# nested comprehensions
# the inital expression can be any arbitrary expression
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
transposed = [[row[i] for row in matrix] for i in range(4)]
transposed = list(zip(*matrix))

# del statement can be used to delete list elements when given index
# del a[0] or del[2:] or del[:]
