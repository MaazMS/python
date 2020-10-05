## create dictionary 
* create a dictionary by enclosing comma separated key: value pairs within curly braces {}.It is also knows associative array.     
* It is mutable.  
* It is dynamic.   
* It is nested.   
## Dictionaries differ from lists primarily in how elements are accessed:   
* List elements are accessed by their position in the list, via indexing.  
* Dictionary elements are accessed via keys.   

## method of dictionary  
1. dict : It is use for create dictionary.  
2. get : Only access value by kay.  
3. values : It return values in dictionary.   
4. items : Access kay and values.  
5. pop  : remove kay and value  in dictionary. Pass kay as argument fixed.    
6. clear : clear all data in dictionary. Do not pass argument. 
7. update : update the value in dictionary by using key.   
8. del : delete whole dictionary or specific value.   

### Example of method  
1. Three way to use dict function.  
**frist way**  ` d = dict({key: 'value', key:'value'}) eg d = dict({1: 'a', 2:'b'})`     
**second way** ` d = dict ([('key', value), ('key',value), ('key',value)]) eg d1 = dict ([('a', 1), ('b',2)])`  
**Third way**  ` d = dict (key='value' , key='value') eg d2 = dict (a= 1, b=2)`     
2. `dict_create = {1: 'a', 2: 'b', 3 :'c' }` and **print(dict_create.get(1))**  
3. `dict_create = {1: 'a', 2: 'b', 3 :'c' }` and **for number in dict_create.values():  print(number)**   
4. `dict_create = {1: 'a', 2: 'b', 3 :'c' }` and **for number in dict_create.items():   print(number)**    
5. `dict_create3 = {'a': 'A', 'b': 'B', 'c':'C'}` and **remove = dict_create3.pop('a')**   
6. `dict_create3 = {'a': 'A', 'b': 'B', 'c':'C'}` and ***clear = dict_create3.clear()*   
7. `dict_create = {1: 'a', 2: 'b', 3 :'c' }` and **dict_create.update({1 : 'z'})**   
8. `dict_create = {1: 'a', 2: 'b', 3 :'c' }` and **del dict_create [1]**     

### Dictionary operation  
1. create dictionary.   
2. add kay and value.  
3. update value by using key.  

### Example of dictionary operation  
1. dict_create = {1: 'a', 2: 'b', 3 :'c' }  
2. `dict_create = {1: 'a', 2: 'b', 3 :'c' }` and **dict_create[4]= 'add items'**   
3. `dict_create = {1: 'a', 2: 'b', 3 :'c' }` and **dict_create[1] = 10** 
 

    