#### print   
1. it is use to show value on screen.  
 
### print method with parameter  
1. objects - object to the printed. * indicates that there may be more than one object.   
2.  sep - objects are separated by sep. Default value: ' '
3. end - end is printed at last  
4. %s - string variable value replace by %s.  

### Example print method with parameter 
1. `print("Maaz" * 3)` output **MaazMaazMaaz**
2. `print('a' , 'z' , sep= '___')` output **a___z**
3. `print('a' , end="string")`  output **astring** 
4. `first_name = "Maaz"` **print("my name is %s" %first_name)** output **my name is Maaz** 

#### input 
1. input is use to take value from user.   
2. by default it take value as string. There for we need int value give int before input.  
3. multiple input separated by space  
4. multiple input separated by comma   
5. multiple integer input separated by comma  

### Example of input 
1. full_name = input(" enter full name ")   
2. Roll_number = int(input(" enter number"))   
3. _list = [number  for number in input("enter multiple input separated by space  ").split()]  
4. _list = [number  for number in input("enter multiple number separated by comma  ").split(',')]  
5. _list = [ int(number)  for number in input("enter multiple number separated by comma  ").split(',')]   
 