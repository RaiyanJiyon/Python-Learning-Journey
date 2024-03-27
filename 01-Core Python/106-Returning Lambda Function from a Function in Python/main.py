'''
In Python, you can return a lambda function from another function, just like any other object. This can be useful when you want to create and return a simple, one-time-use function dynamically within another function.
'''


# Here's an example of returning a lambda function from a function:
def create_multiplier(n):
    """This function creates and returns a lambda function that multiplies a number by n."""
    return lambda x: x * n

# Create a function that multiplies by 3
multiply_by_3 = create_multiplier(3)

# Call the returned lambda function
result = multiply_by_3(5)
print(result)  # Output: 15

'''
In this example:

The create_multiplier() function takes a parameter n and returns a lambda function.
The lambda function returned by create_multiplier() takes a parameter x and multiplies it by n.
We call create_multiplier(3) to create a lambda function that multiplies by 3 and assign it to multiply_by_3.
We then call multiply_by_3(5), passing 5 as an argument. This calls the lambda function with x=5, resulting in 5 * 3 = 15.
'''

# You can also directly return a lambda function without assigning it to a variable:
def create_power_function(n):
    """This function creates and returns a lambda function that raises a number to the power of n."""
    return lambda x: x ** n

# Create a function that squares a number
square_function = create_power_function(2)

# Call the returned lambda function
result = square_function(3)
print(result)  # Output: 9


'''In this example, create_power_function() returns a lambda function that raises a number to the power of n. We then call this returned lambda function to square a number 3, resulting in 3 ** 2 = 9.

Returning lambda functions from functions can be a concise way to create and use simple, one-time-use functions dynamically within your code.'''