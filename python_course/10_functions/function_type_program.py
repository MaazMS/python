#!/usr/bin/env python3
"""
Python Functions and Function Types Program

This program demonstrates all concepts from function_type_documentation.md including:
- Function definitions and characteristics
- Function operations
- Function methods and advanced usage
- Common errors and best practices

Author: Generated from function_type_documentation.md
"""

import functools
import inspect
import time
import random
from typing import Callable, Any


def main():
    """Main function to run all demonstrations"""
    print("=" * 60)
    print("PYTHON FUNCTIONS AND FUNCTION TYPES DEMONSTRATION")
    print("=" * 60)
    
    # Section 1: Function Definitions and Characteristics
    print("\n1. FUNCTION DEFINITIONS AND CHARACTERISTICS")
    print("-" * 50)
    demonstrate_first_class_objects()
    demonstrate_function_properties()
    demonstrate_function_types()
    demonstrate_function_signatures()
    
    # Section 2: Function Operations
    print("\n2. FUNCTION OPERATIONS")
    print("-" * 50)
    demonstrate_basic_operations()
    demonstrate_higher_order_functions()
    demonstrate_function_composition()
    
    # Section 3: Function Methods and Advanced Usage
    print("\n3. FUNCTION METHODS AND ADVANCED USAGE")
    print("-" * 50)
    demonstrate_function_introspection()
    demonstrate_decorators()
    demonstrate_closures()
    demonstrate_caching()
    
    # Section 4: Common Errors and Best Practices
    print("\n4. COMMON ERRORS AND BEST PRACTICES")
    print("-" * 50)
    demonstrate_common_errors()
    demonstrate_error_handling()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


# Section 1: Function Definitions and Characteristics

def demonstrate_first_class_objects():
    """Demonstrate that functions are first-class objects"""
    print("\n1.1 First-Class Objects")
    
    def greet(name):
        """A simple greeting function"""
        return f"Hello, {name}!"
    
    # Functions can be assigned to variables
    my_function = greet
    print(f"Function assigned to variable: {my_function('Alice')}")
    
    # Functions have attributes
    print(f"Function name: {greet.__name__}")
    print(f"Function doc: {greet.__doc__}")
    
    # Functions can be stored in data structures
    function_list = [greet, print, len]
    function_dict = {'greeting': greet, 'output': print}
    print(f"Functions in list: {[f.__name__ for f in function_list]}")
    print(f"Functions in dict: {list(function_dict.keys())}")


def demonstrate_function_properties():
    """Demonstrate function object properties"""
    print("\n1.2 Function Object Properties")
    
    def calculate_area(length, width=10):
        """Calculate area of rectangle"""
        return length * width
    
    print(f"Function name: {calculate_area.__name__}")
    print(f"Function doc: {calculate_area.__doc__}")
    print(f"Function defaults: {calculate_area.__defaults__}")
    print(f"Function code variables: {calculate_area.__code__.co_varnames}")
    print(f"Argument count: {calculate_area.__code__.co_argcount}")


def demonstrate_function_types():
    """Demonstrate different types of functions"""
    print("\n1.3 Types of Functions")
    
    # Built-in functions
    print("Built-in functions:")
    print(f"type(print): {type(print)}")
    print(f"type(len): {type(len)}")
    print(f"type(max): {type(max)}")
    
    numbers = [1, 5, 3, 9, 2]
    print(f"Length: {len(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Sum: {sum(numbers)}")
    
    # User-defined functions
    def user_function(x, y):
        """User-defined function"""
        return x + y
    
    print(f"\nUser-defined function type: {type(user_function)}")
    
    # Lambda functions
    square = lambda x: x ** 2
    print(f"Lambda function type: {type(square)}")
    print(f"Lambda result: {square(5)}")
    
    # Method functions
    class Calculator:
        def add(self, x, y):
            return x + y
        
        @staticmethod
        def multiply(x, y):
            return x * y
        
        @classmethod
        def create_with_default(cls):
            return cls()
    
    calc = Calculator()
    print(f"\nInstance method type: {type(calc.add)}")
    print(f"Static method type: {type(Calculator.multiply)}")
    print(f"Class method type: {type(Calculator.create_with_default)}")


