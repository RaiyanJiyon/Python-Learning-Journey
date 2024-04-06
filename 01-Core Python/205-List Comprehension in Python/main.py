'''
List comprehension in Python provides a concise way to create lists. It allows you to generate a new list by applying an expression to each element of an iterable (such as a list, tuple, set, or string), optionally filtering the elements based on a condition.

The basic syntax of a list comprehension is:
'''

# [expression for item in iterable if condition]

'''
Here's a breakdown of each part:

expression: The expression to be evaluated for each element in the iterable. The result of this expression will be included in the new list.
item: The variable representing each element in the iterable.
iterable: The iterable (e.g., list, tuple, set, string) from which elements are taken.
condition (optional): An optional condition that filters the elements. Only elements for which the condition evaluates to True will be included in the new list.
Here are a few examples of list comprehensions:
'''

# Creating a list of squares of numbers from 0 to 9:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Creating a list of even numbers from 0 to 9:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


# Creating a list of characters in a string:
string = "hello"
chars = [char for char in string]
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']


'''List comprehensions are a powerful and concise way to create lists in Python. They are often used in place of traditional loops for their simplicity and readability. However, they may become less readable if they become too complex, so it's important to strike a balance between conciseness and clarity.'''