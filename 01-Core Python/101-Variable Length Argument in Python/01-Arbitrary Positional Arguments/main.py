'''
In Python, you can define functions that accept a variable number of arguments using variable-length argument syntax. There are two types of variable-length arguments: *args and **kwargs.
'''

'''
Arbitrary Positional Arguments (*args):
Arbitrary positional arguments (often denoted as *args) allow a function to accept a variable number of positional arguments. These arguments are passed to the function as a tuple, allowing you to iterate over them within the function.
'''

# Here's how you can define a function with *args:
def my_function(*args):
    for arg in args:
        print(arg)

# Call the function with multiple arguments
my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello

'''In this example, the function my_function accepts a variable number of positional arguments, which are collected into the args tuple. Inside the function, we iterate over the args tuple and print each argument.'''