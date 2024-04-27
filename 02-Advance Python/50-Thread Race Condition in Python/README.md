# Thread Race Condition in Python

A thread race condition occurs when multiple threads access shared resources or variables concurrently without proper synchronization, leading to unpredictable or incorrect behavior of the program. Race conditions can occur when threads are performing read-modify-write operations on shared data and the order of execution or timing of operations affects the final outcome.

Here's a simple example to illustrate a race condition in Python:

```python
import threading

# Shared resource
counter = 0

# Function to increment the counter
def increment():
    global counter
    for _ in range(1000000):
        counter += 1

# Create two threads to increment the counter
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print("Final value of counter:", counter)
```

In this example:

- We have a shared variable counter that multiple threads (thread1 and thread2) are incrementing concurrently.
- Each thread increments the counter variable 1,000,000 times in a loop.
- Since the counter += 1 operation is not atomic (read-modify-write), multiple threads can interfere with each other, leading to a race condition.
- The final value of the counter variable may vary depending on the timing and order of execution of the threads, resulting in an incorrect value due to the race condition.

To prevent race conditions, you can use synchronization mechanisms such as locks, semaphores, or threading primitives provided by Python's threading module. These mechanisms ensure that only one thread can access the shared resource at a time, preventing concurrent access and potential race conditions.

Here's the modified example using a lock to prevent the race condition:- 

```python
import threading

# Shared resource
counter = 0

# Lock for synchronization
lock = threading.Lock()

# Function to increment the counter
def increment():
    global counter
    for _ in range(1000000):
        with lock:
            counter += 1

# Create two threads to increment the counter
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print("Final value of counter:", counter)
```

In this modified example, we use a Lock object (lock) to synchronize access to the shared counter variable. The with lock statement ensures that only one thread can execute the critical section (increment operation) at a time, preventing race conditions and ensuring correct behavior.