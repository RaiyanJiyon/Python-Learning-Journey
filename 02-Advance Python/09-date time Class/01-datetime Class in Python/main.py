from datetime import datetime, timedelta

# Get current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

# Create a datetime object with specific values
specific_datetime = datetime(2022, 4, 15, 12, 30, 0)
print("Specific datetime:", specific_datetime)

# Extract date and time components
print("Year:", specific_datetime.year)
print("Month:", specific_datetime.month)
print("Day:", specific_datetime.day)
print("Hour:", specific_datetime.hour)
print("Minute:", specific_datetime.minute)
print("Second:", specific_datetime.second)

# Perform arithmetic operations
future_datetime = specific_datetime + timedelta(days=7)
print("Future datetime:", future_datetime)

# Format datetime as string
formatted_datetime = specific_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)

# Parse string to datetime
parsed_datetime = datetime.strptime("2022-04-15 12:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)
