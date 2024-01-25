def Fibonacci():
    n = int(input("Enter a value of n: "))
    first_number = 0
    second_number = 1
    print("Fibonacci sequence up to the", n, "number:")
    print(first_number)
    print(second_number)
    for _ in range(2, n):
        final = first_number + second_number
        print(final)
        first_number, second_number = second_number, final
Fibonacci()
