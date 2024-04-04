'''
In Python, a nested tuple is a tuple that contains other tuples as its elements. This allows you to create a data structure with multiple levels of nesting. Each inner tuple can have its own elements, including other tuples if desired.
'''

# Here's an example of a nested tuple:
nested_tuple = ((1, 2), ('a', 'b', 'c'), (True, False))

print(nested_tuple)

'''
In this example:

nested_tuple is a tuple containing three elements.
Each element is itself a tuple:
(1, 2) is a tuple with two integer elements.
('a', 'b', 'c') is a tuple with three string elements.
(True, False) is a tuple with two boolean elements.
'''

# You can access elements of a nested tuple using indexing. For example:

print(nested_tuple[0])  # Output: (1, 2)
print(nested_tuple[1][0])  # Output: 'a'
print(nested_tuple[2][1])  # Output: False

'''Nested tuples are useful for representing hierarchical data structures or multi-dimensional data. They are immutable like regular tuples, meaning once created, their structure cannot be modified. However, you can access and manipulate their elements using indexing and slicing, just like with regular tuples.'''