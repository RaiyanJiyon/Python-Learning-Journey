# User Defined Exception in Python

In Python, you can create your own custom exceptions by subclassing the built-in Exception class or one of its subclasses. This allows you to define specific types of errors that are meaningful for your application and handle them accordingly.

Here's an example of how you can define a custom exception:

```python
class CustomError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)

# Raise custom exception
raise CustomError("This is a custom error message")
```

In this example:

- We define a new exception class CustomError by subclassing the built-in Exception class.
- The __init__ method is overridden to accept a custom error message.
- Inside the __init__ method, we call the superclass's __init__ method to initialize the exception with the provided message.

You can then raise instances of this custom exception anywhere in your code:

```python
def divide(x, y):
    if y == 0:
        raise CustomError("Cannot divide by zero")
    return x / y

try:
    result = divide(10, 0)
except CustomError as e:
    print("Custom error occurred:", e)
```

In this example:

- We define a function divide() that attempts to divide two numbers.
- Inside the function, we check if the divisor y is zero. If it is, we raise a CustomError exception with the message "Cannot divide by zero".
- We wrap the call to divide() in a try-except block to catch any CustomError exceptions that may be raised.
- If a CustomError exception is caught, we print the error message.


Custom exceptions allow you to create clear and meaningful error messages tailored to your application's specific requirements. They help improve the readability and maintainability of your code by providing a clear indication of what went wrong when an error occurs.






