# Python Variables

## What are Variables?

1. Variables are containers for storing data values.
2. Variables are created when you first assign a value to them.
3. No need to declare variables with specific data types
4. Variable type is determined automatically based on the assigned value
5. Variables can change type after they have been set

## Variable Naming Rules

1. Must start with a letter (a-z, A-Z) or underscore (_)
2. Can contain letters, numbers, and underscores
3. Case-sensitive (age, Age, AGE are different variables)
4. Cannot start with a number
5. Cannot use Python keywords (if, for, while, etc.)

## Variable Types

1. Basic Types :  int, float, str, bool
2. Collections : list, tuple, dict, set
3. Special : None, complex

## Best Practices

1. Use descriptive names (`user_name` not `n`)
2. Follow snake_case convention
3. Initialize variables before use
4. Use type hints for functions
5. Handle type conversions safely

## Basic Data Types (Variable Creation)

* Variables are created when assigned

### Integer Variables

```python
# Integer variables
age = 25
year = 2024
negative_number = -10

print(f"Age: {age}, Type: {type(age)}")
# Output: Age: 25, Type: <class 'int'>
```

### Float Variables

```python
# Float variables
height = 5.9
temperature = -2.5
pi = 3.14159

print(f"Height: {height}, Type: {type(height)}")
# Output: Height: 5.9, Type: <class 'float'>
```

### String Variables

```python
# String variables (single or double quotes)
name = "Maaz"
city = 'Mumbai'
message = """This is a
multi-line string"""

print(f"Name: {name}, Type: {type(name)}")
# Output: Name: Maaz, Type: <class 'str'>
```

### Boolean Variables

```python
# Boolean variables
is_student = True
is_married = False
has_job = True

print(f"Student: {is_student}, Type: {type(is_student)}")
# Output: Student: True, Type: <class 'bool'>
```

### List Variables

```python
# List variables
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed_list = [1, "Hello", 3.14, True]

print(f"Numbers: {numbers}, Type: {type(numbers)}")
# Output: Numbers: [1, 2, 3, 4, 5], Type: <class 'list'>
```

### Dictionary Variables

```python
# Dictionary variables
person = {"name": "Maaz", "age": 25, "city": "Mumbai"}
scores = {"math": 95, "english": 87, "science": 92}

print(f"Person: {person}, Type: {type(person)}")
# Output: Person: {'name': 'Maaz', 'age': 25, 'city': 'Mumbai'}, Type: <class 'dict'>
```

## Global and Local Variables

### Global Variables

Variables created outside functions are global variables:

```python
# Global variable
global_variable = "I am global"

def test_global():
    print(global_variable)  # Can access global variable
    
test_global()
# Output: I am global
```

### Local Variables

Variables created inside functions are local variables:

```python
def test_local():
    local_variable = "I am local"
    print(local_variable)
    
test_local()
# print(local_variable)  # This would cause NameError
```

### Global Keyword

Use `global` keyword to modify global variables inside functions:

```python
counter = 0  # Global variable

def increment():
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment()  # Output: Counter: 1
increment()  # Output: Counter: 2
```

---

## Variable Operations

### Basic Assignment

```python
# Simple assignment
name = "Maaz"
age = 25
height = 5.9
```

### Multiple Assignment

```python
# Assign values to multiple variables in one line
first_name, last_name, age = "Maaz", "Shaikh", 25
print(f"Name: {first_name} {last_name}, Age: {age}")
# Output: Name: Maaz Shaikh, Age: 25

# Assign same value to multiple variables
x = y = z = 10
print(f"x: {x}, y: {y}, z: {z}")
# Output: x: 10, y: 10, z: 10
```

### Variable Swapping

```python
# Swapping variables
a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")

# Python way of swapping
a, b = b, a
print(f"After swap: a = {a}, b = {b}")
# Output: Before swap: a = 5, b = 10
# Output: After swap: a = 10, b = 5
```

### Arithmetic Operations

```python
# Numeric operations
x = 10
y = 3

addition = x + y      # 13
subtraction = x - y   # 7
multiplication = x * y # 30
division = x / y      # 3.333...
floor_division = x // y # 3
modulus = x % y       # 1
power = x ** y        # 1000

print(f"Addition: {addition}")
print(f"Power: {power}")
```

### String Operations

```python
# String concatenation
first_name = "Maaz"
last_name = "Shaikh"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
# Output: Full name: Maaz Shaikh

# String repetition
greeting = "Hello! "
repeated = greeting * 3
print(repeated)
# Output: Hello! Hello! Hello! 
```

### Augmented Assignment

```python
# Augmented assignment operators
number = 10
number += 5   # Same as: number = number + 5
print(number) # Output: 15

text = "Hello"
text += " World"  # Same as: text = text + " World"
print(text)       # Output: Hello World
```

---

## Variable Methods

## Built-in Functions for Variables

### type() - Get Variable Type

```python
name = "Maaz"
age = 25
height = 5.9

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
```

### isinstance() - Check Variable Type

```python
name = "Maaz"
age = 25

print(isinstance(name, str))   # True
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```

### id() - Get Variable Identity

