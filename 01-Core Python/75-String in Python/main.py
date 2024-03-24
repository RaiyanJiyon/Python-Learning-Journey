'''
n Python, a string is a sequence of characters enclosed within either single quotes (') or double quotes ("). Strings are immutable, meaning that once they are created, their contents cannot be changed.

Here are some basic operations and characteristics of strings in Python:
'''

# Creating Strings:
'''You can create a string by enclosing characters within single quotes or double quotes:'''
my_string1 = 'Hello, World!'
my_string2 = "Python Programming"

# String Concatenation:
'''You can concatenate strings using the + operator:'''
full_string = my_string1 + ' ' + my_string2
print(full_string)  # Output: Hello, World! Python Programming

# Accessing Characters:
'''You can access individual characters of a string using indexing:'''
first_char = my_string1[0]  # Accessing the first character
print(first_char)  # Output: H

last_char = my_string2[-1]  # Accessing the last character
print(last_char)  # Output: g

# String Length:
'''You can get the length of a string using the len() function:'''
length = len(my_string1)
print(length)  # Output: 13

# Slicing:
'''You can slice strings to extract substrings:'''
substring = my_string2[7:11]
print(substring)  # Output: Prog

# String Methods:
'''Python provides many built-in string methods for various operations like converting case, finding substrings, splitting, joining, etc. For example:'''
uppercase_string = my_string1.upper()
print(uppercase_string)  # Output: HELLO, WORLD!

split_string = my_string2.split(' ')
print(split_string)  # Output: ['Python', 'Programming']

# String Formatting:
'''You can format strings using the format() method or f-strings (formatted string literals):'''
name = 'Alice'
age = 30
formatted_string = 'My name is {} and I am {} years old.'.format(name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

f_string = f'My name is {name} and I am {age} years old.'
print(f_string)  # Output: My name is Alice and I am 30 years old.


'''Strings in Python are versatile and widely used for various tasks such as text processing, input/output operations, formatting, and more.'''