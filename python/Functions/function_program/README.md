#### definition of function  
1. Function is a group of statements which perform a particular task.   
2. function performs a particular tasks and it have a group of statements.   
### Three usage of function  
1. re-usability once we define a function.  
2. when we are working on a huge application we need not put the entire code in one single.   
3.  Maintenance  of application.  
  
**syntax** 
```  
function declare    
def function_name(argument, argument): 

function_name(argument, argument)  
function call
``` 

### function 
1. `function_name(argument, argument) ` function call  
2. `return (a+b)` return single value   
3. `return addition, subtraction, multiplication`  return multiple value  
**Note** all these values here will be returned as a tuple so that they cannot be modified.  

### assign function to variable  
`variable = function`. function call `variable()`   

### function inside another  
1. outer function call out side.    
2. outer function call inside of function go infinite loop. 
3. inner function call inside of outer function.  

### Example of function inside another 
``` 
def outer_function():
    print("outer function")
    
    def inner_function():  
        print("inner function")
        
    inner_function()
outer_function()

```
### function parameter to another function  
1. pass function name as another function parameter.  

### Example function parameter to another function   
``` 
def display(function_name):
    return "Hello" + function_name

def name():
    return "Maaz "
print(display(name()))
``` 

### return function 
1. return function as return type.  

### Example return function
``` 
def display():
    def message():
        return "Hello"
    return message
fun = display()
print(fun())
```
### pass anything in list  
1. we can pass any thing in function parameter 

### Example pass anything in list 
```  
def fun(ls):
    for i in ls:
        print(i)
fun([1, 2, 3, 4 ])
``` 

### keyword argument 
1. if assign vale of variable by variable name at function call.   
2. The same name parameter is use as function definition.Then value is assign based on variable name.   
### Example keyword argument 
```` 
def average(no1, no2):
    print("no1 = ", no1)
    print("no2 = ", no2)
    return (no1/no2)/2
print(average(2, 2))
print(average(no2=4 , no1= 2))
```` 

### default argument 
1. assign value to function parameter. 
2. if function parameter is not passed value then function parameter value use.  
### Example default argument  
```` 
def average(no1, no2=10):
    print("no1 = ", no1)
    print("no2 = ", no2)
    return (no1/no2)/2
print(average(2, 2))
print(average(no1= 2))
````