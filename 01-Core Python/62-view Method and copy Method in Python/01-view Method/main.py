'''
In Python, when working with NumPy arrays, the view() and copy() methods are used to create new array objects based on existing arrays. However, they behave differently in terms of how they handle memory and data.
'''

'''
view() Method:
The view() method creates a new array object that is a shallow copy of the original array. This means that the new array shares the same data buffer as the original array, but it has a different shape or strides. Changes made to the data in the new array will be reflected in the original array and vice versa.
'''

import numpy as np

# Create an array
arr1 = np.array([1, 2, 3, 4, 5])

# Create a view of the original array
arr2 = arr1.view()

# Modify the view
arr2[0] = 10

# Changes are reflected in the original array
print(arr1)  # Output: [10  2  3  4  5]
