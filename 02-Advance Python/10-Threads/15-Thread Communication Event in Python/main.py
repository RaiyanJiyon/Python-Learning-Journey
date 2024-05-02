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
