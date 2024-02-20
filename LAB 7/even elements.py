def get_even_elements(original_list):
    even_list = [num for num in original_list if num % 2 == 0]
    return even_list


A_List = [1, 2, 3, 4, 5, 6, 7]
print(get_even_elements(A_List))