def demonstrate_function_signatures():
    """Demonstrate comprehensive function signatures"""
    print("\n1.4 Function Signature Characteristics")
    
    def comprehensive_function(
        positional_arg,                    # Required positional argument
        default_arg=10,                   # Default argument
        *args,                           # Variable positional arguments
        keyword_only_arg,                # Keyword-only argument
        keyword_with_default=None,       # Keyword-only with default
        **kwargs                         # Variable keyword arguments
    ):
        """Demonstrates all types of function parameters"""
        print(f"  Positional: {positional_arg}")
        print(f"  Default: {default_arg}")
        print(f"  Args: {args}")
        print(f"  Keyword-only: {keyword_only_arg}")
        print(f"  Keyword with default: {keyword_with_default}")
        print(f"  Kwargs: {kwargs}")
    
    print("Calling comprehensive function:")
    comprehensive_function(
        "required",
        20,
        "extra1", "extra2",
        keyword_only_arg="must_be_keyword",
        keyword_with_default="custom",
        extra_key="extra_value"
    )


# Section 2: Function Operations

def demonstrate_basic_operations():
    """Demonstrate basic function operations"""
    print("\n2.1 Basic Function Operations")
    
    # Simple function
    def add(a, b):
        return a + b
    
    # Function with default parameters
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    # Function with variable arguments
    def sum_all(*numbers):
        return sum(numbers)
    
    # Function with keyword arguments
    def create_profile(**kwargs):
        return kwargs
    
    # Calling functions
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"greet('Alice') = {greet('Alice')}")
    print(f"greet('Bob', 'Hi') = {greet('Bob', 'Hi')}")
    print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
    print(f"create_profile(name='John', age=30) = {create_profile(name='John', age=30)}")
    
    # Function references
    print("\nFunction References:")
    def original_function(x):
        return x * 2
    
    func_copy = original_function
    print(f"func_copy(5) = {func_copy(5)}")
    print(f"Same object? {id(original_function) == id(func_copy)}")
    
    # Storing functions in collections
    operations = {
        'double': lambda x: x * 2,
        'square': lambda x: x ** 2,
        'cube': lambda x: x ** 3
    }
    
    print("Operations on 3:")
    for name, func in operations.items():
        print(f"  {name}(3) = {func(3)}")


def demonstrate_higher_order_functions():
    """Demonstrate higher-order function operations"""
    print("\n2.2 Higher-Order Function Operations")
    
    def apply_operation(numbers, operation):
        """Apply operation to each number"""
        return [operation(num) for num in numbers]
    
    def filter_numbers(numbers, condition):
        """Filter numbers based on condition"""
        return [num for num in numbers if condition(num)]
    
    def reduce_numbers(numbers, operation, initial=0):
        """Reduce numbers using operation"""
        result = initial
        for num in numbers:
            result = operation(result, num)
        return result
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Using functions as arguments
    squared = apply_operation(numbers, lambda x: x ** 2)
    print(f"Squared: {squared}")
    
    evens = filter_numbers(numbers, lambda x: x % 2 == 0)
    print(f"Even numbers: {evens}")
    
    total = reduce_numbers(numbers, lambda x, y: x + y)
    print(f"Sum: {total}")
    
    product = reduce_numbers(numbers, lambda x, y: x * y, 1)
    print(f"Product: {product}")
    
    # Functions returning functions
    print("\nFunction Factories:")
    
    def create_multiplier(factor):
        """Factory function that creates multiplier functions"""
        def multiplier(x):
            return x * factor
        return multiplier
    
    def create_validator(min_val, max_val):
        """Factory function that creates validator functions"""
        def validator(value):
            return min_val <= value <= max_val
        return validator
    
    # Create specific functions
    double = create_multiplier(2)
    triple = create_multiplier(3)
    age_validator = create_validator(0, 120)
    
    print(f"double(5) = {double(5)}")
    print(f"triple(4) = {triple(4)}")
    print(f"age_validator(25) = {age_validator(25)}")
    print(f"age_validator(150) = {age_validator(150)}")


