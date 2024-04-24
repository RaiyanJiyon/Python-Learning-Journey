from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):
        print("This is a shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def description(self):
        print("This is a circle.")

# Trying to instantiate an abstract class raises an error
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

# Creating an instance of Circle
circle = Circle(5)

# Calling methods
print(circle.area())        # Output: 78.5
print(circle.perimeter())   # Output: 31.400000000000002
circle.description()        # Output: This is a circle.
