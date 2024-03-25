'''
Returning Multiple Values:
To return multiple values from a function, you can return a tuple, a list, or any iterable containing the values.
'''

def divide(dividend, divisor):
    """This function divides two numbers and returns the quotient and remainder."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

result = divide(10, 3)
print(result)  # Output: (3, 1)

'''
In this example, the divide() function returns two values: the quotient and the remainder of dividing dividend by divisor. The values are returned as a tuple (quotient, remainder). When you call the function with arguments 10 and 3, it returns (3, 1), which is stored in the result variable.
'''
