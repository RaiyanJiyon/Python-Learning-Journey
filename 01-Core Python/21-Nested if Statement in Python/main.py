'''
In Python, you can nest if statements within other if statements to handle more complex conditional logic. Nested if statements allow you to test multiple conditions within each other, providing a way to create hierarchical decision-making structures. Here's the syntax of nested if statements:
'''

'''
if condition1:
    # Code block to execute if condition1 is True
    if condition2:
        # Code block to execute if both condition1 and condition2 are True
        statement1
        statement2
        # More statements
    else:
        # Code block to execute if condition1 is True but condition2 is False
        statement3
        statement4
        # More statements
else:
    # Code block to execute if condition1 is False
    statement5
    statement6
    # More statements
'''

'''
You can nest if statements to multiple levels to handle more complex scenarios. However, be cautious about excessive nesting, as it can lead to code that is difficult to read and maintain.
'''

# Example of nested if statements:
x = 10

if x > 0:
    print("x is positive")
    
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
        
else:
    print("x is non-positive")

'''In this example, if x is positive, the program checks whether x is even or odd within the nested if statement. Depending on the value of x, it prints corresponding messages. If x is non-positive, it prints a different message.'''