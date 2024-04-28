import threading
import time

counter = 0
lock = threading.RLock()

def increment():
    global counter
    for _ in range(100):
        with lock:
            counter += 1
            print(f"Thread occour by {threading.current_thread().name}")
            with lock:
                counter += 1
                print(f"Thread occour again by {threading.current_thread().name}")


t1 = threading.Thread(target=increment, name='Thread-1')
t2 = threading.Thread(target=increment, name='Thread-2')

t1.start()
t2.start()

t1.join()
t2.join()

print("total counter-", counter)

print("Main Thread Executed")