'''
In Python, a static method is a method that is bound to the class rather than an instance of the class. Unlike instance methods, static methods do not have access to the instance or class state through self or cls parameters. They are defined using the @staticmethod decorator and behave like regular functions but are defined within the class namespace.

Here's an example demonstrating the use of a static method in Python:'''

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


'''
In this example, add() and multiply() are static methods of the MathUtils class. They are defined using the @staticmethod decorator. These methods do not have access to the class or instance state and operate purely on their arguments. Therefore, they are independent of the state of any specific instance of the class.

Static methods are useful for grouping utility functions related to the class within the class namespace. They are similar to regular functions but provide a logical grouping with the class they are associated with. Static methods can be called using the class name and do not require an instance of the class to be created.
'''