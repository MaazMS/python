# Thread

Python virtual machine behind the scenes uses a thread called the main thread to execute the code.
Definition: A thread is a single sequential flow of control within a program.

## 1. Thread Definition and Characteristics

### What is a Thread?

A thread is a lightweight sub-process that can run concurrently with other threads within the same program. It represents an independent path of execution that shares the same memory space with other threads in the process.

### Key Characteristics

- **Lightweight**: Threads require less memory and resources compared to processes
- **Shared Memory**: All threads in a process share the same memory space
- **Concurrent Execution**: Multiple threads can execute simultaneously
- **Independent Flow**: Each thread has its own program counter and stack
- **Communication**: Threads can communicate through shared variables

### Example - Basic Thread Characteristics

```python
import threading
import time

def worker_thread(name, delay):
    """Demonstrates basic thread characteristics"""
    print(f"Thread {name} starting...")
    print(f"Thread {name} ID: {threading.get_ident()}")
    print(f"Thread {name} is alive: {threading.current_thread().is_alive()}")
    
    time.sleep(delay)
    print(f"Thread {name} finished after {delay} seconds")

# Main thread information
print(f"Main thread ID: {threading.get_ident()}")
print(f"Main thread name: {threading.current_thread().name}")
print(f"Active thread count: {threading.active_count()}")

# Create and start threads
t1 = threading.Thread(target=worker_thread, args=("Worker-1", 2))
t2 = threading.Thread(target=worker_thread, args=("Worker-2", 1))

t1.start()
t2.start()

print(f"Active thread count after starting: {threading.active_count()}")
```

## 2. Thread Operations

### Creating Threads

There are multiple ways to create threads in Python:

#### Method 1: Using Function as Target

```python
import threading
import time

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(f"Number: {i}")
        time.sleep(0.5)

# Create thread
thread1 = threading.Thread(target=print_numbers, args=(1, 5))
thread1.start()
thread1.join()  # Wait for thread to complete
```

#### Method 2: Extending Thread Class

```python
import threading
import time

class NumberPrinter(threading.Thread):
    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end
    
    def run(self):
        for i in range(self.start, self.end + 1):
            print(f"Thread {self.name}: {i}")
            time.sleep(0.3)

# Create and start thread
printer = NumberPrinter(10, 15)
printer.start()
printer.join()
```

#### Method 3: Using Lambda Functions

```python
import threading

def greet(name):
    print(f"Hello, {name}!")

# Using lambda
thread = threading.Thread(target=lambda: greet("Python"))
thread.start()
thread.join()
```

### Thread Lifecycle Operations

```python
import threading
import time

def long_running_task():
    for i in range(5):
        print(f"Task running... {i}")
        time.sleep(1)

# Create thread
thread = threading.Thread(target=long_running_task)

print(f"Thread state before start: {thread.is_alive()}")
thread.start()
print(f"Thread state after start: {thread.is_alive()}")

# Wait for completion
thread.join()
print(f"Thread state after completion: {thread.is_alive()}")
```

### Daemon Threads

```python
import threading
import time

def daemon_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

def regular_task():
    for i in range(3):
        print(f"Regular thread: {i}")
        time.sleep(0.5)

# Create daemon thread
daemon = threading.Thread(target=daemon_task)
daemon.daemon = True  # Set as daemon
daemon.start()

# Create regular thread
regular = threading.Thread(target=regular_task)
regular.start()
regular.join()

print("Main thread ending...")
# Daemon thread will automatically terminate when main thread ends
```

## 3. Thread Methods

### Essential Thread Methods with Examples

#### `start()`

Starts the thread's activity by calling the `run()` method.

```python
import threading

def simple_task():
    print("Task executed!")

thread = threading.Thread(target=simple_task)
thread.start()  # Begins thread execution
```

#### `join(timeout=None)`

Waits for the thread to complete before continuing.

```python
import threading
import time

def delayed_task():
    time.sleep(2)
    print("Delayed task completed!")

thread = threading.Thread(target=delayed_task)
thread.start()

print("Waiting for thread to complete...")
thread.join()  # Main thread waits here
print("Thread completed, continuing main thread")

# With timeout
thread2 = threading.Thread(target=delayed_task)
thread2.start()
thread2.join(timeout=1)  # Wait maximum 1 second
if thread2.is_alive():
    print("Thread still running after timeout")
```

#### `is_alive()`

Returns whether the thread is currently executing.

