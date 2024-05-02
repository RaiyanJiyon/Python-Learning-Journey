# Hierarchical Inheritance in Python

Hierarchical inheritance in Python refers to a scenario where multiple classes inherit from a single superclass, forming a hierarchical structure. In hierarchical inheritance, each subclass inherits attributes and methods from the same superclass but may provide its own specialized behavior.

Here's an example demonstrating hierarchical inheritance in Python:

```python
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

class Cat(Animal):  
    def __init__(self, name, color):
        super().__init__("Cat")
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} meows")

# Creating instances of Dog and Cat
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "White")

# Accessing attributes and methods
print(dog.species)  # Output: Dog
print(dog.name)     # Output: Buddy
print(dog.breed)    # Output: Labrador
dog.speak()         # Output: Animal speaks
dog.bark()          # Output: Buddy barks

print(cat.species)  # Output: Cat
print(cat.name)     # Output: Whiskers
print(cat.color)    # Output: White
cat.speak()         # Output: Animal speaks
cat.meow()          # Output: Whiskers meows
```

In this example:

- The Animal class serves as the superclass.
- Both Dog and Cat classes inherit from Animal and serve as subclasses.
- Each subclass (Dog and Cat) inherits attributes and methods from the same superclass (Animal) but provides its own specialized behavior (`bark()` for Dog and `meow()` for Cat).

Hierarchical inheritance allows you to create a class hierarchy where multiple subclasses share common characteristics and behavior from a single superclass but can also have their own specialized behavior. It promotes code reuse and modularity by organizing classes into a hierarchical structure based on their relationships.
