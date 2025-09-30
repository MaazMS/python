# Python Exception Handling

## 1. Exception Definition and Characteristics

Exceptions are runtime errors that occur when something goes wrong during program execution. If not handled properly, exceptions can cause significant issues in your application.

### Characteristics of Exceptions

1. **Abrupt Program Termination**: When an exception occurs, the program stops executing at that point, and subsequent code is not executed.
2. **Unfriendly Error Messages**: Python displays technical error information that may not be user-friendly.
3. **Resource Management Issues**: Improper shutdown of resources like database connections, file streams, or network connections.

### Examples

```python
# Example 1: Division by zero exception
def divide_numbers(a, b):
    return a / b

# This will raise ZeroDivisionError
result = divide_numbers(10, 0)  # Program crashes here
print("This line won't execute")  # Never reached
```

```python
# Example 2: File not found exception
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# This will raise FileNotFoundError
content = read_file("nonexistent.txt")  # Program crashes here
print("File content:", content)  # Never reached
```

```python
# Example 3: Type error exception
def calculate_square(number):
    return number * number

# This will raise TypeError
result = calculate_square("hello")  # Program crashes here
print("Square:", result)  # Never reached
```

### Basic Exception Handling Structure

```python
try:
    # Code that might raise an exception
    risky_operation()
except ExceptionType:
    # Handle specific exception
    handle_error()
else:
    # Execute if no exception occurs
    success_operation()
finally:
    # Always execute (cleanup code)
    cleanup_resources()
```

### Complete Example

```python
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Division successful: {a} / {b} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        result = None
    except TypeError:
        print("Error: Both arguments must be numbers!")
        result = None
    else:
        print("Division completed without errors")
    finally:
        print("Division operation finished")
    
    return result

# Test the function
safe_divide(10, 2)   # Normal case
safe_divide(10, 0)   # Zero division
safe_divide(10, "a") # Type error
```

## 2. Exception Operations

Exception operations involve various ways to handle, raise, and work with exceptions in Python.

### 2.1 Catching Multiple Exceptions

```python
def process_user_input():
    try:
        age = int(input("Enter your age: "))
        income = float(input("Enter your income: "))
        tax_rate = income / age
        print(f"Tax rate: {tax_rate}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Age cannot be zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

### 2.2 Catching Multiple Exceptions in One Block

```python
def file_operations():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as file:
            data = file.read()
            number = int(data)
            result = 100 / number
    except (FileNotFoundError, PermissionError) as file_error:
        print(f"File error: {file_error}")
    except (ValueError, ZeroDivisionError) as math_error:
        print(f"Math error: {math_error}")
```

### 2.3 Raising Custom Exceptions

```python
class CustomError(Exception):
    """Custom exception class"""
    pass

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative!")
    if age > 150:
        raise CustomError("Age seems unrealistic!")
    return True

try:
    user_age = -5
    validate_age(user_age)
except CustomError as e:
    print(f"Validation error: {e}")
```

### 2.4 Re-raising Exceptions

```python
def process_data(data):
    try:
        # Process the data
        result = complex_calculation(data)
        return result
    except ValueError as e:
        print(f"Logging error: {e}")
        # Re-raise the exception for caller to handle
        raise
    except Exception as e:
        # Convert to a more specific exception
        raise ValueError(f"Data processing failed: {e}")

def complex_calculation(data):
    if not isinstance(data, (int, float)):
        raise ValueError("Data must be a number")
    return data ** 2
```

### 2.5 Exception Chaining

```python
def outer_function():
    try:
        inner_function()
    except ValueError as e:
        # Chain exceptions to preserve original error context
        raise RuntimeError("Outer function failed") from e

def inner_function():
    raise ValueError("Inner function error")

try:
    outer_function()
except RuntimeError as e:
    print(f"Main error: {e}")
    print(f"Original cause: {e.__cause__}")
```

## 3. Exception Methods

Python exception objects have several built-in methods and attributes that provide useful information about the error.

### 3.1 Common Exception Attributes

```python
def demonstrate_exception_attributes():
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"Exception type: {type(e)}")
        print(f"Exception message: {str(e)}")
        print(f"Exception args: {e.args}")
        print(f"Exception repr: {repr(e)}")

