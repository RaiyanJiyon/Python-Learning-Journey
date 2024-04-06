'''
Nested list comprehensions in Python allow you to create lists of lists (or other nested structures) using a single expression. They are especially useful when you need to create nested data structures or apply transformations to nested iterables.

The basic syntax of a nested list comprehension is similar to a regular list comprehension, but with an additional level of iteration. Here's the general structure:
'''

# [[expression for item2 in iterable2] for item1 in iterable1]


'''
In this syntax:

expression is the expression to be evaluated.
item2 is the variable representing each element of the inner iterable.
iterable2 is the inner iterable.
item1 is the variable representing each element of the outer iterable.
iterable1 is the outer iterable.
Here are a few examples to illustrate nested list comprehensions:
'''

# Creating a 2D list of zeros with dimensions 3x3:
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)
# Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Flattening a 2D list into a 1D list:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


'''Nested list comprehensions can be powerful tools for concise and expressive code when dealing with nested data structures or performing transformations on nested iterables. However, readability should always be prioritized, especially when dealing with complex nesting.'''