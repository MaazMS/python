# Encapsulation in Python - Complete Guide

## 1. Encapsulation Definition and Characteristics

### What is Encapsulation?

Encapsulation is one of the four fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit called a class, while restricting direct access to some of the object's components.

### Key Characteristics of Encapsulation

1. **Data Hiding**: Internal data is hidden from external access
2. **Access Control**: Controlled access to data through methods
3. **Data Integrity**: Prevents unauthorized modification of data
4. **Modularity**: Code is organized into logical units
5. **Security**: Protects sensitive information from external interference

### Benefits of Encapsulation

- **Security**: Sensitive data is protected from unauthorized access
- **Flexibility**: Internal implementation can be changed without affecting external code
- **Maintainability**: Code is easier to maintain and debug
- **Reusability**: Encapsulated code can be reused in different contexts

### Example - Basic Encapsulation

```python
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance        # Private attribute
    
    def get_balance(self):
        """Public method to access private balance"""
        return self.__balance
    
    def deposit(self, amount):
        """Public method to modify private balance"""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Public method with validation"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

# Usage
account = BankAccount("123456", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)    # This would cause an AttributeError
```

## 2. Encapsulation Operations

### 2.1 Private Fields and Name Mangling

#### Creating Private Fields

Use double underscore (`__`) before field names to make them private.

```python
class Student:
    def __init__(self, name, roll_no, grade):
        self.__name = name        # Private field
        self.__roll_no = roll_no  # Private field
        self.__grade = grade      # Private field
        self.school = "ABC School"  # Public field
    
    def display_info(self):
        """Method to access private fields within the class"""
        print(f"Name: {self.__name}")
        print(f"Roll No: {self.__roll_no}")
        print(f"Grade: {self.__grade}")

# Usage
student = Student("Maaz", 123, "A")
student.display_info()
print(student.school)  # Accessible (public)
# print(student.__name)  # AttributeError: 'Student' object has no attribute '__name'
```

#### Name Mangling Access

Python uses name mangling to access private fields from outside the class.

```python
class Student:
    def __init__(self):
        self.__name = "Maaz"
        self.__roll_no = 123

student = Student()
# Accessing private fields using name mangling
print(student._Student__name)     # Output: Maaz
print(student._Student__roll_no)  # Output: 123

# Note: This breaks encapsulation and should be avoided in production code
```

### 2.2 Protected Fields (Single Underscore)

```python
class Vehicle:
    def __init__(self, make, model):
        self._make = make      # Protected field (convention)
        self._model = model    # Protected field (convention)
        self.__engine_id = "ENG123"  # Private field
    
    def _internal_method(self):
        """Protected method - intended for internal use"""
        return f"Internal processing for {self._make} {self._model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors
    
    def get_info(self):
        # Can access protected fields from parent class
        return f"{self._make} {self._model} with {self.doors} doors"

# Usage
car = Car("Toyota", "Camry", 4)
print(car.get_info())  # Works fine
print(car._make)       # Accessible but not recommended
# print(car.__engine_id)  # AttributeError
```

### 2.3 Data Validation Operations

```python
class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = 0
        self.set_salary(salary)  # Use setter for validation
    
    def set_salary(self, salary):
        """Setter with validation"""
        if isinstance(salary, (int, float)) and salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be a non-negative number")
    
    def get_salary(self):
        """Getter for salary"""
        return self.__salary
    
    def set_name(self, name):
        """Setter with validation"""
        if isinstance(name, str) and len(name.strip()) > 0:
            self.__name = name.strip()
        else:
            raise ValueError("Name must be a non-empty string")
    
    def get_name(self):
        """Getter for name"""
        return self.__name

# Usage with validation
emp = Employee(101, "John Doe", 50000)
print(emp.get_salary())  # Output: 50000

try:
    emp.set_salary(-1000)  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

## 3. Encapsulation Methods

### 3.1 Traditional Getter and Setter Methods

```python
class Rectangle:
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.set_width(width)
        self.set_height(height)
    
    # Getter methods
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    # Setter methods with validation
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be positive")
    
    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be positive")
    
    def get_area(self):
        return self.__width * self.__height
    
    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

# Usage
rect = Rectangle(5, 3)
print(f"Area: {rect.get_area()}")        # Output: Area: 15
print(f"Perimeter: {rect.get_perimeter()}")  # Output: Perimeter: 16

rect.set_width(10)
print(f"New Area: {rect.get_area()}")    # Output: New Area: 30
```

### 3.2 Property Decorators (Pythonic Approach)

```python
class Circle:
    def __init__(self, radius):
        self.__radius = 0
        self.radius = radius  # Use property setter
    
    @property
    def radius(self):
        """Getter for radius"""
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        """Setter for radius with validation"""
        if isinstance(value, (int, float)) and value > 0:
            self.__radius = value
        else:
            raise ValueError("Radius must be a positive number")
    
    @property
    def area(self):
        """Computed property for area"""
        return 3.14159 * self.__radius ** 2
    
    @property
    def circumference(self):
        """Computed property for circumference"""
        return 2 * 3.14159 * self.__radius
    
    @property
    def diameter(self):
        """Computed property for diameter"""
        return 2 * self.__radius

