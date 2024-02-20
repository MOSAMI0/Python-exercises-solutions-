def calculate_sum(my_list):
    total = sum(my_list)
    print("The sum of the elements is:", total)


my_list = []
for i in range(5):
    element = int(input("Please enter five number: "))
    my_list.append(element)

# Print the list
print("The list is:", my_list)
calculate_sum(my_list)
