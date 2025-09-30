# Polymorphism in Python - Complete Guide

## 1. Polymorphism Definition and Characteristics

### What is Polymorphism?

Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP). The word "polymorphism" comes from Greek: "poly" means many and "morphism" means forms. It refers to the ability of different objects to respond to the same interface or method call in their own specific way, allowing a single interface to represent different underlying data types or classes.

### Key Characteristics of Polymorphism

1. **Same Interface, Different Behavior**: Multiple classes can implement the same method with different behaviors
2. **Runtime Method Resolution**: The actual method called is determined at runtime based on the object type
3. **Code Flexibility**: Allows writing more generic and flexible code
4. **Dynamic Typing**: Python's dynamic nature makes polymorphism easier to implement
5. **Abstraction**: Hides implementation details behind a common interface

### Benefits of Polymorphism

- **Code Reusability**: Write code that works with multiple types
- **Maintainability**: Easy to add new types without changing existing code
- **Flexibility**: Allows for dynamic behavior based on object types
- **Extensibility**: New classes can be added that work with existing polymorphic code
- **Abstraction**: Focus on what objects can do rather than what they are

### Example - Basic Polymorphism

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass  # To be overridden by child classes

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says: Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says: Meow! Meow!"

class Cow(Animal):
    def make_sound(self):
        return f"{self.name} says: Moo! Moo!"

# Polymorphic function - same interface, different behaviors
def animal_sound(animal):
    return animal.make_sound()

# Usage - Same function works with different animal types
animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Bessie")]

for animal in animals:
    print(animal_sound(animal))
    # Output:
    # Buddy says: Woof! Woof!
    # Whiskers says: Meow! Meow!
    # Bessie says: Moo! Moo!
```

## 2. Polymorphism Operations

### 2.1 Duck Typing

Duck typing is Python's approach to polymorphism: "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

#### Basic Duck Typing

```python
class Duck:
    def fly(self):
        print("Duck flying")
    
    def swim(self):
        print("Duck swimming")
    
    def quack(self):
        print("Quack! Quack!")

class Airplane:
    def fly(self):
        print("Airplane flying")
    
    def swim(self):
        print("Airplane cannot swim!")

class Fish:
    def swim(self):
        print("Fish swimming")
    
    def fly(self):
        print("Fish cannot fly!")

# Polymorphic functions using duck typing
def make_it_fly(obj):
    obj.fly()  # Calls fly() method regardless of object type

def make_it_swim(obj):
    obj.swim()  # Calls swim() method regardless of object type

# Usage
duck = Duck()
plane = Airplane()
fish = Fish()

# All objects can "fly" (have fly method)
make_it_fly(duck)    # Duck flying
make_it_fly(plane)   # Airplane flying
make_it_fly(fish)    # Fish cannot fly!

# All objects can "swim" (have swim method)
make_it_swim(duck)   # Duck swimming
make_it_swim(plane)  # Airplane cannot swim!
make_it_swim(fish)   # Fish swimming
```

#### Advanced Duck Typing with Multiple Methods

```python
class FileWriter:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)
    
    def close(self):
        print(f"File {self.filename} closed")

class DatabaseWriter:
    def __init__(self, connection_string):
        self.connection = connection_string
    
    def write(self, data):
        print(f"Writing '{data}' to database: {self.connection}")
    
    def close(self):
        print("Database connection closed")

class NetworkWriter:
    def __init__(self, url):
        self.url = url
    
    def write(self, data):
        print(f"Sending '{data}' to {self.url}")
    
    def close(self):
        print("Network connection closed")

# Polymorphic function that works with any "writer-like" object
def save_data(writer, data):
    writer.write(data)
    writer.close()

# Usage - Same function works with different writer types
writers = [
    FileWriter("output.txt"),
    DatabaseWriter("postgresql://localhost:5432/mydb"),
    NetworkWriter("https://api.example.com/data")
]

for writer in writers:
    save_data(writer, "Hello, World!")
