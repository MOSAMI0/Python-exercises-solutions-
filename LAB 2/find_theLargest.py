#A program that request three integer numbers from the user and print the largest one!
number1 = float(input('Enter the 1st number: '))
number2 = float(input('Enter the 2sc number: '))
number3 = float(input('Enter the 3th number: '))
print('The largest number is: ', number1) if number1 > number2 and number1 > number3 else (print('The largest number is: ', number2) if number2 > number1 and number2 > number3 else print('The largest number is: ', number3))
