string = input("Enter a string: ")
reversed_string = ""

# قم بالتكرار على أحرف السلسلة بترتيب عكسي
for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]

print("Reversed string:", reversed_string)
