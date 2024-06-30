# Local Variable in Python

In Python, a local variable is a variable that is defined within a function and can only be used inside that function. Local variables are created when the function starts executing and are destroyed when the function completes.

### Defining and Using Local Variables

Local variables are defined within a function and can only be accessed within that function. They are not accessible outside of the function.

#### Example:

```python
def my_function():
    local_var = 10  # local variable
    print(f"Inside the function, local_var = {local_var}")

my_function()

# Trying to access local_var outside the function will cause an error
# print(local_var)  # Uncommenting this line will raise a NameError
```

In this example:
- `local_var` is defined inside `my_function()`.
- `local_var` is printed inside the function, but attempting to access it outside the function will result in a `NameError` because it is not defined in the global scope.

### Scope of Local Variables

The scope of a local variable is limited to the function in which it is defined. Local variables are only accessible within the block of code where they are declared.

#### Example with Multiple Functions:

```python
def function_one():
    var = 5
    print(f"function_one: var = {var}")

def function_two():
    var = 10
    print(f"function_two: var = {var}")

function_one()  # Output: function_one: var = 5
function_two()  # Output: function_two: var = 10
```

In this example:
- Each function has its own local variable `var`.
- The `var` in `function_one` is independent of the `var` in `function_two`.

### Local Variables vs. Global Variables

Local variables differ from global variables, which are defined outside of any function and can be accessed anywhere in the code.

#### Example of Global and Local Variables:

```python
global_var = 20  # global variable

def my_function():
    local_var = 10  # local variable
    print(f"Inside the function, local_var = {local_var}")
    print(f"Inside the function, global_var = {global_var}")

my_function()

print(f"Outside the function, global_var = {global_var}")
# print(f"Outside the function, local_var = {local_var}")  # Uncommenting this line will raise a NameError
```

In this example:
- `global_var` is a global variable and can be accessed both inside and outside the function.
- `local_var` is a local variable and can only be accessed inside `my_function()`.

### Modifying Global Variables inside a Function

If you need to modify a global variable inside a function, you must use the `global` keyword to indicate that you are referring to the global variable.

#### Example:

```python
global_var = 20  # global variable

def my_function():
    global global_var
    global_var = 10  # modifying the global variable
    print(f"Inside the function, global_var = {global_var}")

my_function()
print(f"Outside the function, global_var = {global_var}")  # Output: Outside the function, global_var = 10
```

In this example:
- The `global` keyword is used to indicate that `global_var` refers to the global variable.
- Modifying `global_var` inside the function changes its value globally.

### Conclusion

Local variables in Python are variables defined within a function and are accessible only within that function. They have a scope limited to the function and are not accessible outside of it. Understanding the difference between local and global variables and their respective scopes is crucial for writing clear and maintainable code.