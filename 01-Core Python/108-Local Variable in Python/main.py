# Here's an example of a local variable within a function:
def my_function():
    # Local variable declaration
    x = 10
    print("Inside the function:", x)

# Call the function
my_function()
# Attempting to access the local variable outside the function will result in an error
# print("Outside the function:", x)  # This would result in a NameError

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