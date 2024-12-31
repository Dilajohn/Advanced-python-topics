""" THREADING IN PYTHON """

""" Definition

Threading in Python allows a program to run multiple threads (smaller units of a process) concurrently,
enabling tasks to execute in parallel. It is especially useful for I/O-bound tasks, such as file operations,
    network requests, or database interactions.

Python’s threading module provides tools to create and manage threads.

***Key Concepts***

1-Thread: A thread is the smallest unit of a process that can be scheduled for execution.
2-Concurrency: Multiple threads run in overlapping time periods.
3-Global Interpreter Lock (GIL): Python's GIL ensures that only one thread executes Python bytecode at a time.
While it limits true parallelism for CPU-bound tasks, threading remains effective for I/O-bound tasks.
4-Multithreading: Refers to running multiple threads within the same process."""

""" Creating and Managing Threads
1-Using the threading.Thread Class """

import threading

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()  # Waits for the thread to complete
print("Thread finished!")

"""
. target: The function to be executed by the thread.
. start(): Starts the thread’s execution.
.join(): Blocks the main thread until the thread completes."""

""" 2-Using a Subclass """

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Thread is running: {i}")

thread = MyThread()
thread.start()
thread.join()

""" Thread Synchronization
When multiple threads access shared resources, conflicts can occur. Python provides synchronization primitives 
to avoid such issues."""

""" 1-Locks A lock prevents multiple threads from accessing a resource simultaneously."""

lock = threading.Lock()

def safe_print():
    with lock:  # Automatically acquires and releases the lock
        print("Safe access to shared resource")

thread1 = threading.Thread(target=safe_print)
thread2 = threading.Thread(target=safe_print)
thread1.start()
thread2.start()

"""
A-lock.acquire(): Acquires the lock.
B-lock.release(): Releases the lock."""

""" 2-RLocks (Reentrant Locks) Allows a thread to acquire the same lock multiple times."""

rlock = threading.RLock()

""" 3- Control access to a resource with a set limit."""

semaphore = threading.Semaphore(2)  # Allows up to 2 threads

def limited_access():
    with semaphore:
        print("Accessing a resource")

thread1 = threading.Thread(target=limited_access)
thread2 = threading.Thread(target=limited_access)
thread3 = threading.Thread(target=limited_access)
thread1.start()
thread2.start()
thread3.start()

"""Thread Communication"""
""" 1-Event Threads can communicate using threading.Event. """

event = threading.Event()

def wait_for_event():
    print("Waiting for the event...")
    event.wait()
    print("Event received!")

thread = threading.Thread(target=wait_for_event)
thread.start()

event.set()  # Signals the event

""" 2-Queue Use queue.Queue for thread-safe communication."""

import queue

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")

def consumer():
    while not q.empty():
        item = q.get()
        print(f"Consumed: {item}")

thread1 = threading.Thread(target=producer)
thread2 = threading.Thread(target=consumer)
thread1.start()
thread1.join()
thread2.start()
thread2.join()

""" ***DEAMON THREADS *** 
A daemon thread runs in the background and is terminated when the main program exits."""

def background_task():
    while True:
        print("Daemon thread running...")

thread = threading.Thread(target=background_task, daemon=True)
thread.start()

""" Thread Pooling with concurrent.futures
The ThreadPoolExecutor simplifies managing a pool of threads. """

from concurrent.futures import ThreadPoolExecutor

def task(name):
    print(f"Executing task {name}")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(task, "Task 1")
    executor.submit(task, "Task 2")
    executor.submit(task, "Task 3")

""" Performance Considerations

I/O-bound tasks: Threading improves performance by handling tasks concurrently.
CPU-bound tasks: Due to the GIL, multiprocessing is better for CPU-intensive tasks.
Avoid race conditions: Use synchronization mechanisms like locks.

Pros and Cons of Threading

Advantages

Concurrency: Improves responsiveness, especially for I/O-bound tasks.
Lightweight: Threads share the same memory space, reducing overhead.
Simplified I/O Operations: Makes handling blocking tasks more efficient.

Disadvantages

GIL Limitation: Prevents true parallelism for CPU-bound tasks.
Complexity: Debugging and managing synchronization issues can be challenging.
Overhead: Context switching between threads adds overhead.

Common Use Cases

Web Scraping: Perform concurrent requests.
GUI Applications: Keep the UI responsive during background tasks.
File I/O: Handle multiple file reads/writes simultaneously.
Networking: Manage multiple client connections.

Threading in Python provides a flexible and efficient way to manage concurrent tasks,
 making it a powerful tool for many applications 

 """