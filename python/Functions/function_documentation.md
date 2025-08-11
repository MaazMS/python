# Python Function Parameters, Arguments, and Return Values Documentation

## 1. Definitions and Characteristics

### Function Parameters and Arguments Overview

**Parameters** are variables defined in a function's signature that accept values when the function is called.
**Arguments** are the actual values passed to a function when it's called.

### 1.1 Function Parameter Types

#### No Arguments

Functions that don't accept any parameters.

```python
def no_argument_function():
    """Function with no parameters"""
    return "Hello, World!"

# Characteristics:
# - Simple function call with empty parentheses
# - No input required
# - Always returns the same result (unless using global variables)

result = no_argument_function()
print(result)  # Output: Hello, World!
print(type(no_argument_function))  # <class 'function'>
```

#### Single Argument

Functions that accept exactly one parameter.

```python
def single_argument_function(name):
    """Function with single parameter"""
    return f"Hello, {name}!"

# Characteristics:
# - Requires exactly one argument
# - Simple parameter passing
# - Type can be any Python object

result = single_argument_function("Alice")
print(result)  # Output: Hello, Alice!

# Can accept different types
print(single_argument_function(123))      # Hello, 123!
print(single_argument_function([1,2,3]))  # Hello, [1, 2, 3]!
```

#### Multiple Arguments

Functions that accept multiple parameters.

```python
def multiple_arguments_function(first_name, last_name, age):
    """Function with multiple parameters"""
    return f"{first_name} {last_name} is {age} years old"

# Characteristics:
# - Requires specific number of arguments
# - Order of arguments matters
# - All parameters are required

result = multiple_arguments_function("John", "Doe", 30)
print(result)  # Output: John Doe is 30 years old

# Positional argument passing
person_info = multiple_arguments_function("Jane", "Smith", 25)
print(person_info)
```

#### Default Arguments

Functions with parameters that have default values.

```python
def default_argument_function(name, greeting="Hello", punctuation="!"):
    """Function with default parameters"""
    return f"{greeting}, {name}{punctuation}"

# Characteristics:
# - Some parameters are optional
# - Default values used when arguments not provided
# - Can mix required and optional parameters

# Using defaults
print(default_argument_function("Alice"))                    # Hello, Alice!
print(default_argument_function("Bob", "Hi"))               # Hi, Bob!
print(default_argument_function("Charlie", "Hey", "?"))     # Hey, Charlie?

# Keyword arguments
print(default_argument_function("Diana", punctuation="!!!")) # Hello, Diana!!!
print(default_argument_function("Eve", greeting="Greetings", punctuation="."))
```

### 1.2 Function as Parameter

#### Passing Functions as Arguments

Functions can be passed as arguments to other functions (higher-order functions).

```python
def function_as_parameter_example():
    """Demonstrate functions as parameters"""
    
    def add(x, y):
        return x + y
    
    def multiply(x, y):
        return x * y
    
    def subtract(x, y):
        return x - y
    
    def calculate(operation_func, a, b):
        """Function that takes another function as parameter"""
        result = operation_func(a, b)
        return f"Result: {result}"
    
    # Characteristics:
    # - Functions are first-class objects
    # - Can be passed like any other value
    # - Enables flexible, reusable code
    
    print(calculate(add, 5, 3))        # Result: 8
    print(calculate(multiply, 4, 7))   # Result: 28
    print(calculate(subtract, 10, 4))  # Result: 6
    
    # Using lambda functions as parameters
    print(calculate(lambda x, y: x ** y, 2, 3))  # Result: 8

function_as_parameter_example()
```

#### No Parameters vs Function Parameters

Comparison between functions with and without parameters.

```python
def parameter_comparison():
    """Compare functions with and without parameters"""
    
    # Function with no parameters
    def get_current_time():
        import datetime
        return datetime.datetime.now()
    
    # Function that takes a function with no parameters
    def execute_function(func):
        """Execute a function that takes no parameters"""
        return func()
    
    # Function that takes a function with parameters
    def execute_with_args(func, *args, **kwargs):
        """Execute a function with arguments"""
        return func(*args, **kwargs)
    
    # Using function with no parameters
    current_time = execute_function(get_current_time)
    print(f"Current time: {current_time}")
    
    # Using function with parameters
    result = execute_with_args(max, [1, 5, 3, 9, 2])
    print(f"Maximum: {result}")
    
    # Function that returns a function
    def create_multiplier(factor):
        def multiplier(x):
            return x * factor
        return multiplier
    
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"Double 5: {execute_with_args(double, 5)}")
    print(f"Triple 4: {execute_with_args(triple, 4)}")

parameter_comparison()
```

### 1.3 Function Return Values

#### Single Return

Functions that return one value.

```python
def single_return_examples():
    """Examples of functions with single return values"""
    
    def calculate_area(length, width):
        """Return single value - area"""
        return length * width
    
    def get_full_name(first, last):
        """Return single string value"""
        return f"{first} {last}"
    
    def is_even(number):
        """Return single boolean value"""
        return number % 2 == 0
    
    def get_user_data():
        """Return single complex object"""
        return {
            'name': 'John Doe',
            'age': 30,
            'email': 'john@example.com'
        }
    
    # Characteristics:
    # - Simple assignment
    # - Single value returned
    # - Can be any Python object type
    
    area = calculate_area(5, 3)
    name = get_full_name("Jane", "Smith")
    even_check = is_even(4)
    user = get_user_data()
    
    print(f"Area: {area}")
    print(f"Name: {name}")
    print(f"Is even: {even_check}")
    print(f"User: {user}")

single_return_examples()
```

#### Multiple Return

Functions that return multiple values.

