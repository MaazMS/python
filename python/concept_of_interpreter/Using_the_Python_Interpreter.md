## Using the Python Interpreter   
![](https://miro.medium.com/max/569/0*qPZqO7mw6RMsGt7B)
Q1. what is interpreter.?    
An interpreter is a kind of program that executes other programs. When you write Python programs , it converts source    
code written by the developer into intermediate language which is again translated into the native language / machine    
language that is executed.       

Q2. what is byte code.?      
byte code is a lower-level, and platform-independent, representation of your source code.        

Q3. what is PVM.?    
**PVM** is stand for **Python Virtual Machine** .The PVM is always present as part of the Python system.   
Technically, it's just the last step of what is called the Python interpreter.

Q4. what is virtual machine. ?   
simple definition is that **a machine that built from software**     
[real life example](https://tech.blog.aknin.name/2010/07/04/pythons-innards-for-my-wife/)      

**Explain**    

**step1 :** Python first compiles your source code (.py file) into byte code. Compiled code is usually stored in .pyc   
files , and is  regenerated when the source code is updated.         

   
**step2 :** The bytecode (.pyc file) is loaded into the Python runtime and interpreted by a Python Virtual Machine ,    
which is a piece of code that reads each instruction in the bytecode and executes whatever operation is indicated.     





1. Invoking the Interpreter     
The Python interpreter is usually installed as /usr/local/bin/python3.8. or to  start it by typing the command:   
python3.8     


Typing an end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt causes the interpreter to   
exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: quit().       

Control-p : It is use for previous command. (previous command which is store in history use by Control-P )
Control-m : It is use go to next line. not like enter button. next line go without any execution command.    
Control-l : It is use for clear all the command and go to first line.(clear all command)         



The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it     
reads and executes commands interactively; when called with a file name argument or with a file as standard input, it    
reads and executes a script from that file.       

1.1. Argument Passing.  
When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and   
assigned to the argv variable in the sys module.  You can access this list by executing import sys. The length of the   
list is at least one; when no script and no arguments are given, sys.argv[0] is an empty string. When the script name is    
given as '-' (meaning standard input), sys.argv[0] is set to '-'.Options found after -c command or -m module are not     
consumed by the Python interpreter’s.     


1.2. Interactive Mode   
When commands are read from a tty, the interpreter is said to be in interactive mode.The interpreter prints a welcome    
message stating its version number and a copyright notice before printing the first prompt.  In this mode it prompts for    
the next command with the primary prompt, usually three greater-than signs (>>>); for continuation lines it prompts with   
the secondary prompt, by default three dots (...) .Continuation lines are needed when entering a multi-line construct.     
example   

````
>>> the_world_is_flat = True 
>>> if the_world_is_flat:   
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
````
 a. The Interpreter and Its Environment    
 1. Source Code Encoding   
By default, Python source files are treated as encoded in UTF-8.       
To declare an encoding other than the default one, a special comment line should be added as the first line of the file.   
The syntax is as follows:    
` # -*- coding: encoding -*-`  
For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:   

` # -*- coding: cp1252 -*-`    
One exception to the first line rule is when the source code starts with a UNIX “shebang” line. In this case, the       
encoding declaration should be added as the second line of the file. For example:   

` #!/usr/bin/env python3  `     
`# -*- coding: cp1252 -*- `    
 
 
 
