#listOfNum = [1, 2, 6, 8]
#print(max(listOfNum), min(listOfNum))
#another way 😁👍
def find_min_max(my_list):
    if len(my_list) == 0:
        print("The list is empty.")
    else:
        minimum = min(my_list)
        maximum = max(my_list)
        print("Minimum value:", minimum)
        print("Maximum value:", maximum)

# Example usage
my_list = [5, 2, 7, 1, 9, 3]
find_min_max(my_list)
