'''
In Python, the min() and max() functions are used to find the minimum and maximum elements in an iterable or to compare multiple values and determine the minimum or maximum among them.

Here's how these functions work:

min() Function:

The min() function returns the smallest element in an iterable or the smallest of two or more arguments.

If the iterable contains multiple elements, min() returns the element with the minimum value.

If multiple arguments are provided, min() returns the smallest of the arguments.

Syntax:

For iterable: min(iterable, default=None, *args)
For multiple arguments: min(arg1, arg2, *args)
Examples:
'''

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(min(numbers))  # Output: 1

words = ['apple', 'banana', 'orange']
print(min(words))  # Output: 'apple'

print(min(5, 3, 9, 1))  # Output: 1


'''
max() Function:

The max() function returns the largest element in an iterable or the largest of two or more arguments.

If the iterable contains multiple elements, max() returns the element with the maximum value.

If multiple arguments are provided, max() returns the largest of the arguments.

Syntax:

For iterable: max(iterable, default=None, *args)
For multiple arguments: max(arg1, arg2, *args)
Examples:
'''

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(max(numbers))  # Output: 9

words = ['apple', 'banana', 'orange']
print(max(words))  # Output: 'orange'

print(max(5, 3, 9, 1))  # Output: 9


'''Both min() and max() functions work with various iterables such as lists, tuples, sets, and even strings. They are handy when you need to quickly find the smallest or largest element in a collection or compare multiple values.'''