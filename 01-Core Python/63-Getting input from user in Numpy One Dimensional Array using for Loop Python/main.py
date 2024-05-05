# Here's the code:
import numpy as np

# Prompt the user to input the number of elements
num_elements = int(input("Enter the number of elements for the array: "))

# Create an empty list to store input values
input_values = []

# Iterate using a for loop to get input from the user
for i in range(num_elements):
    value = float(input(f"Enter value {i + 1}: "))
    input_values.append(value)

# Convert the list to a NumPy array
my_array = np.array(input_values)

# Print the resulting array
print("Resulting array:", my_array)