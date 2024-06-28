# isupper islower and istitle String Functions in Python

In Python, the string methods `isupper()`, `islower()`, and `istitle()` are used to check the case of characters in a string. These methods return `True` if the string meets specific case criteria and `False` otherwise.

### `isupper()` Method

The `isupper()` method returns `True` if all the alphabetic characters in the string are uppercase and there is at least one alphabetic character. Otherwise, it returns `False`.

**Syntax:**

```python
str.isupper()
```

**Example:**

```python
text1 = "HELLO"
text2 = "Hello"
text3 = "123"

print(text1.isupper())  # Output: True
print(text2.isupper())  # Output: False
print(text3.isupper())  # Output: False (no alphabetic characters)
```

### `islower()` Method

The `islower()` method returns `True` if all the alphabetic characters in the string are lowercase and there is at least one alphabetic character. Otherwise, it returns `False`.

**Syntax:**

```python
str.islower()
```

**Example:**

```python
text1 = "hello"
text2 = "Hello"
text3 = "123"

print(text1.islower())  # Output: True
print(text2.islower())  # Output: False
print(text3.islower())  # Output: False (no alphabetic characters)
```

### `istitle()` Method

The `istitle()` method returns `True` if the string is in title case (i.e., the first character of each word is uppercase and the rest of the characters are lowercase). Otherwise, it returns `False`.

**Syntax:**

```python
str.istitle()
```

**Example:**

```python
text1 = "Hello World"
text2 = "hello world"
text3 = "Hello world"
text4 = "123"

print(text1.istitle())  # Output: True
print(text2.istitle())  # Output: False
print(text3.istitle())  # Output: True
print(text4.istitle())  # Output: False (no words)
```

### Combined Examples

Here are some examples demonstrating the use of these methods:

**Example 1: Checking Uppercase Strings**

```python
texts = ["PYTHON", "Python", "python"]

for text in texts:
    print(f"'{text}' is upper: {text.isupper()}")
# Output:
# 'PYTHON' is upper: True
# 'Python' is upper: False
# 'python' is upper: False
```

**Example 2: Checking Lowercase Strings**

```python
texts = ["PYTHON", "Python", "python"]

for text in texts:
    print(f"'{text}' is lower: {text.islower()}")
# Output:
# 'PYTHON' is lower: False
# 'Python' is lower: False
# 'python' is lower: True
```

**Example 3: Checking Title Case Strings**

```python
texts = ["Python Is Fun", "Python is fun", "python is Fun"]

for text in texts:
    print(f"'{text}' is title: {text.istitle()}")
# Output:
# 'Python Is Fun' is title: True
# 'Python is fun' is title: False
# 'python is Fun' is title: False
```

### Conclusion

These string methods (`isupper()`, `islower()`, and `istitle()`) are useful for checking the case of characters in strings. They allow you to determine if a string is fully uppercase, fully lowercase, or in title case, respectively. These methods are straightforward to use and can be very handy in various text processing and validation tasks.