'''
To copy a dictionary in Python, you can use either the copy() method or the built-in dict() constructor. Both methods create a shallow copy of the dictionary, meaning they create a new dictionary containing the same key-value pairs as the original dictionary, but modifying the copy does not affect the original dictionary.

Here's how you can copy a dictionary using both methods:
'''

# Using the copy() method:
original_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Using copy() method to create a copy of the dictionary
copied_dict = original_dict.copy()

# Modify the copied dictionary
copied_dict['age'] = 31

print("Original dictionary:", original_dict)
print("Copied dictionary:", copied_dict)


# Using the dict() constructor:
original_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Using dict() constructor to create a copy of the dictionary
copied_dict = dict(original_dict)

# Modify the copied dictionary
copied_dict['age'] = 31

print("Original dictionary:", original_dict)
print("Copied dictionary:", copied_dict)


'''
Both approaches produce the same result: copied_dict contains a copy of the key-value pairs from original_dict. Any modifications made to copied_dict will not affect original_dict.

Choose the method that suits your preference and coding style. The copy() method may be more explicit, while the dict() constructor is more concise.
'''