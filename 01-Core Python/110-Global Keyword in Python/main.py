'''
In Python, the global keyword is used to declare that a variable inside a function should refer to the globally scoped variable of the same name, rather than creating a new local variable with the same name. This allows you to modify global variables from within a function's scope.
'''


# Here's a basic example of using the global keyword:
global_var = 10

def modify_global():
    global global_var
    global_var = 20

print("Before function call:", global_var)
modify_global()
print("After function call:", global_var)

'''
In this example:

We have a global variable global_var initialized to 10.
Inside the modify_global() function, we use the global keyword to declare that global_var refers to the global variable with the same name.
We modify the value of global_var to 20 within the function.
When we print the value of global_var before and after calling the function, we see that it has been modified.
Without the global keyword, global_var would be treated as a local variable within the modify_global() function, and modifying it would not affect the global variable with the same name.
'''

'''It's important to note that using global variables can make code harder to understand and debug, and it's generally recommended to avoid them when possible. Instead, consider passing values as parameters to functions or returning values from functions. However, in cases where you do need to modify global variables within a function, the global keyword provides a way to do so.'''