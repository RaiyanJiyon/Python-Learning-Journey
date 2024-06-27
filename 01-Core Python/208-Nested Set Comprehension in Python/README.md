# Nested set comprehension in Python

Nested set comprehension in Python is a powerful and concise way to generate sets, especially when dealing with multi-level iterations. It allows you to create a set with nested iterations, filtering, and transformations, all in a single line of code.

### Syntax

```python
{outer_expr for outer_item in outer_iterable if outer_condition for inner_item in inner_iterable if inner_condition}
```

- **`outer_expr`**: The expression for the elements in the resulting set.
- **`outer_item`**: The variable representing each item in the outer iterable.
- **`outer_iterable`**: The outer iterable collection.
- **`outer_condition`** (optional): An optional condition to filter outer items.
- **`inner_item`**: The variable representing each item in the inner iterable.
- **`inner_iterable`**: The inner iterable collection.
- **`inner_condition`** (optional): An optional condition to filter inner items.

### Examples

#### Basic Nested Set Comprehension

Suppose you want to create a set of tuples representing pairs of numbers where the outer number is from 0 to 2 and the inner number is from 0 to 1.

```python
nested_set = {(x, y) for x in range(3) for y in range(2)}
print(nested_set)
# Output: {(0, 1), (1, 1), (0, 0), (2, 0), (2, 1), (1, 0)}
```

#### Filtering in Nested Set Comprehension

Creating a set of pairs where both numbers are even.

```python
even_pairs = {(x, y) for x in range(4) if x % 2 == 0 for y in range(4) if y % 2 == 0}
print(even_pairs)
# Output: {(0, 2), (2, 2), (2, 0), (0, 0)}
```

#### Using Nested Set Comprehension with Strings

Creating a set of unique characters from a list of strings.

```python
words = ["hello", "world"]
unique_chars = {char for word in words for char in word}
print(unique_chars)
# Output: {'o', 'w', 'l', 'r', 'e', 'd', 'h'}
```

#### Combining Nested Set Comprehension with Functions

Suppose you have a function that generates multiples of a number, and you want to create a set of multiples for a range of numbers.

```python
def multiples(n, count):
    return [n * i for i in range(1, count + 1)]

multiples_set = {multiple for x in range(1, 4) for multiple in multiples(x, 3)}
print(multiples_set)
# Output: {1, 2, 3, 4, 6, 9}
```

#### Nested Set Comprehension with Complex Conditions

Creating a set of pairs (x, y) where the sum of x and y is even.

```python
even_sum_pairs = {(x, y) for x in range(5) for y in range(5) if (x + y) % 2 == 0}
print(even_sum_pairs)
# Output: {(0, 4), (4, 0), (1, 3), (2, 2), (3, 1), (0, 2), (2, 0), (4, 4), (3, 3), (1, 1), (4, 2), (2, 4), (0, 0)}
```

### Summary

- Nested set comprehensions provide a concise way to create sets with multiple levels of iteration and filtering.
- They are useful for generating complex sets from iterables with conditions and transformations.
- The syntax is `{outer_expr for outer_item in outer_iterable if outer_condition for inner_item in inner_iterable if inner_condition}`.
- They can be combined with functions and complex conditions to create more sophisticated sets.

Using nested set comprehensions, you can write more expressive and efficient Python code for generating sets with multiple levels of logic.