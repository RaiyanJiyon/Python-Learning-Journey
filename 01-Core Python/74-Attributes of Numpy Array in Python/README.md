# Attributes of Numpy Array in Python

In Python's NumPy library, arrays are the fundamental data structure used for numerical computations. NumPy arrays, or `ndarray` objects, have several attributes that provide information about their shape, size, data type, and memory layout. Here are some of the key attributes of NumPy arrays:

1. **`ndarray.shape`**:
   - Returns a tuple representing the dimensions (shape) of the array.
   - Example:
     ```python
     import numpy as np

     arr = np.array([[1, 2, 3], [4, 5, 6]])
     print(arr.shape)  # Output: (2, 3)
     ```

2. **`ndarray.ndim`**:
   - Returns the number of dimensions (axes) of the array.
   - Example:
     ```python
     import numpy as np

     arr = np.array([[1, 2, 3], [4, 5, 6]])
     print(arr.ndim)  # Output: 2
     ```

3. **`ndarray.size`**:
   - Returns the total number of elements in the array.
   - Example:
     ```python
     import numpy as np

     arr = np.array([[1, 2, 3], [4, 5, 6]])
     print(arr.size)  # Output: 6
     ```

4. **`ndarray.dtype`**:
   - Returns the data type of elements in the array.
   - Example:
     ```python
     import numpy as np

     arr = np.array([1, 2, 3])
     print(arr.dtype)  # Output: int64
     ```

5. **`ndarray.itemsize`**:
   - Returns the size in bytes of each element in the array.
   - Example:
     ```python
     import numpy as np

     arr = np.array([1, 2, 3])
     print(arr.itemsize)  # Output: 8 (for int64, 64 bits = 8 bytes)
     ```

6. **`ndarray.nbytes`**:
   - Returns the total number of bytes consumed by the array.
   - Example:
     ```python
     import numpy as np

     arr = np.array([1, 2, 3])
     print(arr.nbytes)  # Output: 24 (3 elements * 8 bytes each for int64)
     ```

7. **`ndarray.flags`**:
   - Returns information about the memory layout of the array.
   - Example:
     ```python
     import numpy as np

     arr = np.array([1, 2, 3])
     print(arr.flags)
     ```
     Example output:
     ```
     C_CONTIGUOUS : True
     F_CONTIGUOUS : True
     OWNDATA : True
     WRITEABLE : True
     ALIGNED : True
     ...
     ```

8. **`ndarray.strides`**:
   - Returns the tuple of bytes to step in each dimension when traversing an array.
   - Example:
     ```python
     import numpy as np

     arr = np.array([[1, 2, 3], [4, 5, 6]])
     print(arr.strides)  # Output: (24, 8) for a 2x3 array of int64
     ```

These attributes provide essential information about NumPy arrays, enabling you to understand and manipulate them effectively in numerical computations and data processing tasks. Each attribute serves a specific purpose in describing the properties and characteristics of NumPy arrays.