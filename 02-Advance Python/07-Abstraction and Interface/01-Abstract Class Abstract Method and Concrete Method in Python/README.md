# Abstract Class, Abstract Method and Concrete Method in Python

In Python, an abstract class is a class that cannot be instantiated directly. It serves as a blueprint for other classes and may contain one or more abstract methods, which are methods declared but not implemented in the abstract class. Abstract classes are meant to be subclassed, and their abstract methods must be implemented by the subclasses.

Here's an example demonstrating abstract classes and abstract methods using the abc module:

```python
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
```

In this example:

- Shape is an abstract class that inherits from the ABC (Abstract Base Class) class provided by the abc module.

- Shape defines two abstract methods, area() and perimeter(), which must be implemented by its subclasses.

- Shape also defines a concrete method description(), which provides a default implementation but can be overridden by subclasses.

- Circle is a subclass of Shape that implements the area() and perimeter() methods, making it concrete. It also overrides the description() method.



Abstract classes and methods allow you to define a common interface for a group of related classes while enforcing implementation details in the subclasses.
They help promote code abstraction, modularity, and reusability in object-oriented programming.






