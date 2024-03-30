'''
In Python, you can use the built-in math module to perform various mathematical operations. The math module provides functions for mathematical operations beyond basic arithmetic. Here are some commonly used math functions available in the math module:

Trigonometric functions:

math.sin(x): Return the sine of x, where x is in radians.
math.cos(x): Return the cosine of x, where x is in radians.
math.tan(x): Return the tangent of x, where x is in radians.
math.asin(x): Return the arc sine of x, in radians.
math.acos(x): Return the arc cosine of x, in radians.
math.atan(x): Return the arc tangent of x, in radians.
math.atan2(y, x): Return atan(y / x), in radians.
Hyperbolic functions:

math.sinh(x): Return the hyperbolic sine of x.
math.cosh(x): Return the hyperbolic cosine of x.
math.tanh(x): Return the hyperbolic tangent of x.
Exponential and logarithmic functions:

math.exp(x): Return e raised to the power of x.
math.log(x): Return the natural logarithm of x.
math.log10(x): Return the base-10 logarithm of x.
Power and root functions:

math.pow(x, y): Return x raised to the power of y.
math.sqrt(x): Return the square root of x.
math.isqrt(x): Return the integer square root of x.
Rounding and absolute functions:

math.ceil(x): Return the ceiling of x, the smallest integer greater than or equal to x.
math.floor(x): Return the floor of x, the largest integer less than or equal to x.
math.trunc(x): Return the truncated integer value of x.
math.fabs(x): Return the absolute value of x.
Constants:

math.pi: Mathematical constant π (pi).
math.e: Mathematical constant e (Euler's number).
'''

# To use these functions, you need to import the math module:

import math

# Example usage
print(math.sin(math.pi / 2))  # Output: 1.0
print(math.sqrt(16))          # Output: 4.0
print(math.exp(2))            # Output: 7.38905609893065

'''These are just a few examples of the mathematical functions available in Python's math module. You can refer to the Python documentation for the full list of functions and their descriptions.'''