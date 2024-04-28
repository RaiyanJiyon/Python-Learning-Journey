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
