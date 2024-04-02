'''
In Python, the map() function is a built-in function used to apply a specified function to each item in an iterable (such as a list, tuple, or set) and return an iterator that yields the results. The syntax of the map() function is as follows:
'''

# map(function, iterable)

'''
function: A function that takes one or more arguments and performs some operation on them.
iterable: The iterable (e.g., list, tuple, set) whose elements will be passed as arguments to the function.
The map() function applies the function to each element of the iterable and returns an iterator that yields the results.
'''

# Here's an example of how to use the map() function:
# Define a function to square a number
def square(x):
    return x ** 2

# Define an iterable
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each element in the list
squared_numbers = map(square, numbers)

# Convert the result to a list (since map() returns an iterator)
result = list(squared_numbers)

print(result)  # Output: [1, 4, 9, 16, 25]


'''
In this example:

We define a function square(x) that squares a number.
We have a list numbers containing integers from 1 to 5.
We use the map() function to apply the square() function to each element in the numbers list.
The result of map() is an iterator, so we convert it to a list to display the squared numbers.
'''

'''
You can also use lambda functions with map() for simple operations, as shown in the example below:
'''

# Use map() with a lambda function to square each number in the list
squared_numbers = map(lambda x: x ** 2, numbers)
result = list(squared_numbers)

print(result)  # Output: [1, 4, 9, 16, 25]

'''The map() function is useful for applying a function to each element of an iterable and obtaining the transformed results efficiently.'''