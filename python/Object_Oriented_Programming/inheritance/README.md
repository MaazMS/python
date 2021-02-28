### Inheritance
1. Inheritance is the process of defining a new object with the help of an existing object.   
2. reusability of code.  
3. It  `is a relationship` define. eg ` computer is a electronic device`  
4. use parent class name in bracket eg `class child_name(parent name)`
5. use parent class constructor in child class. 

##### Different forms of Inheritance  

1. Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.   
2. Multiple inheritance : When a child class inherits from multiple parent classes, it is called multiple inheritance.   
3. Multilevel inheritance : When a child class becomes a parent class for another child class.   
4. Hierarchical inheritance :  More than one derived classes are created from a single base.  
5. Hybrid inheritance : This form combines more than one form of inheritance. `Multilevel `

### overriding  
overriding : It means a same function name in parent class and child class having different functionality.   
parent class access parent class function and child class access child class function(override function).     

### super    
1. super inbuilt method that invoke the parent class constructor and parent classes methods from the child classes 
constructor and methods.  
2. do not pass self. in super ()  
3. If use super in method then first parent class invoke and after that child class invoke.    
``` 
Example  
class BMW:

    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
   
    def display(self):
        print(" BMW car ")

class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled,  model, make, year):
        super().__init__(model, make, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        super().display()
        print("ThreeSeries of BMW")

bmw = BMW("BMW", '328i', "2018")
bmw.display()

threeSeries = ThreeSeries(True, "BMW", '328i', "2018")
threeSeries.display()
```
 