# Here's an example demonstrating operator overloading in Python:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define behavior for the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Define behavior for the == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Define behavior for the repr() function
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Creating instances of Vector
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Using the + operator with Vector objects
result = v1 + v2
print(result)  # Output: Vector(6, 8)

# Using the == operator with Vector objects
print(v1 == v2)  # Output: False
