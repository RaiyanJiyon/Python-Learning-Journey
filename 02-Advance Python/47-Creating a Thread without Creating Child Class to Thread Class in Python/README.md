# Creating a Thread without Creating Child Class to Thread Class in Python

You can create a thread in Python without creating a child class of the Thread class by passing a target function to the Thread constructor. This target function represents the task that the thread will perform. Here's how you can create a thread without subclassing the Thread class:

```python
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
```

In this example:

- We define a task() function that represents the task that the thread will perform. This function takes two parameters: name (the name of the thread) and delay (the delay in seconds).
- We create a thread (custom_thread) using the Thread constructor and provide the task function as the target. We also pass arguments to the task function using the args parameter.
- We start the thread using the start() method.
The main thread continues executing while the custom thread executes the task() function concurrently.
- We use the join() method to wait for the custom thread to finish execution before the main thread exits.

This approach is suitable for simple tasks or quick experiments where creating a thread subclass may be unnecessary. It allows you to define the task directly as a function and pass it to the thread constructor.