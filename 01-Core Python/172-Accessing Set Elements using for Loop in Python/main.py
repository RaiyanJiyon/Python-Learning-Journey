'''
You can access elements of a set using a for loop in Python. When iterating over a set, the loop iterates over each element in the set, but the order of iteration is arbitrary due to the unordered nature of sets.

Here's how you can access set elements using a for loop:
'''

my_set = {1, 2, 3, 4, 5}

# Accessing elements of a set using a for loop
for element in my_set:
    print(element)


'''
In this example:

We have a set called my_set containing some elements.
We use a for loop to iterate over each element in the set.
During each iteration, the variable element takes on the value of each element in the set, one at a time.
Inside the loop, we print each element.
Since sets are unordered collections, the order of elements during iteration is not guaranteed to be the same as the order in which elements were inserted into the set. However, the loop will iterate over all elements of the set exactly once.
'''