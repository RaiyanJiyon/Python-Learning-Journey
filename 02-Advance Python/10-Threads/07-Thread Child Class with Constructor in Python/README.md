# Thread Child Class with Constructor in Python

To create a thread subclass with a constructor in Python, you can override the __init__() method of the Thread class and provide additional parameters to initialize the thread. Here's how you can create a thread subclass with a constructor:

```python
import threading
import time

# Define a custom thread subclass with a constructor
class CustomThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__(name=name)
        self.delay = delay

    def run(self):
        print(f"Thread '{self.name}' is running with delay {self.delay} seconds")
        time.sleep(self.delay)
        print(f"Thread '{self.name}' is done")

# Create an instance of the custom thread subclass
custom_thread = CustomThread(name="CustomThread", delay=2)

# Start the thread
custom_thread.start()

# Main thread continues executing
print("Main thread is running")

# Wait for the thread to finish
custom_thread.join()

print("Main thread exiting")
```

In this example:

- We define a custom thread subclass CustomThread that inherits from threading.Thread.
- We override the __init__() method to accept additional parameters (name and delay) for initializing the thread. We also call the superclass's __init__() method to initialize the thread with the specified name.
- We store the delay parameter as an instance variable (self.delay) to be used in the run() method.
- We override the run() method to define the task that the thread will perform. In this case, the thread prints its name and the delay, sleeps for the specified delay, and then prints a message indicating that it's done.
- We create an instance of the custom thread subclass (custom_thread) and provide a name and delay for it.
- We start the thread using the start() method.
The main thread continues executing while the custom thread executes its run() method concurrently.
- We use the join() method to wait for the custom thread to finish execution before the main thread exits.

This approach allows you to create thread subclasses with constructors to initialize thread-specific parameters or configuration. It provides flexibility and allows for better organization of code when working with complex thread tasks.