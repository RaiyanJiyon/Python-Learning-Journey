'''
In Python, you can concatenate tuples using the + operator. This operation creates a new tuple containing all the elements of the concatenated tuples. Here's how you can concatenate tuples:
'''

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

concatenated_tuple = tuple1 + tuple2

print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

'''
In this example:

We have two tuples, tuple1 and tuple2, with elements (1, 2, 3) and ('a', 'b', 'c'), respectively.
We use the + operator to concatenate tuple1 and tuple2.
The result is a new tuple concatenated_tuple containing all the elements of tuple1 followed by all the elements of tuple2.
You can also concatenate multiple tuples in a single expression:
'''

tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = (5, 6)

concatenated_tuple = tuple1 + tuple2 + tuple3

print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)


'''This will concatenate all three tuples into a single tuple concatenated_tuple, containing all the elements from tuple1, tuple2, and tuple3.'''