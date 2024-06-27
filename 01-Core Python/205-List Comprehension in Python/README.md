# List comprehension in Python

List comprehension in Python is a concise and readable way to create lists. It allows you to generate lists by applying an expression to each item in an iterable, optionally filtering items with a condition. List comprehensions can replace for-loops for generating lists in a more compact and efficient manner.

### Syntax

```python
[expression for item in iterable if condition]
```

- **`expression`**: The value or transformation applied to each item in the resulting list.
- **`item`**: The variable representing each element in the iterable.
- **`iterable`**: The collection to iterate over.
- **`condition`** (optional): A filtering condition to include only certain items.

### Examples

#### Basic List Comprehension

Creating a list of squares of numbers from 0 to 9.

```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### List Comprehension with Condition

Creating a list of even numbers from 0 to 9.

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

#### Applying a Function in List Comprehension

Using a function to generate a list of factorials.

```python
import math

factorials = [math.factorial(x) for x in range(6)]
print(factorials)  # Output: [1, 1, 2, 6, 24, 120]
```

#### Transforming Elements in List Comprehension

Converting all strings in a list to uppercase.

```python
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']
```

#### Nested List Comprehension

Flattening a nested list (a list of lists) into a single list.

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### List Comprehension with Multiple Conditions

Creating a list of numbers from 0 to 19 that are divisible by both 2 and 3.

```python
divisible_by_2_and_3 = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(divisible_by_2_and_3)  # Output: [0, 6, 12, 18]
```

#### Creating a Cartesian Product

Generating a list of tuples representing the Cartesian product of two ranges.

```python
cartesian_product = [(x, y) for x in range(3) for y in range(2)]
print(cartesian_product)  # Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

### Summary

- **List Comprehension**: A concise way to create lists by applying an expression to elements from an iterable.
- **Syntax**: `[expression for item in iterable if condition]`.
- **Usage**: Generate lists with transformations, filtering, and combining elements from multiple iterables.

List comprehensions in Python offer a powerful and expressive way to create and manipulate lists, improving both the readability and performance of your code.