'''
In Python, the pop() method is a built-in function used to remove and return the element at a specified index from a list. If no index is specified, the pop() method removes and returns the last element of the list.
'''

# Here's an example demonstrating how to use the pop() method:

# Define a list
my_list = [1, 2, 3, 4, 5]

# Remove and return the element at index 2
removed_element = my_list.pop(2)

print("Removed Element:", removed_element)  # Output: Removed Element: 3
print("Updated List:", my_list)             # Output: Updated List: [1, 2, 4, 5]

'''
In this example:

We have a list called my_list containing integers.
We use the pop() method to remove and return the element at index 2, which is 3.
The value 3 is assigned to the variable removed_element.
After the removal, the list is updated to [1, 2, 4, 5].
'''

# If no index is specified, the pop() method removes and returns the last element of the list:
# Remove and return the last element of the list
last_element = my_list.pop()

print("Last Element:", last_element)  # Output: Last Element: 5
print("Updated List:", my_list)        # Output: Updated List: [1, 2, 4]


'''In this case, the last element of the list, which is 5, is removed and assigned to the variable last_element.'''