```

### 2.2 Operator Overloading

Python allows operators to behave differently based on the operands through special methods (magic methods).

#### Basic Operator Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Overload - operator"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Overload * operator for scalar multiplication"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Overload == operator"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

# Usage
v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1 + v2)  # Vector(3, 7)
print(v1 - v2)  # Vector(1, -1)
print(v1 * 3)   # Vector(6, 9)
print(v1 == v2) # False

# The same + operator behaves differently based on operands
print(5 + 3)        # Integer addition: 8
print("Hello" + " World")  # String concatenation: Hello World
print([1, 2] + [3, 4])     # List concatenation: [1, 2, 3, 4]
print(v1 + v2)      # Vector addition: Vector(3, 7)
```

#### Comprehensive Operator Overloading Example

```python
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot add different currencies")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot subtract different currencies")
            return Money(self.amount - other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency)
        return NotImplemented
    
    def __mul__(self, multiplier):
        if isinstance(multiplier, (int, float)):
            return Money(self.amount * multiplier, self.currency)
        return NotImplemented
    
    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Money(self.amount / divisor, self.currency)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount < other.amount
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount <= other.amount
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount > other.amount
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount >= other.amount
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return False
    
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

# Usage
money1 = Money(100.50)
money2 = Money(50.25)

print(money1 + money2)    # USD 150.75
print(money1 - money2)    # USD 50.25
print(money1 * 2)         # USD 201.00
print(money1 / 2)         # USD 50.25

print(money1 > money2)    # True
print(money1 == money2)   # False

# Polymorphic behavior - same operators, different meanings
print(10 + 20)           # Integer addition: 30
print("Hello" + "World") # String concatenation: HelloWorld
print(money1 + money2)   # Money addition: USD 150.75
```

### 2.3 Method Overriding Polymorphism

Method overriding allows child classes to provide specific implementations of methods defined in parent classes.

#### Basic Method Overriding

```python
class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method")
    
    def describe(self):
        return f"A {self.color} shape with area {self.area()}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):  # Override parent method
        return self.width * self.height
    
    def perimeter(self):  # Override parent method
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):  # Override parent method
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):  # Override parent method
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, color, base, height, side1, side2):
        super().__init__(color)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):  # Override parent method
        return 0.5 * self.base * self.height
    
    def perimeter(self):  # Override parent method
        return self.base + self.side1 + self.side2

# Polymorphic function - works with any Shape
def print_shape_info(shape):
    print(f"Shape: {type(shape).__name__}")
    print(f"Color: {shape.color}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print(f"Description: {shape.describe()}")
    print("-" * 40)

# Usage - Same function works with different shape types
shapes = [
    Rectangle("Red", 5, 3),
    Circle("Blue", 4),
    Triangle("Green", 6, 4, 5, 5)
]

for shape in shapes:
    print_shape_info(shape)
```

### 2.4 Interface-like Polymorphism with Abstract Base Classes

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id):
        pass
    
    def log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type}: ${amount}")

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        self.log_transaction("Credit Card Payment", amount)
        return f"Processed ${amount} via Credit Card ending in {self.card_number[-4:]}"
    
    def refund_payment(self, transaction_id):
        self.log_transaction("Credit Card Refund", 0)
        return f"Refunded transaction {transaction_id} to Credit Card"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        self.log_transaction("PayPal Payment", amount)
        return f"Processed ${amount} via PayPal account {self.email}"
    
    def refund_payment(self, transaction_id):
        self.log_transaction("PayPal Refund", 0)
        return f"Refunded transaction {transaction_id} to PayPal account"

class CryptoProcessor(PaymentProcessor):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def process_payment(self, amount):
        self.log_transaction("Crypto Payment", amount)
        return f"Processed ${amount} via Crypto wallet {self.wallet_address[:10]}..."
    
    def refund_payment(self, transaction_id):
        self.log_transaction("Crypto Refund", 0)
        return f"Refunded transaction {transaction_id} to Crypto wallet"

# Polymorphic payment processing
def process_order_payment(processor, amount):
    result = processor.process_payment(amount)
    print(result)
    return result

