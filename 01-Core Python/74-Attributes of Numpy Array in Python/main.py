'''
NumPy arrays have several attributes that provide information about their size, shape, data type, and more. Some of the commonly used attributes of NumPy arrays are as follows:

shape: Returns a tuple indicating the dimensions of the array. For a 1D array, the shape is (n,), for a 2D array, it's (n, m), and so on.

ndim: Returns the number of dimensions of the array.

size: Returns the total number of elements in the array.

dtype: Returns the data type of the elements in the array.

itemsize: Returns the size of each element in bytes.

nbytes: Returns the total number of bytes consumed by the elements of the array.

T (or transpose()): Returns the transpose of the array.

real: Returns the real part of complex numbers in the array.

imag: Returns the imaginary part of complex numbers in the array.

flags: Returns information about the memory layout of the array (e.g., whether it's C-contiguous, Fortran-contiguous, etc.).
'''

# Here's how you can access these attributes:
import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Print the attributes of the array
print("Shape:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Total number of elements:", arr.size)
print("Data type of elements:", arr.dtype)
print("Size of each element (in bytes):", arr.itemsize)
print("Total number of bytes consumed:", arr.nbytes)
print("Transpose of the array:")
print(arr.T)