```python
def multiple_return_examples():
    """Examples of functions with multiple return values"""
    
    def calculate_statistics(numbers):
        """Return multiple values as tuple"""
        if not numbers:
            return 0, 0, 0, 0
        
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        maximum = max(numbers)
        
        return total, count, average, maximum
    
    def parse_name(full_name):
        """Return multiple string values"""
        parts = full_name.split()
        if len(parts) >= 2:
            return parts[0], parts[-1]
        return parts[0], ""
    
    def divide_with_remainder(dividend, divisor):
        """Return quotient and remainder"""
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder
    
    def get_coordinates():
        """Return multiple numeric values"""
        x, y, z = 10.5, 20.3, 15.7
        return x, y, z
    
    # Characteristics:
    # - Returns tuple by default
    # - Can be unpacked into multiple variables
    # - Maintains order of return values
    
    # Unpacking multiple returns
    total, count, avg, max_val = calculate_statistics([1, 2, 3, 4, 5])
    print(f"Total: {total}, Count: {count}, Average: {avg}, Max: {max_val}")
    
    first, last = parse_name("John Doe Smith")
    print(f"First: {first}, Last: {last}")
    
    q, r = divide_with_remainder(17, 5)
    print(f"17 ÷ 5 = {q} remainder {r}")
    
    x, y, z = get_coordinates()
    print(f"Coordinates: ({x}, {y}, {z})")
    
    # Can also receive as tuple
    stats_tuple = calculate_statistics([10, 20, 30])
    print(f"Stats tuple: {stats_tuple}")

multiple_return_examples()
```

### 1.4 Variable Functions

#### Variable Arguments (*args)

Functions that accept variable number of positional arguments.

```python
def variable_args_examples():
    """Examples of functions with variable arguments"""
    
    def sum_all(*args):
        """Sum any number of arguments"""
        return sum(args)
    
    def print_info(title, *details):
        """Print title and variable details"""
        print(f"Title: {title}")
        for i, detail in enumerate(details, 1):
            print(f"  Detail {i}: {detail}")
    
    def find_maximum(*numbers):
        """Find maximum from variable arguments"""
        if not numbers:
            return None
        return max(numbers)
    
    def concatenate_strings(separator=" ", *strings):
        """Concatenate variable strings with separator"""
        return separator.join(strings)
    
    # Characteristics:
    # - *args collects extra positional arguments into tuple
    # - Can handle any number of arguments
    # - Arguments accessed as tuple inside function
    
    print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
    print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
    print(f"Sum of no args: {sum_all()}")
    
    print_info("User Profile", "John Doe", "30 years old", "Engineer")
    
    print(f"Maximum: {find_maximum(5, 2, 8, 1, 9)}")
    
    result = concatenate_strings("-", "apple", "banana", "cherry")
    print(f"Concatenated: {result}")

variable_args_examples()
```

#### Variable Keyword Arguments (**kwargs)

Functions that accept variable number of keyword arguments.

```python
def variable_kwargs_examples():
    """Examples of functions with variable keyword arguments"""
    
    def create_profile(**kwargs):
        """Create profile from keyword arguments"""
        profile = {}
        for key, value in kwargs.items():
            profile[key] = value
        return profile
    
    def configure_database(host, port, **options):
        """Configure database with required and optional parameters"""
        config = {
            'host': host,
            'port': port
        }
        config.update(options)
        return config
    
    def print_formatted(**data):
        """Print data in formatted way"""
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
    
    def flexible_calculator(operation, *args, **kwargs):
        """Calculator with variable args and kwargs"""
        result = None
        
        if operation == "add":
            result = sum(args)
        elif operation == "multiply":
            result = 1
            for num in args:
                result *= num
        
        # Apply modifiers from kwargs
        if kwargs.get('absolute', False):
            result = abs(result)
        if kwargs.get('round_to'):
            result = round(result, kwargs['round_to'])
        
        return result
    
    # Characteristics:
    # - **kwargs collects extra keyword arguments into dictionary
    # - Provides flexible function interfaces
    # - Arguments accessed as dictionary inside function
    
    profile = create_profile(name="Alice", age=25, city="New York", job="Developer")
    print(f"Profile: {profile}")
    
    db_config = configure_database("localhost", 5432, username="admin", password="secret", ssl=True)
    print(f"Database config: {db_config}")
    
    print("User Information:")
    print_formatted(name="Bob", age=30, email="bob@example.com", active=True)
    
    calc_result = flexible_calculator("add", 1, 2, 3, 4, 5, absolute=True, round_to=2)
    print(f"Calculator result: {calc_result}")

variable_kwargs_examples()
```

---

## 2. Operations

### 2.1 Parameter Passing Operations

#### Positional Argument Passing

```python
def positional_operations():
    """Demonstrate positional argument operations"""
    
    def create_rectangle(width, height, color="blue"):
        """Create rectangle with positional and default arguments"""
        return {
            'width': width,
            'height': height,
            'color': color,
            'area': width * height
        }
    
    def process_data(data, operation, *modifiers):
        """Process data with operation and modifiers"""
        result = data
        
        if operation == "uppercase":
            result = result.upper()
        elif operation == "reverse":
            result = result[::-1]
        elif operation == "multiply":
            if modifiers:
                result = result * modifiers[0]
        
        return result
    
    # Positional argument operations
    rect1 = create_rectangle(10, 5)                    # Using default color
    rect2 = create_rectangle(8, 6, "red")              # All positional
    
    print(f"Rectangle 1: {rect1}")
    print(f"Rectangle 2: {rect2}")
    
    # Operations with variable arguments
    text_result = process_data("hello", "uppercase")
    reverse_result = process_data("world", "reverse")
    multiply_result = process_data("hi", "multiply", 3)
    
    print(f"Uppercase: {text_result}")
    print(f"Reverse: {reverse_result}")
    print(f"Multiply: {multiply_result}")

positional_operations()
```

#### Keyword Argument Passing

