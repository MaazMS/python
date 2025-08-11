# Python Functions and Function Types Documentation

## 1. Function Definitions and Characteristics

### Definition

A function in Python is a reusable block of code that performs a specific task. Functions are first-class objects, meaning they can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures.

### Function Type Characteristics

#### 1.1 First-Class Objects

Functions in Python are first-class objects with the following properties:

```python
def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}!"

# Functions can be assigned to variables
my_function = greet
print(my_function("Alice"))  # Output: Hello, Alice!

# Functions have attributes
print(greet.__name__)        # Output: greet
print(greet.__doc__)         # Output: A simple greeting function

# Functions can be stored in data structures
function_list = [greet, print, len]
function_dict = {'greeting': greet, 'output': print}
```

#### 1.2 Function Object Properties

```python
def calculate_area(length, width=10):
    """Calculate area of rectangle"""
    return length * width

# Function attributes
print("Function name:", calculate_area.__name__)
print("Function doc:", calculate_area.__doc__)
print("Function defaults:", calculate_area.__defaults__)
print("Function code:", calculate_area.__code__.co_varnames)
print("Argument count:", calculate_area.__code__.co_argcount)
```

#### 1.3 Types of Functions

##### Built-in Functions

```python
# Built-in functions are always available
print(type(print))    # <class 'builtin_function_or_method'>
print(type(len))      # <class 'builtin_function_or_method'>
print(type(max))      # <class 'builtin_function_or_method'>

# Examples of built-in functions
numbers = [1, 5, 3, 9, 2]
print(f"Length: {len(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
```

##### User-defined Functions

```python
def user_function(x, y):
    """User-defined function"""
    return x + y

print(type(user_function))  # <class 'function'>
```

##### Lambda Functions (Anonymous Functions)

```python
# Lambda function
square = lambda x: x ** 2
print(type(square))  # <class 'function'>
print(square(5))     # Output: 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))     # Output: 7
```

##### Method Functions

```python
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
print(type(calc.add))                    # <class 'method'>
print(type(Calculator.multiply))         # <class 'function'>
print(type(Calculator.create_with_default)) # <class 'method'>
```

#### 1.4 Function Signature Characteristics

```python
def comprehensive_function(
    positional_arg,                    # Required positional argument
    default_arg=10,                   # Default argument
    *args,                           # Variable positional arguments
    keyword_only_arg,                # Keyword-only argument
    keyword_with_default=None,       # Keyword-only with default
    **kwargs                         # Variable keyword arguments
):
    """Demonstrates all types of function parameters"""
    print(f"Positional: {positional_arg}")
    print(f"Default: {default_arg}")
    print(f"Args: {args}")
    print(f"Keyword-only: {keyword_only_arg}")
    print(f"Keyword with default: {keyword_with_default}")
    print(f"Kwargs: {kwargs}")

# Example usage
comprehensive_function(
    "required",
    20,
    "extra1", "extra2",
    keyword_only_arg="must_be_keyword",
    keyword_with_default="custom",
    extra_key="extra_value"
)
```

---

## 2. Function Operations

### 2.1 Basic Function Operations

#### Function Definition and Calling

```python
def basic_operations():
    """Demonstrate basic function operations"""
    
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
    print(add(5, 3))                           # 8
    print(greet("Alice"))                      # Hello, Alice!
    print(greet("Bob", "Hi"))                  # Hi, Bob!
    print(sum_all(1, 2, 3, 4, 5))            # 15
    print(create_profile(name="John", age=30)) # {'name': 'John', 'age': 30}

basic_operations()
```

#### Function Assignment and References

```python
def function_references():
    """Demonstrate function assignment and references"""
    
    def original_function(x):
        return x * 2
    
    # Assign function to variable
    func_copy = original_function
    print(func_copy(5))  # 10
    
    # Functions are objects
    print(id(original_function) == id(func_copy))  # True
    
    # Function aliasing
    double = original_function
    print(double(7))     # 14
    
    # Storing functions in collections
    operations = {
        'double': lambda x: x * 2,
        'square': lambda x: x ** 2,
        'cube': lambda x: x ** 3
    }
    
    for name, func in operations.items():
        print(f"{name}(3) = {func(3)}")

function_references()
```

### 2.2 Higher-Order Function Operations

#### Functions as Arguments

