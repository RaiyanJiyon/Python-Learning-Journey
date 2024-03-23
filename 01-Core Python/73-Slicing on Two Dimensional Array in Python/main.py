'''
Slicing on a two-dimensional NumPy array allows you to extract specific portions of the array based on the indices of rows and columns. You can slice rows, columns, or both simultaneously. Here's how you can perform slicing on a two-dimensional array:
'''
import numpy as np

# Create a two-dimensional NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Slicing rows and columns
# Syntax: arr[start_row:end_row, start_col:end_col]

# Slicing a single row (second row)
print("Second row:", arr[1, :])

# Slicing a single column (second column)
print("Second column:", arr[:, 1])

# Slicing a subarray (extracting a 2x2 subarray from the original array)
print("Subarray:")
print(arr[0:2, 0:2])
