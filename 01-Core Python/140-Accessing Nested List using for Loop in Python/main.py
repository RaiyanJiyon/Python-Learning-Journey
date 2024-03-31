'''
You can access elements of a nested list using a nested loop, typically with a for loop. The outer loop iterates over the outer list, and the inner loop iterates over each inner list. Here's how you can access elements of a nested list using a for loop:
'''

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements using a nested loop
for inner_list in nested_list:
    for element in inner_list:
        print(element, end=" ")
    print()  # Print newline after each inner list

'''
In this example:

The outer loop iterates over each inner list in nested_list.
The inner loop iterates over each element in the current inner list.
The print() function is used to print each element on the same line, followed by a space.
After printing all elements of an inner list, a newline is printed to move to the next line for the next inner list.
'''

'''This loop structure allows you to access and process each element of the nested list individually. You can perform any desired operations on the elements within the loop, such as computation, manipulation, or printing.
'''