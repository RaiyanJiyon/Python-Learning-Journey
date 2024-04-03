'''
Tuples are immutable in Python, which means you cannot modify their elements once they are created. If you try to modify a tuple's element, you will encounter a TypeError. This immutability is one of the key differences between tuples and lists.

Here's an example that demonstrates this:
'''

my_tuple = (1, 2, 3)

# Attempt to modify an element of the tuple
my_tuple[0] = 10  # This will raise a TypeError


# output
# TypeError: 'tuple' object does not support item assignment

'''
As you can see, attempting to modify the first element of the tuple my_tuple raises a TypeError because tuples do not support item assignment.

If you need to modify elements in a collection, consider using a list instead of a tuple, as lists are mutable and allow modification of elements. However, if you need an immutable collection, tuples are a suitable choice.
'''