```python
def higher_order_operations():
    """Demonstrate higher-order function operations"""
    
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

higher_order_operations()
```

#### Functions Returning Functions

```python
def function_factories():
    """Demonstrate functions that return functions"""
    
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
    
    def create_formatter(prefix, suffix):
        """Factory function that creates formatter functions"""
        def formatter(text):
            return f"{prefix}{text}{suffix}"
        return formatter
    
    # Create specific functions
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    age_validator = create_validator(0, 120)
    score_validator = create_validator(0, 100)
    
    html_formatter = create_formatter("<p>", "</p>")
    bracket_formatter = create_formatter("[", "]")
    
    # Use created functions
    print(double(5))                    # 10
    print(triple(4))                    # 12
    print(age_validator(25))            # True
    print(age_validator(150))           # False
    print(html_formatter("Hello"))      # <p>Hello</p>
    print(bracket_formatter("World"))   # [World]

function_factories()
```

### 2.3 Function Composition Operations

```python
def function_composition():
    """Demonstrate function composition operations"""
    
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
    
    print(add_then_multiply(5))      # (5 + 1) * 2 = 12
    print(multiply_then_square(3))   # (3 * 2) ** 2 = 36
    
    # Pipe multiple functions
    complex_operation = pipe(add_one, multiply_by_two, square)
    print(complex_operation(2))      # ((2 + 1) * 2) ** 2 = 36
    
    # String processing pipeline
    process_text = pipe(
        str.strip,
        str.lower,
        lambda s: s.replace(' ', '_'),
        lambda s: f"processed_{s}"
    )
    
    result = process_text("  Hello World  ")
    print(result)  # processed_hello_world

function_composition()
```

---

## 3. Function Methods and Advanced Usage

### 3.1 Function Introspection Methods

```python
import inspect
from typing import Callable, Any

def function_introspection():
    """Demonstrate function introspection methods"""
    
    def sample_function(a: int, b: str = "default", *args, **kwargs) -> str:
        """A sample function for introspection"""
        return f"{a}: {b}"
    
    # Basic function attributes
    print("=== Basic Attributes ===")
    print(f"Name: {sample_function.__name__}")
    print(f"Doc: {sample_function.__doc__}")
    print(f"Module: {sample_function.__module__}")
    print(f"Defaults: {sample_function.__defaults__}")
    print(f"Annotations: {sample_function.__annotations__}")
    
    # Using inspect module
    print("\n=== Inspect Module ===")
    signature = inspect.signature(sample_function)
    print(f"Signature: {signature}")
    
    for param_name, param in signature.parameters.items():
        print(f"Parameter: {param_name}")
        print(f"  Kind: {param.kind}")
        print(f"  Default: {param.default}")
        print(f"  Annotation: {param.annotation}")
    
    # Function source (if available)
    try:
        source = inspect.getsource(sample_function)
        print(f"\nSource:\n{source}")
    except OSError:
        print("Source not available")
    
    # Check if callable
    print(f"Is callable: {callable(sample_function)}")
    print(f"Is function: {inspect.isfunction(sample_function)}")

function_introspection()
```

### 3.2 Decorator Methods

```python
import functools
import time
from typing import Callable, Any

def decorator_methods():
    """Demonstrate decorator methods and patterns"""
    
    # Basic decorator
    def timer(func):
        """Decorator to time function execution"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.4f} seconds")
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
            print(f"Call #{self.count} to {self.func.__name__}")
            return self.func(*args, **kwargs)
    
    # Apply decorators
    @timer
    @CountCalls
    def slow_function(n):
        """A function that takes some time"""
        time.sleep(0.1)
        return sum(range(n))
    
    @repeat(3)
    def random_number():
        """Generate a random number"""
        import random
        return random.randint(1, 100)
    
    # Test decorated functions
    result1 = slow_function(1000)
    result2 = slow_function(2000)
    
    random_results = random_number()
    print(f"Random numbers: {random_results}")

decorator_methods()
```

### 3.3 Closure and Scope Methods

```python
def closure_methods():
    """Demonstrate closure and scope methods"""
    
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
    counter1 = create_counter(10)
    counter2 = create_counter(0)
    
    print(counter1())        # 11
    print(counter1(5))       # 16
    print(counter2())        # 1
    print(counter1.get_count())  # 16
    
    counter1.reset()
    print(counter1())        # 11
    
    # Test bank account
    account = create_bank_account(100)
    
    print(account['balance']())     # 100
    print(account['deposit'](50))   # 150
    print(account['withdraw'](30))  # 120
    print(account['history']())     # Transaction history

closure_methods()
```

