'''
In Python, strings are immutable sequences of characters, and Python provides several built-in string methods to manipulate and transform strings. Here are some commonly used string methods for case conversion and title casing:
'''

# upper(): This method returns a copy of the string with all the characters converted to uppercase.
my_string = "hello, world!"
print(my_string.upper())  # Output: HELLO, WORLD!

# lower(): This method returns a copy of the string with all the characters converted to lowercase.
my_string = "HELLO, WORLD!"
print(my_string.lower())  # Output: hello, world!

# swapcase(): This method returns a copy of the string with uppercase characters converted to lowercase and vice versa.
my_string = "Hello, World!"
print(my_string.swapcase())  # Output: hELLO, wORLD!

# title(): This method returns a copy of the string with the first character of each word capitalized and all other characters lowercase.
my_string = "hello, world!"
print(my_string.title())  # Output: Hello, World!

'''These string methods provide convenient ways to change the case of characters in a string or to convert a string to title case. Keep in mind that these methods return new string objects with the modified content; they do not modify the original string in place because strings are immutable in Python.'''