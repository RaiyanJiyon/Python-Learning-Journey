# Nested if else Statement in Python

In Python, you can nest if-else statements within other if-else statements to handle more complex conditional logic. Nested if-else statements allow you to test multiple conditions in a hierarchical manner, where the execution of one block of code depends on the evaluation of previous conditions. Here's the syntax of nested if-else statements:

```
if condition1:
    # Code block to execute if condition1 is True
    statement1
    statement2
    # More statements
    if condition2:
        # Code block to execute if both condition1 and condition2 are True
        statement3
        statement4
        # More statements
    else:
        # Code block to execute if condition1 is True but condition2 is False
        statement5
        statement6
        # More statements
else:
    # Code block to execute if condition1 is False
    statement7
    statement8
    # More statements
```

In nested if-else statements, the inner if-else blocks are indented further than the outer if-else blocks, indicating their nested structure.

### Example of nested if-else statements:

```python
x = 10

if x > 0:
    print("x is positive")
    
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
        
else:
    print("x is non-positive")
```

In this example:

- The outer if statement checks if x is positive.
- If x is positive, the program proceeds to the nested if-else block, where it checks if x is even or odd.
- Depending on the value of x, it prints corresponding messages.
- If x is non-positive, it executes the code block under the else statement.