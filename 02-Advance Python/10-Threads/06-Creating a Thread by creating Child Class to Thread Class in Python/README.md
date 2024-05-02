# Creating a Thread by creating Child Class to Thread Class in Python

In Python, you can create a thread by subclassing the Thread class from the threading module and overriding its run() method. This approach allows you to define the task that the thread will perform within the run() method of your custom thread subclass. Here's how you can create a thread by subclassing Thread:

```python
import threading
import time

# Define a custom thread subclass
class CustomThread(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(f"Thread '{self.name}' is running")
        time.sleep(2)
        print(f"Thread '{self.name}' is done")

# Create an instance of the custom thread subclass
custom_thread = CustomThread(name="CustomThread")

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
- We override the __init__() method to set the name of the thread using the name parameter.
- We override the run() method to define the task that the thread will perform. In this case, the thread prints its name, sleeps for 2 seconds, and then prints a message indicating that it's done.
- We create an instance of the custom thread subclass (custom_thread) and provide a name for it.
- We start the thread using the start() method.
- The main thread continues executing while the custom thread executes its run() method concurrently.
- We use the join() method to wait for the custom thread to finish execution before the main thread exits.


Subclassing Thread allows for more flexibility and customization, especially when you need to define complex tasks or behavior for your threads. It also makes the code more readable and organized compared to using a function as the target for the thread.