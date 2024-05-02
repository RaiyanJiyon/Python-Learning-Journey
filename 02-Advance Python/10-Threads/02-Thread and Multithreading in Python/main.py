import threading
import time

def task():
    # Simulate some work
    for _ in range(5):
        print(threading.current_thread().name, "is running")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=task, name="Thread-1")
thread2 = threading.Thread(target=task, name="Thread-2")

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("Main thread exiting")
