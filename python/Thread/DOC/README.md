### Thread
Python virtual machine behind the scenes uses a thread called the main thread to execute the code.  

### check main thread  
````  
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
``` 
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
``` 
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
``` 
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
1. create multiple thread   
2. start all thread at a time.  
3. thread are executing concurrently   
``` 
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
``` 
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
in Python 
notifyAll method If multiple threads are waiting    