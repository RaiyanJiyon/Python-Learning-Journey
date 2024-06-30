# Global Keyword in Python

The `global` keyword in Python is used to declare that a variable inside a function is global. It tells the interpreter that the variable should not be treated as a local variable but as a global variable that has been defined outside of the function.

### Why Use the `global` Keyword?

When you assign a value to a variable inside a function, by default, it is treated as a local variable. If you need to modify a global variable inside a function, you must declare it as global using the `global` keyword. Otherwise, Python will treat it as a local variable and the assignment will only affect the local scope of the function.

### Example of Using the `global` Keyword

#### Without `global`

Here is an example demonstrating the behavior without using the `global` keyword:

```python
x = 10

def modify_variable():
    x = 5  # This creates a new local variable x
    print(f"Inside function: x = {x}")

modify_variable()
print(f"Outside function: x = {x}")
```

Output:
```
Inside function: x = 5
Outside function: x = 10
```

In this example:
- `x = 5` inside `modify_variable()` creates a new local variable `x` that shadows the global variable `x`.
- The global variable `x` remains unchanged outside the function.

#### With `global`

Now let's see the effect of using the `global` keyword:

```python
x = 10

def modify_variable():
    global x  # Declare x as global
    x = 5  # Modify the global variable x
    print(f"Inside function: x = {x}")

modify_variable()
print(f"Outside function: x = {x}")
```

Output:
```
Inside function: x = 5
Outside function: x = 5
```

In this example:
- `global x` inside `modify_variable()` indicates that `x` refers to the global variable `x`.
- Modifying `x` inside the function affects the global variable `x`, which is reflected outside the function as well.

### Multiple Global Variables

You can declare multiple global variables within a function using the `global` keyword:

```python
a = 10
b = 20

def modify_variables():
    global a, b
    a = 5
    b = 15
    print(f"Inside function: a = {a}, b = {b}")

modify_variables()
print(f"Outside function: a = {a}, b = {b}")
```

Output:
```
Inside function: a = 5, b = 15
Outside function: a = 5, b = 15
```

### Global Variables in Nested Functions

When dealing with nested functions, the `global` keyword still refers to the global scope. If you need to modify a variable in the enclosing (non-global) scope, you should use the `nonlocal` keyword.

```python
x = 10

def outer_function():
    x = 20
    
    def inner_function():
        global x
        x = 30  # Modifies the global variable x
        print(f"Inside inner_function: x = {x}")
    
    inner_function()
    print(f"Inside outer_function: x = {x}")

outer_function()
print(f"Outside all functions: x = {x}")
```

Output:
```
Inside inner_function: x = 30
Inside outer_function: x = 20
Outside all functions: x = 30
```

In this example:
- `global x` inside `inner_function()` modifies the global variable `x`.
- The `x` inside `outer_function()` remains unchanged as it is a local variable to `outer_function()`.

### Conclusion

The `global` keyword in Python is essential for modifying global variables inside a function. It tells the interpreter to use the global variable instead of creating a new local one. This keyword is particularly useful when you need to manage state or configuration settings across multiple functions. However, it should be used judiciously to maintain code readability and avoid potential side effects from unintended modifications of global state.