import threading
import time

# Define the target function for the thread
def task(name, delay):
    print(f"Thread '{name}' is running with delay {delay} seconds")
    time.sleep(delay)
    print(f"Thread '{name}' is done")

# Create a thread and pass the target function
custom_thread = threading.Thread(target=task, args=("CustomThread", 2))

# Start the thread
custom_thread.start()

# Main thread continues executing
print("Main thread is running")

# Wait for the thread to finish
custom_thread.join()

print("Main thread exiting")
