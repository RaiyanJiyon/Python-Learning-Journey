# Create a file using the with statement
with open("example.txt", "w") as file:
    file.write("Raiyan Jiyon\n")
    file.write("Dhaka, Bangladesh")
# File is automatically closed when exiting the with block

# Open a file using the with statement
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
# File is automatically closed when exiting the with block
