'''
Multilevel inheritance in Python refers to a scenario where a class inherits from a subclass, forming a chain of inheritance with multiple levels. In multilevel inheritance, each subclass inherits attributes and methods from its immediate superclass, as well as from all its ancestor classes up the inheritance hierarchy.

Here's an example demonstrating multilevel inheritance in Python:
'''

class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

class Dog(Animal):  
    def __init__(self, name, breed):
        super().__init__("Dog")
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks")

class Labrador(Dog):  
    def __init__(self, name):
        super().__init__(name, "Labrador")

# Creating an instance of Labrador
labrador = Labrador("Buddy")

# Accessing attributes and methods
print(labrador.species)  # Output: Dog
print(labrador.name)     # Output: Buddy
print(labrador.breed)    # Output: Labrador
labrador.speak()         # Output: Animal speaks
labrador.bark()          # Output: Buddy barks

'''
In this example:

The Animal class serves as the superclass.
The Dog class inherits from Animal and serves as a subclass.
The Labrador class inherits from Dog and serves as a subclass of Dog.
Each subclass (Dog and Labrador) inherits attributes and methods from its immediate superclass (Animal and Dog, respectively) and can also access attributes and methods inherited from ancestor classes (Animal).
Multilevel inheritance allows you to create complex class hierarchies where each subclass can inherit and extend behavior from its superclass and ancestor classes. It promotes code reuse, modularity, and extensibility by enabling you to organize and structure your code in a hierarchical manner.
'''