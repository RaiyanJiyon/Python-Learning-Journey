'''
In Python, the index() method is used to find the index of the first occurrence of a specified value within a list. It returns the index of the first occurrence of the value if found, otherwise, it raises a ValueError. The syntax for using the index() method is:
'''

# index = list_name.index(value)
'''
list_name: The name of the list in which you want to find the index of the value.
value: The value for which you want to find the index.
'''

# Here's an example demonstrating the usage of the index() method:
my_list = [1, 2, 3, 4, 3, 5]

# Find the index of the first occurrence of the value 3
index = my_list.index(3)
print("Index of value 3:", index)  # Output: Index of value 3: 2

'''In this example:

We have a list named my_list containing [1, 2, 3, 4, 3, 5].
We use the index() method to find the index of the first occurrence of the value 3.
The index of the first occurrence of 3 is 2.'''


'''
If the specified value is not found in the list, the index() method raises a ValueError. Therefore, it's a good practice to first check if the value exists in the list using the in operator or handle the ValueError using a try-except block.
'''
my_list = [1, 2, 4, 5]

# Attempt to find the index of the value 3 (which does not exist in the list)
try:
    index = my_list.index(3)
    print("Index of value 3:", index)
except ValueError:
    print("Value not found in the list")

'''The index() method is useful for finding the position of a specific element within a list. It allows you to determine the index of an element based on its value.'''