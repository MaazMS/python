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

    
#### Job stores   
1. Job stores don’t keep the job data in memory, but act as middlemen for saving, loading, updating and searching jobs   
in the backend.    
2. A job’s data is serialized when it is saved to a persistent job store, and deserialized when it’s loaded back from it.   
3. Job stores must never be shared between schedulers      
   
#### Executors   
1. Executors are what handle the running of the jobs.      
2. They do this typically by submitting the job to a thread or process pool.   
3. When the job is done, the executor notifies the scheduler.     

#### Schedulers   
1. You typically have only one scheduler running in your application.    
2. The application developer doesn’t normally deal with the job stores, executors or triggers directly.   
3. scheduler provides the proper interface for adding, modifying and removing jobs.
    
     
Q1. what is BlockingScheduler.? 
A scheduler that runs in the foreground/front.   
  
  
Q2. what is BackgroundScheduler.?     
A scheduler that runs in the background using a separate thread.        

  
  
Q3. what is AsyncIOScheduler.?    
AsyncIOScheduler was meant to be used with the AsyncIO event loop.By default, it will run jobs in the event loop’s      
thread pool.  
The asyncio module provides tools for building concurrent applications using coroutines.   
 

Q4. what is coroutine.? 
A function  which can pause and resume its execution. that means `A` function  is start execution it call B function.   
`B` function is executing it call the function `c` . Then c function is executing and complete and call function `b` .    
function `b` is executing and complete and call function `A` .function `A` is executing and complete.    

