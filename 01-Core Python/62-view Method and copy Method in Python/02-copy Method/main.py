'''
copy() Method:
The copy() method creates a new array object with a complete copy of the data from the original array. This means that changes made to the data in the new array will not affect the original array, and vice versa. The new array is completely independent of the original array.
'''

import numpy as np

# Create an array
arr1 = np.array([1, 2, 3, 4, 5])

# Create a copy of the original array
arr2 = arr1.copy()

# Modify the copy
arr2[0] = 10

# Changes are not reflected in the original array
print(arr1)  # Output: [1 2 3 4 5]

'''Summary:
view() creates a shallow copy that shares the data buffer with the original array.
copy() creates a deep copy with its own separate data buffer, independent of the original array.

Use view() when you want to manipulate array data while preserving the original array, and use copy() when you want a completely independent copy of the array.'''