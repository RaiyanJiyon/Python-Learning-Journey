my_dict = {'name': 'John', 'age': 30}
extra_info = {'city': 'New York', 'job': 'Engineer'}

# Update my_dict with elements from extra_info
my_dict.update(extra_info)

print(my_dict)


'''Updating with an Iterable of Key-Value Pairs:'''

my_dict = {'name': 'John', 'age': 30}

# Update my_dict with key-value pairs from a list of tuples
new_info = [('city', 'New York'), ('job', 'Engineer')]
my_dict.update(new_info)

print(my_dict)