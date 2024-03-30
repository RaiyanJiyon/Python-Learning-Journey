'''
In Python, the extend() method is a built-in function used to append elements from an iterable (such as a list, tuple, or string) to the end of the list. It modifies the original list by adding all the elements from the iterable to the end of the list. The syntax for using the extend() method is as follows:
'''

# list_name.extend(iterable)

'''
Where:

list_name is the name of the list to which you want to append elements.
iterable is an iterable object (such as a list, tuple, string, etc.) containing the elements you want to append to the list.
'''

# Here's an example demonstrating how to use the extend() method:
# Define a list
my_list = [1, 2, 3]

# Define another list containing elements to append
additional_elements = [4, 5, 6]

# Append elements from the additional list to the end of my_list
my_list.extend(additional_elements)

print("Extended List:", my_list)  # Output: Extended List: [1, 2, 3, 4, 5, 6]


'''
In this example:

We have a list called my_list containing some elements.
We define another list called additional_elements containing elements that we want to append to my_list.
We use the extend() method to append all elements from additional_elements to the end of my_list.
After extending, the my_list contains all elements from both lists [1, 2, 3, 4, 5, 6].
'''

'''The extend() method modifies the original list in place and does not return any value. Therefore, you don't need to assign the result of the extend() method to a new variable.
'''