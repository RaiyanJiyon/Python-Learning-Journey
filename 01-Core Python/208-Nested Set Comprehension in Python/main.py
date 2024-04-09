'''
Nested set comprehensions in Python allow you to create sets with multiple levels of iteration and conditionals in a concise and readable manner. They follow a similar syntax to nested list comprehensions but generate sets instead. Here's the basic syntax:
'''

# {expression for outer_var in outer_sequence for inner_var in inner_sequence if condition}

'''
This syntax allows you to iterate over multiple sequences and apply conditions at each level of iteration. Here's an example to illustrate nested set comprehension:
'''

# Example 1: Creating a set of tuples where each tuple contains (x, y) pairs
coordinates = {(x, y) for x in range(3) for y in range(2)}
print(coordinates)  # Output: {(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)}

# Example 2: Creating a set of squares of numbers from nested lists
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squares = {num ** 2 for sublist in numbers for num in sublist}
print(squares)  # Output: {1, 4, 9, 16, 25, 36, 49, 64, 81}


'''
In the first example, we create a set of coordinate tuples (x, y) where x iterates over range(3) and y iterates over range(2).

In the second example, we have a nested list numbers, and we create a set of square numbers by iterating over each sublist in numbers and then over each number in the sublist.
'''

'''Nested set comprehensions can make your code more compact and expressive when dealing with complex data structures and transformations. However, it's essential to maintain readability and avoid excessive nesting, which can make the code hard to understand.
'''