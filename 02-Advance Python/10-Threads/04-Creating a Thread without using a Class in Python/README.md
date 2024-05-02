# Creating a Thread without using a Class in Python

In Python, you can create a thread without using a class by passing a target function to the Thread constructor. This allows you to define the task that the thread will perform directly as a function, rather than as a method of a class. Here's a basic example demonstrating how to create a thread without using a class:

```python
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
```

In this example:

- We define a task() function that simulates some work by printing messages and sleeping for 2 seconds.
- We create a thread (thread) by passing the task function as the target parameter to the Thread constructor.
- We start the thread using the start() method.
The main thread continues executing while the new thread executes the task() function concurrently.
- We use the join() method to wait for the thread to finish execution before the main thread exits.

This approach allows you to create and start a thread with minimal setup and is useful for simple tasks or quick experiments. However, for more complex scenarios or when you need to share data between threads, using a class-based approach with thread subclassing or the target parameter is often preferable.