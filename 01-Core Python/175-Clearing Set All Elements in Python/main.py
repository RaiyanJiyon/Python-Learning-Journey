'''
To clear all elements from a set in Python, you can use the clear() method. This method removes all elements from the set, making it an empty set.

Here's how you can clear all elements from a set:
'''

my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)  # Output: Original set: {1, 2, 3, 4, 5}

# Clear all elements from the set
my_set.clear()

print("Cleared set:", my_set)  # Output: Cleared set: set()


'''
In this example:

We have a set called my_set containing some elements.
We print the original set.
We use the clear() method to remove all elements from the set.
We print the set after clearing it, which results in an empty set set().
After calling clear(), the set becomes empty. It's important to note that calling clear() modifies the original set in place. If you have multiple references to the same set, all references will reflect the change after the clear() operation.
'''