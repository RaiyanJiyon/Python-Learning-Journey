'''
In Python, dictionaries are mutable, meaning you can modify them after creation. You can add, update, or delete key-value pairs as needed. Here's how you can modify a dictionary:
'''

'''
Adding a New Key-Value Pair:
You can add a new key-value pair to a dictionary by simply assigning a value to a new key that doesn't already exist in the dictionary.
'''

my_dict = {'name': 'John', 'age': 30}
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


'''
Updating an Existing Key's Value:
If the key already exists in the dictionary, assigning a new value to that key will update its value.
'''

my_dict = {'name': 'John', 'age': 30}
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31}


'''
Deleting a Key-Value Pair:
You can delete a key-value pair from a dictionary using the del keyword or the pop() method.
'''

my_dict = {'name': 'John', 'age': 30}
del my_dict['age']
print(my_dict)  # Output: {'name': 'John'}

# Using pop() method
my_dict = {'name': 'John', 'age': 30}
my_dict.pop('age')
print(my_dict)  # Output: {'name': 'John'}


'''
Clearing the Entire Dictionary:
You can remove all key-value pairs from a dictionary using the clear() method.
'''

my_dict = {'name': 'John', 'age': 30}
my_dict.clear()
print(my_dict)  # Output: {}


'''These are some of the common ways to modify a dictionary in Python. Dictionaries provide a flexible and efficient way to store and manipulate data with unique keys.'''