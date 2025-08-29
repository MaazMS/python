# Abstraction in Python - Complete Guide

## 1. Abstraction Definition and Characteristics

### What is Abstraction?

Abstraction is one of the four fundamental principles of Object-Oriented Programming (OOP). It refers to the concept of hiding complex implementation details while showing only the essential features of an object. Abstraction focuses on what an object does rather than how it does it, providing a simplified interface for interacting with complex systems.

### Key Characteristics of Abstraction

1. **Information Hiding**: Hide complex implementation details from the user
2. **Essential Features**: Show only the necessary and relevant features
3. **Interface Definition**: Define contracts that must be implemented by concrete classes
4. **Simplified Interaction**: Provide simple methods to interact with complex functionality
5. **Implementation Independence**: Allow multiple implementations of the same interface

### Benefits of Abstraction

- **Simplicity**: Reduces complexity by hiding unnecessary details
- **Maintainability**: Changes to implementation don't affect the interface
- **Reusability**: Abstract interfaces can be implemented by multiple classes
- **Modularity**: Promotes separation of concerns and modular design
- **Flexibility**: Allows for multiple implementations of the same concept
- **Code Organization**: Provides clear structure and contracts

### Types of Abstraction in Python

1. **Data Abstraction**: Hiding data representation details
2. **Process Abstraction**: Hiding implementation details of methods
3. **Abstract Classes**: Classes that cannot be instantiated directly
4. **Interfaces**: Pure abstract classes with all methods abstract

### Example - Basic Abstraction

```python
from abc import ABC, abstractmethod

# Abstract class defining the interface
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    @abstractmethod
    def start_engine(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_fuel_efficiency(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    # Concrete method - can be used by all subclasses
    def get_info(self):
        return f"{self.make} {self.model}"

# Concrete implementation 1
class GasCar(Vehicle):
    def __init__(self, make, model, tank_capacity):
        super().__init__(make, model)
        self.tank_capacity = tank_capacity
        self.engine_running = False
    
    def start_engine(self):
        self.engine_running = True
        return f"{self.get_info()} gas engine started"
    
    def stop_engine(self):
        self.engine_running = False
        return f"{self.get_info()} gas engine stopped"
    
    def get_fuel_efficiency(self):
        return "25 MPG"

# Concrete implementation 2
class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
        self.motor_running = False
    
    def start_engine(self):
        self.motor_running = True
        return f"{self.get_info()} electric motor started silently"
    
    def stop_engine(self):
        self.motor_running = False
        return f"{self.get_info()} electric motor stopped"
    
    def get_fuel_efficiency(self):
        return "100 MPGe"

# Using abstraction - same interface, different implementations
def operate_vehicle(vehicle):
    print(f"Operating: {vehicle.get_info()}")
    print(vehicle.start_engine())
    print(f"Fuel efficiency: {vehicle.get_fuel_efficiency()}")
    print(vehicle.stop_engine())
    print("-" * 40)

# Usage - Client code doesn't need to know implementation details
vehicles = [
    GasCar("Toyota", "Camry", 15.8),
    ElectricCar("Tesla", "Model 3", 75)
]

for vehicle in vehicles:
    operate_vehicle(vehicle)

# Cannot instantiate abstract class
# vehicle = Vehicle("Generic", "Car")  # TypeError: Can't instantiate abstract class
```

## 2. Abstraction Operations

### 2.1 Abstract Classes

Abstract classes serve as blueprints for other classes and cannot be instantiated directly.

#### Basic Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass
    
    # Concrete method available to all subclasses
    def display_info(self):
        return f"A {self.color} {type(self).__name__.lower()} with area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Usage
shapes = [
    Rectangle("red", 5, 3),
    Circle("blue", 4)
]

for shape in shapes:
    print(shape.display_info())
    print(f"Perimeter: {shape.perimeter():.2f}")
    print()
```

#### Abstract Class with Mixed Methods

```python
from abc import ABC, abstractmethod
import logging