```python
x = 10
y = 10
z = x

print(id(x))  # Memory address
print(id(y))  # Same address (Python optimizes small integers)
print(id(z))  # Same address as x
```

### len() - Get Length

```python
name = "Maaz"
numbers = [1, 2, 3, 4, 5]

print(len(name))     # 4
print(len(numbers))  # 5
```

### str(), int(), float() - Type Conversion

```python
# Converting between types
age = 25
age_str = str(age)
print(f"Age as string: '{age_str}'")

height_str = "5.9"
height_float = float(height_str)
print(f"Height as float: {height_float}")

number_str = "42"
number_int = int(number_str)
print(f"Number as int: {number_int}")
```

## Variable Information Methods

### vars() - Get Variables in Current Scope

```python
def show_variables():
    name = "Maaz"
    age = 25
    city = "Mumbai"
    print(vars())  # Shows local variables

show_variables()
# Output: {'name': 'Maaz', 'age': 25, 'city': 'Mumbai'}
```

### globals() - Get Global Variables

```python
global_var = "I am global"

def access_global():
    local_var = "I am local"
    print(globals()['global_var'])  # Access global variable
    
access_global()
# Output: I am global
```

### locals() - Get Local Variables

```python
def show_locals():
    name = "Maaz"
    age = 25
    print(locals())

show_locals()
# Output: {'name': 'Maaz', 'age': 25}
```

---

## Common Errors in Variables

### NameError - Using Undefined Variables

```python
# ERROR: Using undefined variable
# print(undefined_variable)  # NameError: name 'undefined_variable' is not defined

# CORRECT: Define variable before using
defined_variable = "Hello"
print(defined_variable)  # Output: Hello
```

### TypeError - Wrong Data Type Operations

```python
# ERROR: Mixing incompatible types
name = "Maaz"
age = 25
# full_info = name + age  # TypeError: can only concatenate str (not "int") to str

# CORRECT: Convert to same type
full_info = name + " is " + str(age) + " years old"
print(full_info)  # Output: Maaz is 25 years old

# OR use f-strings
full_info = f"{name} is {age} years old"
print(full_info)  # Output: Maaz is 25 years old
```

### ValueError - Invalid Type Conversion

```python
# ERROR: Invalid conversion
# age = int("twenty-five")  # ValueError: invalid literal for int()

# CORRECT: Use valid numeric string
age_str = "25"
age = int(age_str)
print(age)  # Output: 25

# Better: Handle conversion errors
def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to integer")
        return None

result = safe_int_conversion("twenty-five")  # Output: Cannot convert 'twenty-five' to integer
```

### IndentationError - Incorrect Indentation

```python
# ERROR: Incorrect indentation
# def my_function():
# name = "Maaz"  # IndentationError: expected an indented block

# CORRECT: Proper indentation
def my_function():
    name = "Maaz"
    print(name)

my_function()  # Output: Maaz
```

### SyntaxError - Invalid Variable Names

```python
# ERROR: Invalid variable names
# 2name = "Invalid"      # SyntaxError: invalid decimal literal
# first-name = "Invalid" # SyntaxError: invalid syntax
# class = "Invalid"      # SyntaxError: invalid syntax (keyword)

# CORRECT: Valid variable names
name2 = "Valid"
first_name = "Valid"  # Use underscore instead of hyphen
class_name = "Valid"  # Don't use keywords
```

### UnboundLocalError - Local Variable Referenced Before Assignment

```python
counter = 10  # Global variable

def increment():
    print(counter)  # This will cause UnboundLocalError
    counter += 1    # Python sees assignment, treats counter as local

# ERROR: UnboundLocalError when calling increment()

# CORRECT: Use global keyword
def increment_correct():
    global counter
    print(counter)
    counter += 1

increment_correct()  # Works correctly
```

### AttributeError - Calling Wrong Methods

```python
# ERROR: Wrong method for data type
number = 42
# result = number.upper()  # AttributeError: 'int' object has no attribute 'upper'

# CORRECT: Use appropriate methods for data types
text = "hello"
result = text.upper()
print(result)  # Output: HELLO

# Check if method exists
if hasattr(text, 'upper'):
    result = text.upper()
    print(result)  # Output: HELLO
```

### Best Practices to Avoid Errors

```python
# 1. Always initialize variables before use
name = None  # Initialize with None if needed
if some_condition:
    name = "Maaz"

# 2. Use meaningful variable names
# Bad
n = "Maaz"
a = 25

# Good
name = "Maaz"
age = 25

# 3. Use type hints for clarity (Python 3.5+)
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

# 4. Validate input data
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# 5. Use consistent naming conventions
# snake_case for variables and functions
user_name = "Maaz"
first_name = "Maaz"

# UPPER_CASE for constants
MAX_ATTEMPTS = 3
PI = 3.14159
```

---

## Summary

Variables are fundamental to Python programming. Understanding their types, operations, methods, and common pitfalls will help you write better, more reliable code. Remember to:

1. Use descriptive variable names
2. Initialize variables before use
3. Handle type conversions carefully
4. Follow Python naming conventions
5. Use global/local scope appropriately
6. Validate input data when necessary
