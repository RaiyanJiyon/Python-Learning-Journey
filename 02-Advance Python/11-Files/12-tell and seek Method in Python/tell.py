# Open a file in read mode
with open("example.txt", "r") as file:
    # Read the first 10 bytes from the file
    data = file.read(6)
    # Get the current position of the file cursor
    position = file.tell()
    print("Current position:", position)
