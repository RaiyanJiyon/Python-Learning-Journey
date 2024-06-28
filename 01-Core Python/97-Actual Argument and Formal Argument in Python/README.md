# Actual Argument and Formal Argument in Python

In Python, when discussing function parameters, there are two main terms used to differentiate between the arguments used when defining a function (formal parameters) and the arguments supplied when calling the function (actual parameters). Understanding the distinction between these terms helps clarify how functions receive and process input.

### Formal Parameters (Formal Arguments)

Formal parameters are the variables listed inside the parentheses in the function definition. They act as placeholders for values that are passed to the function when it is called. These parameters define what kind of arguments a function expects and how they should be used within the function's body.

**Syntax:**

```python
def function_name(parameter1, parameter2, ...):
    # Function body
    # Operations using parameters
```

In this syntax:
- `parameter1`, `parameter2`, etc., are formal parameters.
- They are placeholders that represent the values or variables passed to the function when it is called.
- The function body uses these parameters to perform computations, manipulate data, or produce output based on the provided arguments.

### Actual Parameters (Actual Arguments)

Actual parameters, also known simply as arguments, are the values or expressions supplied to a function when calling it. These arguments correspond to the formal parameters defined in the function's header. They provide the actual data or values that the function works with during its execution.

**Syntax:**

When calling a function, you pass actual arguments within the parentheses:

```python
function_name(argument1, argument2, ...)
```

In this syntax:
- `argument1`, `argument2`, etc., are actual arguments.
- They are the real data, variables, or expressions passed to the function.
- These arguments are assigned to the corresponding formal parameters (`parameter1`, `parameter2`, ...) inside the function definition.

### Example

Let's illustrate the concept with an example:

```python
def greet(name, message):
    """Function to greet a person with a custom message."""
    print(f"Hello, {name}! {message}")

# Calling the function with actual arguments
greet("Alice", "Good morning!")  # Output: Hello, Alice! Good morning!
```

In this example:
- `greet` is defined with two formal parameters: `name` and `message`.
- When `greet("Alice", "Good morning!")` is called:
  - `"Alice"` and `"Good morning!"` are actual arguments.
  - These arguments are assigned to `name` and `message` respectively inside the function.
  - The function prints `"Hello, Alice! Good morning!"` based on the provided arguments.

### Conclusion

Understanding the distinction between formal parameters (formal arguments) and actual parameters (actual arguments) is crucial for effectively using functions in Python. Formal parameters define the function's interface and expectations, while actual parameters provide the data or values that the function operates on when called. This separation of concerns allows functions to be versatile and reusable across different contexts within a Python program.