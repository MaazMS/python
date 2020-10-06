### continue 
continue : It is use to skip value based on condition.  

### Example of continue  
``` 
no = 0
while no <=20:
    no = no + 1
    if no % 2 == 0:
        continue
    print(no)

``` 
### break  
break : It is use to exit the loop based on condition.  

### Example of break  
``` 
for no in range(1 , 30):
    if no >20:
        break
    print(no)
``` 

### assert  
assert: The assert keyword is used when debugging code. if a condition satisfied returns True, if not, the program will raise an AssertionError.  
