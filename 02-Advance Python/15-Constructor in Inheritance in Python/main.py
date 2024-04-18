'''
In Python, when a subclass is created, it can have its own constructor (__init__() method), which can be used to initialize its own attributes, as well as call the constructor of its superclass to initialize the attributes inherited from the superclass.

Here's an example demonstrating how constructors work in inheritance in Python:
'''

class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

class Dog(Animal):  
    def __init__(self, name, breed):
        # Call superclass constructor to initialize the 'species' attribute
        super().__init__("Dog")
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks")

# Creating an instance of Dog
dog = Dog("Buddy", "Labrador")

# Accessing attributes and methods
print(dog.species)  # Output: Dog
print(dog.name)     # Output: Buddy
print(dog.breed)    # Output: Labrador
dog.speak()         # Output: Animal speaks
dog.bark()          # Output: Buddy barks


'''
In this example:

The Animal class has a constructor that initializes the species attribute.
The Dog class inherits from Animal and has its own constructor that initializes the name and breed attributes. It calls the constructor of its superclass (Animal) using super().__init__("Dog") to initialize the species attribute inherited from Animal.
When an instance of Dog is created, both the constructor of Animal and the constructor of Dog are called, ensuring that all attributes are properly initialized.
The Dog class also defines its own method bark().
This demonstrates how constructors work in inheritance in Python, allowing subclasses to properly initialize both their own attributes and attributes inherited from their superclass.
'''