with open("example.txt", 'w') as file:
    file.write("Data Added")

# Read and Write Mode ("r+")
with open("example.txt", "r+") as file:
    data = file.read()  # Read existing data
    file.write("New data")  # Write new data

# Write and Read Mode ("w+")
with open("example.txt", "w+") as file:
    file.write("New data")  # Write new data
    file.seek(0)  # Move the file pointer to the beginning
    data = file.read()  # Read data

# Append and Read Mode ("a+")
with open("example.txt", "a+") as file:
    file.write("New data")  # Append new data
    file.seek(0)  # Move the file pointer to the beginning
    data = file.read()  # Read data
