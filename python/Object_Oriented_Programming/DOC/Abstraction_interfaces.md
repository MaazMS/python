### abstract
1. abstract method will not have any implementation and it will be marked with at abstract method decorator.   
2. Once we do that any child class that extends or inherits this parent class will have to implement abstract method.   
3. If it doesn't implement the abstract method in extends class that class will also become an abstract class.  
4. you cannot create an object of abstract class.  
5 You can have methods in an abstract class that can have implementation but typically at least one method  
in abstract class is a abstract method.   
6. If all the methods are not abstract then you can create an instance of the class it is not abstract.  
7.  if at least one method in a class is an abstract method then it becomes an abstract class.  
8. The child classes which implement that abstract class should provide an implementation for all the  
abstract methods that are in the parent class.    
9. If we define any parameter to abstract method signature should be exactly the same and it should provide the implementation  
for it.  

### interfaces
interfaces are nothing but abstract classes where all the methods are abstract.   

###  pass
1. It is use to create abstract method.  
2.pass specifically tells that we are not implementing this method. if remove pass and do not written anything it give error.   

### how to create abstract class  
1. from abc import abstractmethod, ABC
2. class BMW(ABC):(abstract class implements ABC)  
3. in abstract class have abstract method   
4. child class implements abstract class similar to inheritance eg `class class_name(abstract class name):`  
5. It is fixed to implements the all abstract method implements in child class otherwise it give error.  
``` 
Example 
from abc import abstractmethod, ABC
class BMW(ABC):

    def start(self) :
        print("starting of car")

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):

    def display(self):
        print("ThreeSeries of BMW")

    def drive(self):
        print("drive method implements because it is abstract method")
threeSeries = ThreeSeries()
threeSeries.start()
threeSeries.display()
```
### how   to create abstract method   
1. from abc import abstractmethod   
2. @abstractmethod
2. def drive(self): pass  
```` 
Example  
@abstractmethod
    def drive(self):
        pass
```` 
 
### interface  
1.  a class with all the methods as abstract methods is called interface.  
2. It do not have interface and implements keyword.  
3. It is fixed to implements the all abstract method implements in child class otherwise it give error.
```` 
Example 
from abc import abstractmethod, ABC
class BMW(ABC):

    @abstractmethod
    def start(self) :
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):

    def start(self):
        print("starting of car")

    def drive(self):
        print("drive a car")

threeSeries = ThreeSeries()
threeSeries.start()
threeSeries.drive()
````