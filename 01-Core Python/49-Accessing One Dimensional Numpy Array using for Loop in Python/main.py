'''
You can access elements of a one-dimensional NumPy array using a for loop just like you would with a Python list. Here's how you can iterate over the elements of a one-dimensional NumPy array using a for loop
'''

import numpy as np

# Create a one-dimensional NumPy array
my_array = np.array([1, 2, 3, 4, 5])

# Access elements of the array using a for loop
for element in my_array:
    print(element)


'''
You can also access the index of each element using the enumerate() function:
'''

# Access elements and their indices using a for loop and enumerate
for index, element in enumerate(my_array):
    print("Index:", index, "Element:", element)

'''Using a for loop to iterate over a one-dimensional NumPy array can be useful for performing various operations on its elements or for applying conditional logic.'''