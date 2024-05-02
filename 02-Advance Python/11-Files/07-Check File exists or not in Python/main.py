import os

# Path to the file
file_path = "example.txt"

# Check if the file exists
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")
