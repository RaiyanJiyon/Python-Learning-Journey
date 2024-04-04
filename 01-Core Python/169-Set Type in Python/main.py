'''
In Python, a set is an unordered collection of unique elements. It is defined by enclosing comma-separated elements within curly braces {}. Sets are mutable, meaning you can add or remove elements after creation, but they themselves are mutable objects, meaning you cannot have sets as elements of another set.

Here's a basic example of a set:
'''

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

'''
Sets automatically remove duplicates when they're created. So, if you attempt to create a set with duplicate elements, the duplicates will be removed:
'''

my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # Output: {1, 2, 3}


# You can also create a set from a list using the set() constructor:
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5}


'''
Sets support various operations such as union, intersection, difference, and more. Being unordered collections, they do not support indexing or slicing. However, you can iterate over elements in a set using a loop or check for membership using the in keyword.
'''

my_set = {1, 2, 3}
for element in my_set:
    print(element)  # Output: 1 2 3

print(1 in my_set)  # Output: True
print(4 in my_set)  # Output: False


'''Sets are often used when you need to perform operations like finding unique elements, membership testing, or removing duplicates from collections.'''