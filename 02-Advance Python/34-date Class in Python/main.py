from datetime import date

# Creating a date object
my_date = date(2024, 4, 15)
print("Date:", my_date)

# Accessing attributes
print("Year:", my_date.year)
print("Month:", my_date.month)
print("Day:", my_date.day)

# Today's date
today_date = date.today()
print("Today's date:", today_date)

# Day of the week (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
print("Day of the week:", today_date.weekday())

# Formatting date
formatted_date = today_date.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)

# Replace year, month, and day
new_date = today_date.replace(year=2025)
print("New date:", new_date)

# Convert date to time.struct_time
time_tuple = today_date.timetuple()
print("Time tuple:", time_tuple)
