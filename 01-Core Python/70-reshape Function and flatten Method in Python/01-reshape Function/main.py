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