class DataProcessor(ABC):
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
    
    # Template method using abstract methods
    def process_data(self, data):
        """Template method defining the processing pipeline"""
        self.logger.info(f"Starting data processing with {self.name}")
        
        validated_data = self.validate_data(data)
        cleaned_data = self.clean_data(validated_data)
        processed_data = self.transform_data(cleaned_data)
        self.save_data(processed_data)
        
        self.logger.info("Data processing completed")
        return processed_data
    
    @abstractmethod
    def validate_data(self, data):
        """Validate input data - must be implemented"""
        pass
    
    @abstractmethod
    def clean_data(self, data):
        """Clean the data - must be implemented"""
        pass
    
    @abstractmethod
    def transform_data(self, data):
        """Transform the data - must be implemented"""
        pass
    
    # Concrete method with default implementation
    def save_data(self, data):
        """Default save implementation - can be overridden"""
        print(f"Saving {len(data)} items using default method")
    
    # Utility method available to all subclasses
    def log_statistics(self, data):
        print(f"Data statistics: {len(data)} items processed")

class CSVProcessor(DataProcessor):
    def validate_data(self, data):
        # CSV-specific validation
        if not isinstance(data, list):
            raise ValueError("CSV data must be a list")
        return data
    
    def clean_data(self, data):
        # Remove empty strings and strip whitespace
        return [item.strip() for item in data if item.strip()]
    
    def transform_data(self, data):
        # Convert to uppercase
        return [item.upper() for item in data]
    
    def save_data(self, data):
        # Override default implementation
        print(f"Saving {len(data)} items to CSV file")

class JSONProcessor(DataProcessor):
    def validate_data(self, data):
        # JSON-specific validation
        if not isinstance(data, list):
            raise ValueError("JSON data must be a list")
        return data
    
    def clean_data(self, data):
        # Remove None values
        return [item for item in data if item is not None]
    
    def transform_data(self, data):
        # Convert to dictionary format
        return [{"value": item, "processed": True} for item in data]

# Usage
data = ["  apple  ", "banana", "", "cherry", None]

processors = [
    CSVProcessor("CSV_Processor"),
    JSONProcessor("JSON_Processor")
]

for processor in processors:
    try:
        result = processor.process_data(data.copy())
        processor.log_statistics(result)
        print(f"Result: {result}")
        print("-" * 50)
    except Exception as e:
        print(f"Error: {e}")
```

### 2.2 Interface-like Classes (Pure Abstract Classes)

Interfaces define contracts that implementing classes must follow.

#### Basic Interface

```python
from abc import ABC, abstractmethod

# Pure interface - all methods are abstract
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def move(self, x, y):
        pass

class Resizable(ABC):
    @abstractmethod
    def resize(self, scale_factor):
        pass
    
    @abstractmethod
    def get_dimensions(self):
        pass

# Multiple interface implementation
class Rectangle(Drawable, Resizable):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # Implement Drawable interface
    def draw(self):
        return f"Drawing rectangle at ({self.x}, {self.y}) with size {self.width}x{self.height}"
    
    def get_area(self):
        return self.width * self.height
    
    def move(self, x, y):
        self.x += x
        self.y += y
        return f"Moved rectangle to ({self.x}, {self.y})"
    
    # Implement Resizable interface
    def resize(self, scale_factor):
        self.width *= scale_factor
        self.height *= scale_factor
        return f"Resized rectangle to {self.width}x{self.height}"
    
    def get_dimensions(self):
        return {"width": self.width, "height": self.height}

class Circle(Drawable, Resizable):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    # Implement Drawable interface
    def draw(self):
        return f"Drawing circle at ({self.x}, {self.y}) with radius {self.radius}"
    
    def get_area(self):
        return 3.14159 * self.radius ** 2
    
    def move(self, x, y):
        self.x += x
        self.y += y
        return f"Moved circle to ({self.x}, {self.y})"
    
    # Implement Resizable interface
    def resize(self, scale_factor):
        self.radius *= scale_factor
        return f"Resized circle to radius {self.radius}"
    
    def get_dimensions(self):
        return {"radius": self.radius}

# Function that works with any Drawable object
def render_shape(shape: Drawable):
    print(shape.draw())
    print(f"Area: {shape.get_area():.2f}")

# Function that works with any Resizable object
def transform_shape(shape: Resizable):
    print(f"Original dimensions: {shape.get_dimensions()}")
    print(shape.resize(1.5))
    print(f"New dimensions: {shape.get_dimensions()}")

# Usage
shapes = [
    Rectangle(0, 0, 10, 5),
    Circle(5, 5, 3)
]

