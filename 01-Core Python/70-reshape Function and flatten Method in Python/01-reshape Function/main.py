'''
In Python, NumPy provides the reshape() function and the flatten() method for reshaping and flattening arrays, respectively.
'''

'''
Reshape Function (reshape()):
The reshape() function in NumPy is used to change the shape of an array without changing its data. It returns a new view of the array with the specified shape.
'''

# Here's how you can use the reshape() function:
import numpy as np

# Create a one-dimensional array
arr = np.arange(1, 13)

# Reshape the array into a two-dimensional array with 3 rows and 4 columns
reshaped_arr = arr.reshape(3, 4)

print("Original array:")
print(arr)
print("\nReshaped array:")
print(reshaped_arr)
