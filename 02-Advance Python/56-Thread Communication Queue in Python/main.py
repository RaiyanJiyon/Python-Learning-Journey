import threading
import queue
import time

# Define a producer function that adds items to the queue
def producer(queue):
    for i in range(5):
        print(f"Producing item {i}")
        queue.put(i)  # Add item to the queue
        time.sleep(1)

# Define a consumer function that consumes items from the queue
def consumer(queue):
    while True:
        item = queue.get()  # Get item from the queue
        if item is None:  # Check for termination signal
            break
        print(f"Consuming item {item}")
        time.sleep(1)

# Create a queue object
q = queue.Queue()

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for producer to finish producing items
producer_thread.join()

# Add a termination signal to the queue to indicate to the consumer that there are no more items
q.put(None)

# Wait for consumer to finish consuming items
consumer_thread.join()

print("All threads have completed")
