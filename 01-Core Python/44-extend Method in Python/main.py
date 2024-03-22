'''
In Python, the extend() method is used to add elements from an iterable (such as a list, tuple, or another array) to the end of the list on which it's called. It modifies the original list in place. The syntax for using the extend() method is:
'''

# list_name.extend(iterable)
'''
list_name: The name of the list to which you want to add elements.
iterable: An iterable object (such as a list, tuple, or array) containing the elements you want to add to the list
'''

# Here's an example demonstrating the usage of the extend() method:
my_list = [1, 2, 3]
other_list = [4, 5, 6]

# Extend my_list with elements from other_list
my_list.extend(other_list)
print("Extended list:", my_list)  # Output: Extended list: [1, 2, 3, 4, 5, 6]

'''In this example:

We have a list named my_list containing [1, 2, 3].
We have another list named other_list containing [4, 5, 6].
We use the extend() method to add elements from other_list to the end of my_list.
After extending my_list, it becomes [1, 2, 3, 4, 5, 6].'''

'''The extend() method is particularly useful when you want to combine multiple lists or concatenate multiple iterable objects into a single list. It directly modifies the original list in place, so any changes made by this method are reflected in the original list.'''