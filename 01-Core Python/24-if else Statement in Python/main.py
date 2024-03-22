'''
In Python, the if-else statement is used to perform conditional execution. It allows you to execute one block of code if a condition is true, and another block of code if the condition is false. Here's the syntax of the if-else statement:
'''

'''
if condition:
    # Code block to execute if the condition is true
    statement1
    statement2
    # More statements
else:
    # Code block to execute if the condition is false
    statement3
    statement4
    # More statements
'''

'''
condition: An expression that evaluates to either True or False.
Indentation: The code block following the if statement and the code block following the else statement must be indented to the same level.
'''

# Example of using the if-else statement:
x = 5

if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

'''In this example, if the value of x is greater than 0, the code block under the if statement is executed, and "x is positive" is printed. If the condition is false (i.e., x is not greater than 0), the code block under the else statement is executed, and "x is non-positive" is printed.'''