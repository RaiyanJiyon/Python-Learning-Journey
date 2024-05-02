class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods using the class name
print("Sum:", MathUtils.add(5, 3))         # Output: Sum: 8
print("Product:", MathUtils.multiply(4, 2)) # Output: Product: 8