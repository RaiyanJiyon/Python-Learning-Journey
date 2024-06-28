# Nested Function in Python

In Python, nested functions are functions defined inside another function. They are useful when you need to perform a specific task that is only relevant to the outer function's scope. Nested functions can access variables from the enclosing (outer) function's scope, making them powerful for encapsulating related functionality and improving code organization.

### Syntax of Nested Functions

Here's how you define a nested function in Python:

```python
def outer_function():
    # Outer function scope
    
    def nested_function():
        # Nested function scope
        print("Inside nested function")
    
    # Outer function can call the nested function
    nested_function()

# Calling the outer function
outer_function()
```

In this example:
- `nested_function()` is defined inside `outer_function()`.
- `nested_function()` can access variables and parameters of `outer_function()` directly.
- When `outer_function()` is called, it in turn calls `nested_function()`.

### Accessing Variables from Enclosing Scope

Nested functions can access variables from the enclosing scope (outer function). This concept is known as **lexical scoping** or **closure**. This allows you to use variables from the outer function without passing them as parameters to the nested function.

**Example:**

```python
def outer_function(x):
    def inner_function():
        print(f"Value of x inside inner function: {x}")
    
    inner_function()

# Calling the outer function
outer_function(10)  # Output: "Value of x inside inner function: 10"
```

In this example:
- `inner_function()` accesses the variable `x` from `outer_function()` directly.

### Returning Functions from Nested Functions

Nested functions can also return other functions. This is particularly useful for creating functions dynamically or depending on certain conditions within the outer function.

**Example:**

```python
def outer_function(x):
    def inner_function():
        return f"Value of x inside inner function: {x}"
    
    return inner_function

# Creating a function using the outer function
my_function = outer_function(15)

# Calling the created function
result = my_function()
print(result)  # Output: "Value of x inside inner function: 15"
```

In this example:
- `outer_function()` returns `inner_function` without calling it immediately.
- `my_function` now references `inner_function`, and calling `my_function()` executes `inner_function` with `x` set to `15`.

### Use Cases of Nested Functions

Nested functions are typically used when:
- You want to encapsulate related functionality that is only relevant within the scope of the outer function.
- You need to access variables from the outer function's scope without passing them explicitly as arguments.
- You want to create functions dynamically based on certain conditions or parameters.

### Conclusion

Nested functions in Python provide a way to organize code, encapsulate functionality, and maintain scope-related variables effectively. By understanding how nested functions work, you can leverage them to create cleaner, more modular code that enhances readability and maintainability in your Python programs.