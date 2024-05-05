# Here's an example to illustrate the usage of the numpy.nonzero() function:
import numpy as np

# Create an array
arr = np.array([[0, 1, 0],
                [2, 0, 3],
                [0, 4, 5]])

# Get the indices of non-zero elements
indices = np.nonzero(arr)

print(indices)