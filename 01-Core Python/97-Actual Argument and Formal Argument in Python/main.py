'''
In Python, when you define a function, you specify parameters inside the parentheses. These parameters are placeholders for the values that you'll provide when you call the function. There are two types of parameters in Python: formal parameters (also known as formal arguments) and actual parameters (also known as actual arguments).
'''

'''
Formal Parameters (Formal Arguments):

Formal parameters are the parameters that you define in the function definition.
They act as placeholders for the values that will be supplied when the function is called.
Formal parameters are used within the function's body to perform operations.
You can think of formal parameters as variables that are local to the function.
Formal parameters are defined within the parentheses of the function definition.
'''

# Example
def greet(name):
    """This function greets the person with the given name."""
    print(f"Hello, {name}!")
'''In this example, name is the formal parameter of the greet() function.'''

'''
Actual Parameters (Actual Arguments):

Actual parameters are the values that you supply to a function when you call it.
They correspond to the formal parameters defined in the function definition.
Actual parameters provide the actual data that the function will operate on.
Actual parameters are passed within the parentheses of the function call.
'''

# Example
greet("Alice")
'''In this example, "Alice" is the actual parameter passed to the greet() function.'''

'''
In summary, formal parameters are placeholders for values used in the function definition, while actual parameters are the values supplied to the function when it is called. The actual parameters are bound to the formal parameters when the function is invoked, and the function operates on these values within its body.
'''