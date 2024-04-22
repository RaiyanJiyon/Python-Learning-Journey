'''
Method overloading in Python refers to the ability to define multiple methods with the same name but with different signatures (number or types of parameters) within a single class. Unlike some other programming languages like Java or C++, Python does not support method overloading in the traditional sense, where multiple methods with the same name can coexist within the same class and the appropriate method is selected based on the number or types of arguments provided.

However, Python provides a flexible alternative using default parameter values and variable-length argument lists to achieve similar functionality. Here's an example:
'''

class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Creating an instance of MathOperations
math_ops = MathOperations()

# This will raise an error because only the second add method is defined
# print(math_ops.add(1, 2))  # Raises TypeError: add() missing 1 required positional argument: 'c'

# Calling the second add method with three arguments
print(math_ops.add(1, 2, 3))  # Output: 6


'''
In this example, we have a class MathOperations with two add() methods. However, only the second add() method is defined, so trying to call the first add() method with two arguments will raise a TypeError.

'''
