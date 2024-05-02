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