### 3.4 Function Caching and Memoization

```python
import functools
import time

def caching_methods():
    """Demonstrate function caching and memoization"""
    
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
                print(f"Computed {func.__name__}{args}")
            else:
                print(f"Cache hit for {func.__name__}{args}")
            
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
        time.sleep(0.1)  # Simulate work
        return x ** 2 + y ** 2
    
    # Test memoization
    print("=== Manual Memoization ===")
    result1 = expensive_calculation(3, 4)  # Computed
    result2 = expensive_calculation(3, 4)  # Cache hit
    result3 = expensive_calculation(5, 6)  # Computed
    
    print(f"Cache contents: {expensive_calculation.cache}")
    
    # Test LRU cache
    print("\n=== LRU Cache ===")
    start = time.time()
    result = fibonacci_cached(30)
    end = time.time()
    print(f"Fibonacci(30) = {result} (took {end-start:.4f}s)")
    
    # Cache info
    print(f"Cache info: {fibonacci_cached.cache_info()}")
    
    # Clear cache
    fibonacci_cached.cache_clear()
    print(f"Cache after clear: {fibonacci_cached.cache_info()}")

caching_methods()
```

---

## 4. Common Errors in Functions and Function Types

### 4.1 Parameter and Argument Errors

#### Error 1: Incorrect Argument Count

```python
def argument_errors():
    """Demonstrate common argument errors and solutions"""
    
    # ❌ WRONG: Function expects specific number of arguments
    def add_three_numbers(a, b, c):
        return a + b + c
    
    try:
        result = add_three_numbers(1, 2)  # TypeError: missing required argument
    except TypeError as e:
        print(f"Error: {e}")
    
    # ✅ CORRECT: Use default parameters or *args
    def add_numbers(a, b, c=0):
        """Version with default parameter"""
        return a + b + c
    
    def add_any_numbers(*args):
        """Version with variable arguments"""
        return sum(args)
    
    print(add_numbers(1, 2))        # Works: 3
    print(add_numbers(1, 2, 3))     # Works: 6
    print(add_any_numbers(1, 2))    # Works: 3
    print(add_any_numbers(1, 2, 3, 4, 5))  # Works: 15

argument_errors()
```

#### Error 2: Mutable Default Arguments

```python
def mutable_default_errors():
    """Demonstrate mutable default argument errors"""
    
    # ❌ WRONG: Mutable default argument
    def wrong_append_to_list(item, target_list=[]):
        target_list.append(item)
        return target_list
    
    # This creates unexpected behavior
    list1 = wrong_append_to_list("first")
    list2 = wrong_append_to_list("second")
    print(f"List1: {list1}")  # ['first', 'second'] - Unexpected!
    print(f"List2: {list2}")  # ['first', 'second'] - Same object!
    
    # ✅ CORRECT: Use None as default and create new object
    def correct_append_to_list(item, target_list=None):
        if target_list is None:
            target_list = []
        target_list.append(item)
        return target_list
    
    list3 = correct_append_to_list("first")
    list4 = correct_append_to_list("second")
    print(f"List3: {list3}")  # ['first'] - Correct!
    print(f"List4: {list4}")  # ['second'] - Correct!
    
    # ✅ ALTERNATIVE: Use copy for shared mutable defaults
    def append_with_default(item, target_list=None, default_list=None):
        if target_list is None:
            target_list = (default_list or []).copy()
        target_list.append(item)
        return target_list

mutable_default_errors()
```

### 4.2 Scope and Variable Errors

#### Error 3: UnboundLocalError

