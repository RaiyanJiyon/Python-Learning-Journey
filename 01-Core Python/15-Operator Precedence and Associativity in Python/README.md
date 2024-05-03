# Operator Precedence and Associativity in Python

In Python, operator precedence determines the order in which operators are evaluated in expressions with multiple operators. If an expression contains operators with different precedence levels, operators with higher precedence are evaluated first. If operators have the same precedence level, the order of evaluation depends on their associativity.

Here's a summary of operator precedence and associativity in Python:

1. `Parentheses ()`: Highest precedence. Parentheses are used to group subexpressions and override the default precedence.

2. `Exponentiation **`: Second-highest precedence. Evaluates exponentiation operations from right to left.

3. `Unary operators +, -, ~`: Next highest precedence. Unary operators are applied to their operands right to left.

4. `Multiplication *, Division /, Floor Division //, Modulus %`: These operators have the same precedence. They are evaluated from left to right.

5. `Addition +, Subtraction -`: These operators have the same precedence. They are evaluated from left to right.

6. `Bitwise Shift <<, >>`: These operators have the same precedence. They are evaluated from left to right.

7. `Bitwise AND &`: Lower precedence than Shift operators. Evaluated from left to right.

8. `Bitwise XOR ^`: Lower precedence than Bitwise AND. Evaluated from left to right.

9. `Bitwise OR |`: Lowest precedence among bitwise operators. Evaluated from left to right.

10. `Comparison Operators ==, !=, <, <=, >, >=, is, is not, in, not in`: These operators have lower precedence than bitwise operators. They are evaluated from left to right.

11. `Boolean NOT not`: Lower precedence than Comparison Operators. Unary operator applied to the operand.

12. `Boolean AND and`: Lower precedence than Boolean NOT. Evaluated from left to right. Short-circuiting occurs (second operand is evaluated only if the first operand is True).

13. `Boolean OR or`: Lowest precedence among boolean operators. Evaluated from left to right. Short-circuiting occurs (second operand is evaluated only if the first operand is False).

Understanding operator precedence and associativity is essential for writing correct and predictable expressions in Python. It helps in avoiding errors and ensures that expressions are evaluated as intended.
