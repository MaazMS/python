### Recursion 
1. Recursion is the process of a function calling itself.  
2. you should use recursion complex problems like traversing trees, binary trees etc.  
**Note** It is not a good candidate for everything.   

### Example of Recursion
``` 
def factorial(no):
    if no== 0:
        result = 1
    else:
        result = no * factorial(no -1)
    return result

print(factorial(3))
```