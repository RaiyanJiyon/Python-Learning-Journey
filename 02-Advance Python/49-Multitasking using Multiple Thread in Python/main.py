import threading
import time

# Define a task function for the first thread
def task1():
    for i in range(5):
        print("Task 1 is running")
        time.sleep(1)

# Define a task function for the second thread
def task2():
    for i in range(5):
        print("Task 2 is running")
        time.sleep(1)

# Create two threads, one for each task
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start both threads
thread1.start()
thread2.start()

# Main thread continues executing
print("Main thread is running")

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread exiting")
