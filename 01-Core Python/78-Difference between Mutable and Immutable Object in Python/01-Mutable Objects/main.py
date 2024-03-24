'''
In Python, objects are categorized into two main types based on their mutability: mutable objects and immutable objects. Understanding the difference between mutable and immutable objects is crucial in Python programming. Here's an explanation of each:
'''

'''
Mutable Objects:
Mutable objects are objects whose state or content can be changed after they are created.
This means that you can modify the object's internal state or contents without creating a new object.
Examples of mutable objects in Python include lists, dictionaries, sets, and user-defined classes with mutable attributes.
Mutable objects are generally modified in-place using methods or assignment operations.
'''

# Example of mutable objects:
my_list = [1, 2, 3]
my_list.append(4)  # Modifying the list in place
print(my_list)  # Output: [1, 2, 3, 4]
