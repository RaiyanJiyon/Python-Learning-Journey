# Memebership Operator in Python

Membership operators in Python are used to test whether a value or variable is found in a sequence (such as `strings`, `lists`, `tuples`, or `dictionaries`). These operators return Boolean values `(True or False)` based on the membership relationship. Here are the membership operators in Python along with examples of their usage:

## in: 
Evaluates to True if the value or variable is found in the sequence.

```python
my_list = [1, 2, 3, 4, 5]
result = 3 in my_list
print(result)  # result will be True
```

## Not in: 
Evaluates to True if the value or variable is not found in the sequence.

```python
my_string = "hello"
result = "a" not in my_string  
print(result)  # result will be True
```

Membership operators are commonly used in conditional statements `(if, elif, else)` and `loops` to check for the presence or absence of elements in a sequence. They provide a convenient way to test for membership without needing to manually iterate over the sequence. Understanding and using membership operators can make your code more concise and readable.

