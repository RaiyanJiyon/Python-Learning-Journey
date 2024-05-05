# Numpy Two Dimensional Array using ones Function in Python

To create a two-dimensional NumPy array filled with ones, you can use the `numpy.ones()` function and specify the desired shape of the array. Here's how you can do it:

```python
import numpy as np

# Define the shape of the array (rows x columns)
rows = 3
cols = 4

# Create a two-dimensional NumPy array filled with ones
two_dim_array = np.ones((rows, cols))

# Print the array
print(two_dim_array)
```

In this code:

- We import the NumPy library as np.
- We define the shape of the array by specifying the number of rows (rows) and columns (cols).
- We create a two-dimensional NumPy array filled with ones using the np.ones() function. 
- The argument to this function is a tuple (rows, cols) specifying the shape of the array.
- Finally, we print the array to display its contents.

This code creates a 3x4 two-dimensional NumPy array filled with ones. You can adjust the values of rows and cols to create arrays of different shapes.