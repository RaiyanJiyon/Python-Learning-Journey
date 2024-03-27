'''
In Python, lambda functions can be nested inside other functions or even inside other lambda functions, although this is less common. This nesting can be useful in situations where you need to create simple, one-time-use functions within the context of a larger function.
'''


# Here's an example of nesting a lambda function inside another function:
def outer_function(n):
    """This is the outer function."""
    return lambda x: x ** n

# Create a function that squares a number
square_function = outer_function(2)
print(square_function(5))  # Output: 25

# Create a function that cubes a number
cube_function = outer_function(3)
print(cube_function(5))  # Output: 125

'''
In this example:

The outer_function() takes an argument n and returns a lambda function.
The returned lambda function takes an argument x and returns x ** n, where n is the value passed to outer_function().
We create two new functions square_function and cube_function by calling outer_function() with arguments 2 and 3 respectively.
We then call these new functions with different arguments to compute the square and cube of a number.
'''

'''
You can also nest lambda functions inside other lambda functions, although this can quickly lead to unreadable code and is generally discouraged for complex cases. Here's an example for demonstration purposes:
'''

add = lambda x: (lambda y: x + y)
result = add(5)(3)
print(result)  # Output: 8


'''In this example, the add lambda function returns another lambda function that adds x (captured from the outer lambda) to y. We then call the outer lambda function with 5 and the inner lambda function with 3, resulting in 5 + 3 = 8.

While nesting lambda functions can be powerful in certain situations, it's essential to balance readability and maintainability when using them. In many cases, it's clearer to define named functions using the def keyword for complex logic or repeated use.'''
