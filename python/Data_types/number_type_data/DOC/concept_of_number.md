## Number Data Type in Python i.e int, float, complex.   
Python supports integers, floating-point numbers and complex numbers. They are defined as int, float, and complex classes in Python    
**Integers** and **floating** points are separated by the `presence` or `absence` of a **decimal point**.   
**Complex numbers** are written in the form, `x + yj`, where `x` is the **real part** and `y` is the **imaginary part.**    
   
**Note**  Python 2 has two integer types - int and long. There is no 'long integer' in Python 3 anymore.       
* type    
`type()` function to know which class a variable.eg print(type(name_of_variable))    

   
* isinstance    
`isinstance()` function to check if variable belongs to a particular class.    
eg. print("int_number belong to class int check ", isinstance(int_number, int))     
**Note** This isinstance function is return true or false.    

### number operation using underscore _ 
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
## length of number in python      
integers can be of any length,    
floating-point number is accurate only up to 15 decimal places **(the 16th place is inaccurate)**.   
example of floating number   
      
input | output     
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

## Type Conversion    


* Converting Integers to Floats.      
method float() will convert integers to floats. To use this function, add an integer inside of the parentheses. 
**exaample**   
``` 
int_number = 10   
int_to_float = float(int_number)
```
In this case, **57** will be converted to **57.0**      

* Converting floats to integers.   
method int() will convert floats to integers . To use this function add float inside of the parentheses.    
```  
float_number = 10.9  
float_number = 10.9 
float_to_int = int(float_number)
```  
In this case, **10.9** will be convert to **10**    
In this case, **10.0** will be convert to **10**     

**Note** `int(10.9)` python cut the number after decimal and remain numbers (before decimal) of float to create integer.    
* Converting string to floats and integers.  
```
int_number_in_string = "123"
float_number_in_string = "123.9"
string_to_int = int(int_number_in_string)
string_to_float = float(float_number_in_string)
``` 
In this case, **"123"** will be convert to **123**    
In this case, **"123.9"** will be convert to **123.9**    

### But if use string and number combination and then convert it give ValueError
```  
number_in_string = "123f"
string_to_int = int(number_in_string)
print("string_to_int",string_to_int)
``` 
ValueError: invalid literal for int() with base 10: '123f'  
**Note** if convert string into number type then number with character give error called valueError.  