```python
def scope_errors():
    """Demonstrate scope-related errors"""
    
    counter = 0
    
    # ❌ WRONG: Trying to modify global variable without declaration
    def wrong_increment():
        counter = counter + 1  # UnboundLocalError
        return counter
    
    try:
        wrong_increment()
    except UnboundLocalError as e:
        print(f"Error: {e}")
    
    # ✅ CORRECT: Use global keyword
    def correct_increment():
        global counter
        counter = counter + 1
        return counter
    
    print(f"Counter after increment: {correct_increment()}")
    
    # ❌ WRONG: Nested function scope issue
    def outer_function():
        x = 10
        
        def wrong_nested():
            x = x + 1  # UnboundLocalError
            return x
        
        return wrong_nested
    
    try:
        func = outer_function()
        func()
    except UnboundLocalError as e:
        print(f"Nested function error: {e}")
    
    # ✅ CORRECT: Use nonlocal keyword
    def correct_outer_function():
        x = 10
        
        def correct_nested():
            nonlocal x
            x = x + 1
            return x
        
        return correct_nested
    
    func = correct_outer_function()
    print(f"Nested function result: {func()}")

scope_errors()
```

#### Error 4: Late Binding Closure Issues

```python
def closure_errors():
    """Demonstrate closure late binding errors"""
    
    # ❌ WRONG: Late binding in loops
    functions = []
    for i in range(5):
        functions.append(lambda: i)  # All lambdas reference same 'i'
    
    print("Wrong closure results:")
    for func in functions:
        print(func())  # All print 4 (last value of i)
    
    # ✅ CORRECT: Capture variable with default argument
    functions_correct = []
    for i in range(5):
        functions_correct.append(lambda x=i: x)  # Capture current value
    
    print("Correct closure results:")
    for func in functions_correct:
        print(func())  # Prints 0, 1, 2, 3, 4
    
    # ✅ ALTERNATIVE: Use function factory
    def create_function(value):
        return lambda: value
    
    functions_factory = []
    for i in range(5):
        functions_factory.append(create_function(i))
    
    print("Function factory results:")
    for func in functions_factory:
        print(func())  # Prints 0, 1, 2, 3, 4

closure_errors()
```

### 4.3 Return Value and Type Errors

#### Error 5: Missing Return Statement

```python
def return_errors():
    """Demonstrate return statement errors"""
    
    # ❌ WRONG: Missing return statement
    def wrong_calculate(x, y):
        result = x + y
        # Missing return statement - function returns None
    
    result = wrong_calculate(5, 3)
    print(f"Wrong result: {result}")  # None
    
    # ✅ CORRECT: Explicit return statement
    def correct_calculate(x, y):
        result = x + y
        return result
    
    result = correct_calculate(5, 3)
    print(f"Correct result: {result}")  # 8
    
    # ❌ WRONG: Inconsistent return types
    def wrong_process_data(data):
        if not data:
            return None
        if len(data) == 1:
            return data[0]  # Returns single item
        else:
            return data     # Returns list
        # Inconsistent return types can cause issues
    
    # ✅ CORRECT: Consistent return types
    def correct_process_data(data):
        if not data:
            return []       # Always return list
        if len(data) == 1:
            return [data[0]]  # Return single item as list
        else:
            return data     # Return list
    
    print(f"Consistent returns: {correct_process_data(['single'])}")

return_errors()
```

#### Error 6: Function Modification Errors

```python
def modification_errors():
    """Demonstrate function modification errors"""
    
    # ❌ WRONG: Modifying function arguments (mutable objects)
    def wrong_process_list(items):
        items.append("processed")  # Modifies original list
        return items
    
    original_list = [1, 2, 3]
    processed = wrong_process_list(original_list)
    print(f"Original after processing: {original_list}")  # Modified!
    
    # ✅ CORRECT: Don't modify input, create new object
    def correct_process_list(items):
        result = items.copy()  # Create copy
        result.append("processed")
        return result
    
    original_list2 = [1, 2, 3]
    processed2 = correct_process_list(original_list2)
    print(f"Original unchanged: {original_list2}")      # Unchanged
    print(f"Processed result: {processed2}")            # Has changes
    
    # ✅ ALTERNATIVE: Make intention clear with naming
    def process_list_inplace(items):
        """Clearly indicates in-place modification"""
        items.append("processed")
        return items
    
    def process_list_copy(items):
        """Clearly indicates returns new copy"""
        return items + ["processed"]

modification_errors()
```

### 4.4 Performance and Memory Errors

#### Error 7: Inefficient Recursive Functions