for shape in shapes:
    render_shape(shape)
    transform_shape(shape)
    print(shape.move(2, 3))
    print("-" * 40)
```

#### Complex Interface Hierarchy

```python
from abc import ABC, abstractmethod

# Base service interface
class Service(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass

# Configurable service interface
class ConfigurableService(Service):
    @abstractmethod
    def configure(self, config):
        pass
    
    @abstractmethod
    def get_config(self):
        pass

# Monitorable service interface
class MonitorableService(Service):
    @abstractmethod
    def get_metrics(self):
        pass
    
    @abstractmethod
    def health_check(self):
        pass

# Database service interface combining multiple interfaces
class DatabaseService(ConfigurableService, MonitorableService):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

# Concrete implementation
class PostgreSQLService(DatabaseService):
    def __init__(self):
        self.running = False
        self.connected = False
        self.config = {}
        self.query_count = 0
    
    # Service interface
    def start(self):
        self.running = True
        return "PostgreSQL service started"
    
    def stop(self):
        self.running = False
        self.connected = False
        return "PostgreSQL service stopped"
    
    def get_status(self):
        return "Running" if self.running else "Stopped"
    
    # ConfigurableService interface
    def configure(self, config):
        self.config.update(config)
        return f"PostgreSQL configured with {len(config)} settings"
    
    def get_config(self):
        return self.config.copy()
    
    # MonitorableService interface
    def get_metrics(self):
        return {
            "queries_executed": self.query_count,
            "status": self.get_status(),
            "connected": self.connected
        }
    
    def health_check(self):
        if not self.running:
            return {"status": "unhealthy", "reason": "service not running"}
        if not self.connected:
            return {"status": "degraded", "reason": "not connected to database"}
        return {"status": "healthy"}
    
    # DatabaseService interface
    def connect(self):
        if self.running:
            self.connected = True
            return "Connected to PostgreSQL database"
        return "Cannot connect - service not running"
    
    def disconnect(self):
        self.connected = False
        return "Disconnected from PostgreSQL database"
    
    def execute_query(self, query):
        if not self.connected:
            return "Error: Not connected to database"
        self.query_count += 1
        return f"Executed query: {query[:50]}..."

# Service manager that works with any Service
class ServiceManager:
    def __init__(self):
        self.services = {}
    
    def add_service(self, name, service: Service):
        self.services[name] = service
    
    def start_all_services(self):
        results = {}
        for name, service in self.services.items():
            results[name] = service.start()
        return results
    
    def get_all_status(self):
        status = {}
        for name, service in self.services.items():
            status[name] = service.get_status()
        return status
    
    def configure_service(self, name, config):
        service = self.services.get(name)
        if isinstance(service, ConfigurableService):
            return service.configure(config)
        return f"Service {name} is not configurable"
    
    def monitor_service(self, name):
        service = self.services.get(name)
        if isinstance(service, MonitorableService):
            return {
                "metrics": service.get_metrics(),
                "health": service.health_check()
            }
        return f"Service {name} is not monitorable"

# Usage
db_service = PostgreSQLService()
manager = ServiceManager()
manager.add_service("postgres", db_service)

# Start services
print("Starting services:")
print(manager.start_all_services())

# Configure service
print("\nConfiguring service:")
print(manager.configure_service("postgres", {
    "host": "localhost",
    "port": 5432,
    "database": "myapp"
}))

# Connect and execute query
print("\nDatabase operations:")
print(db_service.connect())
print(db_service.execute_query("SELECT * FROM users"))

# Monitor service
print("\nMonitoring service:")
monitoring_data = manager.monitor_service("postgres")
print(f"Metrics: {monitoring_data['metrics']}")
print(f"Health: {monitoring_data['health']}")
```

### 2.3 Abstract Properties

Abstract properties ensure that subclasses implement specific attributes.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @property
    @abstractmethod
    def species(self):
        """Abstract property - must be implemented by subclasses"""
        pass
    
    @property
    @abstractmethod
    def sound(self):
        """Abstract property - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    def make_sound(self):
        return f"{self.name} the {self.species} makes a {self.sound} sound"

class Dog(Animal):
    @property
    def species(self):
        return "Canine"
    
    @property
    def sound(self):
        return "bark"
    
    def move(self):
        return f"{self.name} runs on four legs"

class Bird(Animal):
    @property
    def species(self):
        return "Avian"
    
    @property
    def sound(self):
        return "chirp"
    
    def move(self):
        return f"{self.name} flies with wings"

# Usage
animals = [
    Dog("Buddy"),
    Bird("Tweety")
]

for animal in animals:
    print(f"Name: {animal.name}")
    print(f"Species: {animal.species}")
    print(animal.make_sound())
    print(animal.move())
    print("-" * 30)
```

## 3. Abstraction Methods

### 3.1 Creating Abstract Classes

#### Using ABC (Abstract Base Class)

```python
from abc import ABC, abstractmethod

# Method 1: Inherit from ABC
class PaymentProcessor(ABC):
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id
        self.transaction_count = 0
    
    @abstractmethod
    def process_payment(self, amount, payment_details):
        """Process a payment - must be implemented"""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id, amount):
        """Process a refund - must be implemented"""
        pass
    
    # Concrete method available to all subclasses
    def log_transaction(self, transaction_type, amount):
        self.transaction_count += 1
        print(f"Transaction #{self.transaction_count}: {transaction_type} of ${amount}")

# Method 2: Using metaclass (alternative approach)
from abc import ABCMeta

class AlternativePaymentProcessor(metaclass=ABCMeta):
    @abstractmethod
    def process_payment(self, amount, payment_details):
        pass

# Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount, payment_details):
        self.log_transaction("Credit Card Payment", amount)
        card_number = payment_details.get("card_number", "")
        return {
            "status": "success",
            "transaction_id": f"CC_{self.transaction_count}",
            "message": f"Processed ${amount} on card ending in {card_number[-4:]}"
        }
    
    def refund_payment(self, transaction_id, amount):
        self.log_transaction("Credit Card Refund", amount)
        return {
            "status": "success",
            "refund_id": f"REF_{transaction_id}",
            "message": f"Refunded ${amount} to original card"
        }

class DigitalWalletProcessor(PaymentProcessor):
    def process_payment(self, amount, payment_details):
        self.log_transaction("Digital Wallet Payment", amount)
        wallet_id = payment_details.get("wallet_id", "")
        return {
            "status": "success",
            "transaction_id": f"DW_{self.transaction_count}",
            "message": f"Processed ${amount} from wallet {wallet_id}"
        }
    
    def refund_payment(self, transaction_id, amount):
        self.log_transaction("Digital Wallet Refund", amount)
        return {
            "status": "success",
            "refund_id": f"REF_{transaction_id}",
            "message": f"Refunded ${amount} to digital wallet"
        }

# Payment service using abstraction
class PaymentService:
    def __init__(self):
        self.processors = {}
    
    def add_processor(self, payment_type, processor: PaymentProcessor):
        self.processors[payment_type] = processor
    
    def process_payment(self, payment_type, amount, payment_details):
        processor = self.processors.get(payment_type)
        if not processor:
            return {"status": "error", "message": "Payment type not supported"}
        
        return processor.process_payment(amount, payment_details)
    
    def process_refund(self, payment_type, transaction_id, amount):
        processor = self.processors.get(payment_type)
        if not processor:
            return {"status": "error", "message": "Payment type not supported"}
        
        return processor.refund_payment(transaction_id, amount)

# Usage
service = PaymentService()
service.add_processor("credit_card", CreditCardProcessor("MERCHANT_123"))
service.add_processor("digital_wallet", DigitalWalletProcessor("MERCHANT_123"))

# Process payments
payment_result = service.process_payment("credit_card", 99.99, {
    "card_number": "1234567890123456",
    "cvv": "123",
    "expiry": "12/25"
})
print(payment_result)

wallet_result = service.process_payment("digital_wallet", 49.99, {
    "wallet_id": "user@example.com"
})
print(wallet_result)
```

### 3.2 Abstract Method Decorators and Patterns

#### Static and Class Abstract Methods

```python
from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod

class MathOperations(ABC):
    @abstractmethod
    def calculate(self, x, y):
        """Instance method - must be implemented"""
        pass
    
    @abstractclassmethod
    def get_operation_name(cls):
        """Class method - must be implemented"""
        pass
    
    @abstractstaticmethod
    def is_valid_input(x, y):
        """Static method - must be implemented"""
        pass
    
    # Concrete method using abstract methods
    def perform_operation(self, x, y):
        if not self.is_valid_input(x, y):
            return f"Invalid input for {self.get_operation_name()}"
        
        result = self.calculate(x, y)
        return f"{self.get_operation_name()}: {x} op {y} = {result}"

class Addition(MathOperations):
    def calculate(self, x, y):
        return x + y
    
    @classmethod
    def get_operation_name(cls):
        return "Addition"
    
    @staticmethod
    def is_valid_input(x, y):
        return isinstance(x, (int, float)) and isinstance(y, (int, float))

class Division(MathOperations):
    def calculate(self, x, y):
        return x / y
    
    @classmethod
    def get_operation_name(cls):
        return "Division"
    
    @staticmethod
    def is_valid_input(x, y):
        return (isinstance(x, (int, float)) and 
                isinstance(y, (int, float)) and 
                y != 0)

# Usage
operations = [Addition(), Division()]

for operation in operations:
    print(operation.perform_operation(10, 5))
    print(operation.perform_operation(10, 0))  # Division will show invalid input
    print("-" * 30)
```

#### Abstract Context Managers

```python
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    @abstractmethod
    def connect(self):
        """Establish database connection"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Close database connection"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Execute a database query"""
        pass
    
    # Context manager methods
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print(f"Connecting to PostgreSQL: {self.connection_string}")
        self.connection = f"PostgreSQL connection to {self.connection_string}"
        return self.connection
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL")
        self.connection = None
    
    def execute_query(self, query):
        if not self.connection:
            raise RuntimeError("Not connected to database")
        print(f"Executing PostgreSQL query: {query}")
        return f"PostgreSQL result for: {query}"

class MongoDBConnection(DatabaseConnection):
    def connect(self):
        print(f"Connecting to MongoDB: {self.connection_string}")
        self.connection = f"MongoDB connection to {self.connection_string}"
        return self.connection
    
    def disconnect(self):
        print("Disconnecting from MongoDB")
        self.connection = None
    
    def execute_query(self, query):
        if not self.connection:
            raise RuntimeError("Not connected to database")
        print(f"Executing MongoDB query: {query}")
        return f"MongoDB result for: {query}"

# Usage with context manager
connections = [
    PostgreSQLConnection("postgresql://localhost:5432/mydb"),
    MongoDBConnection("mongodb://localhost:27017/mydb")
]

for conn in connections:
    with conn as db:
        result = db.execute_query("SELECT * FROM users")
        print(f"Result: {result}")
    print("-" * 40)
```

### 3.3 Mixin Classes and Abstract Methods

```python
from abc import ABC, abstractmethod

# Abstract base for all shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Mixin for shapes that can be colored
class ColorMixin:
    def __init__(self, *args, color="white", **kwargs):
        super().__init__(*args, **kwargs)
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
    
    def describe_color(self):
        return f"This shape is {self._color}"

# Mixin for shapes that can be moved
class MovableMixin:
    def __init__(self, *args, x=0, y=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        return f"Moved to ({self.x}, {self.y})"
    
    def get_position(self):
        return (self.x, self.y)

# Mixin for shapes that can be scaled
class ScalableMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @abstractmethod
    def scale(self, factor):
        """Scale the shape by given factor"""
        pass

# Concrete shape using multiple mixins
class Rectangle(Shape, ColorMixin, MovableMixin, ScalableMixin):
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def scale(self, factor):
        self.width *= factor
        self.height *= factor
        return f"Scaled to {self.width}x{self.height}"
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height}, {self.color}, at {self.get_position()})"

class Circle(Shape, ColorMixin, MovableMixin, ScalableMixin):
    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def scale(self, factor):
        self.radius *= factor
        return f"Scaled to radius {self.radius}"
    
    def __str__(self):
        return f"Circle(radius={self.radius}, {self.color}, at {self.get_position()})"

# Usage
shapes = [
    Rectangle(10, 5, color="red", x=10, y=20),
    Circle(3, color="blue", x=5, y=15)
]

for shape in shapes:
    print(f"Shape: {shape}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print(shape.describe_color())
    print(shape.move(5, 5))
    print(shape.scale(1.5))
    print("-" * 40)
```

### 3.4 Factory Pattern with Abstract Classes

```python
from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    CAR = "car"
    TRUCK = "truck"
    MOTORCYCLE = "motorcycle"

# Abstract vehicle class
class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def get_max_speed(self):
        pass
    
    @abstractmethod
    def get_fuel_capacity(self):
        pass
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

# Abstract factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, make, model, year):
        pass
    
    @abstractmethod
    def get_vehicle_type(self):
        pass

# Concrete vehicle implementations
class Car(Vehicle):
    def start_engine(self):
        return f"Car {self.get_info()} engine started"
    
    def stop_engine(self):
        return f"Car {self.get_info()} engine stopped"
    
    def get_max_speed(self):
        return 120  # mph
    
    def get_fuel_capacity(self):
        return 15  # gallons

class Truck(Vehicle):
    def start_engine(self):
        return f"Truck {self.get_info()} diesel engine started"
    
    def stop_engine(self):
        return f"Truck {self.get_info()} diesel engine stopped"
    
    def get_max_speed(self):
        return 80  # mph
    
    def get_fuel_capacity(self):
        return 50  # gallons

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"Motorcycle {self.get_info()} engine roared to life"
    
    def stop_engine(self):
        return f"Motorcycle {self.get_info()} engine stopped"
    
    def get_max_speed(self):
        return 150  # mph
    
    def get_fuel_capacity(self):
        return 5  # gallons

# Concrete factories
class CarFactory(VehicleFactory):
    def create_vehicle(self, make, model, year):
        return Car(make, model, year)
    
    def get_vehicle_type(self):
        return VehicleType.CAR

class TruckFactory(VehicleFactory):
    def create_vehicle(self, make, model, year):
        return Truck(make, model, year)
    
    def get_vehicle_type(self):
        return VehicleType.TRUCK

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self, make, model, year):
        return Motorcycle(make, model, year)
    
    def get_vehicle_type(self):
        return VehicleType.MOTORCYCLE

# Factory registry
class VehicleFactoryRegistry:
    def __init__(self):
        self._factories = {}
    
    def register_factory(self, vehicle_type: VehicleType, factory: VehicleFactory):
        self._factories[vehicle_type] = factory
    
    def create_vehicle(self, vehicle_type: VehicleType, make, model, year):
        factory = self._factories.get(vehicle_type)
        if not factory:
            raise ValueError(f"No factory registered for {vehicle_type}")
        return factory.create_vehicle(make, model, year)
    
    def get_available_types(self):
        return list(self._factories.keys())

# Usage
registry = VehicleFactoryRegistry()
registry.register_factory(VehicleType.CAR, CarFactory())
registry.register_factory(VehicleType.TRUCK, TruckFactory())
registry.register_factory(VehicleType.MOTORCYCLE, MotorcycleFactory())

# Create different vehicles using the same interface
vehicle_specs = [
    (VehicleType.CAR, "Toyota", "Camry", 2023),
    (VehicleType.TRUCK, "Ford", "F-150", 2023),
    (VehicleType.MOTORCYCLE, "Harley-Davidson", "Street 750", 2023)
]

for vehicle_type, make, model, year in vehicle_specs:
    vehicle = registry.create_vehicle(vehicle_type, make, model, year)
    print(f"Created: {vehicle.get_info()}")
    print(vehicle.start_engine())
    print(f"Max speed: {vehicle.get_max_speed()} mph")
    print(f"Fuel capacity: {vehicle.get_fuel_capacity()} gallons")
    print(vehicle.stop_engine())
    print("-" * 50)
```

## 4. Common Errors in Abstraction

### 4.1 Error: Forgetting to Implement Abstract Methods

**Wrong Approach:**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    # ERROR: Forgot to implement move() method

# This will raise TypeError when trying to instantiate
try:
    dog = Dog()
except TypeError as e:
    print(f"Error: {e}")
    print("Cannot instantiate Dog because it doesn't implement all abstract methods")
```

**Correct Approach:**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    def move(self):  # Must implement all abstract methods
        return "Running on four legs"

# Now it works correctly
dog = Dog()
print(dog.make_sound())
print(dog.move())
```

### 4.2 Error: Incorrect Abstract Method Signatures

**Wrong Approach:**

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data, options):
        pass