```python
def keyword_operations():
    """Demonstrate keyword argument operations"""
    
    def create_user(name, email, age=None, active=True, **metadata):
        """Create user with keyword arguments"""
        user = {
            'name': name,
            'email': email,
            'age': age,
            'active': active,
            'metadata': metadata
        }
        return user
    
    def format_message(message, **formatting):
        """Format message with various options"""
        result = message
        
        if formatting.get('uppercase', False):
            result = result.upper()
        
        if formatting.get('prefix'):
            result = formatting['prefix'] + result
        
        if formatting.get('suffix'):
            result = result + formatting['suffix']
        
        if formatting.get('repeat', 1) > 1:
            result = result * formatting['repeat']
        
        return result
    
    # Keyword argument operations
    user1 = create_user("John", "john@example.com")
    user2 = create_user(name="Alice", email="alice@example.com", age=25)
    user3 = create_user("Bob", "bob@example.com", department="IT", role="Developer")
    
    print(f"User 1: {user1}")
    print(f"User 2: {user2}")
    print(f"User 3: {user3}")
    
    # Message formatting operations
    msg1 = format_message("Hello", uppercase=True)
    msg2 = format_message("World", prefix=">>> ", suffix=" <<<")
    msg3 = format_message("Hi", repeat=3, prefix="* ")
    
    print(f"Message 1: {msg1}")
    print(f"Message 2: {msg2}")
    print(f"Message 3: {msg3}")

keyword_operations()
```

### 2.2 Function Composition Operations

#### Chaining Functions

```python
def function_chaining():
    """Demonstrate function chaining operations"""
    
    def add_prefix(text, prefix=">>> "):
        return prefix + text
    
    def add_suffix(text, suffix=" <<<"):
        return text + suffix
    
    def make_uppercase(text):
        return text.upper()
    
    def repeat_text(text, times=2):
        return text * times
    
    def chain_functions(data, *functions):
        """Chain multiple functions together"""
        result = data
        for func in functions:
            if isinstance(func, tuple):
                # Function with arguments
                func_name, *args = func
                result = func_name(result, *args)
            else:
                # Function without additional arguments
                result = func(result)
        return result
    
    # Function chaining operations
    original = "hello world"
    
    # Simple chaining
    result1 = add_suffix(add_prefix(make_uppercase(original)))
    print(f"Manual chain: {result1}")
    
    # Using chain function
    result2 = chain_functions(
        original,
        make_uppercase,
        (add_prefix, "*** "),
        (add_suffix, " ***"),
        (repeat_text, 2)
    )
    print(f"Chained result: {result2}")
    
    # Pipeline operations
    def create_pipeline(*operations):
        """Create a reusable pipeline"""
        def pipeline(data):
            return chain_functions(data, *operations)
        return pipeline
    
    # Create reusable pipeline
    text_processor = create_pipeline(
        str.strip,
        make_uppercase,
        (add_prefix, "==> "),
        (add_suffix, " <==")
    )
    
    processed = text_processor("  hello world  ")
    print(f"Pipeline result: {processed}")

function_chaining()
```

### 2.3 Dynamic Function Operations

#### Dynamic Function Creation

```python
def dynamic_function_operations():
    """Demonstrate dynamic function creation operations"""
    
    def create_validator(min_val=None, max_val=None, data_type=None):
        """Create validator function dynamically"""
        def validator(value):
            # Type validation
            if data_type and not isinstance(value, data_type):
                return False, f"Expected {data_type.__name__}, got {type(value).__name__}"
            
            # Range validation
            if min_val is not None and value < min_val:
                return False, f"Value {value} is less than minimum {min_val}"
            
            if max_val is not None and value > max_val:
                return False, f"Value {value} is greater than maximum {max_val}"
            
            return True, "Valid"
        
        return validator
    
    def create_formatter(template, **default_values):
        """Create formatter function dynamically"""
        def formatter(**values):
            # Merge default values with provided values
            format_values = default_values.copy()
            format_values.update(values)
            return template.format(**format_values)
        
        return formatter
    
    def create_calculator(operation):
        """Create calculator function for specific operation"""
        operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else float('inf')
        }
        
        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")
        
        def calculator(*args):
            if len(args) < 2:
                raise ValueError("Calculator requires at least 2 arguments")
            
            result = args[0]
            for arg in args[1:]:
                result = operations[operation](result, arg)
            return result
        
        return calculator
    
    # Dynamic function operations
    
    # Create validators
    age_validator = create_validator(min_val=0, max_val=120, data_type=int)
    score_validator = create_validator(min_val=0, max_val=100)
    
    print("=== Validator Tests ===")
    print(age_validator(25))      # (True, 'Valid')
    print(age_validator(150))     # (False, 'Value 150 is greater than maximum 120')
    print(age_validator("25"))    # (False, 'Expected int, got str')
    
    # Create formatters
    email_formatter = create_formatter(
        "{name} <{email}>",
        name="Unknown User",
        email="no-email@example.com"
    )
    
    greeting_formatter = create_formatter(
        "{greeting}, {name}! Welcome to {place}.",
        greeting="Hello",
        place="our website"
    )
    
    print("\n=== Formatter Tests ===")
    print(email_formatter(name="John Doe", email="john@example.com"))
    print(email_formatter(email="jane@example.com"))
    print(greeting_formatter(name="Alice", place="Python world"))
    
    # Create calculators
    adder = create_calculator('add')
    multiplier = create_calculator('multiply')
    
    print("\n=== Calculator Tests ===")
    print(f"Add 1,2,3,4,5: {adder(1, 2, 3, 4, 5)}")
    print(f"Multiply 2,3,4: {multiplier(2, 3, 4)}")

dynamic_function_operations()
```

---

## 3. Methods

### 3.1 Function Introspection Methods

#### Parameter Inspection

