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