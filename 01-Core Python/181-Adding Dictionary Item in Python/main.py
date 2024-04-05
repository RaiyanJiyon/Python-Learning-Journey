'''
In Python, you can add items to a dictionary by assigning a value to a new key or by using the update() method. Here's how you can add items to a dictionary:
'''

'''
Using Assignment:
You can add a new key-value pair to a dictionary by assigning a value to a new key that doesn't already exist in the dictionary.
'''

my_dict = {'name': 'John', 'age': 30}
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


'''
Using the update() Method:
The update() method adds the key-value pairs from one dictionary (or any iterable of key-value pairs) to another dictionary.
'''

my_dict = {'name': 'John', 'age': 30}
extra_info = {'city': 'New York', 'job': 'Engineer'}
my_dict.update(extra_info)
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}


'''These methods allow you to dynamically add new key-value pairs to a dictionary as needed during program execution. Just be aware that if you try to assign a value to an existing key using the assignment method, it will overwrite the existing value. However, using update() will add new key-value pairs and update existing ones without overwriting.'''