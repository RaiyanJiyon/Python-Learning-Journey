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
