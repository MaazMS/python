#!/usr/bin/env python3
"""
Python Function Parameters, Arguments, and Return Values Program

This program demonstrates all concepts from function_documentation.md including:
- Function parameter types (no args, single, multiple, default)
- Functions as parameters
- Return values (single, multiple)
- Variable functions (*args, **kwargs)
- Function operations and methods
- Common errors and best practices

Author: Generated from function_documentation.md
"""

import inspect
import time
from typing import Any, Callable


def main():
    """Main function to run all demonstrations"""
    print("=" * 70)
    print("PYTHON FUNCTION PARAMETERS, ARGUMENTS, AND RETURN VALUES")
    print("=" * 70)
    
    # Section 1: Definitions and Characteristics
    print("\n1. DEFINITIONS AND CHARACTERISTICS")
    print("-" * 50)
    demonstrate_parameter_types()
    demonstrate_functions_as_parameters()
    demonstrate_return_values()
    demonstrate_variable_functions()
    
    # Section 2: Operations
    print("\n2. OPERATIONS")
    print("-" * 50)
    demonstrate_parameter_operations()
    demonstrate_function_composition()
    demonstrate_dynamic_functions()
    
    # Section 3: Methods
    print("\n3. METHODS")
    print("-" * 50)
    demonstrate_introspection_methods()
    demonstrate_validation_methods()
    demonstrate_return_methods()
    demonstrate_variable_methods()
    
    # Section 4: Common Errors
    print("\n4. COMMON ERRORS AND BEST PRACTICES")
    print("-" * 50)
    demonstrate_common_errors()
    demonstrate_best_practices()
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)


# Section 1: Definitions and Characteristics

def demonstrate_parameter_types():
    """Demonstrate different types of function parameters"""
    print("\n1.1 Function Parameter Types")
    
    # No Arguments
    def no_argument_function():
        """Function with no parameters"""
        return "Hello, World!"
    
    print("No Arguments:")
    result = no_argument_function()
    print(f"  Result: {result}")
    print(f"  Type: {type(no_argument_function)}")
    
    # Single Argument
    def single_argument_function(name):
        """Function with single parameter"""
        return f"Hello, {name}!"
    
    print("\nSingle Argument:")
    print(f"  String: {single_argument_function('Alice')}")
    print(f"  Number: {single_argument_function(123)}")
    print(f"  List: {single_argument_function([1,2,3])}")
    
    # Multiple Arguments
    def multiple_arguments_function(first_name, last_name, age):
        """Function with multiple parameters"""
        return f"{first_name} {last_name} is {age} years old"
    
    print("\nMultiple Arguments:")
    result = multiple_arguments_function("John", "Doe", 30)
    print(f"  Result: {result}")
    
    # Default Arguments
    def default_argument_function(name, greeting="Hello", punctuation="!"):
        """Function with default parameters"""
        return f"{greeting}, {name}{punctuation}"
    
    print("\nDefault Arguments:")
    print(f"  Using defaults: {default_argument_function('Alice')}")
    print(f"  Custom greeting: {default_argument_function('Bob', 'Hi')}")
    print(f"  All custom: {default_argument_function('Charlie', 'Hey', '?')}")
    print(f"  Keyword args: {default_argument_function('Diana', punctuation='!!!')}")


def demonstrate_functions_as_parameters():
    """Demonstrate functions as parameters"""
    print("\n1.2 Functions as Parameters")
    
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
    
    print("Higher-Order Functions:")
    print(f"  Add: {calculate(add, 5, 3)}")
    print(f"  Multiply: {calculate(multiply, 4, 7)}")
    print(f"  Subtract: {calculate(subtract, 10, 4)}")
    print(f"  Lambda: {calculate(lambda x, y: x ** y, 2, 3)}")
    
    # Parameter comparison
    def get_current_time():
        import datetime
        return datetime.datetime.now()
    
    def execute_function(func):
        """Execute a function that takes no parameters"""
        return func()
    
    def execute_with_args(func, *args, **kwargs):
        """Execute a function with arguments"""
        return func(*args, **kwargs)
    
    print("\nParameter Comparison:")
    current_time = execute_function(get_current_time)
    print(f"  Current time: {current_time}")
    
    result = execute_with_args(max, [1, 5, 3, 9, 2])
    print(f"  Maximum: {result}")
    
    # Function factories
    def create_multiplier(factor):
        def multiplier(x):
            return x * factor
        return multiplier
    
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"  Double 5: {execute_with_args(double, 5)}")
    print(f"  Triple 4: {execute_with_args(triple, 4)}")


