#e a program that requests from user to input two numbers and calculate the sum , multiplication , division and subtraction for these two numbers.
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
operation = input('''Chose any operation you want +,-,*,/,** :
press "help" if you didn't know ?
if you want to know if the numbers you entered are 'even or odd ' press "Know" !
''').lower()
if operation == 'know':
    print("The numbers are even :", number1, ",", number2) if number1 and number2 % 2 == 0 else print("The numbers are odd :", number1, ",", number2)
if operation == "help":
    print('''
    ** if u want to power the number like 2^5=32 etc..
    / to divide 
    * to multiply
    + to collect 
    - tp Subtract
    ''')
if operation == '+':
    print('Result:', number1+number2)
if operation == '-':
    print('Result:', number1-number2)
if operation == '*':
    print('Result:', number1*number2)
if operation == '/':
    print('Result:', number1/number2)
if operation == '**':
    print('Result:', number1**number2)

