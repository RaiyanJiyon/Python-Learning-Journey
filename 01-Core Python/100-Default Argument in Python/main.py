'''
In Python, default arguments allow you to specify default values for parameters in a function. If the caller of the function doesn't provide a value for a parameter with a default argument, the default value is used instead. This provides flexibility and convenience, as it allows you to define functions with optional parameters that can be omitted if their default behavior is acceptable.
'''

# Here's an example of using default arguments in a function:
def greet(name, greeting="Hello"):
    """This function greets the person with the given name using the provided greeting."""
    print(f"{greeting}, {name}!")

# Call the greet function with only the required argument
greet("Alice")  # Output: Hello, Alice!

# Call the greet function with both arguments
greet("Bob", "Hi")  # Output: Hi, Bob!

'''
In this example:

The greet() function has a default argument greeting="Hello".
When we call the function with only the required argument greet("Alice"), the default value "Hello" is used for the greeting parameter, and the function prints "Hello, Alice!".
When we call the function with both arguments greet("Bob", "Hi"), the provided value "Hi" overrides the default value, and the function prints "Hi, Bob!".
'''

'''Default arguments are specified in the function definition by providing an assignment (=) to the parameter along with its default value. Parameters with default arguments must come after parameters without default arguments in the function definition.'''