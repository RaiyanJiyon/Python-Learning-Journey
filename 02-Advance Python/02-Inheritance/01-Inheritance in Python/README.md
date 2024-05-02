# Inheritance in Python

Inheritance in Python allows a class (subclass) to inherit attributes and methods from another class (superclass or base class). The subclass can then extend or modify the behavior of the superclass while also inheriting its functionality. This promotes code reuse and facilitates building more complex and specialized classes based on existing ones.

Here's a simple example demonstrating inheritance in Python:

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def speak(self):  # Overriding the speak method
        print(f"{self.name} barks")

# Creating instances of the classes
animal = Animal("Cat")
dog = Dog("Buddy")

# Calling methods
animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Buddy barks
```


In this example:

- The Animal class has an __init__() method to initialize the species and a `speak()` method to print a generic message.
- The Dog class inherits from Animal using the syntax class Dog(Animal).
- The Dog class also has its own __init__() method to initialize the name of the dog and overrides the `speak()` method to print a specific message for dogs.
- When an instance of Dog is created, it inherits the attributes and methods of Animal. However, it can also have its own attributes and methods, and it can override methods from the superclass to provide specialized behavior.

Inheritance allows for creating hierarchies of classes, where subclasses inherit characteristics from their superclass and can further extend or specialize them. This makes code more modular, easier to maintain, and promotes code reuse.
'''