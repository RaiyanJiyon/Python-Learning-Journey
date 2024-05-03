# Data Type in Python

In Python, data types represent the type or kind of data that a variable can store. Python is dynamically typed, meaning you don't have to explicitly declare the data type of a variable. Instead, Python infers the data type based on the value assigned to it. Here are some common data types in Python:


## Numeric Types:

`int`: Integer numbers, e.g., 5, -3, 1000.

`float`: Floating-point numbers, e.g., 3.14, -0.001, 2.0.

`Boolean Type`: Represents the truth values True or False.

## Sequence Types:

`str`: Represents strings of characters, e.g., "hello", 'world'.

`list`: Ordered collection of items, mutable, e.g., [1, 2, 3], ['a', 'b', 'c'].

`tuple`: Ordered collection of items, immutable, e.g., (1, 2, 3), ('a', 'b', 'c').

`range`: Represents a range of numbers, e.g., range(5) represents 0, 1, 2, 3, 4.

## Mapping Type:

`dict`: Collection of key-value pairs, e.g., {'name': 'John', 'age': 30}.

## Set Types:

`set`: Unordered collection of unique items, e.g., {1, 2, 3}.

`frozenset`: Immutable version of a set.

## None Type:

`NoneType`: Represents the absence of a value, usually used to indicate that a variable doesn't refer to anything, e.g., None.

Python also supports complex numbers `(complex)` and several other specialized data types provided by various libraries.

### For example:
```python
x = 5
y = 3.14
z = "hello"

# You can determine the type of a variable or expression using the built-in type() function. For example:
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'str'>
```