class CSVProcessor(DataProcessor):
    # ERROR: Different method signature
    def process(self, data):  # Missing 'options' parameter
        return f"Processing {len(data)} CSV items"

class JSONProcessor(DataProcessor):
    # ERROR: Different method signature
    def process(self, data, options, format_type):  # Extra parameter
        return f"Processing {len(data)} JSON items"

# This will cause issues when using polymorphically
def process_data(processor, data, options):
    try:
        return processor.process(data, options)
    except TypeError as e:
        print(f"Error: {e}")

csv_proc = CSVProcessor()
json_proc = JSONProcessor()

process_data(csv_proc, [1, 2, 3], {"format": "csv"})  # Error: too many arguments
process_data(json_proc, [1, 2, 3], {"format": "json"})  # Error: missing argument
```

**Correct Approach:**

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data, options):
        pass

class CSVProcessor(DataProcessor):
    def process(self, data, options):  # Exact same signature
        format_option = options.get("format", "standard")
        return f"Processing {len(data)} CSV items with {format_option} format"

class JSONProcessor(DataProcessor):
    def process(self, data, options):  # Exact same signature
        indent = options.get("indent", 2)
        return f"Processing {len(data)} JSON items with {indent} indent"

# Now works correctly with polymorphism
def process_data(processor, data, options):
    return processor.process(data, options)

csv_proc = CSVProcessor()
json_proc = JSONProcessor()

print(process_data(csv_proc, [1, 2, 3], {"format": "csv"}))
print(process_data(json_proc, [1, 2, 3], {"indent": 4}))
```

