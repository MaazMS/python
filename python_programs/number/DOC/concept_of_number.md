In interactive mode, the last printed expression is assigned to the variable _.   
That means in the terminal to perform any calculation the result of the calculation is assign to `_` underscore.   
and use `-` value to perform the next operation.    
```
>>> number1 = 1
>>> number2 = 2
>>> number1 + _ 
```
Traceback (most recent call last):    
  File "<stdin>", line 1, in <module>     
NameError: name '_' is not defined   
`>>> number2 + _`    
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>   
NameError: name '_' is not defined  
`>>> number1 + number2`            
3  
`>>> number1 + _`   
4   

## Number Data Type in Python 
Python supports integers, floating-point numbers and complex numbers. They are defined as int, float, and complex classes in Python    
**Integers** and **floating** points are separated by the `presence` or `absence` of a **decimal point**.   
**Complex numbers** are written in the form, `x + yj`, where `x` is the **real part** and `y` is the **imaginary part.**    

* type    
`type()` function to know which class a variable.eg print(type(name_of_variable))    

   
* isinstance    
`isinstance()` function to check if variable belongs to a particular class.    
eg. print("int_number belong to class int check ", isinstance(int_number, int))     
**Note** This isinstance function is return true or false.    



## length of number in python      
integers can be of any length,    
floating-point number is accurate only up to 15 decimal places **(the 16th place is inaccurate)**.   
example of floating number   
      
| input | output     
| --- | --- |     
| 1\.1234567890123450    | 1\.123456789012345     |   
| 1\.1234567890123451    | 1\.123456789012345     |
| 1\.1234567890123452    | 1\.1234567890123452    |
| 1\.1234567890123453    | 1\.1234567890123452    |
| 1\.1234567890123454    | 1\.1234567890123455    |
| 1\.1234567890123455    | 1\.1234567890123455    |
| 1\.1234567890123456    | 1\.1234567890123457    |
| 1\.1234567890123457    | 1\.1234567890123457    |
| 1\.1234567890123458    | 1\.1234567890123457    |
| 1\.1234567890123459    | 1\.123456789012346     |


 

