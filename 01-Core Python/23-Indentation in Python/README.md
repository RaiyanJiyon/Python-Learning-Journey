# Indentation in Python

In Python, indentation is crucial for indicating blocks of code and determining the structure of the program. Unlike many other programming languages that use braces {} or keywords like begin and end to denote blocks of code, Python uses indentation to define the scope of code blocks, such as those within control flow statements (e.g., if, else, for, while) and function definitions.

Here are some key points about indentation in Python:

## Indentation Levels: 
Indentation in Python typically consists of four spaces per level. This is the recommended convention, and most Python codebases and style guides adhere to it. You can use tabs instead of spaces, but mixing tabs and spaces is discouraged.

## Code Blocks: 
Code blocks in Python are defined by their indentation level. All statements within the same block must be indented to the same level.

## Consistency: 
Consistent indentation is crucial for the readability and maintainability of Python code. Inconsistent indentation can lead to syntax errors or produce unexpected behavior.

## Whitespace: 
Apart from indentation, whitespace within lines of code (e.g., spaces and tabs) is generally insignificant in Python, except within string literals. However, it's a good practice to follow a consistent style guide, such as PEP 8, which recommends using spaces for indentation.

### Example of indentation in Python:

```python
x = 10
y = 5

if x > y:
    print("X is greater")  # Indented under the if block
    print(x)
else:
    print("Y is greater") # Indented under the else block
    print(y)
```

In this example, statement1 and statement2 are part of the if block because they are indented under the if statement. Similarly, statement3 and statement4 are part of the else block because they are indented under the else statement.

Indentation is one of the distinctive features of Python and contributes to the readability and elegance of Python code.