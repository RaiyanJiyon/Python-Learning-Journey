from datetime import datetime

# Current date and time
now = datetime.now()

# Format date and time
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
weekday = now.strftime("%A")
month = now.strftime("%B")

print("Formatted date:", formatted_date)
print("Formatted time:", formatted_time)
print("Formatted date and time:", formatted_datetime)
print("Weekday:", weekday)
print("Month:", month)
