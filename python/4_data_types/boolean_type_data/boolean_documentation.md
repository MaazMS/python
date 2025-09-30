# Boolean Type Data Documentation

## 1. Boolean Type Data Definition and Characteristics

### Definition

- Boolean is a data type that represents logical values: `True` or `False`
- Boolean values are case-sensitive in Python (must be capitalized)
- Boolean type is a subclass of integers in Python (True = 1, False = 0)
- Boolean values are immutable objects

### Characteristics

- **Size**: Boolean values occupy 28 bytes in memory (same as small integers)
- **Type**: `bool` is a subclass of `int`
- **Values**: Only two possible values - `True` and `False`
- **Immutable**: Boolean values cannot be changed after creation
- **Case-sensitive**: Must be written as `True` and `False` (not `true` or `false`)

### Examples

```python
# Boolean literals
flag = True
status = False

# Type checking
print(type(True))    # <class 'bool'>
print(type(False))   # <class 'bool'>

# Boolean as subclass of int
print(isinstance(True, int))   # True
print(isinstance(False, int))  # True

# Memory size
import sys
print(sys.getsizeof(True))    # 28
print(sys.getsizeof(False))   # 28
```

## 2. Boolean Type Data Creation

### Direct Assignment

```python
# Direct boolean assignment
is_active = True
is_complete = False
```

### Using bool() Constructor

```python
# Using bool() function
result = bool(1)        # True
result = bool(0)        # False
result = bool("hello")  # True
result = bool("")       # False
result = bool([1,2,3])  # True
result = bool([])       # False
```

### From Expressions

```python
# From comparison expressions
age = 25
is_adult = age >= 18    # True
is_teenager = age < 18  # False

# From logical expressions
x, y = 5, 10
result = x < y and y > 0  # True
```

### Falsy Values (convert to False)

```python
# All these values are considered False
print(bool(None))      # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(0j))        # False (complex zero)
print(bool(""))        # False (empty string)
print(bool([]))        # False (empty list)
print(bool({}))        # False (empty dict)
print(bool(set()))     # False (empty set)
print(bool(()))        # False (empty tuple)
print(bool(range(0)))  # False (empty range)
```

### Truthy Values (convert to True)

```python
# All these values are considered True
print(bool(1))         # True
print(bool(-1))        # True
print(bool(3.14))      # True
print(bool("hello"))   # True
print(bool([1,2]))     # True
print(bool({'a': 1}))  # True
print(bool({1,2,3}))   # True
```

## 3. Boolean Type Data Operations

### Logical Operations

```python
# AND operation
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# OR operation
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# NOT operation
print(not True)         # False
print(not False)        # True
```

### Comparison Operations

```python
# Equality comparison
print(True == True)     # True
print(True == False)    # False
print(False == False)   # True

# Identity comparison
print(True is True)     # True
print(False is False)   # True
print(True is False)    # False

# Inequality comparison
print(True != False)    # True
print(True != True)     # False
```

### Arithmetic Operations (Boolean as integers)

```python
# Addition
print(True + True)      # 2
print(True + False)     # 1
print(False + False)    # 0

# Subtraction
print(True - False)     # 1
print(False - True)     # -1

# Multiplication
print(True * 5)         # 5
print(False * 10)       # 0

# Division
print(True / 2)         # 0.5
print(False / 1)        # 0.0 (if divisor is not 0)
```

### Short-circuit Evaluation

```python
# AND short-circuit
def func1():
    print("func1 called")
    return True

def func2():
    print("func2 called")
    return False

# func2 won't be called if func1 returns False
result = func1() and func2()  # Both called
result = False and func1()    # func1 not called

# OR short-circuit
result = True or func1()      # func1 not called
result = False or func1()     # func1 called
```

## 4. Boolean Type Data Methods

### Built-in Methods

```python
# Since bool is a subclass of int, it inherits int methods
flag = True

# Integer methods available
print(flag.bit_length())    # 1
print(flag.to_bytes(1, 'big'))  # b'\x01'

# Type conversion methods
print(str(True))       # 'True'
print(int(True))       # 1
print(float(True))     # 1.0
print(complex(True))   # (1+0j)
```

### Common Boolean Functions

