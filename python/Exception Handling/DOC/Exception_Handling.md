### exception 
1) exception are runtime errors.If something goes wrong in our application an exception is raised and if we do not handle   
the exception correctly in our application it will cost three things.    
* first our program will terminate abruptly right in between wherever the exception is raised the program will stop right   
there and the code after that line will not be executed.   
* Secondly the Python virtual machine will display the unfriendly exception information to the end user.     
* third improper shutdown of the resources such as database connections or file streams or network connection.    

2) To handle an exception we will wrap the code which might cause an exception inside the try and except block.    
3) Optionally the try and exception also have a else block which will be executed if an exception is not raised.    
4) Finally as the name itself says finally will be executed no matter whether there is an exception or not.   
So if have code like resource closing or resource shut down very well closing database connections files
or network connections etc. All code can go into the finally block because it is executed no matter whether an exception
is thrown or even if an exception is not thrown.   

### The Image of Pythons Exception Hierarchy
![](https://chercher.tech/images/python-programming/python-exception-heirarchi.png)  

### Logging in python   
1) Python has a built-in module logging which allows writing status messages to a file or any other output streams. The    
file can contain the information on which part of the code is executed and what problems have been arisen.    
2) logfile have any name but extension is log. eg `anyname.log`   
3) level are define line number where log is defined. 
```` 
Example  
logging.basicConfig(filename="anyname.log", level=logging.DEBUG)
logging.critical("critical")
logging.error("Error")
logging.warning("warn")
logging.info("info")
logging.debug("debug") 

output : 
CRITICAL:root:critical
ERROR:root:Error
WARNING:root:warn
INFO:root:info
DEBUG:root:debug

````

#### assert 
The assert keyword is used when debugging code. The assert keyword check expression and evaluate into a boolean true or false.  
it is also handle by exception using AssertionError.  
```` 
Example 
try: 
	num  = int(input("Enter the number "))
	assertion num %2==0 "you have to enter the odd number" 
except AssertionError as obj: 
	print(obj) 

print("you have to handel assertion")
````