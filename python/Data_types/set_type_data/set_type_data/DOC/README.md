Perhaps you recall learning about sets and set theory at some point in your mathematical education. Maybe you even remember Venn diagrams:  
![](https://files.realpython.com/media/t.8b7abb515ae8.png)   

### definition of set 
set can be thought of simply as a well-defined collection of distinct objects, typically called elements or members.    
set use curly braces {} to contain the element.  
**Note** if set contain numbers and characters the it display number first and character second.   
* characteristics of set   
1. Sets are unordered.(set not access by index)  
2. set are arbitrary. (different types of data type as well as same data type in set) 
3. Set elements are unique. Duplicate elements are not allowed.  
4. set is immutable type.(do not change set element)
5. A set add and update the value. 

### example of set   
1. days = {'monday', 'tuesday', 'wednesday', 'Thursday', 'Friday',  'Saturday', 'Sunday'}   
2. _set = {1, 'a', 2, 'b'}. But is show first number and second string.   
3. It allow  _set = {1, 2} and It is not allowed  _set = {1, 1} 
4. Do not change set element.  
5. add() and  update () method.  

## set method  
1. add : Add element in the set1. after end element `eg _set.add(6)`
2. update : update set that means add element  after end element `eg _set.update([6])`
3. remove : remove element in the set and remove take argument. `eg _set.remove(6)` 
4. pop : remove first element it does not take parameter. `eg _set.pop()`    
5. clear : clear all element in set. `eg _set.clear()`  
6. discard : remove specific element in set. ` eg set1.discard(4)`  

### Example of set method    
1. `_set = {1, 2, 3, 4, 5}` and **_set.add(6)**  
2. `_set1 = {1, 2, 3, 4, 5}` and **_set1.update([6])**  
3. `_set = {1, 2, 3, 4, 5}` and **_set.remove(1)**   
4. `_set = {1, 2, 3, 4, 5}` and **_set.pop()**  
5. `_set = {1, 2, 3, 4, 5}` and **_set.clear()**  
6. `_set = {1, 2 ,3 ,4, 5, 6}` and **_set.discard(4)**   

## mathematical method  
1.union : remove duplicate element in two set. or use operator `|` 
2. intersection : only duplicate element is show. or use operator `&`    
3. difference : return the set of all elements that are in number but not in number1. use operator `-`  
4. symmetric_difference : return the set of all elements in either number or number1, but not both. use operator `^`   
5. isdisjoint : show common in both set if use operator `^` else return `set()` and isdisjoint return true if no duplicate otherwise return false.   
6. issubset : number1 set all element present in number set means number1 is subset of number. use operator `<=`   
7. issuperset :  number set have all element that are present in number1. use operator `>=`   

## Example of mathematical method  
1. `number = {1, 2 ,3 ,4}` and `number1 = {4, 5, 6, 7}` and **number.union(number1)**    
2. `number = {1, 2 ,3 ,4}` and `number1 = {4, 5, 6, 7}` and **number.intersection(number1)**   
3. `number = {1, 2 ,3 ,4}` and `number1 = {4, 5, 6, 7}` and **number.difference(number1)**  
4. `number = {1, 2 ,3 ,4}` and `number1 = {4, 5, 6, 7}` and **number.symmetric_difference(number1)**   
5. `number = {1, 2 ,3 }` and `number1 = {4, 5, 6, 7}` and **number.isdisjoint(number1)**   
6. `number = {1, 2 ,3 ,4, 5, 6}`  and `number1 = {1, 2, 3}`and **number1.issubset(number)**   
7. `number = {1, 2 ,3 ,4, 5, 6}`  and `number1 = {1, 2, 3}` and **number.issuperset(number1)**     


