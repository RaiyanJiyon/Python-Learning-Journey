'''
In Python, you can copy a list to create a new list with the same elements using various techniques such as slicing, the list() constructor, the copy() method, or the copy module. Let's explore each method:
'''

'''
Using Slicing:

You can use list slicing to create a shallow copy of the original list. This method creates a new list containing all the elements from the original list.
'''

original_list = [1, 2, 3]
copied_list = original_list[:]


'''
Using the list() constructor:

The list() constructor can be used to create a new list with the same elements as the original list.
'''

original_list = [1, 2, 3]
copied_list = list(original_list)


'''
Using the copy() method:

You can use the copy() method of the list to create a shallow copy of the original list.
'''

original_list = [1, 2, 3]
copied_list = original_list.copy()


'''
Using the copy module:

Python's copy module provides a copy() function that can be used to create a shallow copy of the original list.
'''

import copy

original_list = [1, 2, 3]
copied_list = copy.copy(original_list)

'''
All these methods create a shallow copy of the original list, meaning that they create a new list object, but the elements inside the new list are references to the same objects as the elements in the original list. If the elements of the list are mutable objects like lists or dictionaries, changes to these objects inside the copied list will affect the original list and vice versa.
'''

'''If you need a deep copy where the elements are also copied recursively, you can use the copy.deepcopy() function from the copy module. This ensures that changes to the elements in one list do not affect the elements in the other list.
'''
