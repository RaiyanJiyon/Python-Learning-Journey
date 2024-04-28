# Reading Data from file using readline and readlines Method in Python

To read data from a file line by line or as a list of lines in Python, you can use the readline() and readlines() methods available on file objects.

Here's how you can use each method:

## Using readline():

```python
# Open a file in read mode
with open("example.txt", "r") as file:
    # Read the first line from the file
    line = file.readline()
    # Keep reading lines until there are no more lines left
    while line:
        # Process the line (e.g., print it)
        print(line.strip())  # Remove newline character from the end of the line
        # Read the next line
        line = file.readline()
```


In this example:

- We open a file named "example.txt" in read mode using a context manager (with statement).
- We use the readline() method to read the first line from the file into the variable line.
- We enter a loop where we process each line until there are no more lines left in the file.
- Inside the loop, we process each line (e.g., print it) and then read the next line using readline().

## Using readlines():

```python
# Open a file in read mode
with open("example.txt", "r") as file:
    # Read all lines from the file into a list
    lines = file.readlines()

# Process each line in the list
for line in lines:
    # Process the line (e.g., print it)
    print(line.strip())  # Remove newline character from the end of the line
```

In this example:

- We open a file named "example.txt" in read mode using a context manager (with statement).
- We use the readlines() method to read all lines from the file into a list called lines.
- We then process each line in the list (e.g., print it) using a for loop.

Both methods provide different ways to read data from a file line by line or as a list of lines. Choose the method that best fits your use case.








