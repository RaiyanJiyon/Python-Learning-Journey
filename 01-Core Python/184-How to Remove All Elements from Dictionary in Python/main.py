'''
To remove all elements from a dictionary in Python, you can use the clear() method. This method removes all key-value pairs from the dictionary, leaving it empty. Here's how you can use it:
'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Clear all elements from the dictionary
my_dict.clear()

print(my_dict)  # Output: {}


'''
After calling the clear() method on the dictionary my_dict, all elements are removed, and the dictionary becomes empty.

Keep in mind that calling clear() modifies the original dictionary in place. If you have multiple references to the same dictionary, all references will reflect the change after the clear() operation.
'''