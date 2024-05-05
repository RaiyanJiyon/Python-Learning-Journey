# Two Dimensional Numpy Array using array Function in Python

To create a two-dimensional NumPy array using the `np.array()` function in Python, you can pass a nested list as an argument where each sublist represents a row of the array. Here's how you can do it:

```python
import numpy as np

# Create a two-dimensional NumPy array using np.array()
two_dim_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Print the array
print(two_dim_array)
```

In this example:

- We import the NumPy library as np.
- We create a two-dimensional NumPy array using np.- array() and pass a nested list containing three sublists, each representing a row of the array.
- Each sublist [1, 2, 3], [4, 5, 6], and [7, 8, 9] represents a row of the two-dimensional array.
- The resulting array is a 3x3 array with elements [1, 2, 3] in the first row, [4, 5, 6] in the second row, and [7, 8, 9] in the third row.

You can customize the dimensions and elements of the array by modifying the nested list accordingly.