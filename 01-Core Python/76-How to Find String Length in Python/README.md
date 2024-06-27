# How to Find String Length in Python

In Python, you can find the length of a string using the `len()` function. Here’s how you can do it:

### Example

```python
# Define a string
my_string = "Hello, World!"

# Calculate the length of the string
length = len(my_string)

# Print the length
print("Length of the string:", length)
```

#### Output:
```
Length of the string: 13
```

### Explanation

1. **Define a String**: Assign a string to a variable (`my_string` in this case).
   
2. **Use `len()` Function**: Apply the `len()` function to the string variable. This function returns the number of characters in the string.

3. **Print the Length**: Display the length using `print()`.

### Notes

- The `len()` function counts all characters in the string, including spaces and punctuation.
- For an empty string (`""`), `len()` will return `0`.
- `len()` can also be used to find the length of other iterable objects like lists, tuples, and dictionaries.

This method is straightforward and commonly used whenever you need to determine the length of a string in Python.