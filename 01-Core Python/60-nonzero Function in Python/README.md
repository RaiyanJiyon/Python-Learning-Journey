# nonzero Function in Python

In Python, the `numpy.nonzero()` function is used to return the indices of `non-zero elements` in an array. It returns a tuple of arrays, one for each dimension of the input array, containing the indices of non-zero elements along that dimension.

The syntax of the numpy.nonzero() function is as follows:

```
numpy.nonzero(a)
```

`a`: The input array. 


### Here's an example to illustrate the usage of the numpy.nonzero() function:

```python
import numpy as np

# Create an array
arr = np.array([[0, 1, 0],
                [2, 0, 3],
                [0, 4, 5]])

# Get the indices of non-zero elements
indices = np.nonzero(arr)

print(indices)
```

In this example:

The input array arr has non-zero elements at the following indices:

(0, 1) <br>
(1, 0) <br>
(1, 2) <br>
(2, 1) <br>
(2, 2) <br>


The numpy.nonzero() function returns a tuple of arrays, where the first array contains the row indices and the second array contains the column indices of the non-zero elements.
You can use the returned indices to access or manipulate the non-zero elements of the array as needed.