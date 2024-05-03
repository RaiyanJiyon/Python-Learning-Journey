# Example of using logical operators in if statements:
x = 10
y = 5

if x > 0 and y > 0:
    print("Both x and y are positive")

if x % 2 == 0 or y % 2 == 0:
    print("At least one of x or y is even")

if not (x == y):
    print("x and y are not equal")