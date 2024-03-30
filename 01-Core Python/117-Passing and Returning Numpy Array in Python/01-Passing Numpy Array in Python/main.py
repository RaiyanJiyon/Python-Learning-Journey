'''
In Python, NumPy arrays are commonly used for numerical computations due to their efficiency and convenience. You can pass NumPy arrays to functions and return them from functions just like any other object. Here's how you can pass and return NumPy arrays in Python:
'''

# First, let's consider passing a NumPy array to a function:
import numpy as np

def modify_array(arr):
    arr[0] = 100  # Modify the first element of the array

# Create a NumPy array
original_array = np.array([1, 2, 3, 4, 5])

# Pass the NumPy array to the function
modify_array(original_array)

print(original_array)  # Output: [100   2   3   4   5]

'''
In this example:

We define a function modify_array(arr) that takes a NumPy array as input and modifies its first element.
We create a NumPy array original_array with values [1, 2, 3, 4, 5].
We pass original_array to the modify_array() function.
The function modifies the first element of the array to 100, and this modification is reflected in the original array.
'''