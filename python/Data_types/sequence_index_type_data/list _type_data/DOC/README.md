definition : A list is a collection of arbitrary objects. different types of data type is store in list.  
Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([]).  
**a = ['foo', 'bar', 'baz', 'qux']**  

The important characteristics of Python lists are as follows:  

1. Lists are ordered.  
2. Lists can contain any arbitrary objects.(different types of data type as well as same data type in list)  
3. List elements can be accessed by index.(index start from zero)  
4. Lists can be nested to arbitrary depth.  
5. Lists are mutable.(list element can be change)  
6. Lists are dynamic.(add new element in list runtime)  
7. List contain duplicate value.(same value is store in list)    
8. List index start from zero   

### example of list characteristics  
1. `number_list1 = [1, 2, 3, 4, 5, 6]` and `number_list2 = [6, 5, 4, 3, 2, 1]`. number_list1 and number_list2 are not equal.   
2. `_list = [1, 2, 3, 'Maaz', 'Shaikh']` . list contain number and string.  
3. index access left to right `_string[0]` , index access right to left `_string[-1]`start_index : end element : `_string[0 : 6]`   
start_index : end element : number of step (number -1) `_string[0: 6 : 2]`       
4. list inside list. ` nested_list = ['a', 'b', 'c' ,[1, 2, 3] ]`  .   
5.  and 6. original list `_list = [1, 2, 3]` `_list[0] = 10` , `_list[1] = 10`, `_list[2] = 10`. change list `_list = [10, 10, 10]` 
7. `_list = [1, 1, 1, 2, 2,] ` list contain common element 
8. index access left to right `_string[0]`  

#### list function   
1. **append** : Add element end of list. `eg. list.append('a')`   
2. **extend** : appending all the items from list.This allows you to join two lists together. `eg. extend.(['a', 'a'])`    
3. **Inserts** : Inserts an item at a given position. but it not remove insert position element. `eg list1.insert(2,'a')`     
`Note` : It take tow parameter first is index and second is value.    
4. **remove**  : remove take item in the list as parameter and remove it. `eg list.remove(1)`   
5. **pop**     : Removes the item in list without index and with index. `eg list.pop() or list.pop(1)`    
`Note` : without index pop remove last item in list.   
6. **clear**  : Removes all items from the list. Equivalent to del. `eg list.clear() or del list [0]`   
  