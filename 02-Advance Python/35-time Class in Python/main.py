from datetime import time

# Creating a time object
my_time = time(10, 30, 15)
print("Time:", my_time)

# Accessing attributes
print("Hour:", my_time.hour)
print("Minute:", my_time.minute)
print("Second:", my_time.second)
print("Microsecond:", my_time.microsecond)

# Formatting time
formatted_time = my_time.strftime("%H:%M:%S")
print("Formatted time:", formatted_time)

# Replace hour, minute, second, and microsecond
new_time = my_time.replace(hour=12, minute=0, second=0, microsecond=0)
print("New time:", new_time)
