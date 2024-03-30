'''
In Python, you can pass arrays (or more accurately, lists) to functions just like any other object. Lists are mutable, meaning they can be modified in place within a function, and any changes made to them will be reflected outside the function. Here's a simple example demonstrating how to pass a list to a function:
'''

def modify_list(my_list):
    my_list.append(4)  # This modifies the original list

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

'''
In this example:

We define a function modify_list() that takes a single parameter my_list.
Inside the function, we append the value 4 to the end of my_list.
We then define a list my_list with values [1, 2, 3].
We call the modify_list() function, passing my_list as an argument.
After the function call, my_list has been modified to [1, 2, 3, 4].
'''

'''It's important to note that when you pass a list to a function, you are passing a reference to the list object in memory, not a copy of the list. Therefore, any modifications made to the list within the function will affect the original list outside the function. This behavior is consistent with Python's "pass by object reference" model.

You can also pass arrays of other types, such as NumPy arrays, to functions in a similar manner. However, the specific behavior may depend on the type of array and the function being called.
'''