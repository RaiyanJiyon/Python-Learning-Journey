'''

In Python, a dictionary is an unordered collection of key-value pairs. It is also known as an associative array or a hash map in other programming languages. Dictionaries are mutable, meaning they can be modified after creation. Each key in a dictionary must be unique and immutable (such as strings, numbers, or tuples), while values can be of any data type and can be duplicated.

Here's how you can create a dictionary in Python:
'''

# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements of the dictionary
print("Name:", my_dict['name'])  # Output: Name: John
print("Age:", my_dict['age'])    # Output: Age: 30
print("City:", my_dict['city'])  # Output: City: New York


'''
In this example:

We define a dictionary called my_dict using curly braces {}. Each key-value pair is separated by a colon : and each pair is separated by a comma.
The keys 'name', 'age', and 'city' are strings, and their corresponding values are 'John', 30, and 'New York', respectively.
We access elements of the dictionary using square brackets [] with the key to retrieve the corresponding value.
Dictionaries are commonly used when you want to store data in a structured format, where each piece of data has a unique identifier (key). They are versatile data structures that allow for efficient data retrieval and manipulation.
'''