```python
# all() function - returns True if all elements are True
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(all([]))                    # True (empty iterable)

# any() function - returns True if any element is True
print(any([False, False, True]))  # True
print(any([False, False, False])) # False
print(any([]))                    # False (empty iterable)

# isinstance() for type checking
print(isinstance(True, bool))     # True
print(isinstance(1, bool))        # False
print(isinstance(True, int))      # True
```

### Custom Boolean Methods

```python
class CustomBoolean:
    def __init__(self, value):
        self.value = bool(value)
    
    def __bool__(self):
        return self.value
    
    def __str__(self):
        return str(self.value)
    
    def toggle(self):
        self.value = not self.value
        return self.value

# Usage
cb = CustomBoolean(True)
print(bool(cb))         # True
print(cb.toggle())      # False
print(cb.toggle())      # True
```

## 5. Common Errors in Boolean Type Data

### Case Sensitivity Error

```python
# ❌ Wrong - lowercase
# true = True    # This creates a variable named 'true'
# false = False  # This creates a variable named 'false'

# ✅ Correct - proper case
is_valid = True
is_invalid = False
```

### Type Confusion

```python
# ❌ Wrong - comparing with strings
status = True
if status == "True":    # This is False!
    print("This won't print")

# ✅ Correct - direct boolean comparison
if status:
    print("This will print")

# ❌ Wrong - using 1 and 0 for readability
is_active = 1  # Not recommended
is_inactive = 0

# ✅ Correct - use actual boolean values
is_active = True
is_inactive = False
```

### Assignment vs Comparison

```python
# ❌ Wrong - assignment in condition
x = 5
if x = 10:  # SyntaxError: cannot assign to expression
    print("Error")

# ✅ Correct - comparison in condition
if x == 10:
    print("x is 10")

# ✅ Correct - assignment then comparison
x = 10
if x == 10:
    print("x is 10")
```

### Logical Operator Confusion

```python
# ❌ Wrong - using bitwise operators for boolean logic
a, b = True, False
result = a & b    # Works but not recommended for boolean logic

# ✅ Correct - using logical operators
result = a and b  # Preferred for boolean logic

# ❌ Wrong - chaining comparisons incorrectly
x = 5
if x > 0 and < 10:  # SyntaxError
    print("Invalid")

# ✅ Correct - proper chaining
if 0 < x < 10:      # Pythonic way
    print("Valid")

# ✅ Correct - explicit chaining
if x > 0 and x < 10:
    print("Valid")
```

### Boolean Conversion Errors

```python
# ❌ Wrong - assuming all non-zero numbers are True in conditions
values = [0, 1, 2, -1, 0.0, 0.1]
for val in values:
    if val:  # This works, but be explicit about intention
        print(f"{val} is truthy")

# ✅ Correct - explicit boolean conversion when needed
for val in values:
    if bool(val):  # More explicit
        print(f"{val} converts to True")

# ❌ Wrong - not understanding empty container behavior
empty_list = []
if not empty_list == []:  # Confusing double negative
    print("List is not empty")

# ✅ Correct - direct empty check
if empty_list:
    print("List has items")
else:
    print("List is empty")
```

### Common Pitfalls

```python
# 1. Mutable default arguments (not directly boolean, but related)
def process_data(data, flag=True):  # ✅ Correct - immutable default
    if flag:
        return data.upper()
    return data

# 2. Boolean in string formatting
flag = True
message = f"Status: {flag}"  # ✅ Correct - prints "Status: True"

# 3. Boolean in JSON serialization
import json
data = {"is_active": True}
json_str = json.dumps(data)  # ✅ Correct - becomes "true" in JSON

# 4. Boolean arithmetic gotchas
result = True + True  # Result is 2, not True
result = True * False  # Result is 0, not False
```

## Best Practices

1. **Use explicit boolean values**: Use `True` and `False` instead of `1` and `0`
2. **Be explicit in conditions**: Use `if condition:` instead of `if condition == True:`
3. **Use `is` for None checks**: `if value is None:` instead of `if value == None:`
4. **Leverage truthiness**: Use `if my_list:` instead of `if len(my_list) > 0:`
5. **Use `all()` and `any()`**: For checking multiple conditions
6. **Be careful with boolean arithmetic**: Remember that `True + True = 2`

## Summary

Boolean type data in Python is simple yet powerful. Understanding its characteristics, creation methods, operations, and common pitfalls helps write more reliable and readable code. Remember that boolean values are immutable and are subclasses of integers, which enables both logical and arithmetic operations.
