'''
Flatten Method (flatten()):
The flatten() method in NumPy is used to flatten a multi-dimensional array into a one-dimensional array. It returns a new one-dimensional array containing all the elements of the original array.
'''

# Here's how you can use the flatten() method:
import numpy as np

# Create a two-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the array
flattened_arr = arr.flatten()

print("Original array:")
print(arr)
print("\nFlattened array:")
print(flattened_arr)

'''Notes:
reshape() returns a new view of the array with the specified shape, while flatten() returns a new one-dimensional array.
reshape() requires the new shape to be compatible with the original shape of the array, while flatten() always returns a one-dimensional array.

Both reshape() and flatten() do not modify the original array; they return new arrays.'''