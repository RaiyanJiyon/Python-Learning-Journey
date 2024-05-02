class A:
    def method(self):
        print("Method of class A")

class B:
    def method(self):
        print("Method of class B")

class C(A, B):  # Multiple inheritance
    pass

class D(B, A):  # Another example of multiple inheritance
    pass

# Creating instances of C and D
c = C()
d = D()

# Calling the method
c.method()  # Output: Method of class A
d.method()  # Output: Method of class B