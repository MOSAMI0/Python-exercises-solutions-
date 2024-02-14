def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


numbers = int(input('Enter a number: '))
print('The first 10 numbers in the')
print('Fibonacci series are:')
for number in range(1, numbers):
    print(fib(number), end=' ')