# Usage - Same function works with different payment processors
processors = [
    CreditCardProcessor("1234567890123456"),
    PayPalProcessor("user@example.com"),
    CryptoProcessor("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
]

for processor in processors:
    process_order_payment(processor, 99.99)
    print()
```

## 3. Polymorphism Methods

### 3.1 Duck Typing Implementation Patterns

#### Protocol-based Duck Typing

```python
# Define a protocol (informal interface)
class Drawable:
    """Protocol for objects that can be drawn"""
    def draw(self):
        raise NotImplementedError

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        return f"Drawing a circle with radius {self.radius}"

class Square:
    def __init__(self, side):
        self.side = side
    
    def draw(self):
        return f"Drawing a square with side {self.side}"

class Text:
    def __init__(self, content):
        self.content = content
    
    def draw(self):
        return f"Drawing text: '{self.content}'"

# Duck typing function - works with any object that has draw() method
def render_objects(objects):
    for obj in objects:
        # Duck typing: if it has draw(), we can call it
        if hasattr(obj, 'draw') and callable(getattr(obj, 'draw')):
            print(obj.draw())
        else:
            print(f"Object {type(obj).__name__} cannot be drawn")

# Usage
drawable_objects = [
    Circle(5),
    Square(4),
    Text("Hello World"),
    "Not drawable"  # This will be handled gracefully
]

render_objects(drawable_objects)
```

#### Dependency Injection with Duck Typing

```python
class EmailNotifier:
    def __init__(self, smtp_server):
        self.smtp_server = smtp_server
    
    def send(self, message, recipient):
        print(f"Sending email to {recipient} via {self.smtp_server}: {message}")

class SMSNotifier:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def send(self, message, recipient):
        print(f"Sending SMS to {recipient} via API: {message}")

class PushNotifier:
    def __init__(self, app_id):
        self.app_id = app_id
    
    def send(self, message, recipient):
        print(f"Sending push notification to {recipient} via app {self.app_id}: {message}")

class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier  # Dependency injection
    
    def notify_user(self, user_id, message):
        # Duck typing - any object with send() method will work
        self.notifier.send(message, user_id)
    
    def set_notifier(self, notifier):
        """Runtime polymorphism - change behavior at runtime"""
        self.notifier = notifier

# Usage - Same service, different notification methods
email_notifier = EmailNotifier("smtp.gmail.com")
sms_notifier = SMSNotifier("API_KEY_123")
push_notifier = PushNotifier("APP_ID_456")

# Create service with email notifier
service = NotificationService(email_notifier)
service.notify_user("user@example.com", "Welcome!")

# Change to SMS notifier at runtime
service.set_notifier(sms_notifier)
service.notify_user("+1234567890", "Your order is ready!")

# Change to push notifier at runtime
service.set_notifier(push_notifier)
service.notify_user("user_123", "New message received!")
```

### 3.2 Method Overriding Patterns

#### Template Method Pattern

```python
class DataProcessor:
    """Template method pattern using polymorphism"""
    
    def process_data(self, data):
        """Template method - defines the algorithm structure"""
        cleaned_data = self.clean_data(data)
        validated_data = self.validate_data(cleaned_data)
        processed_data = self.transform_data(validated_data)
        self.save_data(processed_data)
        return processed_data
    
    def clean_data(self, data):
        """Default implementation - can be overridden"""
        print("Performing basic data cleaning")
        return [item.strip() if isinstance(item, str) else item for item in data]
    
    def validate_data(self, data):
        """Abstract method - must be overridden"""
        raise NotImplementedError("Subclasses must implement validate_data")
    
    def transform_data(self, data):
        """Abstract method - must be overridden"""
        raise NotImplementedError("Subclasses must implement transform_data")
    
    def save_data(self, data):
        """Default implementation - can be overridden"""
        print(f"Saving {len(data)} items to default storage")

class CSVProcessor(DataProcessor):
    def validate_data(self, data):
        print("Validating CSV data format")
        # Remove empty strings
        return [item for item in data if item]
    
    def transform_data(self, data):
        print("Transforming CSV data")
        # Convert to uppercase
        return [item.upper() if isinstance(item, str) else item for item in data]
    
    def save_data(self, data):
        print(f"Saving {len(data)} items to CSV file")

class JSONProcessor(DataProcessor):
    def clean_data(self, data):
        print("Performing JSON-specific data cleaning")
        # Custom cleaning for JSON
        return super().clean_data(data)
    
    def validate_data(self, data):
        print("Validating JSON data format")
        # JSON-specific validation
        return [item for item in data if isinstance(item, (str, int, float))]
    
    def transform_data(self, data):
        print("Transforming JSON data")
        # Convert to dictionary format
        return [{"value": item} for item in data]
    
    def save_data(self, data):
        print(f"Saving {len(data)} items to JSON file")

# Usage - Same algorithm, different implementations
data = ["  apple  ", "banana", "", "cherry", 123, None]

csv_processor = CSVProcessor()
json_processor = JSONProcessor()

print("=== CSV Processing ===")
csv_result = csv_processor.process_data(data.copy())
print(f"Result: {csv_result}\n")

print("=== JSON Processing ===")
json_result = json_processor.process_data(data.copy())
print(f"Result: {json_result}")
```

### 3.3 Operator Overloading Patterns

#### Fluent Interface with Operator Overloading

```python
class QueryBuilder:
    def __init__(self, table=None):
        self.table = table
        self.conditions = []
        self.fields = ["*"]
        self.order_by_clause = None
        self.limit_clause = None
    
    def __call__(self, table):
        """Make the object callable"""
        return QueryBuilder(table)
    
    def select(self, *fields):
        self.fields = list(fields)
        return self
    
    def where(self, condition):
        self.conditions.append(condition)
        return self
    
    def __and__(self, other):
        """Overload & operator for AND conditions"""
        if isinstance(other, QueryBuilder):
            new_builder = QueryBuilder(self.table)
            new_builder.fields = self.fields
            new_builder.conditions = self.conditions + other.conditions
            return new_builder
        return NotImplemented
    
    def __or__(self, other):
        """Overload | operator for OR conditions"""
        if isinstance(other, QueryBuilder):
            new_builder = QueryBuilder(self.table)
            new_builder.fields = self.fields
            new_builder.conditions = [f"({' AND '.join(self.conditions)}) OR ({' AND '.join(other.conditions)})"]
            return new_builder
        return NotImplemented
    
    def order_by(self, field, direction="ASC"):
        self.order_by_clause = f"ORDER BY {field} {direction}"
        return self
    
    def limit(self, count):
        self.limit_clause = f"LIMIT {count}"
        return self
    
    def __str__(self):
        query = f"SELECT {', '.join(self.fields)} FROM {self.table}"
        
        if self.conditions:
            query += f" WHERE {' AND '.join(self.conditions)}"
        
        if self.order_by_clause:
            query += f" {self.order_by_clause}"
        
        if self.limit_clause:
            query += f" {self.limit_clause}"
        
        return query

# Usage - Fluent interface with operator overloading
query = QueryBuilder()

# Basic query
simple_query = query("users").select("name", "email").where("age > 18")
print(simple_query)

# Complex query with operators
complex_query = (query("users").select("*").where("age > 18") & 
                query("users").where("status = 'active'")).limit(10)
print(complex_query)

# OR query
or_query = (query("users").where("role = 'admin'") | 
           query("users").where("role = 'moderator'"))
print(or_query)
```

### 3.4 Runtime Polymorphism with Strategy Pattern

```python
class SortingStrategy:
    def sort(self, data):
        raise NotImplementedError

class BubbleSort(SortingStrategy):
    def sort(self, data):
        print("Using Bubble Sort")
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class QuickSort(SortingStrategy):
    def sort(self, data):
        print("Using Quick Sort")
        if len(data) <= 1:
            return data
        
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        
        return self.sort(left) + middle + self.sort(right)

class MergeSort(SortingStrategy):
    def sort(self, data):
        print("Using Merge Sort")
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left, right):
        result = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class DataSorter:
    def __init__(self, strategy=None):
        self.strategy = strategy or BubbleSort()
    
    def set_strategy(self, strategy):
        """Runtime polymorphism - change algorithm at runtime"""
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data.copy())

