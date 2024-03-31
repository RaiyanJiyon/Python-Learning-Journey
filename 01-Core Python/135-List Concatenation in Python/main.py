'''
In Python, you can concatenate two or more lists using the concatenation operator + or the extend() method.

Using the + operator:

You can use the + operator to concatenate lists. When you use the + operator between two lists, it creates a new list containing all the elements from both lists in the order they appear. Here's an example:
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

'''
In this example, list1 and list2 are concatenated using the + operator, resulting in a new list concatenated_list containing all the elements from both lists.
'''

'''
Using the extend() method:

You can also use the extend() method to concatenate lists. The extend() method appends all the elements from the specified list to the end of the current list. Here's an example:
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

'''
In this example, list2 is appended to list1 using the extend() method, modifying list1 in place.

Both methods have their uses depending on the specific requirements of your program. The + operator creates a new list, while the extend() method modifies the original list in place. Choose the method that best suits your needs.
'''