### 4.3 Error: Trying to Instantiate Abstract Classes

**Wrong Approach:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        pass
    
    def describe(self):
        return f"A {self.color} shape"

# ERROR: Trying to create instance of abstract class
try:
    shape = Shape("red")
    print(shape.describe())
except TypeError as e:
    print(f"Error: {e}")
```

**Correct Approach:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        pass
    
    def describe(self):
        return f"A {self.color} shape with area {self.area()}"

class Circle(Shape):  # Concrete implementation
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Create instance of concrete class
circle = Circle("red", 5)
print(circle.describe())  # Works correctly
```

### 4.4 Error: Not Using Abstract Base Classes When Needed

**Wrong Approach:**

```python
# No enforcement of interface contract
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement process_payment")

class CreditCardProcessor(PaymentProcessor):
    # Forgot to implement process_payment
    def charge_card(self, amount):  # Different method name
        return f"Charged ${amount} to credit card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):  # Correct implementation
        return f"Processed ${amount} via PayPal"

# No error until runtime
def make_payment(processor, amount):
    return processor.process_payment(amount)

# This will fail at runtime
cc_processor = CreditCardProcessor()  # No error here
try:
    make_payment(cc_processor, 100)  # Error only when method is called
except NotImplementedError as e:
    print(f"Runtime Error: {e}")
```

