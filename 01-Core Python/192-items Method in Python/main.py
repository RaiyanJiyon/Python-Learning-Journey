'''
In Python, the items() method is used to return a view object that displays a list of tuple pairs representing the key-value pairs in the dictionary. It provides a convenient way to iterate over all key-value pairs in a dictionary.

The syntax for the items() method is as follows
'''

# dictionary_items = my_dict.items()

'''Here's how you can use the items() method:'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Using items() method to get key-value pairs
items = my_dict.items()

# Iterating over the key-value pairs and printing them
for key, value in items:
    print("Key:", key, "| Value:", value)


'''
In this example:

We call the items() method on the dictionary my_dict, which returns a view object containing the key-value pairs.
We iterate over the key-value pairs using a for loop, unpacking each pair into key and value variables.
Within the loop, we print each key-value pair.
The items() method is commonly used when you need to iterate over all key-value pairs in a dictionary or when you want to convert a dictionary into a list of tuples representing its contents.
'''