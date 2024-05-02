import time

# Get current time
current_time = time.time()
print("Current time:", current_time)

# Sleep for 2 seconds
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Woke up!")

# Convert timestamp to a string
formatted_time = time.ctime(current_time)
print("Formatted time:", formatted_time)

# Convert timestamp to struct_time objects
utc_time = time.gmtime(current_time)
local_time = time.localtime(current_time)
print("UTC time:", utc_time)
print("Local time:", local_time)

# Format time
formatted_utc_time = time.strftime("%Y-%m-%d %H:%M:%S", utc_time)
formatted_local_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted UTC time:", formatted_utc_time)
print("Formatted local time:", formatted_local_time)
