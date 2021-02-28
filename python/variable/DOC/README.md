### variable 

1. variables are storing data/values.
2. python has no command for declaring variable.
3. A variables is created the moment yoy first assign the value.
4. Variables do not need to be declared with any particular data type
5. data type of variable  can even change after they have been set_type_data.
6. String variables can be declared either by using single or double quotes:
7. A variable can have a short name and it's more descriptive name eg. age,name etc
8. A variable name must start with a letter or the underscore character
9. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
10. Variable names are case-sensitive (age, Age and AGE are three different variables)
11. A variable name cannot start with a number if variable name is start number it give invalid syntax.

### global variables  
1. Variables that are created outside of a function are known as global variables.  
Global variables can be used by everyone, both inside of functions and outside   
2. TO access global variable inside function if global variable and local variable have same name.`print(globals()['variable'])`  
3. create a global variable inside a function,  use the global keyword. `global variable` and  `variable = 10`  
### local variable    
1. create a variable inside a function is called local variable .  
If you create a variable with the same name outside a function, this variable will be local variable,  
and can only be used inside the function.   

###  variable operation  
1. Assign values to multiple variables in one line.after one line value is not assign to variable `eg first_name, last_name = "Maaz", "Shaikh"`  
2. Assign the same value to multiple variables in one line. `eg name = full_name = "Maaz Shaikh"`
3. To combine both text and a variable uses the + character.
4. + character is also use to add a variable to another variable
5. For numbers, the + character works as a mathematical operator:
6. If combine a string and number,It give you TypeError: can only1 concatenate str (not "int") to str