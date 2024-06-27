# The len function in Python

The `len` function in Python is used to return the number of items in an object. It is a built-in function that can be used with a variety of data types, including strings, lists, tuples, sets, dictionaries, and more. The `len` function is straightforward and only takes a single argument.

### Syntax

```python
len(obj)
```

### Parameters

- **`obj`**: The object whose length you want to determine. This can be any iterable object such as a string, list, tuple, set, dictionary, etc.

### Examples

#### String
The length of a string is the number of characters it contains.

```python
text = "Hello, World!"
print(len(text))  # Output: 13
```

#### List
The length of a list is the number of elements in the list.

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3
```

#### Tuple
The length of a tuple is the number of elements in the tuple.

```python
numbers = (1, 2, 3, 4)
print(len(numbers))  # Output: 4
```

#### Set
The length of a set is the number of unique elements in the set.

```python
letters = {'a', 'b', 'c', 'd'}
print(len(letters))  # Output: 4
```

#### Dictionary
The length of a dictionary is the number of key-value pairs it contains.

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
print(len(person))  # Output: 3
```

#### Nested Structures
The `len` function only measures the top-level elements, not nested ones.

```python
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(len(nested_list))  # Output: 3 (three lists inside the main list)

nested_dict = {"a": {"b": 1, "c": 2}, "d": {"e": 3}}
print(len(nested_dict))  # Output: 2 (two top-level keys)
```

#### Empty Structures
For empty structures, `len` returns 0.

```python
empty_list = []
empty_tuple = ()
empty_set = set()
empty_dict = {}

print(len(empty_list))  # Output: 0
print(len(empty_tuple))  # Output: 0
print(len(empty_set))  # Output: 0
print(len(empty_dict))  # Output: 0
```

### Summary

- The `len` function is used to find the number of items in an object.
- It works with various data types, including strings, lists, tuples, sets, and dictionaries.
- For nested structures, it only counts the top-level elements.
- For empty structures, it returns 0.

Using the `len` function is a simple and effective way to determine the size of an object in Python.