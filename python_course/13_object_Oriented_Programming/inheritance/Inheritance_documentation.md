# Inheritance in Python - Complete Guide

## 1. Inheritance Definition and Characteristics

### What is Inheritance?

Inheritance is one of the four fundamental principles of Object-Oriented Programming (OOP). It is the process of defining a new class (child/derived class) based on an existing class (parent/base class), allowing the child class to inherit attributes and methods from the parent class while adding its own unique features.

### Key Characteristics of Inheritance

1. **Code Reusability**: Inherit existing functionality without rewriting code
2. **IS-A Relationship**: Establishes a relationship where child "is a" type of parent (e.g., Car is a Vehicle)
3. **Hierarchical Structure**: Creates a hierarchy of classes from general to specific
4. **Method Overriding**: Child classes can provide specific implementations of parent methods
5. **Extensibility**: Child classes can add new attributes and methods

### Benefits of Inheritance

- **Code Reusability**: Reduces code duplication and development time
- **Maintainability**: Changes in parent class automatically reflect in child classes
- **Polymorphism**: Objects of different classes can be treated uniformly
- **Modularity**: Promotes organized and structured code design
- **Extensibility**: Easy to add new features by extending existing classes

### Example - Basic Inheritance

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        print(f"{self.name} barks: Woof! Woof!")
    
    def fetch(self):  # New method specific to Dog
        print(f"{self.name} is fetching the ball")

# Usage
dog = Dog("Buddy", "Golden Retriever")
dog.eat()        # Inherited from Animal
dog.sleep()      # Inherited from Animal
dog.make_sound() # Overridden in Dog
dog.fetch()      # Specific to Dog

print(f"Name: {dog.name}, Species: {dog.species}, Breed: {dog.breed}")
```

## 2. Inheritance Operations

### 2.1 Types of Inheritance

#### Single Inheritance

One child class inherits from one parent class.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f"{self.make} {self.model} engine started")
    
    def stop_engine(self):
        print(f"{self.make} {self.model} engine stopped")

class Car(Vehicle):  # Single inheritance
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def open_trunk(self):
        print("Trunk opened")
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model} with {self.doors} doors"

# Usage
car = Car("Toyota", "Camry", 2023, 4)
car.start_engine()  # Inherited method
car.open_trunk()    # Car-specific method
print(car.get_info())
```

#### Multiple Inheritance

One child class inherits from multiple parent classes.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Flyable:
    def fly(self):
        print("Flying in the sky")
    
    def land(self):
        print("Landing safely")

class Swimmable:
    def swim(self):
        print("Swimming in water")
    
    def dive(self):
        print("Diving underwater")

class Duck(Animal, Flyable, Swimmable):  # Multiple inheritance
    def __init__(self, name):
        Animal.__init__(self, name, "Bird")  # Call specific parent constructor
    
    def make_sound(self):
        print(f"{self.name} quacks: Quack! Quack!")

# Usage
duck = Duck("Donald")
duck.fly()        # From Flyable
duck.swim()       # From Swimmable
duck.make_sound() # Overridden in Duck

# Check Method Resolution Order (MRO)
print(Duck.__mro__)
```

#### Multilevel Inheritance

A chain of inheritance where a child becomes a parent for another child.

```python
class Vehicle:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
    
    def start(self):
        print("Vehicle started")

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, fuel_type, doors):
        super().__init__(fuel_type)
        self.doors = doors
    
    def drive(self):
        print("Car is driving")

class SportsCar(Car):  # SportsCar inherits from Car (which inherits from Vehicle)
    def __init__(self, fuel_type, doors, top_speed):
        super().__init__(fuel_type, doors)
        self.top_speed = top_speed
    
    def race(self):
        print(f"Racing at {self.top_speed} mph!")

# Usage
sports_car = SportsCar("Gasoline", 2, 200)
sports_car.start()  # From Vehicle
sports_car.drive()  # From Car
sports_car.race()   # From SportsCar
```

#### Hierarchical Inheritance

Multiple child classes inherit from a single parent class.

```python
class Shape:
    def __init__(self, color):
        self.color = color
    
    def display_color(self):
        print(f"Color: {self.color}")

class Rectangle(Shape):  # Rectangle inherits from Shape
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):  # Circle also inherits from Shape
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):  # Triangle also inherits from Shape
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Usage
shapes = [
    Rectangle("Red", 5, 3),
    Circle("Blue", 4),
    Triangle("Green", 6, 4)
]

for shape in shapes:
    shape.display_color()  # Common method from Shape
    print(f"Area: {shape.area()}")  # Specific implementation in each child
    print()
```

#### Hybrid Inheritance

Combination of multiple inheritance types.

```python
class Device:
    def __init__(self, brand):
        self.brand = brand
    
    def power_on(self):
        print(f"{self.brand} device powered on")

class Phone(Device):  # Single inheritance
    def __init__(self, brand, phone_number):
        super().__init__(brand)
        self.phone_number = phone_number
    
    def make_call(self):
        print(f"Making call from {self.phone_number}")