demonstrate_exception_attributes()
```

### 3.2 Traceback Information

```python
import traceback
import sys

def get_exception_details():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        # Get exception information
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        print("Exception Type:", exc_type.__name__)
        print("Exception Value:", exc_value)
        print("Traceback:")
        traceback.print_tb(exc_traceback)
        
        # Get formatted traceback as string
        tb_str = ''.join(traceback.format_tb(exc_traceback))
        print("Formatted traceback:")
        print(tb_str)

get_exception_details()
```

### 3.3 Custom Exception with Methods

```python
class DetailedException(Exception):
    def __init__(self, message, error_code=None, details=None):
        super().__init__(message)
        self.error_code = error_code
        self.details = details or {}
    
    def get_error_code(self):
        return self.error_code
    
    def get_details(self):
        return self.details
    
    def add_detail(self, key, value):
        self.details[key] = value
    
    def __str__(self):
        base_message = super().__str__()
        if self.error_code:
            base_message += f" (Code: {self.error_code})"
        if self.details:
            base_message += f" Details: {self.details}"
        return base_message

# Usage example
def risky_operation():
    error = DetailedException("Operation failed", "ERR001")
    error.add_detail("timestamp", "2024-01-01 12:00:00")
    error.add_detail("user_id", "12345")
    raise error

try:
    risky_operation()
except DetailedException as e:
    print(f"Error: {e}")
    print(f"Error Code: {e.get_error_code()}")
    print(f"Details: {e.get_details()}")
```

### 3.4 Exception Context Managers

```python
from contextlib import contextmanager

@contextmanager
def exception_handler(exception_type, message="An error occurred"):
    try:
        yield
    except exception_type as e:
        print(f"{message}: {e}")
        # Could log to file, send notification, etc.

# Usage
with exception_handler(ValueError, "Invalid input detected"):
    number = int("not_a_number")

with exception_handler(FileNotFoundError, "File operation failed"):
    with open("missing_file.txt", 'r') as f:
        content = f.read()
```

## 4. Common Errors in Exception Handling

Understanding common mistakes helps write better exception handling code.

### 4.1 Catching Too Broad Exceptions

**❌ Bad Practice:**

```python
def bad_exception_handling():
    try:
        # Complex operation
        result = complex_operation()
        return result
    except Exception:
        print("Something went wrong")
        return None  # Hides all errors, making debugging difficult

def complex_operation():
    # This could raise various specific exceptions
    data = fetch_data()
    processed = process_data(data)
    return save_result(processed)
```

**✅ Good Practice:**

```python
def good_exception_handling():
    try:
        result = complex_operation()
        return result
    except ConnectionError:
        print("Network connection failed")
        return None
    except ValueError:
        print("Invalid data format")
        return None
    except FileNotFoundError:
        print("Required file not found")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        # Log the full traceback for debugging
        import logging
        logging.exception("Unexpected error in complex_operation")
        return None
```

### 4.2 Ignoring Exceptions Silently

**❌ Bad Practice:**

```python
def silent_failure():
    try:
        important_operation()
    except:
        pass  # Silently ignoring all exceptions - very dangerous!

def risky_silent_handling():
    try:
        critical_database_operation()
    except Exception:
        return  # Hiding errors without any notification
```

**✅ Good Practice:**

```python
import logging

def proper_error_handling():
    try:
        important_operation()
    except SpecificException as e:
        logging.warning(f"Expected issue occurred: {e}")
        # Handle gracefully with fallback
        fallback_operation()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        # Notify administrators, log for debugging
        notify_admins(str(e))
        raise  # Re-raise if can't handle properly
```

### 4.3 Not Using Specific Exception Types

**❌ Bad Practice:**

```python
def generic_exception_raising():
    if invalid_condition:
        raise Exception("Something is wrong")  # Too generic
    
    if another_condition:
        raise Exception("Another problem")  # Can't distinguish between errors
```

**✅ Good Practice:**

```python
class InvalidConfigurationError(Exception):
    pass

class DataValidationError(Exception):
    pass

def specific_exception_raising():
    if invalid_configuration:
        raise InvalidConfigurationError("Configuration file is malformed")
    
    if invalid_data:
        raise DataValidationError("Input data failed validation checks")

# Usage allows specific handling
try:
    specific_exception_raising()
