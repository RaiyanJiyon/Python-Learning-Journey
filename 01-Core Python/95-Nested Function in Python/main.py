def outer_function():
    """This is the outer function."""
    print("Outer function is executing.")

    def inner_function():
        """This is the inner function."""
        print("Inner function is executing.")

    inner_function()  # Call the inner function

# Call the outer function
outer_function()


# Here's an example demonstrating closure:
def outer_function():
    """This is the outer function."""
    message = "Hello, "

    def inner_function(name):
        """This is the inner function."""
        print(message + name)

    return inner_function

# Assign the returned inner function to a variable
greet = outer_function()

# Call the inner function
greet("Alice")  # Output: Hello, Alice