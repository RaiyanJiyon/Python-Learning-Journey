'''
In Python, you can create a list of tuples by simply enclosing the tuples within square brackets [] separated by commas. Each tuple within the list can have a different length and contain elements of any data type.

Here's an example of creating a list of tuples:
'''

# List of tuples
list_of_tuples = [
    ('apple', 10),
    ('banana', 20),
    ('orange', 15)
]

# Accessing elements of the list of tuples
print(list_of_tuples[0])  # Output: ('apple', 10)
print(list_of_tuples[1][0])  # Output: 'banana'
print(list_of_tuples[2][1])  # Output: 15


'''
In this example:

We have a list called list_of_tuples containing three tuples.
Each tuple represents a pair of data: the name of a fruit and its corresponding quantity.
We access elements of the list of tuples using indexing. For example, list_of_tuples[0] accesses the first tuple in the list, and list_of_tuples[1][0] accesses the first element of the second tuple.
'''

'''You can perform various operations on a list of tuples, such as appending new tuples, iterating over the list, sorting the list based on tuple elements, etc. Lists of tuples are commonly used to represent tabular data or collections of key-value pairs where each pair is represented as a tuple.
'''