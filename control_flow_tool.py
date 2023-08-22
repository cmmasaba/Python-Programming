# they include the if, for and while statements
# they control the execution of the code

# if statements
# elif and else parts are selectively optional
num = int(input('Enter an integer: '))
if num < 0:
    num  = 0
    print('Negative changed to zero')
elif num == 0:
    print('Zero')
elif num == 1:
    print('Single')
else:
    print('More')

# for statement can be used to iterate over items of a sequence
# int the order they appear in the sequence
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

users = {'Hans':'inactive', 'Helena':'inactive', 'Collins':'active'}
# modifying a collection while iterating over the same collection
# by iterationg over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# range is used to terate over a sequence of numbers
# you can specify the start, end and increment

for i in range(5):
    print(i)
random_num = []
for i in range(5, 50, 3):  # start from 5 to and not including 50 in steps of 3
    random_num.append(i)
for i in range(len(random_num)):  # using range and len to iterate a sequence
    print(i, random_num[i])


# break, continue and else clauses in loops
# in a for loop, else statement is executed when the final iteration is reached
# in a while loop, else is executed when the condition becomes false
# break statement is used to break from the innermost loop
# else statement is not executed if the loop was terminated by break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