**Correct Approach:**

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):  # Abstract base class
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    # This would cause TypeError if process_payment is not implemented
    def process_payment(self, amount):  # Must implement
        return f"Charged ${amount} to credit card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processed ${amount} via PayPal"

# Error caught at instantiation time
def make_payment(processor, amount):
    return processor.process_payment(amount)

cc_processor = CreditCardProcessor()  # Works because all methods implemented
paypal_processor = PayPalProcessor()

print(make_payment(cc_processor, 100))
print(make_payment(paypal_processor, 50))
```

### 4.5 Error: Overcomplicating with Unnecessary Abstraction

**Wrong Approach:**

```python
from abc import ABC, abstractmethod

# Over-engineered abstraction for simple functionality
class NumberOperation(ABC):
    @abstractmethod
    def execute(self, numbers):
        pass

class SumOperation(NumberOperation):
    def execute(self, numbers):
        return sum(numbers)

class MaxOperation(NumberOperation):
    def execute(self, numbers):
        return max(numbers)

class MinOperation(NumberOperation):
    def execute(self, numbers):
        return min(numbers)

class NumberProcessor:
    def __init__(self, operation: NumberOperation):
        self.operation = operation
    
    def process(self, numbers):
        return self.operation.execute(numbers)

# Overly complex for simple operations
numbers = [1, 2, 3, 4, 5]
sum_processor = NumberProcessor(SumOperation())
max_processor = NumberProcessor(MaxOperation())

