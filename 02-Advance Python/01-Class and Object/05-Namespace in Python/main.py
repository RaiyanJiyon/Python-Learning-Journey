x = 10  # Global variable

def foo():
    y = 20  # Local variable
    print("Local namespace:", locals())

foo()
print("Global namespace:", globals())
