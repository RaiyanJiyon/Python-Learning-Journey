# Daemon Thread in Python

In Python, a daemon thread is a thread that runs in the background and is considered to be "secondary" to the main program. Daemon threads are typically used for tasks that don't need to be explicitly waited for or joined with other threads.

Here's an example of creating a daemon thread in Python:

```python
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
```

In this example:

1. We define a function `daemon_thread()` that simulates the behavior of a daemon thread. It runs in an infinite loop, printing a message every second.
2. We create a thread object `daemon` and specify the `daemon` attribute as True to mark it as a daemon thread.
3. We start the daemon thread using the `start()` method.
4. The main program continues to run after starting the daemon thread. In this case, we print messages indicating that the main program is still running for a few seconds.
5. After a short delay, the main program exits.

When the main program exits, all daemon threads are terminated automatically, regardless of whether they have completed their tasks or not. Daemon threads are useful for background tasks such as monitoring, logging, or performing periodic cleanup, where you don't need to explicitly manage their lifecycle or wait for them to finish.
