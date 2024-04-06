'''
In Python, the update() method is used to update a dictionary with elements from another dictionary or from an iterable of key-value pairs. It adds key-value pairs from the specified dictionary or iterable to the dictionary on which the method is called. If a key from the specified dictionary already exists in the original dictionary, its value is updated with the new value.

The syntax for the update() method is as follows:
'''

# my_dict.update(iterable_or_dictionary)

'''
Here's how you can use the update() method:

Updating with another Dictionary:
'''

my_dict = {'name': 'John', 'age': 30}
extra_info = {'city': 'New York', 'job': 'Engineer'}

# Update my_dict with elements from extra_info
my_dict.update(extra_info)

print(my_dict)


'''Updating with an Iterable of Key-Value Pairs:'''

my_dict = {'name': 'John', 'age': 30}

# Update my_dict with key-value pairs from a list of tuples
new_info = [('city', 'New York'), ('job', 'Engineer')]
my_dict.update(new_info)

print(my_dict)


'''
In both examples:

We call the update() method on the dictionary my_dict.
We pass either another dictionary or an iterable of key-value pairs to the update() method.
The method updates my_dict with the key-value pairs from the specified dictionary or iterable.
The update() method is commonly used when you want to merge two dictionaries or add multiple key-value pairs to an existing dictionary.
'''