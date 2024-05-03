# append Method in Python

In Python, the `append()` method is used to add an element to the end of a list. This method modifies the original list in place. The syntax for using the `append()` method is:

```
list_name.append(element)
```

`list_name`: The name of the list to which you want to add an element.

`element`: The element you want to append to the list.

## Here's an example demonstrating the usage of the append() method:

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

In this example:

- We have a list named my_list containing [1, 2, 3].
- We use the `append()` method to add the integer 4 to the end of the list.
- After appending 4, the list becomes [1, 2, 3, 4].
- The `append()` method is commonly used when you want to dynamically add elements to a list as your program runs. 

It is efficient for adding elements to the end of the list, but keep in mind that it only adds one element at a time. If you want to add multiple elements to a list at once, you can use methods like `extend()` or `list concatenation`

