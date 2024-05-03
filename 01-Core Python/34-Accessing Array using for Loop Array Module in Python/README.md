# Accessing Array using for Loop Array Module in Python

To access elements of an array created using the array module in Python, you can use a for loop or indexing just like you would with a list. Here's how you can access the elements of an array using a for loop

```python
import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Access elements of the array using a for loop
for element in my_array:
    print(element)
```

In this example, 

we iterate over each element in the array my_array using a for loop and print each element.

You can also access elements of the array using indexing

# Accessing elements of the array using indexing:

```python
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3
```

This will print the first and third elements of the array my_array, respectively.

The array module in Python provides a way to create arrays with elements of a single data type. Once created, you can access elements of the array using a for loop, indexing, or other common methods provided by the array module, such as `append()`, `insert()`, `remove()`, and more.
