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