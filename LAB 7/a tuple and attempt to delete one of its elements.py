my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

my_list = list(my_tuple)

del my_list[2]

my_tuple = tuple(my_list)

print("Updated Tuple:", my_tuple)