class Camera(Device):  # Single inheritance
    def __init__(self, brand, megapixels):
        super().__init__(brand)
        self.megapixels = megapixels
    
    def take_photo(self):
        print(f"Taking {self.megapixels}MP photo")

class SmartPhone(Phone, Camera):  # Multiple inheritance (Hybrid)
    def __init__(self, brand, phone_number, megapixels, os):
        Phone.__init__(self, brand, phone_number)
        Camera.__init__(self, brand, megapixels)
        self.os = os
    
    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.os}")

# Usage
smartphone = SmartPhone("Apple", "+1234567890", 12, "iOS")
smartphone.power_on()      # From Device
smartphone.make_call()     # From Phone
smartphone.take_photo()    # From Camera
smartphone.install_app("Instagram")  # From SmartPhone
```

### 2.2 Method Resolution Order (MRO)

```python
class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):  # Multiple inheritance
    pass

# Check MRO
print("MRO for class D:", D.__mro__)
print("MRO for class D (readable):", [cls.__name__ for cls in D.__mro__])

# Method resolution follows MRO
obj = D()
obj.method()  # Will call B's method (B comes before C in MRO)
```

### 2.3 isinstance() and issubclass()

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

puppy = Puppy()

# isinstance() - checks if object is instance of class
print(isinstance(puppy, Puppy))   # True
print(isinstance(puppy, Dog))     # True
print(isinstance(puppy, Animal))  # True
print(isinstance(puppy, str))     # False

# issubclass() - checks if class is subclass of another class
print(issubclass(Puppy, Dog))     # True
print(issubclass(Dog, Animal))    # True
print(issubclass(Puppy, Animal))  # True
print(issubclass(Animal, Dog))    # False
```

## 3. Inheritance Methods

### 3.1 The super() Function

The `super()` function provides access to methods in a parent class from a child class.

#### Basic super() Usage

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.first_name} {self.last_name}, {self.age} years old")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! Now {self.age} years old")

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, major):
        super().__init__(first_name, last_name, age)  # Call parent constructor
        self.student_id = student_id
        self.major = major
        self.grades = []
    
    def introduce(self):
        super().introduce()  # Call parent method
        print(f"I'm studying {self.major}, Student ID: {self.student_id}")
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_gpa(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0.0

# Usage
student = Student("Alice", "Johnson", 20, "S12345", "Computer Science")
student.introduce()  # Calls both parent and child methods
student.add_grade(3.8)
student.add_grade(3.9)
print(f"GPA: {student.get_gpa():.2f}")
```

#### super() in Multiple Inheritance

```python
class A:
    def __init__(self, a_value):
        self.a_value = a_value
        print(f"A.__init__ called with {a_value}")
    
    def method(self):
        print("A.method called")

class B(A):
    def __init__(self, a_value, b_value):
        super().__init__(a_value)
        self.b_value = b_value
        print(f"B.__init__ called with {b_value}")
    
    def method(self):
        super().method()
        print("B.method called")

class C(A):
    def __init__(self, a_value, c_value):
        super().__init__(a_value)
        self.c_value = c_value
        print(f"C.__init__ called with {c_value}")
    
    def method(self):
        super().method()
        print("C.method called")

class D(B, C):
    def __init__(self, a_value, b_value, c_value, d_value):
        # This follows MRO: D -> B -> C -> A
        super().__init__(a_value, b_value)
        self.c_value = c_value  # Manually set C's attribute
        self.d_value = d_value
        print(f"D.__init__ called with {d_value}")
    
    def method(self):
        super().method()
        print("D.method called")

# Usage
obj = D(1, 2, 3, 4)
print("\nCalling method:")
obj.method()
```

### 3.2 Method Overriding

Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        print(f"{self.make} {self.model} is starting...")
    
    def stop(self):
        print(f"{self.make} {self.model} is stopping...")
    
    def get_info(self):
        return f"{self.make} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
        self.charge_level = 100
    
    def start(self):  # Override parent method
        if self.charge_level > 0:
            print(f"{self.make} {self.model} is starting silently... (Electric)")
        else:
            print("Cannot start: Battery is empty!")
    
    def stop(self):  # Override parent method
        super().stop()  # Call parent method first
        print("Regenerative braking activated")
    
    def charge(self):
        self.charge_level = 100
        print(f"Battery charged to {self.charge_level}%")
    
    def get_info(self):  # Override parent method
        base_info = super().get_info()  # Get parent info
        return f"{base_info} (Electric, {self.battery_capacity}kWh battery)"

# Usage
electric_car = ElectricCar("Tesla", "Model 3", 75)
print(electric_car.get_info())
electric_car.start()
electric_car.stop()
electric_car.charge()
```

### 3.3 Abstract Base Classes and Method Enforcement

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        """Must be implemented by child classes"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Must be implemented by child classes"""
        pass
    
    def display_info(self):  # Concrete method
        print(f"This is a {self.color} shape with area {self.area()}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):  # Must implement abstract method
        return self.width * self.height
    
    def perimeter(self):  # Must implement abstract method
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):  # Must implement abstract method
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):  # Must implement abstract method
        return 2 * 3.14159 * self.radius

