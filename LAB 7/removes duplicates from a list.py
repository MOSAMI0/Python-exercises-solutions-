def remove_duplicates(original_list):
    unique_list = []
    for element in original_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


# Example usage
my_list = [1, 2, 3, 2, 4, 3, 5, 6, 5]
result = remove_duplicates(my_list)
print(result)
