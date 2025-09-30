# Class and Object Documentation

## 1. Class and Object Definition and Characteristics

### Class Definition

1. A class is the collection of objects.  
2. A class is a blueprint or template of objects.  
3. A class does not occupy memory until objects are created.
4. Classes define the structure and behavior that objects will have.
5. Classes encapsulate data (attributes) and functions (methods) that operate on that data.

### Object Definition

1. Objects are instances of a class.
2. Objects are concrete entities that exist in memory.
3. Each object has its own copy of instance variables.
4. Objects can interact with each other through method calls.

### Key Characteristics

- *Encapsulation*: Data and methods are bundled together in a class
- *Abstraction*: Classes hide internal implementation details
- *Instantiation*: Process of creating objects from classes
- *Identity*: Each object has a unique identity in memory
- *State*: Objects maintain their own state through instance variables
- *Behavior*: Objects exhibit behavior through methods

### Example - Comprehensive Class Definition

```python
class BankAccount:
    # Class variable (shared by all instances)
    bank_name = "Global Bank"
    total_accounts = 0
    
    def __init__(self, account_holder, initial_balance=0):
        # Instance variables (unique to each object)
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = f"ACC{BankAccount.total_accounts + 1:04d}"
        BankAccount.total_accounts += 1
        self.transaction_history = []
    
    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, ${self.balance})"
    
    def __repr__(self):
        return f"BankAccount('{self.account_holder}', {self.balance})"

# Creating objects (instances)
account1 = BankAccount("Alice Johnson", 1000)
account2 = BankAccount("Bob Smith", 500)

print(account1)  # Account(ACC0001, Alice Johnson, $1000)
print(account2)  # Account(ACC0002, Bob Smith, $500)
print(f"Total accounts: {BankAccount.total_accounts}")  # Total accounts: 2
```

### Class (Original Content)

1. class is the collection of object.  
2. class is blue print or template of object.  
3. class is not occupy the memory.  

### Basic Examples of Class

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

1. online shopping is the class. object of online shopping are Customer, Order, Product, Address, Payment.  
2. Hospital Management is the class object of Hospital Management are patient, Doctor, Appointment, prescription, Billing.  

### Basic Syntax of Class and Object

```python
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

### *__init__*(parameter)

"*__init__*" is a reserved method in python classes. It is called as a constructor in object oriented terminology.
This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

### self

1. Self points to the current object that is being created of this particular class.
2. self we can assign we can declare and assign the values for the class field.

### Instance Method

instance means particular occurrence of something `(instance means event or an incident)`
instance method  :  A special kind of function that is defined in a class definition.

```python
def function_name(): 
    return  

obj.function_name()  
```

### Setter and Getter Methods

setter method : It is use for receive value by parameter.It along with self. It is also called mutator.  
mutator because we are changing the values.
getter method : It does not require any additional parameters. self Dot the name return value. It is also called accessor.  
accessor because we are accessing the values.

```python  
class Programmer:
    def setName(self, user_name):
        self.name = user_name 
    
    def getName(self):
        return self.name 

p1 = Programmer()
p1.setName("Name")
print(p1.getName())
```

### Static Fields

1. static fields or class level field.
2. It is define globally.
3. static value share by all object of that class. It is shared memory.
4. It is access by `object.static_name` or `class_name.static_name`.

```python
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

### Static Methods (@staticmethod)

1. You need to mark a static method with decorator called at @staticmethod.
2. static method not have self parameter.
3. It is access by class and object.
  
```python
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

### Inner and Outer Classes

1. create class inside class.
2. do not access inner class directly outside of outer class.
3. outer class dot inner class.Now to create an instance of engine here will have to use the outer class name car or the object dot engine.

```python
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

## 2. Class and Object Operations

### Object Creation Operations

1. *Instantiation*: Creating objects from classes
2. *Initialization*: Setting up object state through `*__init__*`
3. *Memory Allocation*: Python automatically manages memory for objects
4. *Reference Assignment*: Variables hold references to objects

### Object Access Operations

1. *Attribute Access*: `object.attribute`
2. *Method Invocation*: `object.method()`
3. *Dynamic Attribute Addition*: Adding attributes at runtime
4. *Attribute Deletion*: Removing attributes using `del`

