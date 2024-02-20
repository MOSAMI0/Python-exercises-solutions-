# Create an empty list
my_list = []

# Prompt the user to enter 10 values
for i in range(10):
    value = int(input("Enter a value: "))
    my_list.append(value)

# Sort the list in ascending order
ascending_order = sorted(my_list)

# Sort the list in descending order
descending_order = sorted(my_list, reverse=True)

# Print the sorted lists
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)
