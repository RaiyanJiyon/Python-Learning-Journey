'''
In Python, the sorted() function is used to sort iterables, such as lists, tuples, and strings, and return a new sorted list. It does not modify the original iterable but creates a new sorted list containing the elements of the original iterable.

Here's how the sorted() function works:

Syntax:
sorted(iterable, *, key=None, reverse=False)
Parameters:
iterable: The iterable to be sorted.
key (optional): A function that takes an element as input and returns a value to use for sorting.
reverse (optional): A Boolean value. If True, the sorted list is in descending order; if False (default), it's in ascending order.
Return Value:
A new sorted list containing the elements of the iterable.
Example Usage:

Sorting a List:
'''

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


# Sorting a Tuple:
letters = ('b', 'd', 'c', 'a')
sorted_letters = sorted(letters)
print(sorted_letters)  # Output: ['a', 'b', 'c', 'd']


# Sorting a String:
word = "hello"
sorted_word = sorted(word)
print(sorted_word)  # Output: ['e', 'h', 'l', 'l', 'o']


# Sorting with Custom Key Function:
words = ['banana', 'apple', 'orange', 'grape']
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['apple', 'grape', 'banana', 'orange']


# Sorting in Reverse Order:

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [9, 6, 5, 5, 4, 3, 3, 2, 1, 1]


'''The sorted() function provides a convenient way to obtain a sorted copy of an iterable without modifying the original data. It's versatile and can be customized with key functions and reverse sorting options to suit various sorting requirements.'''