'''
In Python, functions can return single values or multiple values. Here's how you can return single and multiple values from a function:
'''

'''
Returning a Single Value:
To return a single value from a function, you use the return statement followed by the value you want to return.
'''

def add(a, b):
    """This function adds two numbers."""
    return a + b

result = add(3, 5)
print(result)  # Output: 8

'''
In this example, the add() function returns the sum of two numbers a and b. When you call the function with arguments 3 and 5, it returns 8, which is stored in the result variable.
'''