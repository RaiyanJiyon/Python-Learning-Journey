# Return Single and Multiple Value and Variable from Function in Python

In Python, functions can return both single and multiple values. This flexibility allows functions to produce outputs that can be used in various ways within a program.

### Returning a Single Value

To return a single value from a function in Python, you use the `return` statement followed by the value you want to return. The function will terminate and pass back this value to the caller.

**Syntax:**

```python
def function_name(parameters):
    # Function body
    # Operations
    return value
```

**Example:**

```python
def add_numbers(a, b):
    """Function to add two numbers."""
    result = a + b
    return result

# Calling the function and storing the returned value
sum_result = add_numbers(3, 5)
print("Sum:", sum_result)  # Output: Sum: 8
```

In this example:
- The function `add_numbers` takes two parameters `a` and `b`.
- It calculates their sum and assigns it to `result`.
- The `return result` statement sends the computed sum back to the caller.
- The returned value (`8`) is stored in `sum_result`.

### Returning Multiple Values

Python functions can return multiple values by separating them with commas in the `return` statement. When a function returns multiple values, they are actually returned as a tuple, which can then be unpacked into individual variables or used as a tuple directly.

**Syntax:**

```python
def function_name(parameters):
    # Function body
    # Operations
    return value1, value2, ...
```

**Example:**

```python
def calculate(a, b):
    """Function to perform multiple calculations."""
    sum_result = a + b
    difference = a - b
    product = a * b
    return sum_result, difference, product

# Calling the function and unpacking the returned tuple
s, d, p = calculate(5, 3)
print("Sum:", s)         # Output: Sum: 8
print("Difference:", d)  # Output: Difference: 2
print("Product:", p)     # Output: Product: 15
```

In this example:
- The `calculate` function takes two parameters `a` and `b`.
- It performs addition (`sum_result`), subtraction (`difference`), and multiplication (`product`) operations.
- The `return sum_result, difference, product` statement returns these values as a tuple `(sum_result, difference, product)`.
- When calling `calculate(5, 3)`, the returned tuple `(8, 2, 15)` is unpacked into variables `s`, `d`, and `p` respectively.

### Using a Single Variable to Store Multiple Values

If you assign the return value of a function that returns multiple values to a single variable, Python automatically creates a tuple containing those values.

**Example:**

```python
def get_info():
    """Function to return multiple pieces of information."""
    name = "Alice"
    age = 30
    city = "Wonderland"
    return name, age, city

# Calling the function and storing the returned tuple
info = get_info()
print(info)  # Output: ('Alice', 30, 'Wonderland')
print("Name:", info[0])   # Output: Name: Alice
print("Age:", info[1])    # Output: Age: 30
print("City:", info[2])   # Output: City: Wonderland
```

In this example:
- The `get_info` function returns three values: `name`, `age`, and `city`.
- When `get_info()` is called, the tuple `('Alice', 30, 'Wonderland')` is returned and stored in the variable `info`.
- You can access individual elements of the tuple using indexing (`info[0]`, `info[1]`, etc.).

### Conclusion

Python functions provide flexibility in returning both single and multiple values, allowing you to encapsulate and reuse logic effectively. Whether you need to return a single result or multiple pieces of data from a function, Python's syntax and handling of return values make it straightforward to work with different types of outputs in your programs.