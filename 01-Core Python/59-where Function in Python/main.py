# Here are a few examples to illustrate the usage of numpy.where():
import numpy as np

# Example 1: Using only the condition argument
arr = np.array([1, 2, 3, 4, 5])
indices = np.where(arr > 2)
print(indices)  # Output: (array([2, 3, 4]),)

# Example 2: Using all arguments
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 2, 'greater', 'lesser or equal')
print(result)  # Output: ['lesser or equal' 'lesser or equal' 'greater' 'greater' 'greater']