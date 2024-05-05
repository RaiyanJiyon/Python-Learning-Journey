import numpy as np

# Create a two-dimensional NumPy array
two_dim_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access elements using a for loop
for row in two_dim_array:
    for elem in row:
        print(elem, end=" ")
    print()  # Move to the next line after printing each row
