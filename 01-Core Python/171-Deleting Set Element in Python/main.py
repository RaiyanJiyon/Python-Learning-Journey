'''
In Python, you can delete elements from a set using the remove(), discard(), or pop() methods.
'''

# Using the remove() method:
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

'''
The remove() method removes the specified element from the set. If the element is not present, it raises a KeyError.
'''

# Using the discard() method:
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)  # Output: {1, 2, 4, 5}

'''
The discard() method removes the specified element from the set if it is present. If the element is not present, it does nothing and does not raise any error.
'''

# Using the pop() method:
my_set = {1, 2, 3, 4, 5}
element = my_set.pop()
print("Popped element:", element)  # Output: Popped element: 1
print("Updated set:", my_set)  # Output: Updated set: {2, 3, 4, 5}

'''
The pop() method removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.
'''

'''You can choose the appropriate method based on whether you want to handle the case where the element may not exist in the set (discard()), or if you want to ensure that the element exists before removing it (remove()). Additionally, pop() can be useful if you want to remove and retrieve an arbitrary element from the set.
'''