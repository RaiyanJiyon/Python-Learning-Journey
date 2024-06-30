# Global Variable in Python

In Python, a global variable is a variable that is defined outside of any function and can be accessed and modified throughout the entire script. Unlike local variables, which are confined to the function in which they are declared, global variables have a global scope and are accessible from any part of the code, including inside functions.

### Defining and Using Global Variables

Global variables are defined outside of any function and can be used inside any function without being declared again.

#### Example:

```python
# Defining a global variable
global_var = 20

def my_function():
    print(f"Inside the function, global_var = {global_var}")

my_function()  # Output: Inside the function, global_var = 20

print(f"Outside the function, global_var = {global_var}")  # Output: Outside the function, global_var = 20
```

In this example:
- `global_var` is defined outside of any function, making it a global variable.
- `global_var` is accessed inside `my_function()` and outside the function, demonstrating its global scope.

### Modifying Global Variables inside a Function

To modify a global variable inside a function, you need to use the `global` keyword to indicate that you are referring to the global variable, not a local one.

#### Example:

```python
# Defining a global variable
global_var = 20

def my_function():
    global global_var
    global_var = 10  # Modifying the global variable
    print(f"Inside the function, global_var = {global_var}")

my_function()  # Output: Inside the function, global_var = 10

print(f"Outside the function, global_var = {global_var}")  # Output: Outside the function, global_var = 10
```

In this example:
- The `global` keyword is used inside `my_function()` to refer to the global variable `global_var`.
- Modifying `global_var` inside the function changes its value globally.

### Global Variables in Nested Functions

When dealing with nested functions, the `global` keyword still refers to the global scope, not any enclosing function scopes. To modify variables in the enclosing scope (non-global), you need to use the `nonlocal` keyword.

#### Example with Nested Functions:

```python
global_var = 20

def outer_function():
    outer_var = 30
    
    def inner_function():
        global global_var
        nonlocal outer_var
        global_var = 10  # Modifies the global variable
        outer_var = 15  # Modifies the outer function variable
        print(f"Inside inner_function, global_var = {global_var}")
        print(f"Inside inner_function, outer_var = {outer_var}")
    
    inner_function()
    print(f"Inside outer_function, outer_var = {outer_var}")

outer_function()
print(f"Outside all functions, global_var = {global_var}")
```

In this example:
- `global_var` is modified inside the nested `inner_function()` using the `global` keyword.
- `outer_var` is modified inside the nested `inner_function()` using the `nonlocal` keyword, affecting the variable in the enclosing `outer_function()`.

### Best Practices for Using Global Variables

1. **Minimize Usage**: Use global variables sparingly as they can make the code harder to understand and maintain. Overuse can lead to unexpected behavior and bugs.
2. **Descriptive Names**: Use descriptive names for global variables to avoid naming conflicts and to make the code more readable.
3. **Encapsulation**: Consider encapsulating related global variables within classes or modules to better manage and organize the code.

### Conclusion

Global variables in Python are accessible throughout the entire script, including inside functions. To modify a global variable inside a function, use the `global` keyword. When working with nested functions, use the `nonlocal` keyword to modify variables in the enclosing scope. While global variables can be useful, they should be used judiciously to maintain code clarity and prevent potential issues.