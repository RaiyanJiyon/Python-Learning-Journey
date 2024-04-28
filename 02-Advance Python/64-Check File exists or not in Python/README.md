# Check File exists or not in Python

In Python, you can check whether a file exists or not using the os.path.exists() function from the os module or the Path.exists() method from the pathlib module. Both methods return a boolean value indicating whether the file exists or not.

Here's how you can use each method:

## Using os.path.exists():

```python
import os

# Path to the file
file_path = "example.txt"

# Check if the file exists
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")
```

## Using Path.exists() from pathlib:

```python
from pathlib import Path

# Path to the file
file_path = Path("example.txt")

# Check if the file exists
if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")
```

Both methods work similarly, and you can choose whichever you prefer based on your preference or existing codebase. They are platform-independent and can be used across different operating systems.