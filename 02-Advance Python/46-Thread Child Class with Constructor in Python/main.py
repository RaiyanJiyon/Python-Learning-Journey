import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__(name=name)
        self.delay = delay

    def run(self):
        print(f"Thread {self.name} is running with {self.delay} time late")
        time.sleep(self.delay)
        print(f"Thread {self.name} is finished.")


t = myThread(name="Custom Thread", delay=2)
t.start()

print("Main thread is running")

t.join()

print("Main thread finished.")
