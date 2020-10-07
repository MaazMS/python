## lambda
1. A lambda is an anonymous function that will not have any name.   
2. function lambda will always return a function back.   
3. lambda expressions are very helpful when we use them inside other functions. `eg map, reduce, filter etc.`   
 
**syntax**   
``` 
lambda argument_list: expression  
    return  
```  

``` 
Example 
cube = lambda no : no ** 3
print(cube(5))
```
### difference between lambda and function  
function :  
def keyword followed by the name of the function then the argument list followed by the body of the function    
within which will have multiple statements. And at the end in some cases we return a result back.   
 
lambda : A lambda is an anonymous function that will not have any name. It will always return a function back.  

 ### filter   
filter : It is  returns an iterator based on function condition.     
1. The first parameter is the lambda expression and the second parameter is a sequence which in this case it is list.
 
 ``` 
Example  
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(filter( lambda  no : no % 2 == 0, ls))
print(result) 
```  

### map   
1. map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable.  
2. The first parameter is the lambda expression and the second parameter is a sequence which in this case it is list.  
 ``` 
Example   
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(map( lambda  no : no * 2, ls))
print(result) 
```
### reduce   
1. reduce : It is a function that implements a mathematical technique called folding or reduction.  
2. The first parameter is the lambda expression and the second parameter is a sequence which in this case it is list.  
3. from functools import reduce.  
``` 
Example   
from functools import reduce
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = reduce ( lambda  no1, no2 : no1 + no2, ls)
print(result)
```   

### decorator
1 .decorator takes a function and it will return a function but the function that is returned by the decorator will perform   
 additional logic or additional processing on the function that is given as input.    
 
 ``` 
Example  
def decor(fun):
    def inner():
        dubble_decor_fun =  fun ()
        return dubble_decor_fun  * 2
    return inner
def num():
    return 5

result = decor(num)
print(result()) 
```  
### @decorator 
1 .decorator takes a function and it will return a function but the function that is returned by the decorator will perform   
 additional logic or additional processing on the function that is given as input. 
 
 **syantax** 
 ``` 
@function_name  
```
```` 
Example  
def decor(fun):
    def inner():
        dubble_decor_fun =  fun ()
        return dubble_decor_fun  * 2
    return inner

@decor
def num():
    return 5
print(num())
```` 

### Generators and yield
1. Generators are functions that return a sequence of values but it uses a yield statement.  
2. yield will take each value of x and it will store it in memory and at the end it will return the complete.  
3. It is use for custom sequence. (create custom range).  
``` 
Example  
def sequence(no1 , no2):
    while no1 <no2:
        yield no1
        no1 += 1

result = sequence(10 , 30)
for number in result:
    print(number)
```  
### module
1. A module is nothing but a collection of functions and class.  
2. It is use for reusing the code. `import python_file_name`  

### package  
1. A package is nothing but a collection of modules.  
2. package is contain `__init__.py` without `__init__.py` it is not package.  
