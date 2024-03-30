'''
In Python, you can easily iterate over the elements of a list using a for loop. This allows you to access each element of the list one by one and perform operations on them. Here's how you can access a list using a for loop:
'''

# Define a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements of the list using a for loop
for element in my_list:
    print(element)

'''
In this example:

We define a list called my_list containing integers.
We use a for loop to iterate over each element in the list.
Inside the loop, the variable element represents each individual element of the list, and we print it.
'''

# You can also access the index along with the element by using the enumerate() function:

# Accessing elements and their indices using a for loop
for index, element in enumerate(my_list):
    print("Index:", index, "Element:", element)


'''
In this example:

We use the enumerate() function to get both the index and the element from the list.
Inside the loop, the index variable represents the index of the element, and the element variable represents the element itself.
'''

'''Using a for loop to iterate over a list is a common and efficient way to access its elements and perform operations on them.'''