# Usage
rectangle = Rectangle("Red", 5, 3)
circle = Circle("Blue", 4)

rectangle.display_info()
circle.display_info()

# This would raise TypeError: Can't instantiate abstract class Shape
# shape = Shape("Green")
```

## 4. Common Errors in Inheritance

### 4.1 Error: Forgetting to Call Parent Constructor

**Wrong Approach:**

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100

class Dog(Animal):
    def __init__(self, name, breed):
        # ERROR: Not calling parent constructor
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
try:
    print(dog.name)  # AttributeError: 'Dog' object has no attribute 'name'
except AttributeError as e:
    print(f"Error: {e}")
```

**Correct Approach:**

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(f"Name: {dog.name}, Species: {dog.species}, Breed: {dog.breed}")
```

### 4.2 Error: Incorrect Multiple Inheritance Constructor Calls

**Wrong Approach:**

```python
class A:
    def __init__(self, a_value):
        self.a_value = a_value

class B:
    def __init__(self, b_value):
        self.b_value = b_value

class C(A, B):
    def __init__(self, a_value, b_value, c_value):
        # ERROR: Only calling one parent constructor
        super().__init__(a_value)
        self.c_value = c_value

obj = C(1, 2, 3)
try:
    print(obj.b_value)  # AttributeError: 'C' object has no attribute 'b_value'
except AttributeError as e:
    print(f"Error: {e}")
```

**Correct Approach:**

```python
class A:
    def __init__(self, a_value):
        self.a_value = a_value

class B:
    def __init__(self, b_value):
        self.b_value = b_value

class C(A, B):
    def __init__(self, a_value, b_value, c_value):
        A.__init__(self, a_value)  # Call A's constructor explicitly
        B.__init__(self, b_value)  # Call B's constructor explicitly
        self.c_value = c_value

obj = C(1, 2, 3)
print(f"A: {obj.a_value}, B: {obj.b_value}, C: {obj.c_value}")
```

### 4.3 Error: Diamond Problem in Multiple Inheritance

**Wrong Approach:**

```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()

class C(A):
    def method(self):
        print("C method")
        super().method()

class D(B, C):
    def method(self):
        print("D method")
        # ERROR: This can cause issues with method resolution
        B.method(self)  # Directly calling B's method
        C.method(self)  # Directly calling C's method

obj = D()
obj.method()  # This will call A.method twice!
```

**Correct Approach:**

```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()

class C(A):
    def method(self):
        print("C method")
        super().method()

class D(B, C):
    def method(self):
        print("D method")
        super().method()  # Let MRO handle the resolution

obj = D()
obj.method()  # Follows MRO: D -> B -> C -> A (A called only once)
print("MRO:", [cls.__name__ for cls in D.__mro__])
```

### 4.4 Error: Overriding Without Proper Understanding

**Wrong Approach:**

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        # ERROR: Completely replacing parent logic without consideration
        self._balance -= amount  # No validation!
        return True

account = SavingsAccount(100)
account.withdraw(500)  # This should fail but doesn't!
print(f"Balance: {account.get_balance()}")  # Negative balance!
```

**Correct Approach:**

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
        self.minimum_balance = 100
    
    def withdraw(self, amount):
        # Override with additional validation
        if self._balance - amount < self.minimum_balance:
            print(f"Cannot withdraw: Minimum balance of ${self.minimum_balance} required")
            return False
        return super().withdraw(amount)  # Call parent method

account = SavingsAccount(150)
account.withdraw(100)  # This will fail due to minimum balance
print(f"Balance: {account.get_balance()}")
```

### 4.5 Error: Not Understanding Method Resolution Order

**Wrong Approach:**

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# ERROR: Assuming C's method will be called because it's "closer" to A
obj = D()
result = obj.method()
print(f"Expected C, got: {result}")  # Actually returns "B"
```

**Correct Approach:**

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

obj = D()
print("MRO:", [cls.__name__ for cls in D.__mro__])  # Understand the order
result = obj.method()
print(f"Result: {result}")  # Returns "B" because B comes before C in MRO

# If you want C's method, change the inheritance order:
class D2(C, B):  # C comes before B
    pass

obj2 = D2()
result2 = obj2.method()
print(f"Result with changed order: {result2}")  # Returns "C"
```

### 4.6 Best Practices Summary

1. **Always call parent constructors** using `super().__init__()` or explicit calls
2. **Understand Method Resolution Order (MRO)** in multiple inheritance scenarios
3. **Use super() consistently** instead of direct parent class calls
4. **Override methods thoughtfully** - consider calling parent methods when appropriate
5. **Avoid deep inheritance hierarchies** - prefer composition over inheritance when possible
6. **Use abstract base classes** to enforce method implementation in child classes
7. **Be careful with multiple inheritance** - understand the diamond problem
8. **Test inheritance relationships** using `isinstance()` and `issubclass()`
9. **Document inheritance relationships** clearly in your code
10. **Consider using mixins** for shared functionality across unrelated classes
