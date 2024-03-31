'''
Slicing in Python is a powerful technique used to extract a portion of elements from a sequence such as a list. It allows you to create a new list by specifying a range of indices to extract elements from the original list. The basic syntax for slicing a list is as follows:
'''

# new_list = list_name[start:stop:step]
'''
Where:

list_name is the name of the list you want to slice.
start is the index where the slice starts (inclusive). If omitted, it defaults to 0.
stop is the index where the slice stops (exclusive). If omitted, it defaults to the length of the list.
step is the step size or interval between elements. If omitted, it defaults to 1.
'''

# Here are some examples of slicing on a list:
# Define a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract elements from index 2 to 5 (exclusive)
slice_1 = my_list[2:5]
print(slice_1)  # Output: [3, 4, 5]

# Extract elements from index 0 to 7 with step size of 2
slice_2 = my_list[0:7:2]
print(slice_2)  # Output: [1, 3, 5, 7]

# Extract elements from index 3 to the end of the list
slice_3 = my_list[3:]
print(slice_3)  # Output: [4, 5, 6, 7, 8, 9]

# Extract elements from the beginning to index 5 (exclusive)
slice_4 = my_list[:5]
print(slice_4)  # Output: [1, 2, 3, 4, 5]

# Extract every second element from index 1 to 7 (exclusive)
slice_5 = my_list[1:7:2]
print(slice_5)  # Output: [2, 4, 6]

'''
In these examples:

We have a list called my_list containing integers from 1 to 9.
We use slicing to extract specific portions of the list based on the specified start, stop, and step indices.
The resulting slices are stored in new lists (slice_1, slice_2, etc.) containing the extracted elements.
'''

'''Slicing provides a flexible way to manipulate lists and extract subsets of data based on your specific requirements.
'''