```python
import threading
import time

def monitor_task():
    time.sleep(3)

thread = threading.Thread(target=monitor_task)
print(f"Before start: {thread.is_alive()}")  # False

thread.start()
print(f"After start: {thread.is_alive()}")   # True

time.sleep(1)
print(f"During execution: {thread.is_alive()}")  # True

thread.join()
print(f"After completion: {thread.is_alive()}")  # False
```

#### `getName()` and `setName()`

Get and set thread names.

```python
import threading

def named_task():
    current = threading.current_thread()
    print(f"Thread name: {current.getName()}")

thread = threading.Thread(target=named_task)
print(f"Default name: {thread.getName()}")

thread.setName("CustomWorker")
print(f"Custom name: {thread.getName()}")
thread.start()
thread.join()
```

#### Threading Module Functions

```python
import threading
import time

def worker():
    time.sleep(1)
    print(f"Worker thread: {threading.current_thread().name}")

# Get current thread
print(f"Current thread: {threading.current_thread().name}")

# Get main thread
print(f"Main thread: {threading.main_thread().name}")

# Count active threads
print(f"Active threads before: {threading.active_count()}")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, name=f"Worker-{i}")
    threads.append(t)
    t.start()

print(f"Active threads during: {threading.active_count()}")

# Wait for all threads
for t in threads:
    t.join()

print(f"Active threads after: {threading.active_count()}")
```

## 4. Common Errors in Thread

### Error 1: Race Conditions

**Problem**: Multiple threads accessing shared resources without proper synchronization.

```python
import threading
import time

# PROBLEMATIC CODE - Race Condition
shared_counter = 0

def increment():
    global shared_counter
    for _ in range(100000):
        shared_counter += 1  # Not thread-safe!

# This will produce inconsistent results
threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Expected: 500000, Got: {shared_counter}")  # Usually less than expected
```

**Solution**: Use locks for synchronization.

```python
import threading

shared_counter = 0
counter_lock = threading.Lock()

def safe_increment():
    global shared_counter
    for _ in range(100000):
        with counter_lock:  # Thread-safe increment
            shared_counter += 1

threads = []
for i in range(5):
    t = threading.Thread(target=safe_increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Expected: 500000, Got: {shared_counter}")  # Now consistent
```

### Error 2: Deadlocks

**Problem**: Two or more threads waiting for each other indefinitely.

```python
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_task():
    print("Thread 1: Acquiring lock1")
    lock1.acquire()
    time.sleep(1)
    
    print("Thread 1: Trying to acquire lock2")
    lock2.acquire()  # This will cause deadlock
    
    lock2.release()
    lock1.release()

def thread2_task():
    print("Thread 2: Acquiring lock2")
    lock2.acquire()
    time.sleep(1)
    
    print("Thread 2: Trying to acquire lock1")
    lock1.acquire()  # This will cause deadlock
    
    lock1.release()
    lock2.release()

# DEADLOCK SCENARIO - Don't run this!
# t1 = threading.Thread(target=thread1_task)
# t2 = threading.Thread(target=thread2_task)
# t1.start()
# t2.start()
```

**Solution**: Always acquire locks in the same order.

```python
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def safe_thread1_task():
    print("Thread 1: Acquiring locks in order")
    with lock1:
        with lock2:  # Always acquire in same order
            print("Thread 1: Got both locks")
            time.sleep(1)

def safe_thread2_task():
    print("Thread 2: Acquiring locks in order")
    with lock1:  # Same order as thread1
        with lock2:
            print("Thread 2: Got both locks")
            time.sleep(1)

t1 = threading.Thread(target=safe_thread1_task)
t2 = threading.Thread(target=safe_thread2_task)
t1.start()
t2.start()
t1.join()
t2.join()
```

### Error 3: Starting Thread Multiple Times

**Problem**: Calling `start()` on the same thread object multiple times.

```python
import threading

def simple_task():
    print("Task executed")

thread = threading.Thread(target=simple_task)
thread.start()
thread.join()

try:
    thread.start()  # ERROR: Cannot start thread twice
except RuntimeError as e:
    print(f"Error: {e}")
```

**Solution**: Create new thread objects for each execution.

```python
import threading

def simple_task():
    print("Task executed")

# Create new thread objects for multiple executions
for i in range(3):
    thread = threading.Thread(target=simple_task)
    thread.start()
    thread.join()
```

### Error 4: Forgetting to Join Threads

**Problem**: Main thread exits before child threads complete.

```python
import threading
import time

def long_task():
    time.sleep(3)
    print("Long task completed")

# PROBLEMATIC CODE
thread = threading.Thread(target=long_task)
thread.start()
# Missing join() - main thread may exit before task completes
print("Main thread ending")
```

