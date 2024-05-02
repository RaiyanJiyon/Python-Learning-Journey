import threading

# Create a Semaphore with a maximum value of 2
semaphore = threading.Semaphore(2)

# Define a function that simulates accessing a shared resource
def access_resource(thread_id):
    print(f"Thread {thread_id} is trying to access the resource")
    with semaphore:
        print(f"Thread {thread_id} has acquired the resource")
        # Simulate performing some work
        print(f"Thread {thread_id} is performing some work")
        # Simulate releasing the resource
        print(f"Thread {thread_id} has released the resource")

# Create multiple threads to access the shared resource
threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
