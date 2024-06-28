def divide(dividend, divisor):
    """This function divides two numbers and returns the quotient and remainder."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

result = divide(10, 3)
print(result)  # Output: (3, 1)