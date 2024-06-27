# Dictionary comprehension in Python

Dictionary comprehension in Python is a concise and readable way to create dictionaries. It allows you to generate dictionary contents in a single line of code, similar to list comprehensions. Dictionary comprehensions can be used to transform and filter items to create new dictionaries.

### Syntax

```python
{key_expr: value_expr for item in iterable if condition}
```

- **`key_expr`**: The expression for the key in the new dictionary.
- **`value_expr`**: The expression for the value in the new dictionary.
- **`item`**: The variable representing each item in the iterable.
- **`iterable`**: The collection you are iterating over.
- **`condition`** (optional): An optional condition to filter items.

### Examples

#### Basic Dictionary Comprehension

Creating a dictionary where keys are numbers and values are their squares.

```python
squares = {x: x**2 for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### Filtering Items

Creating a dictionary that includes only even numbers and their squares.

```python
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

#### Transforming a Dictionary

Swapping keys and values in an existing dictionary.

```python
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # Output: {1: 'a', 2: 'b', 3: 'c'}
```

#### Combining Lists into a Dictionary

Creating a dictionary from two lists, one for keys and one for values.

```python
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
combined = {keys[i]: values[i] for i in range(len(keys))}
print(combined)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

#### Using Functions in Dictionary Comprehension

Using a function to generate dictionary values.

```python
def square(x):
    return x * x

squares = {x: square(x) for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### Nested Dictionary Comprehension

Creating a dictionary with complex values, such as another dictionary.

```python
nested_dict = {x: {y: y**2 for y in range(3)} for x in range(3)}
print(nested_dict)
# Output: {0: {0: 0, 1: 1, 2: 4}, 1: {0: 0, 1: 1, 2: 4}, 2: {0: 0, 1: 1, 2: 4}}
```

### Practical Use Cases

#### Counting Characters

Counting the frequency of characters in a string.

```python
text = "hello world"
char_count = {char: text.count(char) for char in set(text)}
print(char_count)  # Output: {'d': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}
```

#### Filtering and Transforming a Dictionary

Filtering out items with values less than 3 and squaring the remaining values.

```python
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_transformed = {k: v**2 for k, v in original.items() if v >= 3}
print(filtered_transformed)  # Output: {'c': 9, 'd': 16}
```

### Summary

- Dictionary comprehensions provide a concise way to create dictionaries.
- They can be used to transform, filter, and combine data.
- The syntax is `{key_expr: value_expr for item in iterable if condition}`.
- Dictionary comprehensions improve readability and can simplify your code.

Using dictionary comprehensions, you can write more expressive and efficient Python code.