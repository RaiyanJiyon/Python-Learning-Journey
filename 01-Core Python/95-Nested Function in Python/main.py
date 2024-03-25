'''
In Python, a nested function is a function defined within another function. Nested functions are useful for encapsulating functionality that is only needed within the scope of the outer function. Here's an example of a nested function:
'''

def outer_function():
    """This is the outer function."""
    print("Outer function is executing.")

    def inner_function():
        """This is the inner function."""
        print("Inner function is executing.")

    inner_function()  # Call the inner function

# Call the outer function
outer_function()


'''
In this example:

outer_function() is the outer function, and inner_function() is the nested function defined inside outer_function().
When outer_function() is called, it prints "Outer function is executing." and then calls inner_function().
inner_function() is executed within the scope of outer_function(), and it prints "Inner function is executing."

Nested functions have access to variables in the enclosing scope (i.e., the scope of the outer function). This concept is known as closure. Nested functions can access variables from the outer function's scope even after the outer function has finished executing.
'''

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

'''In this example:

outer_function() returns the inner function inner_function().
The variable message is defined in the scope of outer_function() and is accessible to inner_function().
Even after outer_function() finishes executing, inner_function() retains access to the variable message, demonstrating closure.'''
