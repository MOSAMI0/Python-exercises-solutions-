#Create a function that takes a tuple and index of element you want to delete and delete the specific element and return the tuple
def delete_element(my_tuple, index):
    my_list = list(my_tuple)

    # Delete the element at the specified index
    del my_list[index]

    # Convert the list back into a tuple
    updated_tuple = tuple(my_list)

    return updated_tuple


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
index = int(input('enter the index you want to remove: '))
print(delete_element(my_tuple, index))
