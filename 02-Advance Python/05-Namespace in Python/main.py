'''
In Python, a namespace is a mapping from names (identifiers) to objects. It's a system to organize and manage names to avoid conflicts and provide a way to access objects. Namespaces are used to determine the scope of identifiers (variables, functions, classes, etc.) and help in avoiding naming collisions.

Python uses namespaces to implement scoping rules. There are several namespaces in Python, including:

Local Namespace: This namespace includes names defined within a function or method. It's created when the function or method is called and gets destroyed when the function or method exits.

Global Namespace: This namespace includes names defined at the top level of a module or script. It's created when the module is imported or when the script is executed and lasts until the Python interpreter terminates.

Enclosing Namespace: This namespace is used for nested functions. It includes names defined in the enclosing function's scope.

Built-in Namespace: This namespace includes built-in functions, exceptions, and other objects provided by Python. It's always available and is created when the Python interpreter starts.

Namespaces are organized in a hierarchical manner, known as the "namespace hierarchy." When a name is referenced, Python searches for it in the local namespace first, then in the enclosing namespaces, then in the global namespace, and finally in the built-in namespace.

Here's a simple example to illustrate namespaces:'''

x = 10  # Global variable

def foo():
    y = 20  # Local variable
    print("Local namespace:", locals())

foo()
print("Global namespace:", globals())