def demonstrate_function_composition():
    """Demonstrate function composition operations"""
    print("\n2.3 Function Composition")
    
    def compose(f, g):
        """Compose two functions: f(g(x))"""
        return lambda x: f(g(x))
    
    def pipe(*functions):
        """Pipe functions together: f1(f2(f3(...)))"""
        def piped_function(x):
            result = x
            for func in functions:
                result = func(result)
            return result
        return piped_function
    
    # Basic functions
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    # Compose functions
    add_then_multiply = compose(multiply_by_two, add_one)
    multiply_then_square = compose(square, multiply_by_two)
    
    print(f"add_then_multiply(5) = {add_then_multiply(5)}")  # (5 + 1) * 2 = 12
    print(f"multiply_then_square(3) = {multiply_then_square(3)}")  # (3 * 2) ** 2 = 36
    
    # Pipe multiple functions
    complex_operation = pipe(add_one, multiply_by_two, square)
    print(f"complex_operation(2) = {complex_operation(2)}")  # ((2 + 1) * 2) ** 2 = 36
    
    # String processing pipeline
    process_text = pipe(
        str.strip,
        str.lower,
        lambda s: s.replace(' ', '_'),
        lambda s: f"processed_{s}"
    )
    
    result = process_text("  Hello World  ")
    print(f"process_text('  Hello World  ') = {result}")


# Section 3: Function Methods and Advanced Usage

def demonstrate_function_introspection():
    """Demonstrate function introspection methods"""
    print("\n3.1 Function Introspection")
    
    def sample_function(a: int, b: str = "default", *args, **kwargs) -> str:
        """A sample function for introspection"""
        return f"{a}: {b}"
    
    # Basic function attributes
    print("Basic Attributes:")
    print(f"  Name: {sample_function.__name__}")
    print(f"  Doc: {sample_function.__doc__}")
    print(f"  Module: {sample_function.__module__}")
    print(f"  Defaults: {sample_function.__defaults__}")
    print(f"  Annotations: {sample_function.__annotations__}")
    
    # Using inspect module
    print("\nInspect Module:")
    signature = inspect.signature(sample_function)
    print(f"  Signature: {signature}")
    
    for param_name, param in signature.parameters.items():
        print(f"  Parameter: {param_name}")
        print(f"    Kind: {param.kind}")
        print(f"    Default: {param.default}")
        print(f"    Annotation: {param.annotation}")
    
    # Check if callable
    print(f"  Is callable: {callable(sample_function)}")
    print(f"  Is function: {inspect.isfunction(sample_function)}")


def demonstrate_decorators():
    """Demonstrate decorator methods and patterns"""
    print("\n3.2 Decorator Methods")
    
    # Basic decorator
    def timer(func):
        """Decorator to time function execution"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"    {func.__name__} took {end - start:.4f} seconds")
            return result
        return wrapper
    
    # Decorator with arguments
    def repeat(times):
        """Decorator to repeat function execution"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for _ in range(times):
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator
    
    # Class-based decorator
    class CountCalls:
        """Decorator to count function calls"""
        def __init__(self, func):
            self.func = func
            self.count = 0
            functools.update_wrapper(self, func)
        
        def __call__(self, *args, **kwargs):
            self.count += 1
            print(f"    Call #{self.count} to {self.func.__name__}")
            return self.func(*args, **kwargs)
    
    # Apply decorators
    @timer
    @CountCalls
    def slow_function(n):
        """A function that takes some time"""
        time.sleep(0.05)  # Reduced sleep time for demo
        return sum(range(n))
    
    @repeat(3)
    def random_number():
        """Generate a random number"""
        return random.randint(1, 100)
    
    # Test decorated functions
    print("Testing decorated functions:")
    result1 = slow_function(1000)
    result2 = slow_function(2000)
    
    random_results = random_number()
    print(f"  Random numbers: {random_results}")


