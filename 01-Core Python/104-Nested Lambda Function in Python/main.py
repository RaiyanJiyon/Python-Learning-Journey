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

add = lambda x: (lambda y: x + y)
result = add(5)(3)
print(result)  # Output: 8