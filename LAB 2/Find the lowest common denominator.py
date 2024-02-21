def find_smallest_common_divisor(Num1, Num2):
    # Find the smaller number
    smaller_num = min(Num1, Num2)

    # Iterate from 2 up to the smaller number
    for divisor in range(2, smaller_num + 1):
        if Num1 % divisor == 0 and Num2 % divisor == 0:
            return divisor

    # If no common divisor is found, return 1
    return 1


num1 = int(input('Enter an integer: '))
num2 = int(input('Enter an integer: '))
smallest_common_divisor = find_smallest_common_divisor(num1, num2)
print("Smallest Common Divisor:", smallest_common_divisor)