### Object Comparison Operations

1. *Identity Comparison*: `is` and `is not`
2. *Equality Comparison*: `==` and `!=`
3. *Custom Comparison*: Implementing `*__eq__*`, `*__lt__*`, etc.

### Example - Object Operations

```python
class Student:
    school_name = "Python High School"
    
    def __init__(self, name, grade, student_id):
        self.name = name
        self.grade = grade
        self.student_id = student_id
        self.subjects = []
    
    def add_subject(self, subject):
        self.subjects.append(subject)
    
    def get_info(self):
        return f"Student: {self.name}, Grade: {self.grade}, ID: {self.student_id}"
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

# 1. Object Creation Operations
student1 = Student("Alice", 10, "S001")  # Instantiation and initialization
student2 = Student("Bob", 10, "S002")
student3 = student1  # Reference assignment

# 2. Object Access Operations
print(student1.name)  # Attribute access
student1.add_subject("Math")  # Method invocation
student1.age = 16  # Dynamic attribute addition
print(hasattr(student1, 'age'))  # Check if attribute exists
del student1.age  # Attribute deletion

# 3. Object Comparison Operations
print(student1 is student2)  # False - different objects
print(student1 is student3)  # True - same object reference
print(student1 == student2)  # False - different student IDs

# 4. Class Operations
print(Student.school_name)  # Access class variable
Student.school_name = "Advanced Python School"  # Modify class variable
print(f"Total students: {len([student1, student2])}")

# 5. Object Inspection Operations
print(type(student1))  # <class '__main__.Student'>
print(isinstance(student1, Student))  # True
print(dir(student1))  # List all attributes and methods
print(vars(student1))  # Dictionary of instance attributes
```

### Advanced Object Operations

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price}"
    
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"
    
    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        return NotImplemented
    
    def __len__(self):
        return len(self.name)

# Advanced operations examples
laptop = Product("Laptop", 1000)
mouse = Product("Mouse", 25)

# String representation operations
print(str(laptop))  # Laptop: $1000
print(repr(mouse))  # Product('Mouse', 25)

# Arithmetic operations
total_price = laptop + mouse  # Custom __add__ method
print(f"Total: ${total_price}")  # Total: $1025

# Length operation
print(len(laptop))  # 6 (length of "Laptop")

# Object lifecycle operations
products = [laptop, mouse]  # Collection operations
del products[0]  # Object removal from collection
```

## 3. Class and Object Methods

### Types of Methods

#### 1. Instance Methods

- Have access to instance data through `self`
- Can modify object state
- Called on object instances

#### 2. Class Methods

- Use `@classmethod` decorator
- Have access to class data through `cls`
- Can be called on class or instances
- Often used as alternative constructors

#### 3. Static Methods

- Use `@staticmethod` decorator
- No access to `self` or `cls`
- Utility functions related to the class
- Can be called on class or instances

#### 4. Special Methods (Magic Methods)

- Start and end with double underscores
- Define how objects behave with built-in functions
- Examples: `*__init__*`, `*__str__*`, `*__add__*`, etc.

### Comprehensive Method Examples

```python
import math
from datetime import datetime