# Usage - Properties can be accessed like attributes
circle = Circle(5)
print(f"Radius: {circle.radius}")           # Output: Radius: 5
print(f"Area: {circle.area:.2f}")          # Output: Area: 78.54
print(f"Circumference: {circle.circumference:.2f}")  # Output: Circumference: 31.42

circle.radius = 10  # Uses setter
print(f"New Area: {circle.area:.2f}")      # Output: New Area: 314.16

try:
    circle.radius = -5  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

### 3.3 Read-Only Properties

```python
class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_year = birth_year
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def full_name(self):
        """Read-only computed property"""
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def birth_year(self):
        return self.__birth_year
    
    @property
    def age(self):
        """Read-only computed property"""
        import datetime
        return datetime.datetime.now().year - self.__birth_year

# Usage
person = Person("John", "Smith", 1990)
print(person.full_name)  # Output: John Smith
print(person.age)        # Output: Current age

# person.full_name = "Jane Doe"  # AttributeError: can't set attribute
```

### 3.4 Class Methods and Static Methods for Encapsulation

```python
class MathUtils:
    __PI = 3.14159  # Private class variable
    
    def __init__(self, value):
        self.__value = value
    
    @classmethod
    def get_pi(cls):
        """Class method to access private class variable"""
        return cls.__PI
    
    @staticmethod
    def is_even(number):
        """Static method for utility function"""
        return number % 2 == 0
    
    def calculate_circle_area(self, radius):
        """Instance method using private class variable"""
        return self.__PI * radius ** 2

# Usage
math_obj = MathUtils(10)
print(MathUtils.get_pi())  # Output: 3.14159
print(MathUtils.is_even(4))  # Output: True
print(math_obj.calculate_circle_area(5))  # Output: 78.53975
```

## 4. Common Errors in Encapsulation

### 4.1 Error: Direct Access to Private Attributes

**Wrong Approach:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

account = BankAccount(1000)
# ERROR: Trying to access private attribute directly
try:
    print(account.__balance)  # AttributeError
except AttributeError as e:
    print(f"Error: {e}")
```

**Correct Approach:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())  # Correct way: 1000
```

### 4.2 Error: Missing Validation in Setters

**Wrong Approach:**

```python
class Student:
    def __init__(self, age):
        self.__age = age
    
    def set_age(self, age):
        # ERROR: No validation
        self.__age = age

student = Student(20)
student.set_age(-5)  # Invalid age accepted
```

**Correct Approach:**

```python
class Student:
    def __init__(self, age):
        self.__age = 0
        self.set_age(age)  # Use setter for validation
    
    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 150:
            self.__age = age
        else:
            raise ValueError("Age must be between 0 and 150")
    
    def get_age(self):
        return self.__age

student = Student(20)
try:
    student.set_age(-5)  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

### 4.3 Error: Inconsistent Access Patterns

**Wrong Approach:**

```python
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    # ERROR: Inconsistent - no getter for price
    def set_price(self, price):
        self.__price = price

product = Product("Laptop", 1000)
# Can get name but not price - inconsistent interface
```

**Correct Approach:**

```python
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = 0
        self.set_price(price)
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Price cannot be negative")

# Or better yet, use properties for consistency
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = 0
        self.price = price  # Use property setter
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price cannot be negative")
```

### 4.4 Error: Breaking Encapsulation with Name Mangling

**Wrong Approach:**

```python
class SecureData:
    def __init__(self, secret):
        self.__secret = secret

data = SecureData("top_secret")
# ERROR: Breaking encapsulation using name mangling
print(data._SecureData__secret)  # Should not do this!
```

**Correct Approach:**

```python
class SecureData:
    def __init__(self, secret):
        self.__secret = secret
    
    def get_secret(self, authorized=False):
        if authorized:
            return self.__secret
        else:
            return "Access Denied"

data = SecureData("top_secret")
print(data.get_secret(authorized=True))   # Controlled access
print(data.get_secret(authorized=False))  # Access Denied
```

### 4.5 Error: Not Using Properties When Appropriate

**Wrong Approach:**

```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def get_celsius(self):
        return self.__celsius
    
    def set_celsius(self, value):
        self.__celsius = value
    
    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

temp = Temperature(25)
# Verbose and not Pythonic
print(temp.get_celsius())
print(temp.get_fahrenheit())
```

**Correct Approach:**

```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self.__celsius = value
    
    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
# Clean and Pythonic
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 86
print(temp.celsius)     # 30.0
```

### 4.6 Best Practices Summary

1. **Use properties instead of getter/setter methods** for a more Pythonic approach
2. **Always validate data** in setters to maintain data integrity
3. **Provide consistent interfaces** - if you have a setter, provide a getter
4. **Don't break encapsulation** by accessing private attributes directly
5. **Use meaningful names** for your methods and properties
6. **Document your code** to explain the purpose of encapsulation
7. **Consider using `@property` decorators** for computed values
8. **Validate input parameters** in constructors and methods