# Usage - Runtime polymorphism with strategy pattern
data = [64, 34, 25, 12, 22, 11, 90]
sorter = DataSorter()

# Start with bubble sort
result1 = sorter.sort_data(data)
print(f"Result: {result1}\n")

# Change to quick sort at runtime
sorter.set_strategy(QuickSort())
result2 = sorter.sort_data(data)
print(f"Result: {result2}\n")

# Change to merge sort at runtime
sorter.set_strategy(MergeSort())
result3 = sorter.sort_data(data)
print(f"Result: {result3}")
```

## 4. Common Errors in Polymorphism

### 4.1 Error: Not Implementing Required Methods

**Wrong Approach:**

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # ERROR: Forgot to implement area method

def calculate_total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()  # Will raise NotImplementedError
    return total

rectangle = Rectangle(5, 3)
try:
    calculate_total_area([rectangle])
except NotImplementedError as e:
    print(f"Error: {e}")
```

**Correct Approach:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # Must implement abstract method
        return self.width * self.height

def calculate_total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

rectangle = Rectangle(5, 3)
total_area = calculate_total_area([rectangle])
print(f"Total area: {total_area}")  # Works correctly
```

### 4.2 Error: Incorrect Operator Overloading

**Wrong Approach:**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        # ERROR: Not checking type, not handling edge cases
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
try:
    result = v1 + 5  # TypeError: 'int' object has no attribute 'x'
except TypeError as e:
    print(f"Error: {e}")
```