except InvalidConfigurationError:
    load_default_configuration()
except DataValidationError:
    request_user_input()
```

### 4.4 Improper Finally Block Usage

**❌ Bad Practice:**

```python
def improper_finally():
    file = None
    try:
        file = open("data.txt", "r")
        data = file.read()
        return data  # File might not be closed if exception occurs
    except FileNotFoundError:
        return None
    finally:
        file.close()  # This will fail if file is None
```

**✅ Good Practice:**

```python
def proper_finally():
    file = None
    try:
        file = open("data.txt", "r")
        data = file.read()
        return data
    except FileNotFoundError:
        return None
    finally:
        if file is not None:
            file.close()

# Even better - use context managers
def best_practice():
    try:
        with open("data.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return None
```

### 4.5 Modifying Exception Arguments

**❌ Bad Practice:**

```python
def modifying_exception():
    try:
        risky_operation()
    except ValueError as e:
        e.args = ("Modified error message",)  # Don't modify exception
        raise e
```

**✅ Good Practice:**

```python
def proper_exception_modification():
    try:
        risky_operation()
    except ValueError as e:
        # Create new exception with additional context
        raise ValueError(f"Operation failed in module X: {e}") from e
```

### 4.6 Exception Handling Anti-patterns

**❌ Bad Practice:**

```python
# Anti-pattern 1: Exception for flow control
def bad_flow_control():
    try:
        return expensive_operation()
    except:
        return default_value()  # Using exceptions for normal flow

# Anti-pattern 2: Nested try-except blocks
def nested_mess():
    try:
        try:
            operation1()
        except Error1:
            try:
                operation2()
            except Error2:
                operation3()
    except Error3:
        pass
```

**✅ Good Practice:**

```python
# Better flow control
def good_flow_control():
    if can_perform_expensive_operation():
        return expensive_operation()
    else:
        return default_value()

# Better structure
def clean_structure():
    try:
        result = attempt_operation()
        return result
    except (Error1, Error2) as e:
        return handle_expected_errors(e)
    except Error3:
        return handle_critical_error()
```

## 5. Python Exception Hierarchy

### The Exception Hierarchy Diagram

All Python exceptions inherit from the `BaseException` class. Understanding this hierarchy helps in writing more effective exception handling code.

### Key Exception Classes

```python
# Common built-in exceptions and their usage
def demonstrate_exception_hierarchy():
    exceptions_demo = {
        'ValueError': lambda: int('not_a_number'),
        'TypeError': lambda: 'string' + 5,
        'IndexError': lambda: [1, 2, 3][10],
        'KeyError': lambda: {'a': 1}['b'],
        'FileNotFoundError': lambda: open('missing.txt'),
        'ZeroDivisionError': lambda: 1 / 0,
        'AttributeError': lambda: 'string'.missing_method(),
        'ImportError': lambda: __import__('nonexistent_module')
    }
    
    for exc_name, func in exceptions_demo.items():
        try:
            func()
        except Exception as e:
            print(f"{exc_name}: {type(e).__name__} - {e}")

demonstrate_exception_hierarchy()
```

## 6. Logging in Python

Python has a built-in `logging` module that allows writing status messages to files or other output streams. This is essential for debugging and monitoring applications.

### 6.1 Basic Logging Configuration

```python
import logging

# Basic configuration
logging.basicConfig(
    filename="application.log", 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Different logging levels
logging.critical("This is a critical message")
logging.error("This is an error message")
logging.warning("This is a warning message")
logging.info("This is an info message")
logging.debug("This is a debug message")
```

**Output in `application.log`:**

```bash
2024-01-01 12:00:00,000 - CRITICAL - This is a critical message
2024-01-01 12:00:00,001 - ERROR - This is an error message
2024-01-01 12:00:00,002 - WARNING - This is a warning message
2024-01-01 12:00:00,003 - INFO - This is an info message
2024-01-01 12:00:00,004 - DEBUG - This is a debug message
```

### 6.2 Advanced Logging with Exception Handling

```python
import logging
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # Also print to console
    ]
)

logger = logging.getLogger(__name__)

def divide_with_logging(a, b):
    try:
        logger.info(f"Attempting to divide {a} by {b}")
        result = a / b
        logger.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"Division by zero error: {e}")
        logger.exception("Full traceback:")  # Logs the full traceback
        return None
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        logger.exception("Critical error occurred:")
        raise

