'''
You can also access elements of a list using a while loop in Python. Here's how you can do it:
'''

# Define a list
my_list = [1, 2, 3, 4, 5]

# Initialize an index variable
index = 0

# Accessing elements of the list using a while loop
while index < len(my_list):
    print(my_list[index])
    index += 1


'''
In this example:

We define a list called my_list containing integers.
We initialize an index variable to keep track of the current position in the list.
We use a while loop to iterate over the list as long as the index is less than the length of the list.
Inside the loop, we print the element at the current index using my_list[index].
After printing the element, we increment the index by 1 to move to the next element in the list.
'''

'''Using a while loop to iterate over a list gives you more control over the iteration process compared to a for loop, but it requires more explicit handling of the loop variable and termination condition.
'''