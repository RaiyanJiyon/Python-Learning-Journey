class OuterClass:
    def __init__(self, outer_attr):
        self.outer_attr = outer_attr

    class InnerClass:
        def __init__(self, inner_attr):
            self.inner_attr = inner_attr

        def display(self):
            print(f"Inner attribute: {self.inner_attr}")

# Creating an instance of the outer class
outer_obj = OuterClass("outer_value")

# Creating an instance of the inner class using the outer class
inner_obj = outer_obj.InnerClass("inner_value")

# Accessing and calling methods of the inner class
inner_obj.display()  # Output: Inner attribute: inner_value