# Define a function that takes a dictionary as an argument
def process_dictionary(input_dict):
    for key, value in input_dict.items():
        print(key + ":", value)

# Create a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Call the function and pass the dictionary as an argument
process_dictionary(my_dict)