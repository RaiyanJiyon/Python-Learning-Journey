'''
In Python, aliasing a list refers to creating multiple references (or aliases) to the same list object. This means that changes made to one reference of the list will affect all other references to the same list object. Here's how aliasing works:
'''

# Creating a list
original_list = [1, 2, 3]

# Creating an alias to the original list
alias_list = original_list

# Modifying the alias_list
alias_list.append(4)

# Both lists are affected because they refer to the same object
print(original_list)  # Output: [1, 2, 3, 4]
print(alias_list)     # Output: [1, 2, 3, 4]

'''
In this example, original_list and alias_list both refer to the same list object [1, 2, 3]. When we append 4 to alias_list, the modification is reflected in both lists because they are aliases of each other.
'''

'''
It's essential to understand aliasing when working with mutable objects like lists in Python because unintentional aliasing can lead to unexpected behavior in your code. To avoid unintended aliasing, you can use the copy() method or the list() constructor to create a separate copy of the list:
'''

# Creating a copy of the original list
copied_list = original_list.copy()

# Modifying the copied_list
copied_list.append(5)

# Only the copied_list is affected
print(original_list)  # Output: [1, 2, 3, 4]
print(copied_list)    # Output: [1, 2, 3, 4, 5]

'''Now, modifying copied_list does not affect original_list because copied_list is a separate copy of the list.'''