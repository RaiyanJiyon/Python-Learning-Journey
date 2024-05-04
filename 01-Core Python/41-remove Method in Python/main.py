# Here's an example demonstrating the usage of the remove() method:
my_list = [1, 2, 3, 4, 3, 5]

# Remove the first occurrence of the value 3
my_list.remove(3)
print("Modified list:", my_list)  # Output: Modified list: [1, 2, 4, 3, 5]

my_list = [1, 2, 4, 5]

# Attempt to remove the value 3 (which does not exist in the list)
try:
    my_list.remove(3)
    print("Modified list:", my_list)
except ValueError:
    print("Value not found in the list")