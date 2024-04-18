'''

Single inheritance in Python refers to the concept where a class (subclass) inherits attributes and methods from only one other class (superclass or base class). In single inheritance, each subclass has exactly one superclass.

Here's a simple example demonstrating single inheritance in Python:
'''

class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def bark(self):
        print(f"{self.name} barks")

# Creating an instance of Dog
dog = Dog("Buddy")

# Accessing attributes and methods
print(dog.species)  # Output: Dog
dog.speak()         # Output: Animal speaks
dog.bark()          # Output: Buddy barks

'''
In this example, the Animal class is the superclass, and the Dog class is the subclass. The Dog class inherits from Animal using the syntax class Dog(Animal). As a result, the Dog class inherits the species attribute and speak() method from the Animal class.

Single inheritance allows the Dog class to reuse the behavior defined in the Animal class and extend it by adding its own attributes and methods. It promotes code reuse, modularity, and polymorphism by allowing for the creation of class hierarchies where subclasses inherit and specialize behavior from their superclass.
'''