class Circle:
    # Class variable
    pi = 3.14159
    total_circles = 0
    
    def __init__(self, radius):
        """Constructor - Special Method"""
        self.radius = radius
        self.created_at = datetime.now()
        Circle.total_circles += 1
    
    # Instance Methods
    def area(self):
        """Calculate area of the circle"""
        return Circle.pi * self.radius ** 2
    
    def circumference(self):
        """Calculate circumference of the circle"""
        return 2 * Circle.pi * self.radius
    
    def resize(self, factor):
        """Resize the circle by a factor"""
        self.radius *= factor
        return self
    
    def get_info(self):
        """Get detailed information about the circle"""
        return {
            'radius': self.radius,
            'area': self.area(),
            'circumference': self.circumference(),
            'created_at': self.created_at
        }
    
    # Class Methods
    @classmethod
    def from_diameter(cls, diameter):
        """Alternative constructor from diameter"""
        return cls(diameter / 2)
    
    @classmethod
    def from_area(cls, area):
        """Alternative constructor from area"""
        radius = math.sqrt(area / cls.pi)
        return cls(radius)
    
    @classmethod
    def get_total_circles(cls):
        """Get total number of circles created"""
        return cls.total_circles
    
    @classmethod
    def set_precision(cls, new_pi):
        """Set new value for pi"""
        cls.pi = new_pi
    
    # Static Methods
    @staticmethod
    def is_valid_radius(radius):
        """Check if radius is valid"""
        return isinstance(radius, (int, float)) and radius > 0
    
    @staticmethod
    def compare_areas(circle1, circle2):
        """Compare areas of two circles"""
        area1 = circle1.area()
        area2 = circle2.area()
        if area1 > area2:
            return f"First circle is larger by {area1 - area2:.2f} units"
        elif area2 > area1:
            return f"Second circle is larger by {area2 - area1:.2f} units"
        else:
            return "Both circles have equal areas"
    
    @staticmethod
    def distance_between_centers(circle1, circle2, x1, y1, x2, y2):
        """Calculate distance between centers of two circles"""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Special Methods (Magic Methods)
    def __str__(self):
        """String representation for users"""
        return f"Circle(radius={self.radius:.2f})"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Circle({self.radius})"
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Circle):
            return abs(self.radius - other.radius) < 0.001
        return False
    
    def __lt__(self, other):
        """Less than comparison"""
        if isinstance(other, Circle):
            return self.area() < other.area()
        return NotImplemented
    
    def __add__(self, other):
        """Add two circles (combine areas)"""
        if isinstance(other, Circle):
            combined_area = self.area() + other.area()
            return Circle.from_area(combined_area)
        return NotImplemented
    
    def __mul__(self, factor):
        """Multiply circle radius by a factor"""
        if isinstance(factor, (int, float)):
            return Circle(self.radius * factor)
        return NotImplemented
    
    def __len__(self):
        """Return circumference as length"""
        return int(self.circumference())
    
    def __bool__(self):
        """Boolean representation"""
        return self.radius > 0
    
    def __del__(self):
        """Destructor"""
        Circle.total_circles -= 1
        print(f"Circle with radius {self.radius} deleted")

# Examples of using different types of methods:

# 1. Instance Methods
circle1 = Circle(5)
print(f"Area: {circle1.area()}")  # Area: 78.54
print(f"Circumference: {circle1.circumference()}")  # Circumference: 31.42
circle1.resize(2)  # Method chaining
print(f"New radius: {circle1.radius}")  # New radius: 10

# 2. Class Methods
circle2 = Circle.from_diameter(10)  # Alternative constructor
circle3 = Circle.from_area(50)  # Another alternative constructor
print(f"Total circles: {Circle.get_total_circles()}")  # Total circles: 3

# 3. Static Methods
print(Circle.is_valid_radius(5))  # True
print(Circle.is_valid_radius(-3))  # False
print(Circle.compare_areas(circle1, circle2))

# 4. Special Methods
print(str(circle1))  # Circle(radius=10.00)
print(repr(circle2))  # Circle(5.0)
print(circle1 == circle2)  # False
print(circle1 > circle2)  # True (based on area)
combined = circle1 + circle2  # Custom addition
scaled = circle1 * 0.5  # Custom multiplication
print(len(circle1))  # Circumference as integer
print(bool(Circle(0)))  # False
```

### Method Resolution Order (MRO) Example

```python
class Animal:
    def speak(self):
        return "Animal makes a sound"
    
    def move(self):
        return "Animal moves"

class Mammal(Animal):
    def speak(self):
        return "Mammal makes a sound"
    
    def breathe(self):
        return "Mammal breathes air"

class Dog(Mammal):
    def speak(self):
        return "Dog barks"
    
    def fetch(self):
        return "Dog fetches"

# Method resolution and super() usage
class GermanShepherd(Dog):
    def speak(self):
        # Call parent method using super()
        parent_sound = super().speak()
        return f"{parent_sound} loudly"
    
    def guard(self):
        return "German Shepherd guards"

