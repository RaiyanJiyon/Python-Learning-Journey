# Prompt the user to enter key-value pairs separated by commas
user_input = input("Enter key-value pairs separated by comma (key1:value1, key2:value2, ...): ")

# Split the input string into a list of key-value pairs
pairs = user_input.split(',')

# Initialize an empty dictionary to store the key-value pairs
user_dict = {}

# Iterate over each key-value pair in the list
for pair in pairs:
    # Split each pair into key and value using colon (:) as the delimiter
    key, value = pair.split(':')
    
    # Remove leading and trailing whitespace from key and value
    cleaned_key = key.strip()
    cleaned_value = value.strip()
    
    # Add the cleaned key-value pair to the user_dict dictionary
    user_dict[cleaned_key] = cleaned_value

# Print the resulting dictionary containing the user's input
print("User Dictionary: ", user_dict)