**Correct Approach:**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented
    
    def __radd__(self, other):
        # Handle reverse addition (5 + vector)
        return self.__add__(other)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1 + v2)  # Vector addition: Vector(3, 7)
print(v1 + 5)   # Scalar addition: Vector(7, 8)
print(5 + v1)   # Reverse addition: Vector(7, 8)
```

### 4.3 Error: Breaking Liskov Substitution Principle

**Wrong Approach:**

```python
class Bird:
    def fly(self):
        return "Flying high in the sky"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"

class Penguin(Bird):
    def fly(self):
        # ERROR: Penguin can't fly, but we're forcing it to "fly"
        raise Exception("Penguins cannot fly!")

def make_bird_fly(bird):
    return bird.fly()

birds = [Sparrow(), Penguin()]

for bird in birds:
    try:
        print(make_bird_fly(bird))
    except Exception as e:
        print(f"Error: {e}")  # Breaks polymorphism
```

**Correct Approach:**

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return self.fly()
    
    def fly(self):
        return "Flying high in the sky"

class SwimmingBird(Bird):
    def move(self):
        return self.swim()
    
    def swim(self):
        return "Swimming in water"

class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow flying"

class Penguin(SwimmingBird):
    def swim(self):
        return "Penguin swimming"

def make_bird_move(bird):
    return bird.move()  # Polymorphic method that works for all birds

birds = [Sparrow(), Penguin()]

for bird in birds:
    print(make_bird_move(bird))  # Works correctly for all birds
```

### 4.4 Error: Inconsistent Method Signatures

**Wrong Approach:**

```python
class PaymentProcessor:
    def process(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount, card_number, cvv):  # ERROR: Different signature
        return f"Processing ${amount} with card {card_number}"

class PayPalProcessor(PaymentProcessor):
    def process(self, amount, email):  # ERROR: Different signature
        return f"Processing ${amount} with PayPal {email}"

def process_payment(processor, amount):
    # ERROR: This will fail because subclasses have different signatures
    return processor.process(amount)

try:
    cc_processor = CreditCardProcessor()
    process_payment(cc_processor, 100)  # TypeError: missing arguments
except TypeError as e:
    print(f"Error: {e}")
```

**Correct Approach:**

