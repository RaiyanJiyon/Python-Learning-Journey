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