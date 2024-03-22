'''
In Python, the any() and all() functions are built-in functions that are used to check whether elements in an iterable satisfy certain conditions. Both functions return a boolean value indicating the result of the condition checks.

Here's a brief explanation of each function:
'''

'''
any() Function:

The any() function returns True if at least one element in the iterable evaluates to True, and False if all elements evaluate to False.
It takes an iterable (such as a list, tuple, or array) as its argument.
If the iterable is empty, any() returns False.
'''

# Example usage of the any() function
iterable1 = [True, False, False]
iterable2 = [False, False, False]
iterable3 = []

print(any(iterable1))  # Output: True
print(any(iterable2))  # Output: False
print(any(iterable3))  # Output: False
