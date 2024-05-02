# Lines of data to write to the file
lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]

# Open a file in write mode (creates a new file or truncates existing content)
with open("example.txt", "w") as file:
    # Write lines of data to the file
    file.writelines(lines)
