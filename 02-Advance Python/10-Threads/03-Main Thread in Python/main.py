import threading

def task():
    print("Task is running.")

thread = threading.Thread(target=task)

thread.start()