print(f"Sum: {sum_processor.process(numbers)}")
print(f"Max: {max_processor.process(numbers)}")
```

**Correct Approach:**

```python
# Simple, direct approach for simple operations
def calculate_sum(numbers):
    return sum(numbers)

def calculate_max(numbers):
    return max(numbers)

def calculate_min(numbers):
    return min(numbers)

# Or using a simple class if needed
class NumberProcessor:
    @staticmethod
    def sum(numbers):
        return sum(numbers)
    
    @staticmethod
    def max(numbers):
        return max(numbers)
    
    @staticmethod
    def min(numbers):
        return min(numbers)

# Simple and straightforward
numbers = [1, 2, 3, 4, 5]
print(f"Sum: {NumberProcessor.sum(numbers)}")
print(f"Max: {NumberProcessor.max(numbers)}")
print(f"Min: {NumberProcessor.min(numbers)}")

# Use abstraction only when you need polymorphic behavior
# or when you have complex operations that benefit from it
```

### 4.6 Error: Mixing Abstraction Levels

**Wrong Approach:**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    # ERROR: Too specific method in abstract base
    @abstractmethod
    def shift_gear(self):  # Not all vehicles have gears
        pass
    
    # ERROR: Implementation detail in abstract class
    @abstractmethod
    def check_oil_level(self):  # Too low-level
        pass

class ElectricCar(Vehicle):
    def start(self):
        return "Electric motor started"
    
    def accelerate(self):
        return "Accelerating smoothly"
    
    def shift_gear(self):
        # ERROR: Electric cars don't have gears
        return "Electric cars don't have gears to shift"
    
    def check_oil_level(self):
        # ERROR: Electric cars don't have oil
        return "Electric cars don't have oil"
```

