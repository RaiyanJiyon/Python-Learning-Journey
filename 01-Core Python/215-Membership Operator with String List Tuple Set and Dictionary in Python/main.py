'''
In Python, the membership operators (in and not in) are used to check whether a value exists in a sequence (such as a string, list, tuple, set, or dictionary) or not. Here's how they work with different data types:

String:

The in operator checks whether a substring exists within a string.

Example:
'''

my_string = "hello"
print('e' in my_string)  # Output: True
print('world' not in my_string)  # Output: True


'''
List:

The in operator checks whether an element exists in a list.

Example:
'''

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 not in my_list)  # Output: True


'''
Tuple:

The in operator checks whether an element exists in a tuple.

Example:
'''

my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # Output: True
print(6 not in my_tuple)  # Output: True


'''
Set:

The in operator checks whether an element exists in a set.

Example:
'''

my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True
print(6 not in my_set)  # Output: True


'''
Dictionary:

The in and not in operators check whether a key exists in a dictionary (not for values).

Example:
'''

my_dict = {'a': 1, 'b': 2, 'c': 3}
print('a' in my_dict)  # Output: True
print('d' not in my_dict)  # Output: True


'''These membership operators are handy for checking the existence of elements or substrings in different types of collections or sequences. They are commonly used in conditional statements or loops to perform specific actions based on the presence or absence of certain values.'''