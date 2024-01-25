def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]
# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
