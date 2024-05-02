# Open a file in write mode
file_write = open("output.txt", "w")
file_write.write('Raiyan Jiyon\n')
file_write.write('221902113\n')
file_write.close()  # Always close files after using them

# Open the file in read mode
file_read = open("output.txt", "r")
data = file_read.read()  # Read the contents of the file
print(data)
file_read.close()

# Open a file in binary mode for reading and writing
file_binary = open("output.txt", "rb+")
binary_data = file_binary.read()  # Read the binary data from the file
print(binary_data)
file_binary.close()

# Open a file in text mode for appending
file_append = open("output.txt", "a")
file_append.write('23\n')  # Add newline to separate from previous content
file_append.close()  # Always close files after using them
