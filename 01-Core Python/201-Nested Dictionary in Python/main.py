'''
A nested dictionary in Python is a dictionary that contains another dictionary (or dictionaries) as its values. This allows you to represent hierarchical or structured data more effectively, where each level of the dictionary represents a different level of the hierarchy.

Here's an example of a nested dictionary:
'''

nested_dict = {
    'person1': {'name': 'John', 'age': 30, 'city': 'New York'},
    'person2': {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
}


'''
In this example, nested_dict is a dictionary with two key-value pairs, where each value is itself a dictionary representing information about a person. Each inner dictionary contains keys such as 'name', 'age', and 'city', with corresponding values.

You can access elements of a nested dictionary using multiple keys. For example:
'''

# Accessing nested dictionary elements
print("Name of person1:", nested_dict['person1']['name'])  # Output: Name of person1: John
print("Age of person2:", nested_dict['person2']['age'])    # Output: Age of person2: 25


