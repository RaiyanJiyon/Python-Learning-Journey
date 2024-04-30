def divide(x, y):
    assert y != 0, "Cannot divide by zero"
    return x / y

result = divide(10, 0)  # This will raise an AssertionError with the message "Cannot divide by zero"
