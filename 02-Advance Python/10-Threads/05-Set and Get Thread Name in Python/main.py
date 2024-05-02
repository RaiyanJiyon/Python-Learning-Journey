import threading

def task():
    print(f"Thread '{threading.current_thread().name}' is running")

# Create a thread with a custom name
custom_thread = threading.Thread(target=task, name="CustomThread")

# Start the thread
custom_thread.start()

# Get the name of the thread
print("Thread name:", custom_thread.name)
