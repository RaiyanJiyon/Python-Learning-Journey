'''
In Python, you can add elements to a set using the add() method to add a single element, and the update() method to add multiple elements. Both methods modify the original set in place.

Here's how you can add single and multiple elements to a set:
'''

# Adding a Single Element:
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}


# Adding Multiple Elements:
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}


'''
In both examples:

We have a set my_set containing some initial elements.
To add elements, we use the add() method to add a single element (4) in the first example, and the update() method to add multiple elements (4, 5, 6) in the second example.
The add() method takes a single argument, while the update() method takes an iterable (such as a list, tuple, or another set) containing the elements to be added.
Both methods modify the original set in place.
'''

'''It's worth noting that if you try to add an element that already exists in the set, it will not be added again, as sets in Python cannot contain duplicate elements.
'''