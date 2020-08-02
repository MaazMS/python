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