```python
def performance_errors():
    """Demonstrate performance-related errors"""
    
    # ❌ WRONG: Inefficient recursion without memoization
    def wrong_fibonacci(n):
        if n <= 1:
            return n
        return wrong_fibonacci(n-1) + wrong_fibonacci(n-2)
    
    # This is extremely slow for large n
    # print(wrong_fibonacci(35))  # Takes several seconds
    
    # ✅ CORRECT: Memoized recursion
    @functools.lru_cache(maxsize=None)
    def correct_fibonacci(n):
        if n <= 1:
            return n
        return correct_fibonacci(n-1) + correct_fibonacci(n-2)
    
    # Much faster
    result = correct_fibonacci(35)
    print(f"Fibonacci(35) = {result}")
    
    # ✅ ALTERNATIVE: Iterative approach
    def iterative_fibonacci(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    result2 = iterative_fibonacci(35)
    print(f"Iterative Fibonacci(35) = {result2}")

performance_errors()
```

### 4.5 Error Handling Best Practices

```python
def error_handling_best_practices():
    """Demonstrate best practices for error handling in functions"""
    
    # ✅ GOOD: Validate inputs
    def safe_divide(a, b):
        """Safely divide two numbers with input validation"""
        # Type checking
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        
        # Value checking
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        
        return a / b
    
    # ✅ GOOD: Provide meaningful error messages
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
    
    # ✅ GOOD: Use try-except appropriately
    def robust_file_reader(filename):
        """Robustly read file with proper error handling"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            return None
        except PermissionError:
            print(f"Error: Permission denied for '{filename}'")
            return None
        except UnicodeDecodeError:
            print(f"Error: Cannot decode '{filename}' as UTF-8")
            return None
        except Exception as e:
            print(f"Unexpected error reading '{filename}': {e}")
            return None
    
    # Test error handling
    try:
        result = safe_divide(10, 2)
        print(f"Division result: {result}")
        
        user = process_user_data({
            'name': 'john doe',
            'email': 'JOHN@EXAMPLE.COM',
            'age': 30
        })
        print(f"Processed user: {user}")
        
    except (TypeError, ValueError) as e:
        print(f"Input error: {e}")

error_handling_best_practices()
```

### Common Error Prevention Checklist

```python
def error_prevention_checklist():
    """Comprehensive checklist for preventing function errors"""
    
    print("""
=== Function Error Prevention Checklist ===

1. PARAMETER DESIGN:
   ✓ Use descriptive parameter names
   ✓ Provide default values where appropriate
   ✓ Avoid mutable default arguments
   ✓ Use type hints for clarity
   ✓ Document parameter requirements

2. INPUT VALIDATION:
   ✓ Check parameter types
   ✓ Validate parameter values and ranges
   ✓ Handle edge cases (empty inputs, None values)
   ✓ Provide clear error messages

3. SCOPE MANAGEMENT:
   ✓ Use global/nonlocal keywords appropriately
   ✓ Avoid variable name conflicts
   ✓ Be careful with closure variable capture
   ✓ Understand variable lifetime

4. RETURN VALUES:
   ✓ Always return consistent types
   ✓ Document return value types and meanings
   ✓ Consider returning None vs empty collections
   ✓ Use explicit return statements

5. SIDE EFFECTS:
   ✓ Minimize function side effects
   ✓ Document any side effects clearly
   ✓ Don't modify input parameters unexpectedly
   ✓ Use pure functions where possible

6. PERFORMANCE:
   ✓ Use memoization for expensive recursive functions
   ✓ Consider iterative alternatives to recursion
   ✓ Profile functions for performance bottlenecks
   ✓ Use appropriate data structures

7. ERROR HANDLING:
   ✓ Validate inputs early
   ✓ Use appropriate exception types
   ✓ Provide meaningful error messages
   ✓ Handle exceptions at appropriate levels

8. TESTING:
   ✓ Test with valid inputs
   ✓ Test edge cases and boundary conditions
   ✓ Test error conditions
   ✓ Use unit tests for complex functions
    """)

error_prevention_checklist()
```

---

## Summary

This documentation covers:

1. **Function Definitions and Characteristics**: Types of functions, function properties, and signature characteristics
2. **Function Operations**: Basic operations, higher-order functions, and function composition
3. **Function Methods**: Introspection, decorators, closures, and caching techniques
4. **Common Errors**: Parameter errors, scope issues, return problems, and performance pitfalls

Functions are powerful tools in Python, but proper understanding of their behavior and common pitfalls is essential for writing robust, maintainable code.
