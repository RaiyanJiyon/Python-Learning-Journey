'''
In Python, the concept of "pass by object reference" or "call by object reference" is often used to describe how arguments are passed to functions. However, it's important to understand that Python does not strictly adhere to either pass by value or pass by reference, as seen in some other programming languages. Instead, Python uses a mechanism that can be thought of as "pass by object reference."

Here's how it works:

Pass by Object Reference:
When you pass an argument to a function in Python, you are actually passing a reference to the object in memory, not the object itself.
If the object is mutable (e.g., a list or a dictionary), changes made to the object inside the function will affect the original object outside the function.
If the object is immutable (e.g., a string or a tuple), changes made to the object inside the function will not affect the original object outside the function. Instead, a new object will be created with the modified value.
'''

# Here's an example to illustrate this behavior:
def modify_list(my_list):
    my_list.append(4)  # This modifies the original list

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

def modify_string(my_string):
    my_string += " World"  # This creates a new string object

my_string = "Hello"
modify_string(my_string)
print(my_string)  # Output: Hello

'''
In this example:

When my_list is passed to the modify_list() function, changes made to my_list inside the function are reflected in the original list outside the function.
When my_string is passed to the modify_string() function, the += operation creates a new string object with the concatenated value, but this change is not reflected in the original string object outside the function.
'''

'''Understanding how Python handles objects and references is essential for writing correct and efficient code, especially when dealing with mutable objects like lists and dictionaries.
'''