def demonstrate_closures():
    """Demonstrate closure and scope methods"""
    print("\n3.3 Closure and Scope Methods")
    
    def create_counter(initial=0):
        """Create a counter function using closure"""
        count = initial
        
        def counter(increment=1):
            nonlocal count
            count += increment
            return count
        
        # Add methods to the function
        def reset():
            nonlocal count
            count = initial
        
        def get_count():
            return count
        
        # Attach methods as attributes
        counter.reset = reset
        counter.get_count = get_count
        counter.initial = initial
        
        return counter
    
    def create_bank_account(initial_balance=0):
        """Create a bank account using closure"""
        balance = initial_balance
        transaction_history = []
        
        def deposit(amount):
            nonlocal balance
            if amount > 0:
                balance += amount
                transaction_history.append(f"Deposit: +${amount}")
                return balance
            else:
                raise ValueError("Deposit amount must be positive")
        
        def withdraw(amount):
            nonlocal balance
            if amount > 0 and amount <= balance:
                balance -= amount
                transaction_history.append(f"Withdrawal: -${amount}")
                return balance
            else:
                raise ValueError("Invalid withdrawal amount")
        
        def get_balance():
            return balance
        
        def get_history():
            return transaction_history.copy()
        
        # Return a dictionary of functions
        return {
            'deposit': deposit,
            'withdraw': withdraw,
            'balance': get_balance,
            'history': get_history
        }
    
    # Test counter
    print("Testing counter:")
    counter1 = create_counter(10)
    counter2 = create_counter(0)
    
    print(f"  counter1() = {counter1()}")        # 11
    print(f"  counter1(5) = {counter1(5)}")       # 16
    print(f"  counter2() = {counter2()}")        # 1
    print(f"  counter1.get_count() = {counter1.get_count()}")  # 16
    
    counter1.reset()
    print(f"  After reset: counter1() = {counter1()}")        # 11
    
    # Test bank account
    print("\nTesting bank account:")
    account = create_bank_account(100)
    
    print(f"  Initial balance: ${account['balance']()}")
    print(f"  After deposit $50: ${account['deposit'](50)}")
    print(f"  After withdrawal $30: ${account['withdraw'](30)}")
    print(f"  Transaction history: {account['history']()}")


def demonstrate_caching():
    """Demonstrate function caching and memoization"""
    print("\n3.4 Function Caching and Memoization")
    
    # Manual memoization
    def memoize(func):
        """Manual memoization decorator"""
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            key = str(args) + str(sorted(kwargs.items()))
            
            if key not in cache:
                cache[key] = func(*args, **kwargs)
                print(f"    Computed {func.__name__}{args}")
            else:
                print(f"    Cache hit for {func.__name__}{args}")
            
            return cache[key]
        
        wrapper.cache = cache
        wrapper.cache_clear = lambda: cache.clear()
        return wrapper
    
    # Using functools.lru_cache
    @functools.lru_cache(maxsize=128)
    def fibonacci_cached(n):
        """Fibonacci with LRU cache"""
        if n <= 1:
            return n
        return fibonacci_cached(n-1) + fibonacci_cached(n-2)
    
    @memoize
    def expensive_calculation(x, y):
        """Simulate expensive calculation"""
        time.sleep(0.05)  # Reduced sleep time for demo
        return x ** 2 + y ** 2
    
    # Test memoization
    print("Manual Memoization:")
    result1 = expensive_calculation(3, 4)  # Computed
    result2 = expensive_calculation(3, 4)  # Cache hit
    result3 = expensive_calculation(5, 6)  # Computed
    
    print(f"  Cache contents: {expensive_calculation.cache}")
    
    # Test LRU cache
    print("\nLRU Cache:")
    start = time.time()
    result = fibonacci_cached(20)  # Reduced from 30 for demo speed
    end = time.time()
    print(f"  Fibonacci(20) = {result} (took {end-start:.4f}s)")
    print(f"  Cache info: {fibonacci_cached.cache_info()}")


# Section 4: Common Errors and Best Practices