# Usage
divide_with_logging(10, 2)
divide_with_logging(10, 0)
```

### 6.3 Custom Logger for Exception Handling

```python
import logging
from functools import wraps

class ExceptionLogger:
    def __init__(self, logger_name="exception_logger"):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        
        # Create file handler
        fh = logging.FileHandler('exceptions.log')
        fh.setLevel(logging.DEBUG)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
    
    def log_exception(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.exception(f"Exception in {func.__name__}: {e}")
                raise
        return wrapper

# Usage
exception_logger = ExceptionLogger()

@exception_logger.log_exception
def risky_function(x, y):
    return x / y

risky_function(10, 0)  # This will log the exception and re-raise it
```

## 7. Assert Statement

The `assert` statement is used for debugging purposes. It tests a condition and raises an `AssertionError` if the condition is false.

### 7.1 Basic Assert Usage

```python
def validate_positive_number(num):
    assert num > 0, "Number must be positive"
    return num * 2

# Examples
try:
    result = validate_positive_number(5)  # Works fine
    print(f"Result: {result}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    result = validate_positive_number(-3)  # Raises AssertionError
except AssertionError as e:
    print(f"Assertion failed: {e}")
```

### 7.2 Assert in Exception Handling

```python
def process_user_data(data):
    try:
        # Assert for debugging - helps catch programming errors early
        assert isinstance(data, dict), "Data must be a dictionary"
        assert 'name' in data, "Data must contain 'name' field"
        assert 'age' in data, "Data must contain 'age' field"
        assert data['age'] >= 0, "Age must be non-negative"
        
        # Process the data
        name = data['name'].strip()
        age = int(data['age'])
        
        return f"User: {name}, Age: {age}"
        
    except AssertionError as e:
        print(f"Data validation failed: {e}")
        return None
    except (ValueError, TypeError) as e:
        print(f"Data processing error: {e}")
        return None

# Test cases
valid_data = {'name': 'John', 'age': 25}
invalid_data1 = {'name': 'Jane'}  # Missing age
invalid_data2 = {'name': 'Bob', 'age': -5}  # Negative age
invalid_data3 = "not a dict"  # Wrong type

print(process_user_data(valid_data))
print(process_user_data(invalid_data1))
print(process_user_data(invalid_data2))
print(process_user_data(invalid_data3))
```

### 7.3 Assert Best Practices

```python
# ✅ Good: Use assert for debugging and development
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All elements must be numbers"
    return sum(numbers) / len(numbers)

# ❌ Bad: Don't use assert for user input validation in production
def bad_user_input_validation(user_age):
    assert user_age >= 0, "Age cannot be negative"  # Don't do this!
    return user_age

# ✅ Good: Use proper exception handling for user input
def good_user_input_validation(user_age):
    if not isinstance(user_age, (int, float)):
        raise TypeError("Age must be a number")
    if user_age < 0:
        raise ValueError("Age cannot be negative")
    return user_age

# Example with proper error handling
def safe_calculate_average(numbers):
    try:
        # Use assert for internal consistency checks
        assert isinstance(numbers, list), "Expected list input"
        
        # Use proper validation for user data
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        
        for i, num in enumerate(numbers):
            if not isinstance(num, (int, float)):
                raise TypeError(f"Element at index {i} is not a number: {num}")
        
        return sum(numbers) / len(numbers)
        
    except AssertionError as e:
        print(f"Internal error: {e}")
        raise
    except (ValueError, TypeError) as e:
        print(f"Input validation error: {e}")
        return None

# Usage
print(safe_calculate_average([1, 2, 3, 4, 5]))  # Works
print(safe_calculate_average([]))  # Handles empty list
print(safe_calculate_average([1, 'two', 3]))  # Handles invalid data
```

### Important Notes

1. **Log Files**: Can have any name but typically use `.log` extension (e.g., `application.log`)
2. **Logging Levels**: DEBUG < INFO < WARNING < ERROR < CRITICAL
3. **Assert Statement**: Should be used for debugging, not for handling user input errors
4. **Production Code**: Assertions can be disabled with `python -O`, so don't rely on them for critical validations
