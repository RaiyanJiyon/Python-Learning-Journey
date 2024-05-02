# Difference between Abstract Class and Interface in Python

In Python, both abstract classes and interfaces serve the purpose of defining a contract that subclasses must adhere to by implementing certain methods. However, there are differences in how they are implemented and used:

**Abstract Class:**
- An abstract class is a class that cannot be instantiated directly and is meant to be subclassed.
- Abstract classes may contain both abstract methods (methods without implementation) and concrete methods (methods with implementation).
- Abstract classes can have attributes and methods with implementation, in addition to abstract methods.
- Subclasses of an abstract class must implement all the abstract methods defined in the abstract class, but they may also inherit and use the concrete methods and attributes defined in the abstract class.
- Abstract classes are defined using the abc module and the @abstractmethod decorator.

**Interface:**
- In Python, interfaces are typically implemented using abstract base classes (ABCs) and abstract methods.
- An interface defines a contract specifying a set of methods that a class must implement, without providing any implementation details.
- Interfaces in Python are often created by defining an abstract base class with one or more abstract methods, which must be implemented by subclasses.
- Subclasses implementing an interface must provide concrete implementations for all the methods defined in the interface.
- Interfaces do not provide any implementation for the methods they define; they only specify the method signatures.
- Python does not have a specific language construct for interfaces, but they can be achieved using abstract base classes and abstract methods.

In summary, abstract classes in Python can contain both abstract and concrete methods, can have attributes and implementation details, and serve as a partial implementation of a class. Interfaces, on the other hand, define a contract specifying the methods that must be implemented by subclasses, without providing any implementation details, and are typically implemented using abstract base classes and abstract methods.
