from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        print("Drawing a circle")

class Square(Drawable):
    def draw(self):
        print("Drawing a square")

# Trying to instantiate an abstract class raises an error
# drawable = Drawable()  # TypeError: Can't instantiate abstract class Drawable with abstract methods draw

# Creating instances of Circle and Square
circle = Circle()
square = Square()

# Calling the draw method on Circle and Square objects
circle.draw()  # Output: Drawing a circle
square.draw()  # Output: Drawing a square
