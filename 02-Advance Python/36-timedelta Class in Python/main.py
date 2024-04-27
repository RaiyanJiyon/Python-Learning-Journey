from datetime import datetime, timedelta

# Creating timedelta objects
delta1 = timedelta(days=5, seconds=3600, microseconds=500)
delta2 = timedelta(days=3)

# Accessing attributes
print("Days:", delta1.days)
print("Seconds:", delta1.seconds)
print("Microseconds:", delta1.microseconds)

# Total number of seconds
total_seconds = delta1.total_seconds()
print("Total seconds:", total_seconds)

# Arithmetic operations
now = datetime.now()
future_date = now + delta1
past_date = now - delta2
print("Future date:", future_date)
print("Past date:", past_date)
