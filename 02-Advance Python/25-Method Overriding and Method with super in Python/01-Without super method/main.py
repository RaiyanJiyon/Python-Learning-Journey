'''
Method overriding in Python refers to the ability of a subclass to provide a new implementation for a method that is already defined in its superclass. When a method is called on an object of the subclass, the overridden method in the subclass is invoked instead of the method in the superclass.

Here's an example demonstrating method overriding in Python:
'''

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  
    def speak(self):
        print("Dog barks")

# Creating an instance of Dog
dog = Dog()

# Calling the speak method
dog.speak()  # Output: Dog barks

'''
In this example:

The Animal class has a speak() method.
The Dog class inherits from Animal and provides its own implementation of the speak() method.
When calling the speak() method on an instance of Dog, the overridden method in Dog is invoked, printing "Dog barks" instead of "Animal speaks".

'''