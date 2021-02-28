#### how language is translate and execute  

High level programming language convert to machine language in two ways as  
1. Compilers   
2. Interpreters   

**Compilers**   
Convert high level program to its machine or CPU instruction sets I,e machine bytecode. Therefore to do this compiler   
checks for its syntax first and convert whole program to machine or CPU understandable bytecode.      

Ex: c, c++, Java

**Interpreters**   
Interpreters work differently , they take each expression or line of program and convert to machine code and execute it.   
Therefore if any syntax error in some line of interpreted language, you will get error only when that line is encountered.   

step 1 : check python first line  syntax and compile.  
step 2 : compiled is correct then convert into bytecode.   
step 3 : The byte code is execute.  
step 4 : step 1 to step 3 are repeated if syntax error is show  by compiler Then   
step 5 : compiler is show syntax error and program is stop.   

example [here](https://github.com/MaazMS/python/blob/master/python/concept_of_interpreter/interpreter_example.py)   
In this example line number 5 **print(a)** a is not define there for line 1 to line number 4 are execute but line number   
5 syntax error the program is stop and line number 6  is not execute.      
![](https://github.com/MaazMS/python/blob/master/python/images/interpreter_example.png?raw=true)

