# tell and seek Method in Python

In Python, the tell() and seek() methods are used to manipulate the current position of the file cursor within an open file.

Here's a brief explanation of each method:

In Python, the `tell()` and `seek()` methods are used to manipulate the current position of the file cursor within an open file.

**tell() method:**
- The `tell()` method returns the current position of the file cursor (pointer) within the file.
- It returns an integer representing the byte offset from the beginning of the file where the file cursor is currently located.
- After reading or writing data from/to a file, the file cursor moves forward to the end of the data that was read or written.
- This method can be useful for keeping track of the current position within a file, especially when reading or writing data sequentially.

Example:

```python
# Open a file in read mode
with open("example.txt", "r") as file:
    # Read the first 10 bytes from the file
    data = file.read(10)
    # Get the current position of the file cursor
    position = file.tell()
    print("Current position:", position)
```

## seek() method:
The `seek()` method is used to change the position of the file cursor within the file.
It takes two arguments: offset and whence.
- `offset`: The number of bytes to move the cursor relative to the reference point specified by `whence`.
- `whence`: Optional parameter specifying the reference point from which the offset is applied. It can take one of the following values:
  - 0 (default): Indicates the beginning of the file.
  - 1: Indicates the current position of the file cursor.
  - 2: Indicates the end of the file.
After using the `seek()` method, subsequent read or write operations will occur from the new cursor position.

Example:

```python
# Open a file in read mode
with open("example.txt", "r") as file:
    # Move the cursor to the 20th byte from the beginning of the file
    file.seek(20)
    # Read data from the new cursor position
    data = file.read()
    print(data)
```

These methods are particularly useful when you need to read or write data at specific locations within a file, or when you want to navigate through the file in a non-sequential manner.






