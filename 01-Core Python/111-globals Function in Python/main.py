'''
In Python, the globals() function returns a dictionary representing the current global symbol table. The global symbol table contains information about the global variables in the current module, including their names and values.
'''

# Here's how you can use the globals() function:
global_var = 10

def my_function():
    local_var = 20
    print("Global variables:", globals())
    print("Local variables:", locals())

# Call the function
my_function()

'''
In this example:

We define a global variable global_var with the value 10.
Inside the my_function() function, we define a local variable local_var with the value 20.
When we call the my_function() function, we print the global variables and local variables using the globals() and locals() functions.
The globals() function returns a dictionary containing all the global variables and their values.
The locals() function returns a dictionary containing all the local variables and their values within the function's scope.
'''

'''It's important to note that while globals() provides access to global variables, modifying the dictionary returned by globals() doesn't affect the actual global variables. The dictionary returned by globals() is a snapshot of the global symbol table at the time the function is called.

The primary use case for the globals() function is for introspection or debugging purposes, such as examining the current state of global variables within a function. However, modifying global variables directly using globals() is generally not recommended, as it can lead to code that is hard to understand and maintain. Instead, it's usually better to use explicit assignments or function parameters to modify global variables.
'''