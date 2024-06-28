# Istrip rstrip and strip String Function in Python

The `lstrip()`, `rstrip()`, and `strip()` methods in Python are used to remove whitespace (or other specified characters) from the beginning, end, or both ends of a string, respectively. These methods are useful for cleaning up strings, especially when dealing with user input or parsing data.

### `lstrip()` Method

The `lstrip()` method returns a copy of the string with leading whitespace removed. If a character argument is passed, it removes occurrences of that character from the start of the string.

**Syntax:**

```python
str.lstrip([chars])
```

- **`chars`** (optional): A string specifying the set of characters to be removed.

**Example:**

```python
text = "   Hello, World!   "
result = text.lstrip()
print(result)  # Output: "Hello, World!   "

# With specified characters
text = "xxxHello, World!xxx"
result = text.lstrip('x')
print(result)  # Output: "Hello, World!xxx"
```

### `rstrip()` Method

The `rstrip()` method returns a copy of the string with trailing whitespace removed. If a character argument is passed, it removes occurrences of that character from the end of the string.

**Syntax:**

```python
str.rstrip([chars])
```

- **`chars`** (optional): A string specifying the set of characters to be removed.

**Example:**

```python
text = "   Hello, World!   "
result = text.rstrip()
print(result)  # Output: "   Hello, World!"

# With specified characters
text = "xxxHello, World!xxx"
result = text.rstrip('x')
print(result)  # Output: "xxxHello, World!"
```

### `strip()` Method

The `strip()` method returns a copy of the string with leading and trailing whitespace removed. If a character argument is passed, it removes occurrences of that character from both the start and end of the string.

**Syntax:**

```python
str.strip([chars])
```

- **`chars`** (optional): A string specifying the set of characters to be removed.

**Example:**

```python
text = "   Hello, World!   "
result = text.strip()
print(result)  # Output: "Hello, World!"

# With specified characters
text = "xxxHello, World!xxx"
result = text.strip('x')
print(result)  # Output: "Hello, World!"
```

### Combined Examples

Here are some examples demonstrating the use of these methods:

**Example 1: Removing Leading and Trailing Whitespace**

```python
text = "   Python Programming   "

print(f"Original: '{text}'")
print(f"lstrip(): '{text.lstrip()}'")  # Output: "Python Programming   "
print(f"rstrip(): '{text.rstrip()}'")  # Output: "   Python Programming"
print(f"strip(): '{text.strip()}'")    # Output: "Python Programming"
```

**Example 2: Removing Specific Characters**

```python
text = "!!!Hello, World!!!"

print(f"Original: '{text}'")
print(f"lstrip('!'): '{text.lstrip('!')}'")  # Output: "Hello, World!!!"
print(f"rstrip('!'): '{text.rstrip('!')}'")  # Output: "!!!Hello, World"
print(f"strip('!'): '{text.strip('!')}'")    # Output: "Hello, World"
```

**Example 3: Cleaning User Input**

```python
user_input = "   user@example.com   "
cleaned_input = user_input.strip()
print(f"User input: '{user_input}'")
print(f"Cleaned input: '{cleaned_input}'")  # Output: "user@example.com"
```

### Conclusion

The `lstrip()`, `rstrip()`, and `strip()` methods are very useful for removing unwanted whitespace or specific characters from strings. These methods help ensure that strings are clean and formatted correctly, which is particularly important when processing user input or parsing data from various sources.