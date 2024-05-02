# Polymorphism in Python 

Polymorphism in Python refers to the ability of different objects to respond to the same method or function call in different ways. It allows objects of different classes to be treated as objects of a common superclass, and methods to be called on these objects without knowing their specific class types.

There are two main types of polymorphism in Python: method overriding and duck typing.

## Method Overriding: 
Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. When a method is called on an object of the subclass, the overridden method in the subclass is invoked instead of the method in the superclass.

## Duck Typing: 
Duck typing is a concept in Python where the type or class of an object is determined by its behavior (methods and attributes) rather than its inheritance hierarchy or explicit type declaration. If an object behaves like a certain type, it can be treated as that type.


In both examples, different objects respond to the same method call (speak()), but the specific behavior executed depends on the type of the object. This demonstrates polymorphic behavior, where objects of different classes exhibit different behavior in response to the same method call.

Polymorphism promotes code flexibility, extensibility, and modularity by allowing for interchangeable use of objects and enabling dynamic behavior at runtime. It facilitates code reuse and promotes the principle of "programming to an interface, not an implementation."






