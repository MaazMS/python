Tuples are defined by enclosing the elements in parentheses **()**.   
Tuples are immutable.( fixed value that cannot be changed.)  

## Why use a tuple instead of a list?   
* Program execution is faster when manipulating a tuple than it is for the equivalent list.   
* Sometimes you don’t want data to be modified. If the values in the collection are meant to remain constant for the     
life of the program, using a tuple instead of a list guards against accidental modification.   
* There is another Python data type that you will encounter shortly called a dictionary, which requires as one of its    
components a value that is of an immutable type. A tuple can be used for this purpose, whereas a list can’t be.   

##  implicitly interpreting the input as a tuple.
``` 
>>> name = 'maaz'
>>> number = 30
>>> name , number
('maaz', 30) 
``` 
## tuple operation 
1. create tuple 
2. Tuple element assign to variable.    
3. tuple element assign by index.(tuple index start from zero)    

## example of tuple operation   
1. _tuple = (1, 2, 3, 4)   
2. This is tuple. `number  = (1, 2, 3 )` assign value `s1, s2, s3 = number` s1= 1, s2=2, s3 =3.  
3. _tuple[0]. access value of tuple by index.  

*Note** There is no ambiguity when defining an empty tuple, nor one with two or more elements. Python knows you are defining a tuple:  

  