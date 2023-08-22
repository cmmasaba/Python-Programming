# Generating fibonacci series upto a number given by the user

upper_limit = int(input("Generate Fibonacci Series upto which number?: "))
a,b = 0,1
fibonacci = []
while a < upper_limit:
    fibonacci.append(a)
    a,b = b,a+b
print(f'The Fibonacci Series from 1 to {upper_limit} is {fibonacci}')
