class MyClass:
    class_variable = 10  # Class variable

    def __init__(self, value):
        self.instance_variable = value  # Instance variable

    @classmethod
    def class_method(cls, x):
        print("Class variable:", cls.class_variable)
        print("Called with:", x)

# Calling the class method using the class name
MyClass.class_method(5)
# Output:
# Class variable: 10
# Called with: 5

# Creating an instance of MyClass
obj = MyClass(20)

# Calling the class method using the instance
obj.class_method(7)
# Output:
# Class variable: 10
# Called with: 7