# Testing method resolution
dog = GermanShepherd()
print(dog.speak())  # Dog barks loudly
print(dog.breathe())  # Mammal breathes air (inherited)
print(dog.move())  # Animal moves (inherited)
print(GermanShepherd.__mro__)  # Method Resolution Order
```

### Property Methods (Getters and Setters)

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property for fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Computed property for kelvin"""
        return self._celsius + 273.15

# Using property methods
temp = Temperature(25)
print(f"Celsius: {temp.celsius}")  # Celsius: 25
print(f"Fahrenheit: {temp.fahrenheit}")  # Fahrenheit: 77.0
print(f"Kelvin: {temp.kelvin}")  # Kelvin: 298.15

temp.fahrenheit = 100  # Using setter
print(f"Celsius: {temp.celsius}")  # Celsius: 37.77777777777778
```

## 4. Common Errors in Class and Object Programming

### 1. Forgetting `self` Parameter

#### ❌ Error Example

```python
class Calculator:
    def add(a, b):  # Missing 'self' parameter
        return a + b

calc = Calculator()
calc.add(5, 3)  # TypeError: add() takes 2 positional arguments but 3 were given
```

#### ✅ Correct Solution

```python
class Calculator:
    def add(self, a, b):  # Include 'self' parameter
        return a + b

calc = Calculator()
result = calc.add(5, 3)  # Works correctly
print(result)  # 8
```

### 2. Confusing Class Variables vs Instance Variables

#### ❌ Error Example of Class Variables vs Instance Variables

```python
class Student:
    grades = []  # This is a class variable (shared by all instances)
    
    def __init__(self, name):
        self.name = name
    
    def add_grade(self, grade):
        self.grades.append(grade)  # Modifies class variable!

student1 = Student("Alice")
student2 = Student("Bob")

student1.add_grade(85)
student2.add_grade(92)

print(student1.grades)  # [85, 92] - Wrong! Alice sees Bob's grades
print(student2.grades)  # [85, 92] - Wrong! Bob sees Alice's grades
```

#### ✅ Correct Solution of Class Variables vs Instance Variables

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # Instance variable (unique to each object)
    
    def add_grade(self, grade):
        self.grades.append(grade)

student1 = Student("Alice")
student2 = Student("Bob")

student1.add_grade(85)
student2.add_grade(92)

print(student1.grades)  # [85] - Correct!
print(student2.grades)  # [92] - Correct!
```

### 3. Incorrect Method Calls

#### ❌ Error Example of Incorrect Method Calls

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start_engine(self):
        return f"{self.brand} engine started"

# Wrong ways to call methods
Car.start_engine()  # TypeError: missing required argument 'self'
car = Car("Toyota")
Car.start_engine(car.brand)  # TypeError: expected Car instance, got str
```

#### ✅ Correct Solution of Incorrect Method Calls

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start_engine(self):
        return f"{self.brand} engine started"

car = Car("Toyota")
print(car.start_engine())  # Correct: Toyota engine started

# Or using class method with instance
print(Car.start_engine(car))  # Also correct: Toyota engine started
```

### 4. Modifying Mutable Default Arguments

#### ❌ Error Example of Modifying Mutable Default Arguments

```python
class ShoppingCart:
    def __init__(self, items=[]):  # Dangerous! Mutable default argument
        self.items = items
    
    def add_item(self, item):
        self.items.append(item)

cart1 = ShoppingCart()
cart1.add_item("apple")

cart2 = ShoppingCart()  # This will have "apple" already!
print(cart2.items)  # ['apple'] - Wrong!
```

#### ✅ Correct Solution of Modifying Mutable Default Arguments

```python
class ShoppingCart:
    def __init__(self, items=None):  # Use None as default
        if items is None:
            self.items = []  # Create new list for each instance
        else:
            self.items = items.copy()  # Create copy to avoid sharing
    
    def add_item(self, item):
        self.items.append(item)

cart1 = ShoppingCart()
cart1.add_item("apple")

cart2 = ShoppingCart()
print(cart2.items)  # [] - Correct!
```

### 5. Incorrect Use of Class Methods and Static Methods

#### ❌ Error Example of Incorrect Use of Class Methods and Static Methods

```python
class MathUtils:
    multiplier = 2
    
    def multiply(self, x):  # Should be static method
        return x * 5
    
    @staticmethod
    def get_multiplier():  # Should be class method
        return MathUtils.multiplier  # Hard-coded class name
    
    @classmethod
    def power(cls, x, y):  # Should be static method
        return x ** y  # Doesn't use cls

