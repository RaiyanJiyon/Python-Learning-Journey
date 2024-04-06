'''
In Python, the keys() method is used to return a view object that displays a list of all keys in the dictionary. It provides a convenient way to iterate over all keys in a dictionary or to obtain a list of keys.

The syntax for the keys() method is as follows:
'''

# dictionary_keys = my_dict.keys()

'''Here's how you can use the keys() method:'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Using keys() method to get keys
keys = my_dict.keys()

# Iterating over the keys and printing them
for key in keys:
    print("Key:", key)

'''
In this example:

We call the keys() method on the dictionary my_dict, which returns a view object containing all keys in the dictionary.
We iterate over the keys using a for loop and print each key.
The keys() method is commonly used when you need to iterate over all keys in a dictionary or when you want to obtain a list of keys for further processing.
'''