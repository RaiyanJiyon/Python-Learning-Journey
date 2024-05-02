# Writing Data to File using writelines Method in Python

In Python, you can write multiple lines of data to a file using the writelines() method available on file objects. This method takes an iterable (such as a list) containing the lines of data to be written to the file.

Here's an example demonstrating how to use the writelines() method:

```python
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
```

In this example:

- We define a list called lines containing the lines of data to be written to the file.
- We open a file named "example.txt" in write mode using a context manager (with statement). If the file does not exist, it will be created. If the file already exists, its contents will be truncated (cleared).
- We use the writelines() method to write the lines of data contained in the lines list to the file. Each line in the list is written to the file sequentially.

After executing this code, the file "example.txt" will contain the following content:

```python
Line 1
Line 2
Line 3
```

Each line of data from the lines list is written to a separate line in the file. Remember to include newline characters (\n) at the end of each line if you want each line to be written on a separate line in the file.