**Correct Approach:**

```python
from abc import ABC, abstractmethod

# High-level abstraction
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

# Mid-level abstractions for specific vehicle types
class GasVehicle(Vehicle):
    @abstractmethod
    def check_oil_level(self):
        pass
    
    @abstractmethod
    def refuel(self):
        pass

class ElectricVehicle(Vehicle):
    @abstractmethod
    def charge_battery(self):
        pass
    
    @abstractmethod
    def check_battery_level(self):
        pass

# Concrete implementations
class GasCar(GasVehicle):
    def start(self):
        return "Gas engine started"
    
    def accelerate(self):
        return "Accelerating with gas engine"
    
    def stop(self):
        return "Stopped gas car"
    
    def check_oil_level(self):
        return "Oil level: OK"
    
    def refuel(self):
        return "Refueling with gasoline"

class ElectricCar(ElectricVehicle):
    def start(self):
        return "Electric motor started"
    
    def accelerate(self):
        return "Accelerating smoothly with electric motor"
    
    def stop(self):
        return "Stopped electric car"
    
    def charge_battery(self):
        return "Charging battery"
    
    def check_battery_level(self):
        return "Battery level: 85%"

# Usage - proper abstraction levels
vehicles = [GasCar(), ElectricCar()]

for vehicle in vehicles:
    print(f"Vehicle type: {type(vehicle).__name__}")
    print(vehicle.start())
    print(vehicle.accelerate())
    print(vehicle.stop())
    
    # Type-specific operations
    if isinstance(vehicle, GasVehicle):
        print(vehicle.check_oil_level())
    elif isinstance(vehicle, ElectricVehicle):
        print(vehicle.check_battery_level())
    
    print("-" * 30)
```

### 4.7 Best Practices Summary

1. **Always implement all abstract methods** in concrete classes
2. **Keep method signatures consistent** between abstract and concrete methods
3. **Don't try to instantiate abstract classes** directly
4. **Use ABC when you need interface contracts** to catch errors early
5. **Don't over-abstract simple functionality** - use abstraction when it adds value
6. **Keep abstraction levels consistent** - don't mix high-level and low-level concerns
7. **Use type hints** to make abstract interfaces clearer
8. **Document abstract methods** with clear docstrings explaining expected behavior
9. **Consider composition over inheritance** when abstraction becomes too complex
10. **Test abstract implementations** thoroughly to ensure contract compliance
