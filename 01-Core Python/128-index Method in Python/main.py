'''
In Python, the index() method is a built-in function used to find the index of the first occurrence of a specified value within a list. It returns the index of the first occurrence of the specified value in the list. If the value is not found in the list, the index() method raises a ValueError exception. The syntax for using the index() method is as follows:
'''

# index = list_name.index(value)

'''
Where:

list_name is the name of the list in which you want to find the index of the value.
value is the value for which you want to find the index.
'''

# Here's an example demonstrating how to use the index() method:
# Define a list
my_list = [1, 2, 3, 4, 3, 5]

# Find the index of the first occurrence of the value 3
index = my_list.index(3)

print("Index:", index)  # Output: Index: 2


'''
In this example:

We have a list called my_list containing integers.
We use the index() method to find the index of the first occurrence of the value 3 in the list.
The index of the first occurrence of 3 is 2, so it is assigned to the variable index.
If the specified value is not found in the list, the index() method raises a ValueError exception:
'''

# Attempt to find the index of a value that does not exist in the list
# index = my_list.index(6)  Raises ValueError: 6 is not in list

'''It's important to note that the index() method only returns the index of the first occurrence of the specified value. If there are multiple occurrences of the value in the list and you want to find all of their indices, you would need to use a loop or list comprehension to iterate over the list and find each occurrence individually.'''
