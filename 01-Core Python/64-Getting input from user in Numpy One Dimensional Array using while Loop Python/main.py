import numpy as np

# Prompt the user to input the number of elements
num_elements = int(input("Enter the number of elements for the array: "))

# Create an empty list to store input values
input_values = []

# Use a while loop to get input from the user until desired number of elements is reached
count = 0
while count < num_elements:
    value = float(input(f"Enter value {count + 1}: "))
    input_values.append(value)
    count += 1

# Convert the list to a NumPy array
my_array = np.array(input_values)

# Print the resulting array
print("Resulting array:", my_array)