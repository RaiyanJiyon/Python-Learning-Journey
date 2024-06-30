# Here's an example of returning a lambda function from a function:
def create_multiplier(n):
    """This function creates and returns a lambda function that multiplies a number by n."""
    return lambda x: x * n

# Create a function that multiplies by 3
multiply_by_3 = create_multiplier(3)

# Call the returned lambda function
result = multiply_by_3(5)
print(result)  # Output: 15

# You can also directly return a lambda function without assigning it to a variable:
def create_power_function(n):
    """This function creates and returns a lambda function that raises a number to the power of n."""
    return lambda x: x ** n

# Create a function that squares a number
square_function = create_power_function(2)

# Call the returned lambda function
result = square_function(3)
print(result)  # Output: 9