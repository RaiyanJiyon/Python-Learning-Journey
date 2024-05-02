import threading
import time

# Define a function for the daemon thread
def daemon_thread():
    while True:
        print("Daemon thread is running")
        time.sleep(1)

# Create a daemon thread
daemon = threading.Thread(target=daemon_thread)
daemon.daemon = True  # Set the thread as a daemon thread

# Start the daemon thread
daemon.start()

# Main program continues running
print("Main program is still running")
time.sleep(3)
print("Main program is exiting")
