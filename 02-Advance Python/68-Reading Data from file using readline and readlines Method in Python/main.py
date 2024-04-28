with open('example.txt', 'w') as file1:
    file1.write("Raiyan Jiyon\n")
    file1.write("Raiyan Jiyon\n")
    file1.write("Raiyan Jiyon\n")
    file1.write("Raiyan Jiyon\n")

# Open a file in read mode
with open("example.txt", "r") as file2:
    # Read all lines from the file into a list
    lines = file2.readlines()

# Process each line in the list
for line in lines:
    # Process the line (e.g., print it)
    print(line.strip())  # Remove newline character from the end of the line
