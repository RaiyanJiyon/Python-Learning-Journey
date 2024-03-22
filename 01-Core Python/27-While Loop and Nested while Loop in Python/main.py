'''
In Python, the while loop is used to repeatedly execute a block of code as long as a condition remains true. The loop continues iterating until the condition becomes false. Here's the syntax of the while loop:
'''

'''
while condition:
    # Code block to execute while the condition is true
    statement1
    statement2
    # More statements
'''

'''
condition: An expression that evaluates to either True or False. The loop continues as long as this condition is true.
Indentation: The code block within the while loop must be indented.
'''

# Example of a while loop:
x = 0

while x < 5:
    print(x)
    x += 1

'''
This loop prints the values of x from 0 to 4 because the loop continues as long as x is less than 5.

You can also use the break statement to exit the loop prematurely if a certain condition is met, or the continue statement to skip the rest of the loop's code block and continue with the next iteration.
'''

# Example of nested while loops:
x = 0

while x < 3:
    y = 0
    while y < 3:
        print(x, y)
        y += 1
    x += 1

'''This nested while loop prints pairs of values (x, y) where x ranges from 0 to 2 and y ranges from 0 to 2 for each value of x. The outer loop controls the value of x, and the inner loop controls the value of y. The inner loop is executed fully for each iteration of the outer loop.'''