```python
class PaymentProcessor:
    def __init__(self, **config):
        self.config = config
    
    def process(self, amount):
        raise NotImplementedError("Subclasses must implement process method")

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number, cvv):
        super().__init__(card_number=card_number, cvv=cvv)
    
    def process(self, amount):  # Same signature as parent
        return f"Processing ${amount} with card {self.config['card_number']}"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        super().__init__(email=email)
    
    def process(self, amount):  # Same signature as parent
        return f"Processing ${amount} with PayPal {self.config['email']}"

def process_payment(processor, amount):
    return processor.process(amount)  # Works with consistent interface

# Usage
cc_processor = CreditCardProcessor("1234-5678-9012-3456", "123")
paypal_processor = PayPalProcessor("user@example.com")

print(process_payment(cc_processor, 100))
print(process_payment(paypal_processor, 100))
```

### 4.5 Error: Not Handling Duck Typing Gracefully

**Wrong Approach:**

```python
def make_sound(animal):
    # ERROR: Assumes all objects have make_sound method
    return animal.make_sound()

class Dog:
    def make_sound(self):
        return "Woof!"

class Car:
    def start_engine(self):
        return "Engine started"

animals = [Dog(), Car()]  # Car is not an animal!

for animal in animals:
    try:
        print(make_sound(animal))
    except AttributeError as e:
        print(f"Error: {e}")  # Car doesn't have make_sound method
```

**Correct Approach:**

```python
def make_sound(obj):
    # Check if object has the required method
    if hasattr(obj, 'make_sound') and callable(getattr(obj, 'make_sound')):
        return obj.make_sound()
    else:
        return f"{type(obj).__name__} cannot make a sound"

class Dog:
    def make_sound(self):
        return "Woof!"

class Car:
    def start_engine(self):
        return "Engine started"

class Cat:
    def make_sound(self):
        return "Meow!"

objects = [Dog(), Car(), Cat()]

for obj in objects:
    print(make_sound(obj))  # Handles all objects gracefully
```

### 4.6 Error: Overcomplicating with Unnecessary Polymorphism

**Wrong Approach:**

```python
# Over-engineered solution for a simple problem
class NumberProcessor:
    def process(self, number):
        raise NotImplementedError

class EvenNumberProcessor(NumberProcessor):
    def process(self, number):
        if number % 2 == 0:
            return f"Even: {number}"
        raise ValueError("Not an even number")

class OddNumberProcessor(NumberProcessor):
    def process(self, number):
        if number % 2 == 1:
            return f"Odd: {number}"
        raise ValueError("Not an odd number")

# Unnecessarily complex for a simple task
def process_numbers(numbers):
    even_processor = EvenNumberProcessor()
    odd_processor = OddNumberProcessor()
    
    results = []
    for number in numbers:
        if number % 2 == 0:
            results.append(even_processor.process(number))
        else:
            results.append(odd_processor.process(number))
    
    return results
```

**Correct Approach:**

```python
# Simple, direct solution
def process_numbers(numbers):
    results = []
    for number in numbers:
        if number % 2 == 0:
            results.append(f"Even: {number}")
        else:
            results.append(f"Odd: {number}")
    return results

# Or even simpler with list comprehension
def process_numbers_simple(numbers):
    return [f"{'Even' if n % 2 == 0 else 'Odd'}: {n}" for n in numbers]

numbers = [1, 2, 3, 4, 5]
print(process_numbers(numbers))
print(process_numbers_simple(numbers))
```

### 4.7 Best Practices Summary

1. **Use Abstract Base Classes** to enforce interface contracts
2. **Check types in operator overloading** to handle different operand types
3. **Follow Liskov Substitution Principle** - subclasses should be substitutable for their base classes
4. **Keep method signatures consistent** across polymorphic classes
5. **Handle duck typing gracefully** with proper error checking
6. **Don't overuse polymorphism** - sometimes simple solutions are better
7. **Document expected interfaces** clearly for duck typing
8. **Use type hints** to make polymorphic code more maintainable
9. **Test polymorphic behavior** with different object types
10. **Consider composition over inheritance** when polymorphism becomes complex
