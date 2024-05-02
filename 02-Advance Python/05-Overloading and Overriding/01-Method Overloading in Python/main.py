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