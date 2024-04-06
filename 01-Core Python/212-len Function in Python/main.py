'''
In Python, the len() function is used to get the length or size of an object. The behavior of len() depends on the type of object it is applied to. Here's how it works with different types of objects:

Lists, Tuples, Strings, Sets, and Dictionaries:

For sequences like lists, tuples, strings, and sets, len() returns the number of elements in the sequence.

For dictionaries, len() returns the number of key-value pairs (i.e., the number of keys) in the dictionary.

Example:
'''

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

my_string = "Hello, world!"
print(len(my_string))  # Output: 13

my_set = {1, 2, 3}
print(len(my_set))  # Output: 3

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))  # Output: 3


'''The len() function is versatile and widely used in Python for determining the size or length of various objects, making it a fundamental tool for working with collections and sequences.'''