```python
import inspect
from typing import Any, Callable

def parameter_inspection_methods():
    """Methods for inspecting function parameters"""
    
    def sample_function(
        required_arg: str,
        default_arg: int = 10,
        *args: Any,
        keyword_only: bool,
        keyword_with_default: str = "default",
        **kwargs: Any
    ) -> dict:
        """Sample function with all parameter types"""
        return {
            'required': required_arg,
            'default': default_arg,
            'args': args,
            'keyword_only': keyword_only,
            'keyword_default': keyword_with_default,
            'kwargs': kwargs
        }
    
    def inspect_function_parameters(func: Callable) -> dict:
        """Inspect function parameters and return information"""
        sig = inspect.signature(func)
        param_info = {}
        
        for name, param in sig.parameters.items():
            param_info[name] = {
                'name': name,
                'kind': param.kind.name,
                'default': param.default if param.default != inspect.Parameter.empty else 'No default',
                'annotation': param.annotation if param.annotation != inspect.Parameter.empty else 'No annotation'
            }
        
        return {
            'function_name': func.__name__,
            'parameters': param_info,
            'return_annotation': sig.return_annotation if sig.return_annotation != inspect.Signature.empty else 'No annotation'
        }
    
    def get_function_metadata(func: Callable) -> dict:
        """Get comprehensive function metadata"""
        return {
            'name': func.__name__,
            'doc': func.__doc__,
            'module': func.__module__,
            'defaults': func.__defaults__,
            'kwdefaults': func.__kwdefaults__,
            'annotations': func.__annotations__,
            'code_info': {
                'filename': func.__code__.co_filename,
                'line_number': func.__code__.co_firstlineno,
                'arg_count': func.__code__.co_argcount,
                'var_names': func.__code__.co_varnames
            }
        }
    
    # Inspect parameters
    print("=== Parameter Inspection ===")
    param_info = inspect_function_parameters(sample_function)
    
    print(f"Function: {param_info['function_name']}")
    print(f"Return type: {param_info['return_annotation']}")
    print("\nParameters:")
    for name, info in param_info['parameters'].items():
        print(f"  {name}:")
        print(f"    Kind: {info['kind']}")
        print(f"    Default: {info['default']}")
        print(f"    Annotation: {info['annotation']}")
    
    # Get metadata
    print("\n=== Function Metadata ===")
    metadata = get_function_metadata(sample_function)
    for key, value in metadata.items():
        if key != 'code_info':
            print(f"{key}: {value}")
    
    print("Code info:")
    for key, value in metadata['code_info'].items():
        print(f"  {key}: {value}")

parameter_inspection_methods()
```

### 3.2 Parameter Validation Methods

#### Advanced Validation

```python
def parameter_validation_methods():
    """Methods for parameter validation"""
    
    def validate_types(**type_specs):
        """Decorator for type validation"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Get function signature
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                
                # Validate types
                for param_name, expected_type in type_specs.items():
                    if param_name in bound_args.arguments:
                        value = bound_args.arguments[param_name]
                        if not isinstance(value, expected_type):
                            raise TypeError(
                                f"Parameter '{param_name}' expected {expected_type.__name__}, "
                                f"got {type(value).__name__}"
                            )
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def validate_range(**range_specs):
        """Decorator for range validation"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                
                for param_name, (min_val, max_val) in range_specs.items():
                    if param_name in bound_args.arguments:
                        value = bound_args.arguments[param_name]
                        if not (min_val <= value <= max_val):
                            raise ValueError(
                                f"Parameter '{param_name}' must be between {min_val} and {max_val}, "
                                f"got {value}"
                            )
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def validate_required(*required_params):
        """Decorator for required parameter validation"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                
                for param_name in required_params:
                    if param_name not in bound_args.arguments:
                        raise ValueError(f"Required parameter '{param_name}' is missing")
                    
                    value = bound_args.arguments[param_name]
                    if value is None:
                        raise ValueError(f"Required parameter '{param_name}' cannot be None")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    # Apply validation decorators
    @validate_types(name=str, age=int, score=float)
    @validate_range(age=(0, 120), score=(0.0, 100.0))
    @validate_required('name', 'age')
    def create_student_record(name, age, score=0.0, **extra_info):
        """Create student record with validation"""
        return {
            'name': name,
            'age': age,
            'score': score,
            'extra_info': extra_info
        }
    
    # Test validation methods
    print("=== Validation Methods ===")
    
    try:
        # Valid record
        record1 = create_student_record("Alice", 20, 85.5, grade="A")
        print(f"Valid record: {record1}")
        
        # Valid with defaults
        record2 = create_student_record("Bob", 22)
        print(f"Valid with defaults: {record2}")
        
        # Invalid type
        try:
            create_student_record("Charlie", "twenty", 90.0)
        except TypeError as e:
            print(f"Type error: {e}")
        
        # Invalid range
        try:
            create_student_record("Diana", 25, 150.0)
        except ValueError as e:
            print(f"Range error: {e}")
        
        # Missing required
        try:
            create_student_record(age=30, score=75.0)
        except ValueError as e:
            print(f"Required error: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

parameter_validation_methods()
```

### 3.3 Return Value Methods

#### Multiple Return Handling

