# Class Variable or Static Variable in Python


In Python, class variables (also known as static variables) are variables that are shared among all instances of a class. They are declared within the class but outside of any method, typically at the beginning of the class definition. Class variables are accessed using the class name itself or through an instance of the class.

Here's an example demonstrating class variables:

```python
class Circle:
    # Class variable
    pi = 3.14159

    def __init__(self, radius):
        # Instance variable
        self.radius = radius

    def calculate_area(self):
        # Accessing class variable within instance method
        return self.pi * self.radius ** 2

# Creating objects (instances) of the Circle class
circle1 = Circle(5)
circle2 = Circle(3)

# Accessing class variable using class name
print("Value of pi:", Circle.pi)  # Output: Value of pi: 3.14159

# Accessing class variable using instance
print("Value of pi (through instance):", circle1.pi)  # Output: Value of pi (through instance): 3.14159

# Accessing instance variable and calling method
print("Area of circle1:", circle1.calculate_area())  # Output: Area of circle1: 78.53975
print("Area of circle2:", circle2.calculate_area())  # Output: Area of circle2: 28.27431
```


In this example, 
- pi is a class variable because it is declared within the class but outside any method. 
- It is accessed using the class name Circle or through instances of the class circle1 and circle2.

Class variables are useful for storing data that is shared among all instances of a class, such as constants or configuration parameters. They are accessed using the class name, which makes their usage consistent across all instances of the class.
