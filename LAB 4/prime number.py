n = int(input("Enter the value of n: "))

print("Prime numbers up to", n, ":")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    # Print prime numbers
    if is_prime:
        print(num)
