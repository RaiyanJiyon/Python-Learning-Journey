# Duck Typing in Python

Duck typing is a concept in Python (and other dynamically typed languages) where the type or class of an object is determined by its behavior rather than its inheritance hierarchy or explicit interface implementations. The term "duck typing" comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

In Python, duck typing means that the suitability of an object for a particular purpose is determined by whether it supports the required methods or behaviors, rather than its explicit type or class.

Here's an example to illustrate duck typing:


```python
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
```

In this example:

1. We define three classes: Dog, Duck, and Car.
2. Both Dog and Duck classes have a `sound()` method.
3. The `make_sound()` function takes an argument entity and calls its `sound()` method.
4. We create objects of different classes (dog, duck, and car) and pass them to the `make_sound()` function.
5. The function works successfully with dog and duck objects because they both have a `sound()` method. However, it throws an AttributeError when called with the car object because it doesn't have a `sound()` method.

In duck typing, Python doesn't check the explicit type of the object; instead, it checks whether the object supports the required methods or behaviors at runtime. This flexible approach allows for more dynamic and expressive code, as objects can be used interchangeably based on their behavior rather than their class or inheritance hierarchy.
