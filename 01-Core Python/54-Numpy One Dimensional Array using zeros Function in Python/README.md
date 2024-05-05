# Numpy One Dimensional Array using zeros Function in Python

You can create a one-dimensional NumPy array filled with zeros using the `numpy.zeros()` function. This function generates an array of specified shape and fills it with zeros.

Here's how you can create a one-dimensional NumPy array filled with zeros using the `numpy.zeros()` function:

```python
import numpy as np

# Create a one-dimensional NumPy array with 5 zeros
my_array = np.zeros(5)

# Print the array
print(my_array)
```

In this example:

- We first import the NumPy library as `np`.
- We use the `np.zeros()` function to create a one-dimensional NumPy array named `my_array`.
- The function takes one argument: the shape of the array (in this case, 5).
- The `np.zeros()` function generates an array of shape (5,) filled with zeros and stores it in the array `my_array`.
- Finally, we print the array to display the values.

Each element in the array is initialized to 0.0. The `numpy.zeros()` function is useful when you need to create an array of zeros to store data or initialize an array before filling it with actual values.