```python
def return_value_methods():
    """Methods for handling return values"""
    
    def safe_divide(a, b):
        """Safely divide with multiple return scenarios"""
        if b == 0:
            return None, "Division by zero error"
        return a / b, "Success"
    
    def parse_config_line(line):
        """Parse configuration line with multiple returns"""
        line = line.strip()
        if not line or line.startswith('#'):
            return None, None, "Comment or empty line"
        
        if '=' not in line:
            return None, None, "Invalid format"
        
        key, value = line.split('=', 1)
        return key.strip(), value.strip(), "Parsed successfully"
    
    def get_user_info(user_id):
        """Get user info with different return scenarios"""
        # Simulate database lookup
        users = {
            1: {"name": "Alice", "email": "alice@example.com", "active": True},
            2: {"name": "Bob", "email": "bob@example.com", "active": False},
            3: {"name": "Charlie", "email": "charlie@example.com", "active": True}
        }
        
        if user_id not in users:
            return None, False, "User not found"
        
        user = users[user_id]
        return user, user['active'], "User found"
    
    def process_multiple_returns(func, *args, **kwargs):
        """Generic processor for functions with multiple returns"""
        try:
            result = func(*args, **kwargs)
            
            if isinstance(result, tuple):
                return {
                    'success': True,
                    'data': result,
                    'count': len(result),
                    'message': 'Multiple values returned'
                }
            else:
                return {
                    'success': True,
                    'data': result,
                    'count': 1,
                    'message': 'Single value returned'
                }
        except Exception as e:
            return {
                'success': False,
                'data': None,
                'count': 0,
                'message': str(e)
            }
    
    def unpack_with_defaults(result_tuple, *default_values):
        """Unpack tuple with default values for missing elements"""
        if not isinstance(result_tuple, tuple):
            result_tuple = (result_tuple,)
        
        unpacked = list(result_tuple)
        
        # Pad with defaults if needed
        while len(unpacked) < len(default_values):
            unpacked.append(default_values[len(unpacked)])
        
        return tuple(unpacked)
    
    # Test return value methods
    print("=== Return Value Methods ===")
    
    # Test safe divide
    result1, msg1 = safe_divide(10, 2)
    result2, msg2 = safe_divide(10, 0)
    print(f"10/2: {result1}, {msg1}")
    print(f"10/0: {result2}, {msg2}")
    
    # Test config parsing
    key1, val1, status1 = parse_config_line("database_host=localhost")
    key2, val2, status2 = parse_config_line("# This is a comment")
    print(f"Config 1: {key1}={val1}, {status1}")
    print(f"Config 2: {key2}={val2}, {status2}")
    
    # Test user info
    user1, active1, msg_1 = get_user_info(1)
    user2, active2, msg_2 = get_user_info(999)
    print(f"User 1: {user1}, Active: {active1}, {msg_1}")
    print(f"User 999: {user2}, Active: {active2}, {msg_2}")
    
    # Test generic processor
    proc_result1 = process_multiple_returns(safe_divide, 15, 3)
    proc_result2 = process_multiple_returns(len, "hello")
    print(f"Processed divide: {proc_result1}")
    print(f"Processed len: {proc_result2}")
    
    # Test unpacking with defaults
    unpacked1 = unpack_with_defaults((1, 2), 0, 0, 0)
    unpacked2 = unpack_with_defaults((1,), 0, 0, 0)
    print(f"Unpacked 1: {unpacked1}")
    print(f"Unpacked 2: {unpacked2}")

return_value_methods()
```

### 3.4 Variable Function Methods

#### Advanced Variable Arguments

```python
def variable_function_methods():
    """Advanced methods for variable functions"""
    
    def flexible_function_caller(func, *pos_args, **kw_args):
        """Call function with flexible arguments"""
        try:
            # Try to call with all arguments
            result = func(*pos_args, **kw_args)
            return result, True, "Success"
        except TypeError as e:
            # Handle argument mismatch
            return None, False, str(e)
    
    def argument_distributor(func_list, *args, **kwargs):
        """Distribute arguments to multiple functions"""
        results = {}
        
        for func in func_list:
            func_name = func.__name__
            try:
                # Get function signature
                sig = inspect.signature(func)
                
                # Filter arguments that the function can accept
                filtered_args = []
                filtered_kwargs = {}
                
                param_names = list(sig.parameters.keys())
                
                # Add positional arguments up to function's capacity
                for i, arg in enumerate(args):
                    if i < len(param_names):
                        param = sig.parameters[param_names[i]]
                        if param.kind in (param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD):
                            filtered_args.append(arg)
                
                # Add keyword arguments that the function accepts
                for key, value in kwargs.items():
                    if key in param_names:
                        param = sig.parameters[key]
                        if param.kind in (param.POSITIONAL_OR_KEYWORD, param.KEYWORD_ONLY):
                            filtered_kwargs[key] = value
                
                result = func(*filtered_args, **filtered_kwargs)
                results[func_name] = {'result': result, 'success': True, 'error': None}
                
            except Exception as e:
                results[func_name] = {'result': None, 'success': False, 'error': str(e)}
        
        return results
    
    def create_argument_mapper(**mappings):
        """Create function that maps arguments to different names"""
        def mapper(func):
            def wrapper(*args, **kwargs):
                # Map keyword arguments
                new_kwargs = {}
                for key, value in kwargs.items():
                    new_key = mappings.get(key, key)
                    new_kwargs[new_key] = value
                
                return func(*args, **new_kwargs)
            return wrapper
        return mapper
    
    def variadic_compose(*functions):
        """Compose functions with variable arguments"""
        def composed(*args, **kwargs):
            if not functions:
                return args[0] if args else None
            
            result = functions[0](*args, **kwargs)
            
            for func in functions[1:]:
                if isinstance(result, tuple):
                    result = func(*result)
                else:
                    result = func(result)
            
            return result
        return composed
    
    # Test functions for demonstration
    def add_two(a, b):
        return a + b
    
    def add_three(a, b, c):
        return a + b + c
    
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    def calculate_area(width, height):
        return width * height
    
    @create_argument_mapper(w='width', h='height')
    def mapped_area(width, height):
        return width * height
    
    # Test variable function methods
    print("=== Variable Function Methods ===")
    
    # Test flexible caller
    result1, success1, msg1 = flexible_function_caller(add_two, 5, 3)
    result2, success2, msg2 = flexible_function_caller(add_three, 1, 2)  # Missing argument
    print(f"Flexible call 1: {result1}, Success: {success1}, {msg1}")
    print(f"Flexible call 2: {result2}, Success: {success2}, {msg2}")
    
    # Test argument distributor
    functions = [add_two, greet, calculate_area]
    distributed = argument_distributor(functions, 5, 3, name="Alice", greeting="Hi", width=10, height=20)
    
    print("\nArgument Distribution Results:")
    for func_name, result_info in distributed.items():
        print(f"  {func_name}: {result_info}")
    
    # Test argument mapper
    mapped_result = mapped_area(w=5, h=3)
    print(f"\nMapped area result: {mapped_result}")
    
    # Test variadic composition
    def double(x):
        return x * 2
    
    def add_ten(x):
        return x + 10
    
    composed_func = variadic_compose(add_two, double, add_ten)
    comp_result = composed_func(3, 4)  # (3+4)*2+10 = 24
    print(f"Composed function result: {comp_result}")

variable_function_methods()
```

