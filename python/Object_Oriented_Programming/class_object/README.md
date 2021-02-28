### class  
1. class is the collection of object.  
2. class is blue print or template of object.  
3. class is not occupy the memory.  

### Example of class 
1. sport is the class.  
object of sport are baseball,basketball,cricket,football.  
attribute of sport are Player,Ball,fieldLength,fieldWidth,Referee,Audience,score Board,Whether .
method of sport class are run,jump,field.  

2. fruit is the class 
object of fruit are apple, banana, blackberry ect.  
attribute of attribute is colour, size, test etc.  

### Objects 
1. Objects are an instance of a class.  
2. Object is a collection of data with associated behaviors.    

### Example of Objects  
 
1. online shopping is the class.  
object of online shopping are Customer, Order, Product, Address, Payment.  
 
2. Hospital Management is the class 
object of Hospital Management are patient, Doctor, Appointment, prescription, Billing.  

### syntax of class and object. 
``` 
class class_name: 
    
    def __init__(self, argument):
        self.variable_name1 = value 
        self.variable_name2 = argument 
    
    def function_name(parameter):
        statement 
   
object_name1 = class_name()
object_name2 = class_name(argument, argument)
object_name1.function_name(parameter)
```
### __init__(parameter)  
"__init__" is a reserved method in python classes. It is called as a constructor in object oriented terminology.         
This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.   

### self  
1. Self points to the current object that is being created of this particular class.    
2.  self we can assign we can declare and assign the values for the class field.    

### instance method  
instance means particular occurrence of something `(instance means event or an incident)`   
instance method  :  A special kind of function that is defined in a class definition.   
**syntax**  
``` 
def function_name(): 
    return  

obj.function_name()  
``` 

### setter and getter method  
setter method : It is use for receive value by parameter.It along with self. It is also called mutator.  
mutator because we are changing the values.   
getter method : It does not require any additional parameters. self Dot the name return value. It is also called accessor.  
accessor because we are accessing the values.
``` 
class Programmer:
    def setName(self, user_name):
        self.name = user_name 
    
    def getName(self):
        return self.name 

p1 = Programmer()
p1.setName("Name")
print(p1.getName())
```

### static  
1. static fields or class level field.  
2. It is define globally.  
3. static value share by all object of that class. It is shared memory.  
4. It is access by `object.static_name` or `class_name.static_name`.  
``` 
Example bord is static variable
class Student:
    bord = "state bord"
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

s1  = Student("Shaikh", 1)
print(s1.name)
print(s1.rollno)
print(s1.bord)
print(Student.bord)
``` 

### @staticmethod  
1. You need to mark a static method with decorator called at @staticmethod. 
2. static method not have self parameter. 
3. It is access by class and object.     
``` 
class ObjectCounter:

    numberOfObjects = 0   
    def __init__(self):  
        ObjectCounter.numberOfObjects += 1  

    @staticmethod   
    def displayCount():  
        print("number of objec", ObjectCounter.numberOfObjects)  
        
obj1   = ObjectCounter()   
Obj2   = ObjectCounter()   

ObjectCounter.displayCount()  
obj1.displayCount()  
 
```  

### inner and outer class 
1. create class inside class.   
2. do not access inner class directly outside of outer class. 
3. outer class dot inner class. 
Now to create an instance of engine here will have to use the outer class name car or the object dot engine.   

``` 
class Car:

    def __init__(self, make, year ):
        self.make = make
        self.year = year

    class Engine:

        def __init__(self, number):
            self.number = number

        def started(self):
            print(" Engine started")

c1 = Car("BMW", 2020)
E1 = c1.Engine("s6")
E1.started()
Car.Engine.started("s10")

```