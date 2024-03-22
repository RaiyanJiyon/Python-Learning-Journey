'''
In Python, the reverse() method is used to reverse the order of elements in a list. It modifies the original list in place and does not return any value (it returns None). The syntax for using the reverse() method is:
'''

# list_name.reverse()
'''
list_name: The name of the list that you want to reverse.
'''

# Here's an example demonstrating the usage of the reverse() method:
my_list = [1, 2, 3, 4, 5]

# Reverse the order of elements in the list
my_list.reverse()
print("Reversed list:", my_list)  # Output: Reversed list: [5, 4, 3, 2, 1]

'''In this example:

We have a list named my_list containing [1, 2, 3, 4, 5].
We use the reverse() method to reverse the order of elements in the list.
After reversing, the list becomes [5, 4, 3, 2, 1].'''

'''
The reverse() method directly modifies the original list in place, so any changes made by this method are reflected in the original list. If you want to create a new list with the reversed order of elements without modifying the original list, you can use slicing:
'''
my_list = [1, 2, 3, 4, 5]

# Create a new list with the reversed order of elements
reversed_list = my_list[::-1]
print("Original list:", my_list)      # Output: Original list: [1, 2, 3, 4, 5]
print("Reversed list:", reversed_list)  # Output: Reversed list: [5, 4, 3, 2, 1]

'''The reverse() method is useful when you need to reverse the order of elements in a list in place, without creating a new list object.'''