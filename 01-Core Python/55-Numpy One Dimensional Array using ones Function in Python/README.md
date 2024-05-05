# Numpy One Dimensional Array using ones Function in Python

You can create a one-dimensional NumPy array filled with ones using the `numpy.ones()` function. This function generates an array of specified shape and fills it with ones.

Here's how you can create a one-dimensional NumPy array filled with ones using the `numpy.ones()` function:

```python
import numpy as np

# Create a one-dimensional NumPy array with 5 ones
my_array = np.ones(5)

# Print the array
print(my_array)
```

In this example:

- We first import the NumPy library as `np`.
- We use the `np.ones()` function to create a one-dimensional NumPy array named `my_array`.
- The function takes one argument: the shape of the array (in this case, 5).
- The `np.ones()` function generates an array of shape (5,) filled with ones and stores it in the array `my_array`.
- Finally, we print the array to display the values.

Each element in the array is initialized to 1.0. The `numpy.ones()` function is useful when you need to create an array filled with ones to store data or initialize an array before filling it with actual values.