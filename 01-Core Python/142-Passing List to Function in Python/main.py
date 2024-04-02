'''
In Python, you can pass a list to a function just like you would pass any other object. Lists are mutable objects, so any changes made to the list within the function will affect the original list. Here's how you can pass a list to a function:
'''

def process_list(my_list):
    # Modify the list inside the function
    my_list.append(4)
    my_list[0] = "a"
    print("Inside the function:", my_list)

# Define a list
original_list = [1, 2, 3]

# Call the function and pass the list as an argument
process_list(original_list)

# Changes made inside the function affect the original list
print("Outside the function:", original_list)


'''
In this example:

We define a function process_list that takes a list my_list as a parameter.
Inside the function, we modify the list by appending an element (4) and changing the value of the first element ('a').
We define an original_list containing [1, 2, 3].
We call the process_list function and pass original_list as an argument.
Changes made to original_list inside the function are reflected outside the function as well, demonstrating that lists are mutable objects in Python.
'''

'''You can manipulate the list inside the function as needed, including appending, removing, or modifying elements. However, be cautious when modifying the list within the function, especially if you want to preserve the original list. If you need to work with a copy of the original list inside the function to avoid modifying it, you can create a copy of the list using the copy() method or the slicing technique discussed earlier.
'''