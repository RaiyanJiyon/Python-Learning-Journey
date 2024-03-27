'''
In Python, a local variable is a variable that is declared within the scope of a function or a block of code, such as a loop or a conditional statement. Local variables are accessible only within the block in which they are defined, and they are destroyed when the block exits.
'''


# Here's an example of a local variable within a function:
def my_function():
    # Local variable declaration
    x = 10
    print("Inside the function:", x)

# Call the function
my_function()
# Attempting to access the local variable outside the function will result in an error
# print("Outside the function:", x)  # This would result in a NameError

'''
In this example:

The variable x is declared within the scope of the function my_function().
It is accessible only within the function, so attempting to access it outside the function would result in a NameError.
When my_function() is called, the local variable x is assigned the value 10, and "Inside the function: 10" is printed.
'''

# Local variables can also be defined within loops, conditional statements, or any other block of code:
def my_function():
    if True:
        # Local variable declaration within a conditional statement
        y = 20
        print("Inside the conditional statement:", y)

    # Local variable declaration within the function
    z = 30
    print("Inside the function:", z)

# Call the function
my_function()
# Attempting to access the local variable defined within the conditional statement
# outside its scope would result in an error
# print("Outside the conditional statement:", y)  # This would result in a NameError


'''In this example, y is a local variable defined within the conditional statement, and z is a local variable defined within the function scope. Both variables are accessible only within their respective blocks of code.

Local variables help maintain encapsulation and prevent unintended side effects by limiting their scope to the block in which they are defined.'''