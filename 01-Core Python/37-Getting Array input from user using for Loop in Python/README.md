# Getting Array input from user using for Loop in Python

To get array input from the user using a for loop in Python, you can prompt the user to enter each element of the array iteratively within the loop. You can use the append() method to add each input element to the array. Here's how you can do it:

```python
import array
```

## Create an empty array to store user input

```python
my_array = array.array('i')  # 'i' represents the typecode for integers
```

## Get the number of elements in the array from the user

```python
n = int(input("Enter the number of elements: "))
```

## Iterate n times to get input for each element

```python
for i in range(n):
    # Prompt the user to enter an integer for each element
    element = int(input("Enter element {}: ".format(i + 1)))
    # Append the input element to the array
    my_array.append(element)

# Print the array
print("Array:", my_array)
```

In this example:

- We first import the array module.
- We create an empty array named my_array to store user input.
- We prompt the user to enter the number of elements (n) they want to input into the array.
- We use a for loop to iterate n times, where each iteration prompts the user to enter an integer for each element of the array.
- Within the loop, we convert the user input to an integer using int(`input()`), and then use the `append()` method to add the input element to the array.
- Finally, we print the array to display the elements entered by the user.

This approach allows the user to input elements into the array interactively, and the array is populated dynamically as the user provides input.