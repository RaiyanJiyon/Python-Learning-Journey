# Formating Date and Time in Python

In Python, you can format dates and times using the `strftime()` method (string format time) provided by the datetime module. This method allows you to specify a format string to represent a date or time object as a string in a customized format. The format string contains format codes that represent various components of the date and time.

Here are some commonly used format codes for formatting dates and times:

- `%Y`: Year with century as a decimal number (e.g., 2022).
- `%m`: Month as a zero-padded decimal number (e.g., 04 for April).
- `%d`: Day of the month as a zero-padded decimal number (e.g., 15).
- `%H`: Hour (24-hour clock) as a zero-padded decimal number (e.g., 13 for 1 PM).
- `%M`: Minute as a zero-padded decimal number (e.g., 05).
- `%S`: Second as a zero-padded decimal number (e.g., 30).
- `%A`: Weekday as a full name (e.g., Monday).
- `%B`: Month as a full name (e.g., April).
- `%c`: Locale's appropriate date and time representation (e.g., "Thu Apr 15 13:05:30 2022" in the C locale).
- `%x`: Locale's appropriate date representation (e.g., "04/15/22" in the US locale).
- `%X`: Locale's appropriate time representation (e.g., "13:05:30" in the US locale).

Here's an example demonstrating how to format dates and times using the `strftime()` method:

```python
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
```

This will output something like:

```
Formatted date: 2022-04-15
Formatted time: 13:05:30
Formatted date and time: 2022-04-15 13:05:30
Weekday: Friday
Month: April
```

In this example, %Y, %m, %d, %H, %M, and %S are format codes representing the year, month, day, hour, minute, and second components of the date and time, respectively. Similarly, %A and %B represent the weekday and month names. You can customize the format string according to your requirements to represent the date and time in various formats.