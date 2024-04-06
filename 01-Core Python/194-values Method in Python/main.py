'''
In Python, the values() method is used to return a view object that displays a list of all values in the dictionary. It provides a convenient way to iterate over all values in a dictionary or to obtain a list of values.

The syntax for the values() method is as follows:
'''

# dictionary_values = my_dict.values()

'''Here's how you can use the values() method:'''

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Using values() method to get values
values = my_dict.values()

# Iterating over the values and printing them
for value in values:
    print("Value:", value)


'''
In this example:

We call the values() method on the dictionary my_dict, which returns a view object containing all values in the dictionary.
We iterate over the values using a for loop and print each value.
The values() method is commonly used when you need to iterate over all values in a dictionary or when you want to obtain a list of values for further processing.
'''