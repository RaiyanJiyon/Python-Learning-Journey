# File Object Variables in Python

In Python, when you open a file using the open() function, it returns a file object, which is an instance of the built-in file class. This file object provides methods and attributes that allow you to interact with the opened file. You can assign this file object to a variable for easier reference and manipulation.

Here's an example of how you can assign a file object to a variable:

```python
# Open a file in read mode
file = open("example.txt", "r")

# Now 'file' is a variable that holds the file object
```

Once you have the file object assigned to a variable, you can use it to perform various operations such as reading, writing, or closing the file.

Here are some common methods and attributes you can use with a file object:

Methods:
read(size): Reads and returns the specified number of bytes from the file.
readline(): Reads and returns the next line from the file.
readlines(): Reads and returns a list of lines from the file.
write(string): Writes the specified string to the file.
close(): Closes the file.
and more...
Attributes:
name: Returns the name of the file.
mode: Returns the access mode with which the file was opened.
closed: Returns True if the file is closed, False otherwise.
and more...
Here's an example demonstrating the usage of a file object variable:

```python
# Open a file in read mode
file = open("example.txt", "r")

# Read the first line from the file
line = file.readline()
print(line)

# Close the file
file.close()
```

Remember to always close the file after you're done with it to free up system resources and ensure that any changes are flushed to disk.