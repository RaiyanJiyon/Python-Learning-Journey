# reshape Function and flatten Method in Python

In Python, NumPy provides the `reshape()` function and the `flatten()` method for reshaping and flattening arrays, respectively.

## Reshape Function (reshape()):
The reshape() function in NumPy is used to change the shape of an array without changing its data. It returns a new view of the array with the specified shape.


### Here's how you can use the reshape() function:

```python
import numpy as np

# Create a one-dimensional array
arr = np.arange(1, 13)

# Reshape the array into a two-dimensional array with 3 rows and 4 columns
reshaped_arr = arr.reshape(3, 4)

print("Original array:")
print(arr)
print("\nReshaped array:")
print(reshaped_arr)
```

## Flatten Method (flatten()):
The flatten() method in NumPy is used to flatten a multi-dimensional array into a one-dimensional array. It returns a new one-dimensional array containing all the elements of the original array.
'''

### Here's how you can use the flatten() method:

```python
import numpy as np

# Create a two-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the array
flattened_arr = arr.flatten()

print("Original array:")
print(arr)
print("\nFlattened array:")
print(flattened_arr)
```

`Notes`:
- reshape() returns a new view of the array with the specified shape, while flatten() returns a new one-dimensional array.
- reshape() requires the new shape to be compatible with the original shape of the array, while flatten() always returns a one-dimensional array.

Both reshape() and flatten() do not modify the original array; they return new arrays.