---

## 4. Common Errors

### 4.1 Parameter and Argument Errors

#### Error 1: Argument Count Mismatch

```python
def argument_count_errors():
    """Common argument count errors and solutions"""
    
    # ❌ WRONG: Fixed parameter function called with wrong argument count
    def wrong_fixed_params(a, b, c):
        return a + b + c
    
    try:
        result = wrong_fixed_params(1, 2)  # Missing argument
        print(result)
    except TypeError as e:
        print(f"Error: {e}")
    
    try:
        result = wrong_fixed_params(1, 2, 3, 4)  # Too many arguments
        print(result)
    except TypeError as e:
        print(f"Error: {e}")
    
    # ✅ CORRECT: Use default parameters or variable arguments
    def correct_flexible_params(a, b, c=0):
        """Function with default parameter"""
        return a + b + c
    
    def correct_variable_params(*args):
        """Function with variable arguments"""
        return sum(args)
    
    # Test correct versions
    print(f"Flexible params (2 args): {correct_flexible_params(1, 2)}")
    print(f"Flexible params (3 args): {correct_flexible_params(1, 2, 3)}")
    print(f"Variable params (2 args): {correct_variable_params(1, 2)}")
    print(f"Variable params (4 args): {correct_variable_params(1, 2, 3, 4)}")

argument_count_errors()
```

#### Error 2: Keyword Argument Errors

```python
def keyword_argument_errors():
    """Common keyword argument errors"""
    
    def sample_function(name, age, city="Unknown"):
        return f"{name}, {age}, from {city}"
    
    # ❌ WRONG: Using undefined keyword arguments
    try:
        result = sample_function("Alice", 25, country="USA")  # 'country' not defined
        print(result)
    except TypeError as e:
        print(f"Undefined keyword error: {e}")
    
    # ❌ WRONG: Duplicate keyword arguments
    try:
        result = sample_function("Bob", age=30, age=35)  # Duplicate 'age'
        print(result)
    except SyntaxError as e:
        print(f"Duplicate keyword error: {e}")
    
    # ❌ WRONG: Positional argument after keyword argument
    try:
        # This would cause SyntaxError at parse time
        # result = sample_function(name="Charlie", 40, "New York")
        pass
    except SyntaxError as e:
        print(f"Positional after keyword error: {e}")
    
    # ✅ CORRECT: Proper keyword argument usage
    def correct_function(name, age, city="Unknown", **extra_info):
        """Function that accepts extra keyword arguments"""
        result = f"{name}, {age}, from {city}"
        if extra_info:
            extras = ", ".join(f"{k}: {v}" for k, v in extra_info.items())
            result += f" ({extras})"
        return result
    
    # Test correct usage
    print(f"Correct 1: {correct_function('Alice', 25)}")
    print(f"Correct 2: {correct_function('Bob', 30, city='Paris')}")
    print(f"Correct 3: {correct_function('Charlie', 35, country='USA', job='Engineer')}")

keyword_argument_errors()
```

### 4.2 Return Value Errors

#### Error 3: Inconsistent Return Types

```python
def return_type_errors():
    """Common return type errors"""
    
    # ❌ WRONG: Inconsistent return types
    def wrong_process_data(data):
        """Function with inconsistent return types"""
        if not data:
            return None  # Returns None
        
        if len(data) == 1:
            return data[0]  # Returns single item
        
        if len(data) < 5:
            return data  # Returns list
        
        return len(data)  # Returns integer
    
    # This creates problems for callers
    results = [
        wrong_process_data([]),
        wrong_process_data([1]),
        wrong_process_data([1, 2, 3]),
        wrong_process_data([1, 2, 3, 4, 5, 6])
    ]
    
    print("Inconsistent return types:")
    for i, result in enumerate(results):
        print(f"  Result {i}: {result} (type: {type(result).__name__})")
    
    # ✅ CORRECT: Consistent return types
    def correct_process_data(data):
        """Function with consistent return types"""
        if not data:
            return []  # Always return list
        
        if len(data) == 1:
            return [data[0]]  # Return single item as list
        
        if len(data) < 5:
            return data[:]  # Return copy of list
        
        return data[:5]  # Return first 5 items as list
    
    # Test consistent version
    correct_results = [
        correct_process_data([]),
        correct_process_data([1]),
        correct_process_data([1, 2, 3]),
        correct_process_data([1, 2, 3, 4, 5, 6])
    ]
    
    print("\nConsistent return types:")
    for i, result in enumerate(correct_results):
        print(f"  Result {i}: {result} (type: {type(result).__name__})")

return_type_errors()
```

#### Error 4: Missing Return Statements

