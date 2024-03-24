'''
In Python, you can check the characteristics of the characters in a string using the following string methods:
'''

# isdigit(): This method returns True if all characters in the string are digits (0-9), otherwise it returns False.
my_string = "12345"
print(my_string.isdigit())  # Output: True

my_string = "123abc"
print(my_string.isdigit())  # Output: False

# isalpha(): This method returns True if all characters in the string are alphabetic characters (a-z or A-Z), otherwise it returns False.
my_string = "abc"
print(my_string.isalpha())  # Output: True

my_string = "123abc"
print(my_string.isalpha())  # Output: False

# isalnum(): This method returns True if all characters in the string are alphanumeric characters (a-z, A-Z, or 0-9), otherwise it returns False.
my_string = "abc123"
print(my_string.isalnum())  # Output: True

my_string = "123@"
print(my_string.isalnum())  # Output: False


'''These methods are useful for validating the contents of strings, such as checking if a string consists only of digits, alphabetic characters, or alphanumeric characters. They can be used in conditional statements or boolean expressions to perform specific actions based on the characteristics of the string.'''