def demonstrate_return_values():
    """Demonstrate single and multiple return values"""
    print("\n1.3 Return Values")
    
    # Single Return
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
    
    print("Single Return Values:")
    area = calculate_area(5, 3)
    name = get_full_name("Jane", "Smith")
    even_check = is_even(4)
    user = get_user_data()
    
    print(f"  Area: {area}")
    print(f"  Name: {name}")
    print(f"  Is even: {even_check}")
    print(f"  User: {user}")
    
    # Multiple Return
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
    
    print("\nMultiple Return Values:")
    # Unpacking multiple returns
    total, count, avg, max_val = calculate_statistics([1, 2, 3, 4, 5])
    print(f"  Stats - Total: {total}, Count: {count}, Average: {avg}, Max: {max_val}")
    
    first, last = parse_name("John Doe Smith")
    print(f"  Name - First: {first}, Last: {last}")
    
    q, r = divide_with_remainder(17, 5)
    print(f"  Division - 17 ÷ 5 = {q} remainder {r}")
    
    x, y, z = get_coordinates()
    print(f"  Coordinates: ({x}, {y}, {z})")
    
    # Can also receive as tuple
    stats_tuple = calculate_statistics([10, 20, 30])
    print(f"  Stats tuple: {stats_tuple}")


def demonstrate_variable_functions():
    """Demonstrate variable arguments (*args and **kwargs)"""
    print("\n1.4 Variable Functions")
    
    # Variable Arguments (*args)
    def sum_all(*args):
        """Sum any number of arguments"""
        return sum(args)
    
    def print_info(title, *details):
        """Print title and variable details"""
        print(f"    Title: {title}")
        for i, detail in enumerate(details, 1):
            print(f"      Detail {i}: {detail}")
    
    def find_maximum(*numbers):
        """Find maximum from variable arguments"""
        if not numbers:
            return None
        return max(numbers)
    
    def concatenate_strings(separator=" ", *strings):
        """Concatenate variable strings with separator"""
        return separator.join(strings)
    
    print("Variable Arguments (*args):")
    print(f"  Sum of 1,2,3: {sum_all(1, 2, 3)}")
    print(f"  Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
    print(f"  Sum of no args: {sum_all()}")
    
    print("  Print info:")
    print_info("User Profile", "John Doe", "30 years old", "Engineer")
    
    print(f"  Maximum: {find_maximum(5, 2, 8, 1, 9)}")
    
    result = concatenate_strings("-", "apple", "banana", "cherry")
    print(f"  Concatenated: {result}")
    
    # Variable Keyword Arguments (**kwargs)
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
            print(f"    {key.capitalize()}: {value}")
    
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
    
    print("\nVariable Keyword Arguments (**kwargs):")
    profile = create_profile(name="Alice", age=25, city="New York", job="Developer")
    print(f"  Profile: {profile}")
    
    db_config = configure_database("localhost", 5432, username="admin", password="secret", ssl=True)
    print(f"  Database config: {db_config}")
    
    print("  User Information:")
    print_formatted(name="Bob", age=30, email="bob@example.com", active=True)
    
    calc_result = flexible_calculator("add", 1, 2, 3, 4, 5, absolute=True, round_to=2)
    print(f"  Calculator result: {calc_result}")


# Section 2: Operations

def demonstrate_parameter_operations():
    """Demonstrate parameter passing operations"""
    print("\n2.1 Parameter Passing Operations")
    
    # Positional Argument Passing
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
    
    print("Positional Arguments:")
    rect1 = create_rectangle(10, 5)                    # Using default color
    rect2 = create_rectangle(8, 6, "red")              # All positional
    
    print(f"  Rectangle 1: {rect1}")
    print(f"  Rectangle 2: {rect2}")
    
    # Operations with variable arguments
    text_result = process_data("hello", "uppercase")
    reverse_result = process_data("world", "reverse")
    multiply_result = process_data("hi", "multiply", 3)
    
    print(f"  Uppercase: {text_result}")
    print(f"  Reverse: {reverse_result}")
    print(f"  Multiply: {multiply_result}")
    
    # Keyword Argument Passing
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
    
    print("\nKeyword Arguments:")
    user1 = create_user("John", "john@example.com")
    user2 = create_user(name="Alice", email="alice@example.com", age=25)
    user3 = create_user("Bob", "bob@example.com", department="IT", role="Developer")
    
    print(f"  User 1: {user1}")
    print(f"  User 2: {user2}")
    print(f"  User 3: {user3}")
    
    # Message formatting operations
    msg1 = format_message("Hello", uppercase=True)
    msg2 = format_message("World", prefix=">>> ", suffix=" <<<")
    msg3 = format_message("Hi", repeat=3, prefix="* ")
    
    print(f"  Message 1: {msg1}")
    print(f"  Message 2: {msg2}")
    print(f"  Message 3: {msg3}")


def demonstrate_function_composition():
    """Demonstrate function chaining operations"""
    print("\n2.2 Function Composition Operations")
    
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


def demonstrate_dynamic_functions():
    """Demonstrate dynamic function creation operations"""
    print("\n2.3 Dynamic Function Operations")
    
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
    
    print("Validator Tests:")
    print(f"  Age 25: {age_validator(25)}")      # (True, 'Valid')
    print(f"  Age 150: {age_validator(150)}")     # (False, 'Value 150 is greater than maximum 120')
    print(f"  Age '25': {age_validator('25')}")    # (False, 'Expected int, got str')
    
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
    
    print("\nFormatter Tests:")
    print(f"  Email 1: {email_formatter(name='John Doe', email='john@example.com')}")
    print(f"  Email 2: {email_formatter(email='jane@example.com')}")
    print(f"  Greeting: {greeting_formatter(name='Alice', place='Python world')}")
    
    # Create calculators
    adder = create_calculator('add')
    multiplier = create_calculator('multiply')
    
    print("\nCalculator Tests:")
    print(f"  Add 1,2,3,4,5: {adder(1, 2, 3, 4, 5)}")
    print(f"  Multiply 2,3,4: {multiplier(2, 3, 4)}")


# Section 3: Methods

def demonstrate_introspection_methods():
    """Methods for inspecting function parameters"""
    print("\n3.1 Function Introspection Methods")
    
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
    print("Parameter Inspection:")
    param_info = inspect_function_parameters(sample_function)
    
    print(f"  Function: {param_info['function_name']}")
    print(f"  Return type: {param_info['return_annotation']}")
    print("  Parameters:")
    for name, info in param_info['parameters'].items():
        print(f"    {name}:")
        print(f"      Kind: {info['kind']}")
        print(f"      Default: {info['default']}")
        print(f"      Annotation: {info['annotation']}")
    
    # Get metadata
    print("\nFunction Metadata:")
    metadata = get_function_metadata(sample_function)
    for key, value in metadata.items():
        if key != 'code_info':
            print(f"  {key}: {value}")
    
    print("  Code info:")
    for key, value in metadata['code_info'].items():
        print(f"    {key}: {value}")


def demonstrate_validation_methods():
    """Methods for parameter validation"""
    print("\n3.2 Parameter Validation Methods")
    
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
    print("Validation Methods:")
    
    try:
        # Valid record
        record1 = create_student_record("Alice", 20, 85.5, grade="A")
        print(f"  Valid record: {record1}")
        
        # Valid with defaults
        record2 = create_student_record("Bob", 22)
        print(f"  Valid with defaults: {record2}")
        
        # Invalid type
        try:
            create_student_record("Charlie", "twenty", 90.0)
        except TypeError as e:
            print(f"  Type error: {e}")
        
        # Invalid range
        try:
            create_student_record("Diana", 25, 150.0)
        except ValueError as e:
            print(f"  Range error: {e}")
        
        # Missing required
        try:
            create_student_record(age=30, score=75.0)
        except ValueError as e:
            print(f"  Required error: {e}")
    
    except Exception as e:
        print(f"  Unexpected error: {e}")


def demonstrate_return_methods():
    """Methods for handling return values"""
    print("\n3.3 Return Value Methods")
    
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
    print("Return Value Methods:")
    
    # Test safe divide
    result1, msg1 = safe_divide(10, 2)
    result2, msg2 = safe_divide(10, 0)
    print(f"  10/2: {result1}, {msg1}")
    print(f"  10/0: {result2}, {msg2}")
    
    # Test config parsing
    key1, val1, status1 = parse_config_line("database_host=localhost")
    key2, val2, status2 = parse_config_line("# This is a comment")
    print(f"  Config 1: {key1}={val1}, {status1}")
    print(f"  Config 2: {key2}={val2}, {status2}")
    
    # Test user info
    user1, active1, msg_1 = get_user_info(1)
    user2, active2, msg_2 = get_user_info(999)
    print(f"  User 1: {user1}, Active: {active1}, {msg_1}")
    print(f"  User 999: {user2}, Active: {active2}, {msg_2}")
    
    # Test generic processor
    proc_result1 = process_multiple_returns(safe_divide, 15, 3)
    proc_result2 = process_multiple_returns(len, "hello")
    print(f"  Processed divide: {proc_result1}")
    print(f"  Processed len: {proc_result2}")
    
    # Test unpacking with defaults
    unpacked1 = unpack_with_defaults((1, 2), 0, 0, 0)
    unpacked2 = unpack_with_defaults((1,), 0, 0, 0)
    print(f"  Unpacked 1: {unpacked1}")
    print(f"  Unpacked 2: {unpacked2}")


def demonstrate_variable_methods():
    """Advanced methods for variable functions"""
    print("\n3.4 Variable Function Methods")
    
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
    print("Variable Function Methods:")
    
    # Test flexible caller
    result1, success1, msg1 = flexible_function_caller(add_two, 5, 3)
    result2, success2, msg2 = flexible_function_caller(add_three, 1, 2)  # Missing argument
    print(f"  Flexible call 1: {result1}, Success: {success1}, {msg1}")
    print(f"  Flexible call 2: {result2}, Success: {success2}, {msg2}")
    
    # Test argument distributor
    functions = [add_two, greet, calculate_area]
    distributed = argument_distributor(functions, 5, 3, name="Alice", greeting="Hi", width=10, height=20)
    
    print("  Argument Distribution Results:")
    for func_name, result_info in distributed.items():
        print(f"    {func_name}: {result_info}")
    
    # Test argument mapper
    mapped_result = mapped_area(w=5, h=3)
    print(f"  Mapped area result: {mapped_result}")
    
    # Test variadic composition
    def double(x):
        return x * 2
    
    def add_ten(x):
        return x + 10
    
    composed_func = variadic_compose(add_two, double, add_ten)
    comp_result = composed_func(3, 4)  # (3+4)*2+10 = 24
    print(f"  Composed function result: {comp_result}")


# Section 4: Common Errors

def demonstrate_common_errors():
    """Demonstrate common function errors and solutions"""
    print("\n4.1 Common Function Errors")
    
    # Error 1: Argument Count Mismatch
    print("Error 1: Argument Count Mismatch")
    
    def wrong_fixed_params(a, b, c):
        return a + b + c
    
    try:
        result = wrong_fixed_params(1, 2)  # Missing argument
        print(result)
    except TypeError as e:
        print(f"  Error: {e}")
    
    try:
        result = wrong_fixed_params(1, 2, 3, 4)  # Too many arguments
        print(result)
    except TypeError as e:
        print(f"  Error: {e}")
    
    # Solutions
    def correct_flexible_params(a, b, c=0):
        """Function with default parameter"""
        return a + b + c
    
    def correct_variable_params(*args):
        """Function with variable arguments"""
        return sum(args)
    
    # Test correct versions
    print(f"  Fixed with default: {correct_flexible_params(1, 2)}")
    print(f"  Fixed with default (3 args): {correct_flexible_params(1, 2, 3)}")
    print(f"  Fixed with *args (2 args): {correct_variable_params(1, 2)}")
    print(f"  Fixed with *args (4 args): {correct_variable_params(1, 2, 3, 4)}")
    
    # Error 2: Keyword Argument Errors
    print("\nError 2: Keyword Argument Errors")
    
    def sample_function(name, age, city="Unknown"):
        return f"{name}, {age}, from {city}"
    
    # Wrong: Using undefined keyword arguments
    try:
        result = sample_function("Alice", 25, country="USA")  # 'country' not defined
        print(result)
    except TypeError as e:
        print(f"  Undefined keyword error: {e}")
    
    # Correct: Proper keyword argument usage
    def correct_function(name, age, city="Unknown", **extra_info):
        """Function that accepts extra keyword arguments"""
        result = f"{name}, {age}, from {city}"
        if extra_info:
            extras = ", ".join(f"{k}: {v}" for k, v in extra_info.items())
            result += f" ({extras})"
        return result
    
    # Test correct usage
    print(f"  Correct 1: {correct_function('Alice', 25)}")
    print(f"  Correct 2: {correct_function('Bob', 30, city='Paris')}")
    print(f"  Correct 3: {correct_function('Charlie', 35, country='USA', job='Engineer')}")
    
    # Error 3: Inconsistent Return Types
    print("\nError 3: Inconsistent Return Types")
    
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
    
    print("  Inconsistent return types:")
    for i, result in enumerate(results):
        print(f"    Result {i}: {result} (type: {type(result).__name__})")
    
    # Correct: Consistent return types
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
    
    print("  Consistent return types:")
    for i, result in enumerate(correct_results):
        print(f"    Result {i}: {result} (type: {type(result).__name__})")
    
    # Error 4: Missing Return Statements
    print("\nError 4: Missing Return Statements")
    
    def wrong_calculate_discount(price, discount_percent):
        """Calculate discount but forget to return result"""
        if discount_percent > 100:
            discount_percent = 100
        
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        
        # Missing return statement - function returns None
    
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
    
    # Test wrong functions
    result1 = wrong_calculate_discount(100, 20)
    result2 = wrong_get_grade(50)
    
    print(f"  Wrong discount result: {result1}")  # None
    print(f"  Wrong grade result: {result2}")     # None
    
    # Correct versions
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
    
    # Test correct functions
    correct_result1 = correct_calculate_discount(100, 20)
    correct_result2 = correct_get_grade(50)
    
    print(f"  Correct discount result: {correct_result1}")  # 80.0
    print(f"  Correct grade result: {correct_result2}")     # F
    
    # Error 5: *args and **kwargs Misuse
    print("\nError 5: *args and **kwargs Misuse")
    
    def sample_func_for_args(a, b, c=10):
        return a + b + c
    
    try:
        args_tuple = (1, 2, 3, 4)  # Too many arguments
        result = sample_func_for_args(*args_tuple)
        print(result)
    except TypeError as e:
        print(f"  Args unpacking error: {e}")
    
    try:
        kwargs_dict = {'a': 1, 'b': 2, 'd': 4}  # 'd' is not a parameter
        result = sample_func_for_args(**kwargs_dict)
        print(result)
    except TypeError as e:
        print(f"  Kwargs unpacking error: {e}")
    
    # Correct: Proper *args and **kwargs usage
    def correct_variable_function(required_arg, *args, optional_kw=None, **kwargs):
        """Correct parameter order and usage"""
        result = {
            'required': required_arg,
            'args': args,
            'optional_kw': optional_kw,
            'kwargs': kwargs
        }
        return result
    
    # Test correct usage
    correct_result = correct_variable_function(
        'required_value',
        1, 2, 3,
        optional_kw='optional_value',
        extra1='value1',
        extra2='value2'
    )
    print(f"  Correct variable function: {correct_result}")


def demonstrate_best_practices():
    """Demonstrate best practices for function parameters"""
    print("\n4.2 Error Prevention Best Practices")
    
    print("""
Function Parameter Error Prevention Checklist:

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
        if isinstance(x, str):
            raise TypeError("String values not allowed")
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
    
    print(f"Robust processor results: {results}")
    print(f"Error count: {errors}")
    print(f"Error details: {error_details}")


if __name__ == "__main__":
    main()
