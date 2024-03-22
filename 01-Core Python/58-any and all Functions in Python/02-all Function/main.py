'''
all() Function:

The all() function returns True if all elements in the iterable evaluate to True, and False if at least one element evaluates to False.
It also takes an iterable as its argument.
If the iterable is empty, all() returns True.
'''

# Example usage of the all() function
iterable1 = [True, True, True]
iterable2 = [True, False, True]
iterable3 = []

print(all(iterable1))  # Output: True
print(all(iterable2))  # Output: False
print(all(iterable3))  # Output: True

'''Both functions are commonly used for checking conditions across multiple elements in an iterable, such as lists or arrays. They provide a concise and efficient way to perform such checks in Python code.'''