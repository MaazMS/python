#### what is command line argument  
The command line arguments are those arguments that are passed when our Python program is run.   

#### why use command line argument  
1. pass file location  
2. dynamically pass value to program.  
3. database name  
4. connection URL   
5. remote IP. etc   

* python run time to our program through a list called `argv`.   
* access the elements we can use `sys.argv` **eg. sys.argv[0]**       


 ### pycharm setting for command line  
RUN > Edit configurations > parameters give value

### file name and location using command line argument  
```` 
import sys   
ls = sys.argv 
print(ls)
print(sys.argv[0])
```` 

**Note** command line argument length is 1.  `print(len(ls))`