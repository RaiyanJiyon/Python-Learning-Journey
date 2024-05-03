# Here's how you can create a one-dimensional array using the array module:
import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Print the array
print(my_array)

# You can also add elements to the array using the append() method:
my_array.append(6)

# And access elements of the array using indexing, just like with lists:
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3