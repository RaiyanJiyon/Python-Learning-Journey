# upper lower swapcase and title String Functions in Python

In Python, strings come with a variety of built-in methods for changing the case of the characters. Here are some of the commonly used string case methods: `upper()`, `lower()`, `swapcase()`, and `title()`. These methods provide an easy way to manipulate the case of strings.

### `upper()` Method

The `upper()` method returns a copy of the string with all the characters converted to uppercase.

**Syntax:**

```python
str.upper()
```

**Example:**

```python
text = "Hello, World!"
result = text.upper()
print(result)  # Output: "HELLO, WORLD!"
```

### `lower()` Method

The `lower()` method returns a copy of the string with all the characters converted to lowercase.

**Syntax:**

```python
str.lower()
```

**Example:**

```python
text = "Hello, World!"
result = text.lower()
print(result)  # Output: "hello, world!"
```

### `swapcase()` Method

The `swapcase()` method returns a copy of the string with all the uppercase characters converted to lowercase and vice versa.

**Syntax:**

```python
str.swapcase()
```

**Example:**

```python
text = "Hello, World!"
result = text.swapcase()
print(result)  # Output: "hELLO, wORLD!"
```

### `title()` Method

The `title()` method returns a copy of the string with the first character of each word converted to uppercase and the remaining characters converted to lowercase.

**Syntax:**

```python
str.title()
```

**Example:**

```python
text = "hello, world!"
result = text.title()
print(result)  # Output: "Hello, World!"
```

### Combined Examples

Here are some examples demonstrating the use of these methods:

**Example 1: Combining `upper()` and `lower()`**

```python
text = "Python is Fun!"

upper_text = text.upper()
lower_text = text.lower()

print(upper_text)  # Output: "PYTHON IS FUN!"
print(lower_text)  # Output: "python is fun!"
```

**Example 2: Using `swapcase()`**

```python
text = "Python Is FUN!"

swapped_text = text.swapcase()

print(swapped_text)  # Output: "pYTHON iS fun!"
```

**Example 3: Using `title()`**

```python
text = "python is fun!"

title_text = text.title()

print(title_text)  # Output: "Python Is Fun!"
```

**Example 4: Chaining Methods**

You can chain these methods together to achieve complex transformations:

```python
text = "hello, WORLD!"

result = text.lower().title().swapcase()

print(result)  # Output: "hELLO, wORLD!"
```

### Conclusion

These string methods (`upper()`, `lower()`, `swapcase()`, and `title()`) are very useful for manipulating the case of strings in Python. They allow you to convert strings to uppercase, lowercase, swap the case of characters, and capitalize the first letter of each word in a string. These methods are simple to use and can be combined to perform more complex string manipulations.