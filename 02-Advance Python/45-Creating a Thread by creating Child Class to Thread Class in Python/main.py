import threading
import time

# Define a custom thread subclass
class CustomThread(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(f"Thread '{self.name}' is running")
        time.sleep(2)
        print(f"Thread '{self.name}' is done")

# Create an instance of the custom thread subclass
custom_thread = CustomThread(name="CustomThread")

# Start the thread
custom_thread.start()

# Main thread continues executing
print("Main thread is running")

# Wait for the thread to finish
custom_thread.join()

print("Main thread exiting")
