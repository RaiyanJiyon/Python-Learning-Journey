# Nested list comprehensions in Python

Nested list comprehensions in Python provide a concise way to generate lists that involve multiple levels of iteration. They are particularly useful for transforming and filtering elements from nested iterables such as lists of lists.

### Syntax

The basic syntax for a nested list comprehension is:

```python
[expression for outer_item in outer_iterable for inner_item in inner_iterable if condition]
```

- **`expression`**: The value to include in the resulting list.
- **`outer_item`**: The variable representing each element in the outer iterable.
- **`outer_iterable`**: The outer iterable collection.
- **`inner_item`**: The variable representing each element in the inner iterable.
- **`inner_iterable`**: The inner iterable collection.
- **`condition`** (optional): A filtering condition for the elements.

### Examples

#### Flattening a Nested List

Suppose you have a list of lists and you want to flatten it into a single list.

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### Applying a Transformation to a Nested List

You can apply a transformation, such as squaring each element in a nested list.

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squared = [[item**2 for item in sublist] for sublist in nested_list]
print(squared)  # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

#### Filtering Elements in a Nested List

You can also filter elements. For instance, extracting only even numbers from a nested list.

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [item for sublist in nested_list for item in sublist if item % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8]
```

#### Creating a Cartesian Product

Generating a Cartesian product of two ranges.

```python
cartesian_product = [(x, y) for x in range(3) for y in range(2)]
print(cartesian_product)  # Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

#### Nested Loops with Conditions

Combining elements from two lists but only if they meet a certain condition.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [(x, y) for x in list1 for y in list2 if x + y > 5]
print(combined)  # Output: [(1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
```

### Summary

- **Nested List Comprehension**: Allows concise generation of lists involving multiple levels of iteration.
- **Syntax**: `[expression for outer_item in outer_iterable for inner_item in inner_iterable if condition]`.
- **Usage**: Flatten nested lists, apply transformations, filter elements, create Cartesian products, and more.

Nested list comprehensions are a powerful feature in Python that can simplify complex list operations and make your code more readable and expressive.