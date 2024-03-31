'''
In Python, a nested list is a list that contains other lists as its elements. These lists can be of different lengths and can contain any data types, including other lists. Nested lists are a powerful way to represent structured data and can be used to create multi-dimensional data structures such as matrices or trees.
'''

# Here's an example of a nested list:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

'''
In this example, nested_list contains three inner lists, each representing a row of a matrix. Each inner list contains three elements.

You can access elements of a nested list using multiple indexing. For example, to access the element 5 in the above nested_list, you would use:
'''

element = nested_list[1][1]
print(element)  # Output: 5

'''
Here, nested_list[1] accesses the second inner list [4, 5, 6], and nested_list[1][1] accesses the second element of that inner list, which is 5.

Nested lists can also be used to represent irregular or jagged data structures, where the sublists can have different lengths. For example:
'''

jagged_list = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]

'''
In this example, jagged_list contains three inner lists, each with a different length.

You can manipulate nested lists using list methods and list comprehensions, just like regular lists. Nested lists provide a flexible way to represent and work with complex data structures in Python.
'''