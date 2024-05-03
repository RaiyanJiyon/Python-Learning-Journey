# for loop and Nested for Loop in Python

In Python, the for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It allows you to execute a block of code multiple times, once for each item in the sequence. Here's the syntax of the for loop:

```
for item in sequence:
    # Code block to execute for each item in the sequence
    statement1
    statement2
    # More statements
```

`item`: A variable that represents each item in the sequence during each iteration of the loop.

`sequence`: The sequence or iterable object over which the loop iterates.

`Indentation`: The code block within the for loop must be indented.

### Example of using a for loop to iterate over a list:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

This loop iterates over each item in the fruits list and prints it.

You can also use nested for loops to iterate over nested sequences or to perform iterations within iterations:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

This nested for loop prints pairs of values (i, j) where i ranges from 0 to 2 and j ranges from 0 to 1 for each value of i. The inner loop controls the value of j, and the outer loop controls the value of i.

Nested for loops are commonly used for tasks such as iterating over 2D arrays, generating combinations or permutations, and implementing nested data structures. They provide a way to handle more complex iteration patterns in Python.
