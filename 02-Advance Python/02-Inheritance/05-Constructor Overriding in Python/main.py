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