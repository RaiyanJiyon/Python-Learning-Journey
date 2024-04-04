'''
To copy the elements of a set in Python, you can use either the copy() method or the set() constructor. Both methods create a shallow copy of the set, meaning they create a new set containing the same elements as the original set, but modifying the copy does not affect the original set.

Here's how you can copy a set:
'''

# Using the copy() method:
original_set = {1, 2, 3}
copied_set = original_set.copy()

# Modify the copied set
copied_set.add(4)

print("Original set:", original_set)  # Output: Original set: {1, 2, 3}
print("Copied set:", copied_set)      # Output: Copied set: {1, 2, 3, 4}


# Using the set() constructor:
original_set = {1, 2, 3}
copied_set = set(original_set)

# Modify the copied set
copied_set.add(4)

print("Original set:", original_set)  # Output: Original set: {1, 2, 3}
print("Copied set:", copied_set)      # Output: Copied set: {1, 2, 3, 4}


'''Both approaches produce the same result: copied_set contains a copy of the elements from original_set. Any modifications made to copied_set will not affect original_set.

Choose the method that suits your preference and coding style. The copy() method may be more explicit, while the set() constructor is more concise.'''