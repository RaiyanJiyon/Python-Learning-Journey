# C Style String Formatting in Python

In Python, C-style string formatting is achieved using the `%` operator, which is similar to the `printf` style of formatting strings in C. This method allows you to embed variables within a string by using format specifiers.

### Basic Syntax

The basic syntax for C-style string formatting is:

```python
"format string" % (values)
```

- **`"format string"`**: A string containing format specifiers (placeholders) that determine how the values will be formatted.
- **`(values)`**: A tuple containing the values to be inserted into the format string.

### Common Format Specifiers

- **`%s`**: String (or any object with a string representation, like numbers)
- **`%d`**: Integer
- **`%f`**: Floating-point number
- **`%.<number of digits>f`**: Floating-point number with a fixed number of digits after the decimal point
- **`%x`**: Integer in hexadecimal (lowercase)
- **`%X`**: Integer in hexadecimal (uppercase)

### Examples

#### Example 1: Basic String Formatting

```python
name = "Alice"
age = 30

formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: "My name is Alice and I am 30 years old."
```

#### Example 2: Formatting Floating-Point Numbers

```python
pi = 3.141592653589793

formatted_string = "Pi to three decimal places: %.3f" % pi
print(formatted_string)  # Output: "Pi to three decimal places: 3.142"
```

#### Example 3: Multiple Variables

```python
name = "Bob"
age = 25
height = 5.9

formatted_string = "Name: %s, Age: %d, Height: %.1f" % (name, age, height)
print(formatted_string)  # Output: "Name: Bob, Age: 25, Height: 5.9"
```

#### Example 4: Hexadecimal Formatting

```python
number = 255

formatted_string = "The number %d in hexadecimal is %x" % (number, number)
print(formatted_string)  # Output: "The number 255 in hexadecimal is ff"
```

### Formatting with Dictionaries

You can also use a dictionary for formatting. Each key in the dictionary can be referenced using `(key)s` within the format string.

```python
data = {'name': 'Charlie', 'age': 28}

formatted_string = "Name: %(name)s, Age: %(age)d" % data
print(formatted_string)  # Output: "Name: Charlie, Age: 28"
```

### Padding and Alignment

You can add padding and specify alignment for the output. The format specifier `%[flags][width][.precision]type` is used to control the output format.

#### Example 5: Padding and Alignment

```python
number = 42

formatted_string = "Number: %5d" % number
print(formatted_string)  # Output: "Number:    42" (padded with spaces on the left)

formatted_string = "Number: %-5d" % number
print(formatted_string)  # Output: "Number: 42   " (padded with spaces on the right)
```

### Limitations

- **Type Safety**: The `%` operator does not provide type safety. If you use the wrong format specifier for a value, it will raise a `TypeError`.
- **Deprecated**: While still supported, C-style string formatting is considered outdated. Modern Python code often uses the `str.format()` method or f-strings (formatted string literals) introduced in Python 3.6.

### Conclusion

C-style string formatting using the `%` operator is a powerful and flexible way to format strings in Python, especially for those familiar with C. However, for new projects, consider using more modern approaches like `str.format()` or f-strings for better readability and functionality.