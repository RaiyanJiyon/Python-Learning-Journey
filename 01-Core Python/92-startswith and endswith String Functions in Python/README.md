# startswith and endswith String Functions in Python

In Python, the `startswith()` and `endswith()` methods are used to check whether a string starts or ends with a specified substring or set of characters. These methods return `True` if the string meets the specified condition and `False` otherwise.

### `startswith()` Method

The `startswith()` method checks if the string starts with the specified prefix (substring).

**Syntax:**

```python
str.startswith(prefix[, start[, end]])
```

- **`prefix`**: The prefix (substring) to check.
- **`start`** (optional): Beginning index to start the search within the string.
- **`end`** (optional): Ending index to end the search within the string.

**Example:**

```python
text = "Hello, World!"

print(text.startswith("Hello"))  # Output: True
print(text.startswith("World"))  # Output: False
```

You can also specify the starting and ending indices for the search:

```python
text = "Hello, World!"

print(text.startswith("World", 7))  # Output: True (starting from index 7)
```

### `endswith()` Method

The `endswith()` method checks if the string ends with the specified suffix (substring).

**Syntax:**

```python
str.endswith(suffix[, start[, end]])
```

- **`suffix`**: The suffix (substring) to check.
- **`start`** (optional): Beginning index to start the search within the string.
- **`end`** (optional): Ending index to end the search within the string.

**Example:**

```python
text = "Hello, World!"

print(text.endswith("World!"))  # Output: True
print(text.endswith("Hello"))   # Output: False
```

You can also specify the starting and ending indices for the search:

```python
text = "Hello, World!"

print(text.endswith("Hello", 0, 5))  # Output: True (search from index 0 to 5)
```

### Combined Examples

Here are some combined examples demonstrating the use of these methods:

**Example 1: Checking File Extensions**

```python
file_name = "script.py"

if file_name.endswith(".py"):
    print("Python script detected.")
elif file_name.endswith(".txt"):
    print("Text file detected.")
else:
    print("Unknown file type.")
```

**Example 2: Filtering File Names**

```python
file_names = ["script.py", "data.csv", "README.md", "image.jpg"]

python_files = [file for file in file_names if file.endswith(".py")]
print(python_files)  # Output: ['script.py']
```

**Example 3: Checking Protocol in URLs**

```python
url = "https://www.example.com"

if url.startswith("https://"):
    print("Secure connection")
elif url.startswith("http://"):
    print("Insecure connection")
else:
    print("Unknown protocol")
```

### Conclusion

The `startswith()` and `endswith()` methods provide convenient ways to check whether a string begins or ends with a specified substring or set of characters. These methods are useful for various tasks such as file type checking, URL validation, and filtering data based on prefixes or suffixes. Understanding and using these methods effectively can simplify string manipulation tasks in Python.