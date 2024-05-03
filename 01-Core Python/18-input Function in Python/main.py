# Example of using the input() function:
name = input("Enter your name: ")
print("Hello,", name)

'''
In this example, the input() function displays the prompt "Enter your name: ", waits for the user to input their name, and then stores the input in the variable name. The print() function then displays a greeting message using the user's input.

It's important to note that the input() function always returns a string, even if the user enters a number or other type of data. If you want to convert the input to a different data type (e.g., integer or float), you need to explicitly perform type conversion using functions like int() or float().
'''

# Example of converting input to an integer:
age = int(input("Enter your age: "))