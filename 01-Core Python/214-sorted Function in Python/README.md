The `sorted` function in Python is used to sort an iterable (e.g., list, tuple, string, etc.) and return a new sorted list. It doesn't modify the original iterable but creates a new one.

### Syntax
```python
sorted(iterable, key=None, reverse=False)
```

### Parameters
- **iterable**: The sequence (e.g., list, tuple, string) to be sorted.
- **key**: A function that serves as a key for the sort comparison. Defaults to `None`.
- **reverse**: A boolean value. If `True`, the sorted list is reversed (or sorted in descending order). Defaults to `False`.

### Examples

#### Sorting a List
```python
numbers = [4, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 4, 5, 6, 9]
```

#### Sorting a List in Reverse Order
```python
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # Output: [9, 6, 5, 4, 2, 1]
```

#### Sorting a List of Strings
```python
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry', 'date']
```

#### Sorting a List of Strings by Length
```python
sorted_words_by_length = sorted(words, key=len)
print(sorted_words_by_length)  # Output: ['date', 'apple', 'banana', 'cherry']
```

#### Sorting a List of Tuples
```python
students = [("John", 22), ("Jane", 21), ("Dave", 25)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)  # Output: [('Jane', 21), ('John', 22), ('Dave', 25)]
```

#### Sorting a Dictionary by Keys
To sort a dictionary by its keys, you can use the `sorted` function on the dictionary's keys or items.

```python
dictionary = {'banana': 3, 'apple': 4, 'cherry': 2}
sorted_keys = sorted(dictionary)
print(sorted_keys)  # Output: ['apple', 'banana', 'cherry']

sorted_items = sorted(dictionary.items())
print(sorted_items)  # Output: [('apple', 4), ('banana', 3), ('cherry', 2)]
```

#### Sorting a Dictionary by Values
To sort a dictionary by its values, you can use a lambda function as the key.

```python
sorted_by_value = sorted(dictionary.items(), key=lambda item: item[1])
print(sorted_by_value)  # Output: [('cherry', 2), ('banana', 3), ('apple', 4)]
```

### Advanced Usage

#### Sorting with a Custom Key Function
You can define a custom function to be used as the `key` for sorting.

```python
def custom_sort(s):
    return len(s), s

words = ["apple", "banana", "cherry", "date"]
sorted_words_custom = sorted(words, key=custom_sort)
print(sorted_words_custom)  # Output: ['date', 'apple', 'banana', 'cherry']
```

In this example, the words are sorted primarily by their length and secondarily by alphabetical order when lengths are the same.

### Summary
The `sorted` function is a powerful and flexible tool for sorting iterables in Python. It provides a straightforward way to sort data by various criteria, using the `key` and `reverse` parameters to customize the sorting behavior.