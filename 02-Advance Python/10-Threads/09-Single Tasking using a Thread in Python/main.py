import threading
import time

# Define the task function
def single_task():
    print("Single task is running")
    time.sleep(2)  # Simulate some work
    print("Single task is done")

# Create a thread for the single task
task_thread = threading.Thread(target=single_task)

# Start the thread
task_thread.start()

# Main thread continues executing
print("Main thread is running")

# Wait for the thread to finish
task_thread.join()

print("Main thread exiting")
