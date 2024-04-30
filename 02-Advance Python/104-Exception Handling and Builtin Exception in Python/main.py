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
