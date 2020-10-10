#### polymorphism 
`poly` means multi or many and  `morphic` means shapes.  
This shape is replaced with behavior that is if we can have different types of behavior or different behavior based     
on the data or the objects that the functions are dealing with then that is nothing but polymorphism.  

### different way to achieve polymorphism   
1. DuckTyping 
2. DuckTyping through dependency injection  
3. `+` plus operator for overloading  
4. method overriding(runtime polymorphism)   


### DuckTyping
Call talk `def CallTalk(obj)` which takes an object is going to invoke any method on the object.   
* The key here is that in Python We do not specify what type of object is this.  
* As a result we can pass it any type of object at runtime.  
* dynamic nature that side effect of this dynamic nature of passing parameters is nothing but duck typing.  
* It is define outside of class.   
* same function name `callTalk()` do multiple things depending on what we pass to it dynamically at run time.   

### DuckTyping for Dependency Injection
* injection is nothing but simply injecting an object into an other object.   
* Flight class call AirbusEngine function `start()` with the help of class filed ` self.engine.start()` inside class function.  

```` 
Example 
class Flight:

    def __init__(self, engine):
        self.engine = engine # inject object

    def startEngine(self):
        self.engine.start()

class AirbusEngine:

    def start(self):
        print("Starting airbus engine")

air = AirbusEngine()
fli = Flight(air)
fli.startEngine()
```` 

### `+` plus operator   
1. +` plus operator  perform multiple things so we can call it polymorphic.  
2. using integer it add two number.  
3. for using string two strings it will append them as one string.  
4. If you use two lists then it will come out with a single list using those two lists.   

### method overriding 
1. left side is parent class = child class .  
2. So dynamically at runtime, we can switch what is there on the right hand side, but on the left hand 
side will always have the parent interface or class.    
3. But in Python, again, we don't need this method over riding We have already implemented at runtime   
polymorphism comes for free because of the dynamic typing in Python.   
4. It always need inheritance.   
