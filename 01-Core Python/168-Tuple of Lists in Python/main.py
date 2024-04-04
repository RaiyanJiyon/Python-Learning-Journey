'''
In Python, you can create a tuple of lists by enclosing the lists within parentheses () and separating them with commas. Each list within the tuple can contain elements of any data type and can have different lengths.

Here's an example of creating a tuple of lists:
'''

# Tuple of lists
tuple_of_lists = (
    [1, 2, 3],
    ['a', 'b', 'c'],
    ['apple', 'banana', 'orange']
)

# Accessing elements of the tuple of lists
print(tuple_of_lists[0])  # Output: [1, 2, 3]
print(tuple_of_lists[1][0])  # Output: 'a'
print(tuple_of_lists[2][2])  # Output: 'orange'


'''
In this example:

We have a tuple called tuple_of_lists containing three lists.
Each list represents a sequence of elements: integers, characters, and strings, respectively.
We access elements of the tuple of lists using indexing. For example, tuple_of_lists[0] accesses the first list in the tuple, and tuple_of_lists[1][0] accesses the first element of the second list.
'''

'''You can perform various operations on a tuple of lists, such as appending new elements to the lists, iterating over the tuple, accessing and modifying elements of the lists, etc. Tuples of lists can be useful when you want to group related lists together, especially when the number of lists is fixed and known in advance.
'''