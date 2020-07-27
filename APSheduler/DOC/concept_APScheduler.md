# Basic concepts       
APScheduler has four kinds of components       
  
* triggers  

* job stores  

* executors  
 
* schedulers        
 
  
#### Triggers
1 . Triggers contain the scheduling logic.   
2. Each job has its own trigger which determines when the job should be run next.       
3 .Beyond their initial configuration, triggers are completely stateless.  
4. A trigger instructs the scheduler when is the next time a job should run.           

for example    
`def tick(parameter): print(parameter)`

`scheduler.add_job(`
 `   function,`
    `args=(1, ),`
  `  trigger='interval',`
    `seconds=3 `
`)`

In the above example interval is the trigger.    
if the job fires at "2000-01-01T00:00:00Z", then the trigger with 3 seconds as interval should report that the next time is "2000-01-01T00:00:03Z"   

    
#### Job stores   
1. Job stores don’t keep the job data in memory, but act as middlemen for saving, loading, updating and searching jobs   
in the backend.    
2. A job’s data is serialized when it is saved to a persistent job store, and deserialized when it’s loaded back from it.      
3. Job stores must never be shared between schedulers         
4. If job is not stores in the database job states will be lost when the process restarts.      
In below example, APScheduler adds a JobStore named sqlalchemy. The job added later chooses sqlalchemy as its JobStore.    
The JobStore persists the job into an SQLite database.   
`scheduler.add_jobstore('sqlalchemy', url='sqlite:////sched.db')`    
`scheduler.add_job(function, args=(1, ), trigger='interval', seconds=3, jobstore='sqlalchemy')`  
      
      
#### Executors   
1. Executors are what handle the running of the jobs.      
2. They do this typically by submitting the job to a thread or process pool.   
3. When the job is done, the executor notifies the scheduler.     

#### Schedulers   
1. You typically have only one scheduler running in your application.    
2. The application developer doesn’t normally deal with the job stores, executors or triggers directly.   
3. scheduler provides the proper interface for adding, modifying and removing jobs.
    
#### Trigger by data    
It  is use when you want to run the job just once at a certain point of time.   
The run_date can be given either as a date/datetime object or text (in the ISO 8601 format). 
[example](https://github.com/MaazMS/python/tree/master/APSheduler/trigger_data)     

     
Q1. what is BlockingScheduler.? 
1. A scheduler that runs in the foreground/front.   
2. so when you call start() , the call never returns.    
3. BlockingScheduler can be useful if you want to use APScheduler as a standalone scheduler (e.g. to build a daemon)     
     
Q2. what is BackgroundScheduler.?     
1. A scheduler that runs in the background using a separate thread.        
2. BackgroundScheduler runs in a thread inside your existing application.   
3.  Calling start() will start the scheduler and it will continue running after the call returns  
  
  
Q3. what is AsyncIOScheduler.?    
AsyncIOScheduler was meant to be used with the AsyncIO event loop.By default, it will run jobs in the event loop’s      
thread pool.  
The asyncio module provides tools for building concurrent applications using coroutines.   
 

Q4. what is coroutine.? 
A function  which can pause and resume its execution. that means `A` function  is start execution it call B function.   
`B` function is executing it call the function `c` . Then c function is executing and complete and call function `b` .    
function `b` is executing and complete and call function `A` .function `A` is executing and complete.    

Q.5 why need MemoryJobStore
If you always recreate your jobs at the start of your application, then you can probably go with default MemoryJobStore.   

Q6. how a job persistence.
If you need your jobs to persist over scheduler restarts or application crashes, then your choice SQLAlchemyJobStore.    
(Stores jobs in a database table using SQLAlchemy. The table will be created if it doesn’t exist in the database.)        

Q7. what is ThreadPoolExecutor.   
The ThreadPoolExecutor manages a set of worker threads passing tasks to them as they become available for more work.   
[example](https://www.youtube.com/watch?v=q6hxTYGbpDo)       

Q8. what is ProcessPoolExecutor. ?    
The ProcessPoolExecutor is use when we are indeed running our tasks across multiple processes.   
[Example](https://tutorialedge.net/python/concurrency/python-processpoolexecutor-tutorial/)   



