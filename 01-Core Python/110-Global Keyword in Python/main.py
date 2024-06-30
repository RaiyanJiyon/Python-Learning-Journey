# Here's a basic example of using the global keyword:
global_var = 10

def modify_global():
    global global_var
    global_var = 20

print("Before function call:", global_var)
modify_global()
print("After function call:", global_var)