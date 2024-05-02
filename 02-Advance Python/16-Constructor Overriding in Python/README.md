# Constructor Overriding in Python

In Python, when a subclass provides its own __init__() method, it overrides the constructor of its superclass. This allows the subclass to customize the initialization process by providing its own set of parameters and initialization logic, while still having the option to call the constructor of its superclass if needed.

Here's an example demonstrating constructor overriding in Python:

```python
class Animal:
    def __init__(self, species):
        self.species = species
        print("Animal constructor")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call superclass constructor to initialize the 'species' attribute
        super().__init__("Dog")
        self.name = name
        self.breed = breed
        print("Dog constructor")

# Creating an instance of Dog
dog = Dog("Buddy", "Labrador")

# Accessing attributes
print(dog.species)  # Output: Dog
print(dog.name)     # Output: Buddy
print(dog.breed)    # Output: Labrador
```

In this example:

- The Animal class has a constructor that initializes the species attribute.
- The Dog class inherits from Animal and provides its own constructor (__init__() method) to initialize the name and breed attributes. 
- It calls the constructor of its superclass (Animal) using `super()`.
- __init__("Dog") to initialize the species attribute inherited from Animal.
- When an instance of Dog is created, the constructor of Animal is overridden by the constructor of Dog. Both constructors are not called explicitly; instead, the constructor of Dog implicitly calls the constructor of Animal using `super().__init__("Dog")`.


This demonstrates how constructor overriding works in Python, allowing subclasses to customize the initialization process while still having the option to leverage the initialization logic provided by their superclass.