```python
def missing_return_errors():
    """Common missing return statement errors"""
    
    # ❌ WRONG: Missing return statement
    def wrong_calculate_discount(price, discount_percent):
        """Calculate discount but forget to return result"""
        if discount_percent > 100:
            discount_percent = 100
        
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        
        # Missing return statement - function returns None
    
    # ❌ WRONG: Conditional return paths missing
    def wrong_get_grade(score):
        """Get grade but missing return in some paths"""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        # Missing return for scores < 60
    
    # ❌ WRONG: Early return in loop without final return
    def wrong_find_item(items, target):
        """Find item but missing return when not found"""
        for item in items:
            if item == target:
                return True
        # Missing return False when item not found
    
    # Test wrong functions
    result1 = wrong_calculate_discount(100, 20)
    result2 = wrong_get_grade(50)
    result3 = wrong_find_item([1, 2, 3], 5)
    
    print("Wrong function results:")
    print(f"  Discount result: {result1}")  # None
    print(f"  Grade result: {result2}")     # None
    print(f"  Find result: {result3}")      # None
    
    # ✅ CORRECT: Proper return statements
    def correct_calculate_discount(price, discount_percent):
        """Calculate discount with proper return"""
        if discount_percent > 100:
            discount_percent = 100
        
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        
        return final_price  # Always return result
    
    def correct_get_grade(score):
        """Get grade with complete return paths"""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'  # Handle all cases
    
    def correct_find_item(items, target):
        """Find item with proper return"""
        for item in items:
            if item == target:
                return True
        return False  # Return False when not found
    
    # Test correct functions
    correct_result1 = correct_calculate_discount(100, 20)
    correct_result2 = correct_get_grade(50)
    correct_result3 = correct_find_item([1, 2, 3], 5)
    
    print("\nCorrect function results:")
    print(f"  Discount result: {correct_result1}")  # 80.0
    print(f"  Grade result: {correct_result2}")     # F
    print(f"  Find result: {correct_result3}")      # False

missing_return_errors()
```

### 4.3 Variable Function Errors

#### Error 5: *args and **kwargs Misuse

```python
def args_kwargs_errors():
    """Common *args and **kwargs errors"""
    
    # ❌ WRONG: Incorrect parameter order
    try:
        # This would cause SyntaxError
        # def wrong_order(**kwargs, *args):
        #     pass
        pass
    except SyntaxError as e:
        print(f"Parameter order error: {e}")
    
    # ❌ WRONG: Using *args/**kwargs incorrectly in calls
    def sample_function(a, b, c=10):
        return a + b + c
    
    try:
        args_tuple = (1, 2, 3, 4)  # Too many arguments
        result = sample_function(*args_tuple)
        print(result)
    except TypeError as e:
        print(f"Args unpacking error: {e}")
    
    try:
        kwargs_dict = {'a': 1, 'b': 2, 'd': 4}  # 'd' is not a parameter
        result = sample_function(**kwargs_dict)
        print(result)
    except TypeError as e:
        print(f"Kwargs unpacking error: {e}")
    
    # ❌ WRONG: Modifying *args or **kwargs
    def wrong_modify_args(*args, **kwargs):
        """Incorrectly trying to modify args and kwargs"""
        try:
            args[0] = 999  # TypeError: tuple doesn't support item assignment
        except TypeError as e:
            print(f"Args modification error: {e}")
        
        kwargs['new_key'] = 'new_value'  # This works but affects original dict
        return args, kwargs
    
    original_kwargs = {'x': 1, 'y': 2}
    result_args, result_kwargs = wrong_modify_args(1, 2, 3, **original_kwargs)
    print(f"Original kwargs after function: {original_kwargs}")  # Modified!
    
    # ✅ CORRECT: Proper *args and **kwargs usage
    def correct_variable_function(required_arg, *args, optional_kw=None, **kwargs):
        """Correct parameter order and usage"""
        result = {
            'required': required_arg,
            'args': args,
            'optional_kw': optional_kw,
            'kwargs': kwargs
        }
        return result
    
    def correct_safe_modify(*args, **kwargs):
        """Safely work with args and kwargs"""
        # Convert to mutable types if modification needed
        args_list = list(args)
        kwargs_copy = kwargs.copy()
        
        if args_list:
            args_list[0] = 999
        
        kwargs_copy['new_key'] = 'new_value'
        
        return tuple(args_list), kwargs_copy
    
    # Test correct usage
    correct_result = correct_variable_function(
        'required_value',
        1, 2, 3,
        optional_kw='optional_value',
        extra1='value1',
        extra2='value2'
    )
    print(f"\nCorrect variable function: {correct_result}")
    
    # Test safe modification
    original_kwargs2 = {'x': 1, 'y': 2}
    safe_args, safe_kwargs = correct_safe_modify(1, 2, 3, **original_kwargs2)
    print(f"Safe modification result: args={safe_args}, kwargs={safe_kwargs}")
    print(f"Original kwargs unchanged: {original_kwargs2}")

args_kwargs_errors()
```

### 4.4 Function as Parameter Errors

#### Error 6: Function Parameter Misuse

