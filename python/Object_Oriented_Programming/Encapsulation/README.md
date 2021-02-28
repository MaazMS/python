### Encapsulation  

Encapsulation : Encapsulation is about protecting the properties and the functionality of an object from other objects.  
Another definition for encapsulation is writing the data and code into one single unit.  
Example: The easiest way to remember that is by having a capsule diagram.   


#### Private Fields and Name Mangling

create private fields : use two underscore before fields ` eg __name ` 
out side of class object can not access them (fields) because they are hidden. 
inside class :   
you can access private fields by using function of class. `print(self.__name)`  inside function.  
outside class:  
name mangling use to  access private data outside of class. eg `obj._ClassName__fieldname`
``` 
Example  Private Fields
class Student:

    def __init__(self):
        self.__name = "Maaz"
        self.__roll_no = 123

    def display(self):
        print(self.__name)
        print(self.__roll_no)
s1 = Student()
s1.display()

```

```` 
Example mangling
class Student:

    def __init__(self):
        self.__name = "Maaz"
        self.__roll_no = 123

s1 = Student()
print(s1._Student__name)
print(s1._Student__roll_no)
````

### getter and setter  for private fields
setter : assign value to private fields. eg `  def setName(self, user_name): self.__name  = user_name`   
getter : accessing value of private fields. eg `    def getName(self):   return self.__name` 

``` 
Example 
class Programmer:

    def setName(self, user_name):
         self.__name  = user_name

    def getName(self):
        return self.__name
p1 = Programmer()
p1.setName("Name") 
print(p1.getName())
```