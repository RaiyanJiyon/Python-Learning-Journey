# Thread Communication Condition in Python

In Python, thread communication can also be achieved using Condition objects provided by the threading module. Condition objects allow multiple threads to wait for a condition to be true and to notify other threads when the condition becomes true.

Here's how you can use Condition for thread communication:

```python
import threading
import time

# Create a Condition object
condition = threading.Condition()

# Shared resource
shared_resource = []

# Producer function that adds items to the shared resource
def producer():
    for i in range(5):
        with condition:
            shared_resource.append(i)
            print(f"Produced item {i}")
            condition.notify()  # Notify waiting threads
            time.sleep(1)

# Consumer function that consumes items from the shared resource
def consumer():
    for i in range(5):
        with condition:
            while not shared_resource:
                condition.wait()  # Wait until the condition is notified
            item = shared_resource.pop(0)
            print(f"Consumed item {item}")
            time.sleep(1)

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to complete
producer_thread.join()
consumer_thread.join()

print("All threads have completed")
```

In this example:

1. We create a Condition object named `condition`.
2. We define a shared resource, `shared_resource`, which will be accessed by the producer and consumer threads.
3. The `producer()` function adds items to the `shared_resource` list and notifies waiting threads using `condition.notify()` after adding each item.
4. The `consumer()` function consumes items from the `shared_resource` list. If the list is empty, the consumer waits using `condition.wait()` until the producer notifies the condition.
5. Two threads, one for the producer and one for the consumer, are created and started.
6. After both threads have completed, the main thread prints "All threads have completed".

Using Condition objects, you can synchronize the execution of multiple threads based on specific conditions or events in your program, facilitating effective thread communication and coordination.
