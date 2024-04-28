with open('example.txt', 'w') as file:
    file.write("Data 1")
    file.write("Data 2")
    file.write("Data 3")
    file.write("Data 4")

with open("example.txt", "r") as file:
    # Move the cursor to the 20th byte from the beginning of the file
    file.seek(20)
    # Read data from the new cursor position
    data = file.read()
    print(data)

