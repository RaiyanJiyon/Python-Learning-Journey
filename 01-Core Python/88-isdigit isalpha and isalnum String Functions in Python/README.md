# isdigit isalpha and isalnum String Functions in Python

In Python, the string methods `isdigit()`, `isalpha()`, and `isalnum()` are used to check the types of characters in a string. These methods return `True` if the string meets specific criteria and `False` otherwise.

### `isdigit()` Method

The `isdigit()` method returns `True` if all the characters in the string are digits (0-9) and there is at least one character. Otherwise, it returns `False`.

**Syntax:**

```python
str.isdigit()
```

**Example:**

```python
text1 = "12345"
text2 = "12345a"
text3 = ""

print(text1.isdigit())  # Output: True
print(text2.isdigit())  # Output: False
print(text3.isdigit())  # Output: False (empty string)
```

### `isalpha()` Method

The `isalpha()` method returns `True` if all the characters in the string are alphabetic (a-z, A-Z) and there is at least one character. Otherwise, it returns `False`.

**Syntax:**

```python
str.isalpha()
```

**Example:**

```python
text1 = "Hello"
text2 = "Hello123"
text3 = ""

print(text1.isalpha())  # Output: True
print(text2.isalpha())  # Output: False
print(text3.isalpha())  # Output: False (empty string)
```

### `isalnum()` Method

The `isalnum()` method returns `True` if all the characters in the string are alphanumeric (a-z, A-Z, 0-9) and there is at least one character. Otherwise, it returns `False`.

**Syntax:**

```python
str.isalnum()
```

**Example:**

```python
text1 = "Hello123"
text2 = "Hello 123"
text3 = ""

print(text1.isalnum())  # Output: True
print(text2.isalnum())  # Output: False (space is not alphanumeric)
print(text3.isalnum())  # Output: False (empty string)
```

### Combined Examples

Here are some examples demonstrating the use of these methods:

**Example 1: Checking if a String Contains Only Digits**

```python
texts = ["12345", "123a45", ""]

for text in texts:
    print(f"'{text}' is digit: {text.isdigit()}")
# Output:
# '12345' is digit: True
# '123a45' is digit: False
# '' is digit: False
```

**Example 2: Checking if a String Contains Only Alphabetic Characters**

```python
texts = ["Hello", "Hello123", ""]

for text in texts:
    print(f"'{text}' is alpha: {text.isalpha()}")
# Output:
# 'Hello' is alpha: True
# 'Hello123' is alpha: False
# '' is alpha: False
```

**Example 3: Checking if a String Contains Only Alphanumeric Characters**

```python
texts = ["Hello123", "Hello 123", ""]

for text in texts:
    print(f"'{text}' is alnum: {text.isalnum()}")
# Output:
# 'Hello123' is alnum: True
# 'Hello 123' is alnum: False
# '' is alnum: False
```

### Conclusion

The string methods `isdigit()`, `isalpha()`, and `isalnum()` are useful for checking the types of characters in strings. They allow you to determine if a string consists solely of digits, alphabetic characters, or alphanumeric characters, respectively. These methods are straightforward to use and can be very handy in various text processing and validation tasks.