**Solution**: Always join threads when needed.

```python
import threading
import time

def long_task():
    time.sleep(3)
    print("Long task completed")

thread = threading.Thread(target=long_task)
thread.start()
thread.join()  # Wait for completion
print("Main thread ending")
```

### Error 5: Shared Mutable State Without Protection

**Problem**: Modifying shared lists, dictionaries without synchronization.

```python
import threading

shared_list = []

def append_items(start, end):
    for i in range(start, end):
        shared_list.append(i)  # Not thread-safe for lists

# This can cause data corruption
threads = []
for i in range(5):
    t = threading.Thread(target=append_items, args=(i*10, (i+1)*10))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"List length: {len(shared_list)}")  # May be inconsistent
```

**Solution**: Use thread-safe alternatives or locks.

```python
import threading
from queue import Queue

# Using thread-safe Queue
safe_queue = Queue()
list_lock = threading.Lock()
shared_list = []

def safe_append_items(start, end):
    items = list(range(start, end))
    with list_lock:
        shared_list.extend(items)  # Thread-safe with lock

threads = []
for i in range(5):
    t = threading.Thread(target=safe_append_items, args=(i*10, (i+1)*10))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"List length: {len(shared_list)}")  # Consistent results
```

### check main thread  

````python
if threading.current_thread() == threading.main_thread():
 print("Main thread")
else:
 print("not main Thread") 
 ````  

#### Thread using a function  

step 1: from threading import Thread  
step 2: thread_object = Thread(target=function_name)
step 3: thread_object.start()

#### display Thread Names

first execute main thread
second thread name  is `Thread-1`

```python
import threading
from threading import Thread

def dispalynumber():
 i = 0
 print(threading.current_thread().getName())
 while (i<=10):
  print(i)
  i+=1
print(threading.current_thread().getName())
t = Thread(target=dispalynumber)
t.start()
```  

#### Thread extending Thread  Class  

1. override run method extend parent class
2. Thread start by calling function start eg `t.start()`

```python
from threading import Thread
class myThread(Thread):
    def run(self):
        i = 0
        while (i <= 10):
            print(i)
            i += 1
t = myThread()
t.start()
```  

#### Thread using without extending Thread Class

1. Not override run method extend parent class.
2. Thread start by calling function start eg `t.start()`

```python
from threading import *
class myThread:
    def dispalynumber(self):
        print(current_thread().getName())
        i = 0
        while (i <= 10):
            print(i)
            i += 1
obj = myThread()
t = Thread(target=obj.dispalynumber)
t.start()
```

#### Multithreading in action

1. multiple threads running at the same time and performing different tasks in a single program.
1. create multiple thread
1. start all thread at a time.  
1. thread are executing concurrently

```python
obj = myThread()
t = Thread(target=obj.dispalynumber)
t.start()

t1 = Thread(target=obj.dispalynumber)
t1.start()

t2 = Thread(target=obj.dispalynumber)
t2.start()
```

#### usecase for mulithreading  

1. book bus ticket  

```python
Example
from threading import *
import threading

class BookMyBus():
    def bus(self):
        print("\n", threading.current_thread().getName(), "\n")
        print("conforming a seat")
        print("processing the payment")
        print("printing the ticket")
obj = BookMyBus()
t1 = Thread(target=obj.bus)
t2 = Thread(target=obj.bus)
t3 = Thread(target=obj.bus)
t1.start()
t2.start()
t3.start()
```

#### Thread Synchronization

1. When multiple threads are accessing the same resources is called Synchronization.
2. lock an object, when a thread locks an object it enters into a room of its own. It will take that object and it will
own that object and only when that thread releases that object the other threads can use that object or resource.
3. This process of thread acquiring a lock and entering a room is also known as threat `mutex`.

#### first way  of synchronization

step1 : first we need to create a lock object and invoke l.acquire So the thread will acquire a lock on the current object.
Once it acquires the lock, until it invokes the release method no other thread can process or use the current object.  
step 2: `acquire()` it is use to acquire the lock.
step 3 : `relase()` release lock of thread.

#### second way  of synchronization

step 1 : use semaphore acquiring a lock but internally it uses a counter.
step 2: `acquire()` it is use to acquire the semaphore.
step 3 : `relase()` release semaphore of thread.

#### Thread Communication using wait, notifyall and notify

1. `wait(), notify() and notifyAll()`. So these methods are available on a class called Condition from the multi-threading API.
2. `condition()` is a class available from the threading module which we are going to use to communicate between threads conditionally.
in Python notifyAll method If multiple threads are waiting
