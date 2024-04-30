class CustomError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)

def divide(x, y):
    if y == 0:
        raise CustomError("Cannot divide by zero")
    return x / y

try:
    result = divide(10, 0)
except CustomError as e:
    print("Custom error occurred:", e)
