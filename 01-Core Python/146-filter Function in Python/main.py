'''
In Python, the filter() function is a built-in function that allows you to filter elements from an iterable (such as a list, tuple, or set) based on a specified condition. It takes two arguments: a function that defines the condition for filtering, and an iterable containing the elements to be filtered.

The syntax of the filter() function is as follows:
'''

# filter(function, iterable)

'''
function: A function that returns True or False based on whether an element should be included in the filtered result.
iterable: The iterable (e.g., list, tuple, set) from which elements will be filtered.
The filter() function returns an iterator that yields the elements from the iterable for which the function returns True.
'''

# Here's an example of how to use the filter() function:
# Define a function to filter even numbers
def is_even(x):
    return x % 2 == 0

# Define an iterable
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to filter even numbers from the list
filtered_numbers = filter(is_even, numbers)

# Convert the result to a list (since filter() returns an iterator)
result = list(filtered_numbers)

print(result)  # Output: [2, 4, 6, 8, 10]

'''
In this example:

We define a function is_even(x) that returns True if x is even.
We have a list numbers containing integers from 1 to 10.
We use the filter() function to filter even numbers from the numbers list based on the is_even() function.
The result of filter() is an iterator, so we convert it to a list to display the filtered numbers.
'''

# You can use lambda functions with filter() for simple filtering conditions, as shown in the example below:
# Use filter() with a lambda function to filter even numbers
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
result = list(filtered_numbers)

print(result)  # Output: [2, 4, 6, 8, 10]

'''The filter() function is useful for quickly filtering elements from iterables based on custom conditions without the need for writing explicit loops'''