def demonstrate_common_errors():
    """Demonstrate common function errors and solutions"""
    print("\n4.1 Common Function Errors")
    
    # Error 1: Incorrect Argument Count
    print("Error 1: Incorrect Argument Count")
    
    def add_three_numbers(a, b, c):
        return a + b + c
    
    try:
        result = add_three_numbers(1, 2)  # TypeError: missing required argument
    except TypeError as e:
        print(f"  Error: {e}")
    
    # Solutions
    def add_numbers(a, b, c=0):
        """Version with default parameter"""
        return a + b + c
    
    def add_any_numbers(*args):
        """Version with variable arguments"""
        return sum(args)
    
    print(f"  Fixed with default: add_numbers(1, 2) = {add_numbers(1, 2)}")
    print(f"  Fixed with *args: add_any_numbers(1, 2, 3, 4, 5) = {add_any_numbers(1, 2, 3, 4, 5)}")
    
    # Error 2: Mutable Default Arguments
    print("\nError 2: Mutable Default Arguments")
    
    def wrong_append_to_list(item, target_list=[]):
        target_list.append(item)
        return target_list
    
    # This creates unexpected behavior
    list1 = wrong_append_to_list("first")
    list2 = wrong_append_to_list("second")
    print(f"  Wrong - List1: {list1}")  # ['first', 'second'] - Unexpected!
    print(f"  Wrong - List2: {list2}")  # ['first', 'second'] - Same object!
    
    # Correct version
    def correct_append_to_list(item, target_list=None):
        if target_list is None:
            target_list = []
        target_list.append(item)
        return target_list
    
    list3 = correct_append_to_list("first")
    list4 = correct_append_to_list("second")
    print(f"  Correct - List3: {list3}")  # ['first'] - Correct!
    print(f"  Correct - List4: {list4}")  # ['second'] - Correct!
    
    # Error 3: UnboundLocalError
    print("\nError 3: UnboundLocalError")
    
    # Demonstrate the error with a local example
    def demonstrate_unboundlocal():
        x = 10
        
        def wrong_nested():
            x = x + 1  # UnboundLocalError
            return x
        
        try:
            wrong_nested()
        except UnboundLocalError as e:
            print(f"  Error: {e}")
        
        # Correct version using nonlocal
        def correct_nested():
            nonlocal x
            x = x + 1
            return x
        
        result = correct_nested()
        print(f"  Fixed: Nested function result = {result}")
    
    demonstrate_unboundlocal()
    
    # Error 4: Late Binding Closure Issues
    print("\nError 4: Late Binding Closure Issues")
    
    # Wrong: Late binding in loops
    functions = []
    for i in range(3):  # Reduced range for demo
        functions.append(lambda: i)  # All lambdas reference same 'i'
    
    print("  Wrong closure results:")
    for func in functions:
        print(f"    {func()}")  # All print 2 (last value of i)
    
    # Correct: Capture variable with default argument
    functions_correct = []
    for i in range(3):
        functions_correct.append(lambda x=i: x)  # Capture current value
    
    print("  Correct closure results:")
    for func in functions_correct:
        print(f"    {func()}")  # Prints 0, 1, 2


def demonstrate_error_handling():
    """Demonstrate best practices for error handling in functions"""
    print("\n4.2 Error Handling Best Practices")
    
    def safe_divide(a, b):
        """Safely divide two numbers with input validation"""
        # Type checking
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        
        # Value checking
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        
        return a / b
    
    def process_user_data(user_data):
        """Process user data with comprehensive error handling"""
        if not isinstance(user_data, dict):
            raise TypeError(f"Expected dict, got {type(user_data).__name__}")
        
        required_fields = ['name', 'email', 'age']
        missing_fields = [field for field in required_fields 
                         if field not in user_data]
        
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        
        # Validate field types
        if not isinstance(user_data['name'], str):
            raise TypeError("Name must be a string")
        
        if not isinstance(user_data['age'], int) or user_data['age'] < 0:
            raise ValueError("Age must be a non-negative integer")
        
        if '@' not in user_data['email']:
            raise ValueError("Invalid email format")
        
        return {
            'name': user_data['name'].strip().title(),
            'email': user_data['email'].lower().strip(),
            'age': user_data['age']
        }
    
    def robust_file_reader(filename):
        """Robustly read file with proper error handling"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"  Error: File '{filename}' not found")
            return None
        except PermissionError:
            print(f"  Error: Permission denied for '{filename}'")
            return None
        except UnicodeDecodeError:
            print(f"  Error: Cannot decode '{filename}' as UTF-8")
            return None
        except Exception as e:
            print(f"  Unexpected error reading '{filename}': {e}")
            return None
    
    # Test error handling
    print("Testing error handling:")
    
    try:
        result = safe_divide(10, 2)
        print(f"  Division result: {result}")
        
        user = process_user_data({
            'name': 'john doe',
            'email': 'JOHN@EXAMPLE.COM',
            'age': 30
        })
        print(f"  Processed user: {user}")
        
    except (TypeError, ValueError) as e:
        print(f"  Input error: {e}")
    
    # Test file reading (will fail gracefully)
    content = robust_file_reader("nonexistent_file.txt")
    
    # Print error prevention checklist
    print("\nError Prevention Checklist:")
    checklist_items = [
        "✓ Use descriptive parameter names",
        "✓ Provide default values where appropriate", 
        "✓ Avoid mutable default arguments",
        "✓ Use type hints for clarity",
        "✓ Validate inputs early",
        "✓ Use appropriate exception types",
        "✓ Provide meaningful error messages",
        "✓ Handle exceptions at appropriate levels"
    ]
    
    for item in checklist_items:
        print(f"  {item}")


if __name__ == "__main__":
    main()
