# if Statement with Logical Operator in Python

In Python, you can use logical operators (and, or, not) within if statements to combine multiple conditions and create more complex conditional expressions. Logical operators allow you to perform logical operations on boolean values and evaluate whether multiple conditions are true or false. Here's how you can use logical operators in if statements:

```
if condition1 and condition2:
    # Code block to execute if both condition1 and condition2 are True
    statement1
    statement2
    # More statements
elif condition3 or condition4:
    # Code block to execute if either condition3 or condition4 is True
    statement3
    statement4
    # More statements
else:
    # Code block to execute if none of the conditions are met
    statement5
    statement6
    # More statements
```

### Example of using logical operators in if statements:

```python
x = 10
y = 5

if x > 0 and y > 0:
    print("Both x and y are positive")

if x % 2 == 0 or y % 2 == 0:
    print("At least one of x or y is even")

if not (x == y):
    print("x and y are not equal")
```

In this example:

- The first if statement checks if both x and y are positive.
- The second if statement checks if either x or y is even.
- The third if statement uses the not operator to check if x and y are not equal.