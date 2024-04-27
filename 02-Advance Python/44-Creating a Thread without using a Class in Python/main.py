import threading
import time

def task():
    print("Thread is running")
    time.sleep(2)
    print("Thread is done")

# Create a thread
thread = threading.Thread(target=task)

# Start the thread
thread.start()

# Main thread continues executing
print("Main thread is running")

# Wait for the thread to finish
thread.join()

print("Main thread exiting")
