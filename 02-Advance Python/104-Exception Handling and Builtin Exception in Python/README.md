# Exception Handling and Builtin Exception in Python

Exception handling in Python allows you to gracefully manage errors that occur during the execution of your program. Python provides a way to catch and handle exceptions using try, except, else, and finally blocks. Additionally, Python has a built-in hierarchy of exception classes to represent different types of errors.

Here's an overview of how exception handling works in Python:

### try, except, else, and finally Blocks:

```python
try:
    # Code that may raise an exception
    result = 10 / 0  # Division by zero will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle specific exception
    print("Division by zero error")
except Exception as e:
    # Handle any other exception
    print("An error occurred:", e)
else:
    # Execute if no exception is raised
    print("No exception occurred")
finally:
    # Execute regardless of whether an exception occurred
    print("Finally block")
```

- The try block contains the code that may raise an exception.
- The except block catches and handles specific exceptions. You can have multiple except blocks to handle different types of exceptions.
- The else block executes if no exception occurs in the try block.
- The finally block executes regardless of whether an exception occurred. It is often used for cleanup tasks such as closing files or releasing resources.


## Built-in Exception Hierarchy:
Python has a built-in hierarchy of exception classes, where each class represents a specific type of error. Some common built-in exceptions include:

- **Exception**: Base class for all built-in exceptions.
- **ZeroDivisionError**: Raised when division or modulo by zero occurs.
- **TypeError**: Raised when an operation or function is applied to an object of an inappropriate type.
- **ValueError**: Raised when a function receives an argument of the correct type but with an inappropriate value.
- **FileNotFoundError**: Raised when a file or directory is requested but cannot be found.
- **IOError**: Base class for I/O related errors.

You can catch these exceptions using `except` blocks and handle them appropriately in your code.

```python
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("An error occurred:", e)
```

By catching and handling exceptions, you can make your code more robust and resilient to errors.

Remember, it's important to handle exceptions appropriately in your code to ensure that your program behaves predictably and gracefully in the face of errors.