```python
def function_parameter_errors():
    """Common errors when using functions as parameters"""
    
    # ❌ WRONG: Calling function instead of passing it
    def wrong_higher_order_usage():
        """Demonstrate wrong way to pass functions"""
        
        def add(x, y):
            return x + y
        
        def apply_operation(func, a, b):
            return func(a, b)
        
        # Wrong: Calling function instead of passing it
        try:
            result = apply_operation(add(5, 3), 10, 20)  # add(5,3) returns 8, not a function
            print(result)
        except TypeError as e:
            print(f"Function call error: {e}")
    
    # ❌ WRONG: Not checking if parameter is callable
    def wrong_no_callable_check(func, data):
        """Function that doesn't check if parameter is callable"""
        return func(data)  # Will fail if func is not callable
    
    try:
        result = wrong_no_callable_check("not_a_function", [1, 2, 3])
        print(result)
    except TypeError as e:
        print(f"Not callable error: {e}")
    
    # ❌ WRONG: Assuming function signature
    def wrong_signature_assumption(func, data):
        """Function that assumes specific signature"""
        return func(data, "extra_param")  # Assumes func takes 2 parameters
    
    def single_param_func(x):
        return x * 2
    
    try:
        result = wrong_signature_assumption(single_param_func, 5)
        print(result)
    except TypeError as e:
        print(f"Signature assumption error: {e}")
    
    # ✅ CORRECT: Proper function parameter handling
    def correct_higher_order_usage():
        """Demonstrate correct way to pass functions"""
        
        def add(x, y):
            return x + y
        
        def multiply(x, y):
            return x * y
        
        def apply_operation(func, a, b):
            return func(a, b)
        
        # Correct: Pass function reference, not call result
        result1 = apply_operation(add, 5, 3)        # Pass add function
        result2 = apply_operation(multiply, 4, 7)   # Pass multiply function
        
        print(f"Correct add result: {result1}")
        print(f"Correct multiply result: {result2}")
    
    def correct_callable_check(func, data):
        """Function that properly checks if parameter is callable"""
        if not callable(func):
            raise TypeError(f"Expected callable, got {type(func).__name__}")
        
        return func(data)
    
    def correct_flexible_signature(func, data, *args, **kwargs):
        """Function that handles flexible signatures"""
        try:
            # Try with additional arguments
            return func(data, *args, **kwargs)
        except TypeError:
            try:
                # Try with just data
                return func(data)
            except TypeError:
                # Try with no arguments
                return func()
    
    # Test correct implementations
    wrong_higher_order_usage()
    correct_higher_order_usage()
    
    # Test callable check
    try:
        result = correct_callable_check(len, [1, 2, 3, 4])
        print(f"Callable check result: {result}")
        
        correct_callable_check("not_callable", [1, 2, 3])
    except TypeError as e:
        print(f"Proper callable check error: {e}")
    
    # Test flexible signature
    def no_param_func():
        return "no params"
    
    def one_param_func(x):
        return f"one param: {x}"
    
    def two_param_func(x, y):
        return f"two params: {x}, {y}"
    
    print(f"Flexible signature 1: {correct_flexible_signature(no_param_func, 'data')}")
    print(f"Flexible signature 2: {correct_flexible_signature(one_param_func, 'data')}")
    print(f"Flexible signature 3: {correct_flexible_signature(two_param_func, 'data', 'extra')}")

function_parameter_errors()
```

### 4.5 Error Prevention Best Practices

```python
def error_prevention_best_practices():
    """Best practices for preventing function parameter errors"""
    
    print("""
=== Function Parameter Error Prevention Checklist ===

1. PARAMETER DESIGN:
   ✓ Use descriptive parameter names
   ✓ Provide sensible default values
   ✓ Order parameters logically (required first, then optional)
   ✓ Use type hints for clarity
   ✓ Document parameter requirements and constraints

2. ARGUMENT VALIDATION:
   ✓ Check parameter types at function entry
   ✓ Validate parameter values and ranges
   ✓ Handle None values appropriately
   ✓ Provide clear error messages for invalid inputs

3. RETURN VALUE CONSISTENCY:
   ✓ Always return the same type from all code paths
   ✓ Document return value types and meanings
   ✓ Use explicit return statements
   ✓ Handle all possible execution paths

4. VARIABLE ARGUMENTS:
   ✓ Use correct parameter order (*args before **kwargs)
   ✓ Don't modify *args directly (it's a tuple)
   ✓ Make copies of **kwargs if modification needed
   ✓ Validate variable arguments appropriately

5. FUNCTION PARAMETERS:
   ✓ Check if function parameters are callable
   ✓ Don't assume function signatures
   ✓ Pass function references, not function calls
   ✓ Handle function execution errors gracefully

6. ERROR HANDLING:
   ✓ Use try-except blocks for risky operations
   ✓ Provide meaningful error messages
   ✓ Log errors appropriately
   ✓ Fail fast with clear error indication

7. TESTING:
   ✓ Test with valid parameter combinations
   ✓ Test edge cases and boundary conditions
   ✓ Test error conditions and exception handling
   ✓ Test all return paths and scenarios
    """)
    
    # Example of comprehensive best practices implementation
    def robust_data_processor(
        data: list,
        processor_func: callable,
        *extra_args,
        validate: bool = True,
        default_value = None,
        **processor_kwargs
    ) -> tuple:
        """
        Robust data processor implementing best practices.
        
        Args:
            data: List of data items to process
            processor_func: Function to apply to each data item
            *extra_args: Additional positional arguments for processor_func
            validate: Whether to validate inputs
            default_value: Value to use for failed processing
            **processor_kwargs: Additional keyword arguments for processor_func
        
        Returns:
            tuple: (processed_results, error_count, errors_list)
        """
        # Input validation
        if validate:
            if not isinstance(data, list):
                raise TypeError(f"Expected list for data, got {type(data).__name__}")
            
            if not callable(processor_func):
                raise TypeError(f"Expected callable for processor_func, got {type(processor_func).__name__}")
        
        processed_results = []
        error_count = 0
        errors_list = []
        
        for i, item in enumerate(data):
            try:
                # Flexible function calling
                result = processor_func(item, *extra_args, **processor_kwargs)
                processed_results.append(result)
                
            except Exception as e:
                error_count += 1
                error_info = {
                    'index': i,
                    'item': item,
                    'error': str(e),
                    'error_type': type(e).__name__
                }
                errors_list.append(error_info)
                processed_results.append(default_value)
        
        return processed_results, error_count, errors_list
    
    # Test robust implementation
    def test_processor(x):
        if x < 0:
            raise ValueError("Negative values not allowed")
        return x * 2
    
    test_data = [1, 2, -3, 4, "invalid", 6]
    results, errors, error_details = robust_data_processor(
        test_data,
        test_processor,
        validate=True,
        default_value=0
    )
    
    print(f"\nRobust processor results: {results}")
    print(f"Error count: {errors}")
    print(f"Error details: {error_details}")

error_prevention_best_practices()
```

---

## Summary

This comprehensive documentation covers:

1. **Definitions and Characteristics**: All types of function parameters, arguments, and return values
2. **Operations**: Parameter passing, function composition, and dynamic function creation
3. **Methods**: Introspection, validation, return handling, and variable argument techniques
4. **Common Errors**: Detailed examples of common mistakes and their solutions

The documentation provides practical, runnable examples for each concept, demonstrating both incorrect and correct approaches to help developers avoid common pitfalls and write robust, maintainable code.
