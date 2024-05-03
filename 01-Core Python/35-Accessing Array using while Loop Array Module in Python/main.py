import array

# Create an array of integers
my_array = array.array('i', [10, 20, 30, 40, 50])

# Get the length of the array
array_length = len(my_array)

# Initialize an index variable
index = 0

# Access elements of the array using a while loop
while index < array_length:
    print(my_array[index])
    index += 1