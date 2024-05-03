# Getting Array Input from user using while Loop in Python

```python
import array

## Create an empty array to store user input
my_array = array.array('i')  # 'i' represents the typecode for integers

# Get the number of elements in the array from the user
n = int(input("Enter the number of elements: "))

# Initialize a counter variable
count = 0

# Get input for each element using a while loop
while count < n:
    # Prompt the user to enter an integer for each element
    element = int(input("Enter element {}: ".format(count + 1)))
    # Append the input element to the array
    my_array.append(element)
    # Increment the counter
    count += 1

# Print the array
print("Array:", my_array)
```