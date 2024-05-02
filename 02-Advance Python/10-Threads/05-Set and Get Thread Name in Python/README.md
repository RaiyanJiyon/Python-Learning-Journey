# Set and Get Thread Name in Python

In Python's threading module, you can set and get the name of a thread using the name attribute. When you create a thread, you can optionally specify a name for it. If you don't provide a name, Python assigns a default name.

Here's how you can set and get the name of a thread:

```python
import threading

def task():
    print(f"Thread '{threading.current_thread().name}' is running")

# Create a thread with a custom name
custom_thread = threading.Thread(target=task, name="CustomThread")

# Start the thread
custom_thread.start()

# Get the name of the thread
print("Thread name:", custom_thread.name)
```

In this example:

- We define a task() function that prints the name of the current thread.
- We create a thread (custom_thread) using the Thread constructor and provide a custom name "CustomThread".
- We start the thread using the start() method.
- We get the name of the thread using the name attribute and print it.

Alternatively, if you want to set the name of the current thread (usually the main thread), you can use the threading.current_thread().name attribute directly. However, note that attempting to set the name of the current thread using threading.current_thread().name = "NewName" is not supported and will raise an AttributeError.

```python
import threading

# Get the name of the current thread (usually the main thread)
print("Current thread name:", threading.current_thread().name)
```

The ability to set and get the name of a thread is useful for identifying and debugging threads in multi-threaded programs. It allows you to give meaningful names to threads and easily identify them when analyzing logs or debugging issues.