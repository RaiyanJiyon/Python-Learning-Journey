# Open a file in write mode
with open("example.txt", "w") as file1:
    # Read the entire contents of the file
    data = file1.write("Raiyan Jiyon")

# Open a file in read mode
with open("example.txt", "r") as file2:
    # Read the entire contents of the file
    data = file2.read()

# Print the data read from the file
print(data)
