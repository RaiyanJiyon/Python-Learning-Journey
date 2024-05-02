# Thread Communication Event in Python

In Python, thread communication can be achieved using various synchronization primitives, one of which is the Event class provided by the threading module. An Event is a simple synchronization object that allows one thread to signal an event and other threads to wait for that event to occur.

Here's how you can use the Event class for thread communication:

```python
import threading
import time

# Create an Event object
event = threading.Event()

# Define a function that waits for the event to be set
def wait_for_event():
    print("Thread waiting for event to be set")
    event.wait()  # Wait until the event is set
    print("Event has been set, continuing execution")

# Define a function that sets the event
def set_event():
    print("Setting event")
    time.sleep(3)  # Simulate some work before setting the event
    event.set()  # Set the event

# Create threads
thread1 = threading.Thread(target=wait_for_event)
thread2 = threading.Thread(target=set_event)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads have completed")
```

In this example:

1. We create an Event object named `event`.
2. The `wait_for_event()` function waits for the event to be set using the `event.wait()` method. This function will block until another thread calls `event.set()` to set the event.
3. The `set_event()` function sets the event after simulating some work using `time.sleep()`.
4. Two threads are created: one to wait for the event (`thread1`) and another to set the event (`thread2`).
5. Both threads are started, and `thread1` will wait until `thread2` sets the event.
6. After both threads have completed, the main thread prints "All threads have completed".

By using Event objects, you can coordinate the execution of multiple threads based on the occurrence of events or conditions in your program. This enables effective thread communication and synchronization in multi-threaded applications.
