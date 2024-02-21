def gcd(x, y):
    if x < y:
        a = x #another way: a=x;x=y;y=a
        x = y
        y = a
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)


num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another integer: '))
print('The greatest common divisor of', 'the two numbers is', gcd(num1, num2))
