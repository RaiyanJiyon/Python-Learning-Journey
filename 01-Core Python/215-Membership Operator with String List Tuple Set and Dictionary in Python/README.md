# Membership Operator with String List Tuple Set and Dictionary in Python

The membership operator `in` in Python is used to check if a value exists within an iterable, such as strings, lists, tuples, sets, and dictionaries. It returns `True` if the value is found in the iterable and `False` otherwise. Here's how the membership operator can be used with different data structures:

### String

Checking if a substring exists within a string.

```python
text = "hello world"
print('hello' in text)  # Output: True
print('Python' in text)  # Output: False
```

### List

Checking if an element exists within a list.

```python
fruits = ["apple", "banana", "cherry"]
print('banana' in fruits)  # Output: True
print('grape' in fruits)  # Output: False
```

### Tuple

Checking if an element exists within a tuple.

```python
numbers = (1, 2, 3, 4)
print(3 in numbers)  # Output: True
print(5 in numbers)  # Output: False
```

### Set

Checking if an element exists within a set.

```python
unique_numbers = {1, 2, 3, 4}
print(2 in unique_numbers)  # Output: True
print(5 in unique_numbers)  # Output: False
```

### Dictionary

Checking if a key exists within a dictionary.

```python
student_grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}
print('Alice' in student_grades)  # Output: True
print('David' in student_grades)  # Output: False
```

To check if a value exists within a dictionary, you can use the `values()` method:

```python
print('A' in student_grades.values())  # Output: True
print('D' in student_grades.values())  # Output: False
```

### Examples with Multiple Data Structures

#### Strings in Lists

Checking if a string exists within a list of strings.

```python
words = ["apple", "banana", "cherry"]
print('banana' in words)  # Output: True
print('grape' in words)  # Output: False
```

#### Elements in Nested Lists

Checking if an element exists within nested lists.

```python
nested_list = [[1, 2], [3, 4], [5, 6]]
print(3 in nested_list)  # Output: False
print([3, 4] in nested_list)  # Output: True
```

#### Tuples in Lists

Checking if a tuple exists within a list of tuples.

```python
tuple_list = [(1, 2), (3, 4), (5, 6)]
print((3, 4) in tuple_list)  # Output: True
print((7, 8) in tuple_list)  # Output: False
```

### Summary

- The membership operator `in` is used to check if an item exists within an iterable.
- **Strings**: Checks if a substring exists within a string.
- **Lists**: Checks if an element exists within a list.
- **Tuples**: Checks if an element exists within a tuple.
- **Sets**: Checks if an element exists within a set.
- **Dictionaries**: Checks if a key exists within a dictionary; use `values()` method to check for values.

The `in` operator is a versatile and efficient way to test membership across different data structures in Python.