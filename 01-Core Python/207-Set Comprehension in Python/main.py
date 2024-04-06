'''
Set comprehension in Python is similar to list comprehension but creates sets instead of lists. It provides a concise way to create sets by applying an expression to each element of an iterable, optionally filtering the elements based on a condition.

The basic syntax of a set comprehension is:
'''

# {expression for item in iterable if condition}

'''
Here's a breakdown of each part:

expression: The expression to be evaluated for each element in the iterable. The result of this expression will be included in the new set.
item: The variable representing each element in the iterable.
iterable: The iterable (e.g., list, tuple, set, string) from which elements are taken.
condition (optional): An optional condition that filters the elements. Only elements for which the condition evaluates to True will be included in the new set.
Here are a few examples of set comprehensions:
'''

# Creating a set of squares of numbers from 0 to 9:
squares = {x**2 for x in range(10)}
print(squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}


# Creating a set of even numbers from 0 to 9:
evens = {x for x in range(10) if x % 2 == 0}
print(evens)  # Output: {0, 2, 4, 6, 8}


'''Set comprehensions are a powerful and concise way to create sets in Python. They are often used in place of traditional loops for their simplicity and readability. However, they may become less readable if they become too complex, so it's important to strike a balance between conciseness and clarity.'''