# Usage problems
MathUtils.multiply(10)  # TypeError: missing 'self' argument
```

#### ✅ Correct Solution of Incorrect Use of Class Methods and Static Methods

```python
class MathUtils:
    multiplier = 2
    
    @staticmethod
    def multiply(x, factor=5):  # Static method - no self/cls needed
        return x * factor
    
    @classmethod
    def get_multiplier(cls):  # Class method - uses cls
        return cls.multiplier
    
    @staticmethod
    def power(x, y):  # Static method - utility function
        return x ** y

# Correct usage
print(MathUtils.multiply(10))  # 50
print(MathUtils.get_multiplier())  # 2
print(MathUtils.power(2, 3))  # 8
```

### 6. Circular Import and Naming Conflicts

#### ❌ Error Example of  Circular Import and Naming Conflicts

```python
# file1.py
from file2 import ClassB

class ClassA:
    def __init__(self):
        self.b = ClassB()

# file2.py
from file1 import ClassA  # Circular import!

class ClassB:
    def __init__(self):
        self.a = ClassA()
```

#### ✅ Correct Solution of  Circular Import and Naming Conflicts

```python
# file1.py
class ClassA:
    def __init__(self):
        from file2 import ClassB  # Import inside method
        self.b = ClassB()

# file2.py
class ClassB:
    def __init__(self):
        # Don't create circular dependency
        self.a = None
    
    def set_a(self, a_instance):
        self.a = a_instance
```

### 7. Incorrect Inheritance and super() Usage

#### ❌ Error Example of Incorrect Inheritance and super() Usage

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        # Forgot to call parent constructor
        self.breed = breed
    
    def speak(self):
        # Wrong way to call parent method
        return Animal.speak(self) + " - Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # AttributeError: 'Dog' object has no attribute 'name'
```

#### ✅ Correct Solution of Incorrect Inheritance and super() Usage

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
    
    def speak(self):
        parent_sound = super().speak()  # Correct way to call parent method
        return parent_sound + " - Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # Buddy
print(dog.speak())  # Buddy makes a sound - Woof!
```

### 8. Memory Leaks with Circular References

#### ❌ Error Example of Memory Leaks with Circular References

```python
class Parent:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self  # Circular reference

class Child:
    def __init__(self, name):
        self.name = name
        self.parent = None

# This creates circular references that may not be garbage collected
parent = Parent("John")
child = Child("Jane")
parent.add_child(child)
```

#### ✅ Better Solution

```python
import weakref

class Parent:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = weakref.ref(self)  # Weak reference

class Child:
    def __init__(self, name):
        self.name = name
        self.parent = None
    
    def get_parent(self):
        if self.parent is not None:
            return self.parent()  # Call weak reference
        return None

# Better memory management
parent = Parent("John")
child = Child("Jane")
parent.add_child(child)
print(child.get_parent().name)  # John
```

### 9. Debugging Tips and Best Practices

#### Use `*__str__*` and `*__repr__*` for Better Debugging

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

point = Point(3, 4)
print(point)  # Point(3, 4)
print(repr(point))  # Point(x=3, y=4)
print([point])  # [Point(x=3, y=4)]
```

#### Use Type Hints for Better Code Documentation

```python
from typing import List, Optional

class Student:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.grades: List[float] = []
    
    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)
    
    def get_average(self) -> Optional[float]:
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)
```

### 10. Common AttributeError Solutions

#### Problem and Solution

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Common errors and solutions:
rect = Rectangle(5, 3)

# Error: Typo in attribute name
try:
    print(rect.widht)  # AttributeError: 'Rectangle' object has no attribute 'widht'
except AttributeError as e:
    print(f"Error: {e}")
    print(f"Available attributes: {dir(rect)}")

# Solution: Use hasattr() for safety
if hasattr(rect, 'width'):
    print(f"Width: {rect.width}")

# Solution: Use getattr() with default
width = getattr(rect, 'width', 0)
unknown = getattr(rect, 'unknown_attr', 'Not found')
print(f"Width: {width}, Unknown: {unknown}")
```
