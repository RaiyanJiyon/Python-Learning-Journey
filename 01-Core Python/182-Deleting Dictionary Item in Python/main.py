'''
In Python, you can delete items from a dictionary using the del keyword or the pop() method. Here's how you can delete items from a dictionary:
'''

'''
Using del Keyword:
You can delete a specific item (key-value pair) from a dictionary using the del keyword followed by the key you want to delete.
'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
del my_dict['age']
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}


'''
Using pop() Method:
The pop() method removes the item with the specified key and returns its value. If the key is not found, it raises a KeyError.
'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
removed_age = my_dict.pop('age')
print("Removed age:", removed_age)  # Output: Removed age: 30
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}


'''
Using popitem() Method:
The popitem() method removes the last inserted item (key-value pair) from the dictionary and returns it as a tuple. If the dictionary is empty, it raises a KeyError
'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
removed_item = my_dict.popitem()
print("Removed item:", removed_item)  # Output: Removed item: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John', 'age': 30}


'''These methods allow you to remove specific items from a dictionary based on their keys. Choose the appropriate method based on whether you need to retrieve the value of the deleted item or if you need to remove the last inserted item.'''