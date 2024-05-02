class Dog:
    def sound(self):
        return "Woof!"

class Duck:
    def sound(self):
        return "Quack!"

class Car:
    def drive(self):
        return "Vroom!"

def make_sound(entity):
    print(entity.sound())

# Objects of different classes
dog = Dog()
duck = Duck()
car = Car()

# Calling the make_sound function with different objects
make_sound(dog)  # Output: Woof!
make_sound(duck)  # Output: Quack!
make_sound(car)  # Throws an AttributeError: 'Car' object has no attribute 'sound'
