# lists in python and related operations
# comma-separated values which can be of same type of different type

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

