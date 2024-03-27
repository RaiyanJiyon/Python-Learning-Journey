'''
In Python, a global variable is a variable declared outside of any function or block of code, and it is accessible throughout the entire program. Unlike local variables, which are scoped to the function or block in which they are defined, global variables can be accessed and modified from anywhere in the program.
'''


# Here's an example of a global variable:

# Global variable declaration
global_var = 10

def my_function():
    # Accessing the global variable within the function
    print("Inside the function:", global_var)

# Call the function
my_function()
# Accessing the global variable outside the function
print("Outside the function:", global_var)

'''
In this example:

The variable global_var is declared outside of any function, making it a global variable.
It is accessible both inside and outside the my_function() function.
Inside the function, the global variable is accessed without any prefix.
Outside the function, the global variable is accessed similarly.
'''


'''While global variables provide a convenient way to share data across different parts of a program, they should be used judiciously to avoid potential issues such as unintended side effects and difficulties in debugging and maintaining code. It's generally recommended to minimize the use of global variables and prefer passing data explicitly as function arguments whenever possible.'''