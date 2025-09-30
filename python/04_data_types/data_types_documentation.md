# Built-in Data Types in Python

| Category | Data Type | Description | Access Method |
| --- | --- | --- | --- |
| Text Type | str | Single, double, and triple quotes | Index-based |
| Numeric Types | int, float, complex | Integers, decimal numbers, complex numbers (a + bj) | Direct access |
| Sequence Types | list, tuple, range | list[] - mutable(Changeable), tuple() - immutable(Unchangeable), range() - sequence of numbers | Index-based |
| Mapping Type | dict | {} - key-value pairs, mutable(Changeable) | Key-based |
| Set Types | set, frozenset | set{} - mutable(Changeable), frozenset - immutable (Unchangeable)| No indexing |
| Boolean Type | bool | True or False values | Direct access |
| Binary Types | bytes, bytearray, memoryview | Binary data handling | Index-based |
| None Type | NoneType | Represents absence of value | Direct access |
| Function Types | function, builtin_function_or_method | User-defined and built-in functions | Direct access |
| Other Types | type, module, slice, ellipsis | Advanced types and objects | Varies |

## What is type()

The `type()` method returns the class type of the argument (object) passed as a parameter.

Python has a built-in method called `type()` which is useful for determining the type of a variable used in the program during runtime. When a single argument (object) is passed to the `type()` built-in function, it returns the type of the given object.

### Example

```python
x = 5
print(type(x))  # <class 'int'>

y = "Hello"
print(type(y))  # <class 'str'>

z = [1, 2, 3]
print(type(z))  # <class 'list'>
```

## Access Methods: Index vs Non-Index

### Index-Based Access (Sequence Types)

These data types support accessing elements using numerical indices (0, 1, 2, ...):

```python
# String - Index-based access
text = "Python"
print(text[0])    # 'P' (first character)
print(text[2])    # 't' (third character)
print(text[-1])   # 'n' (last character)

# List - Index-based access
fruits = ['apple', 'banana', 'orange']
print(fruits[0])  # 'apple'
print(fruits[1])  # 'banana'
print(fruits[-1]) # 'orange' (last element)

# Tuple - Index-based access
coordinates = (10, 20, 30)
print(coordinates[0])  # 10
print(coordinates[2])  # 30

# Range - Index-based access
numbers = range(5, 15)
print(numbers[0])  # 5
print(numbers[3])  # 8

# Bytes - Index-based access
byte_data = b'Hello'
print(byte_data[0])  # 72 (ASCII value of 'H')
print(byte_data[1])  # 101 (ASCII value of 'e')
```

### Key-Based Access (Mapping Type)

Dictionary uses keys instead of indices:

```python
# Dictionary - Key-based access
student = {'name': 'John', 'age': 20, 'grade': 'A'}
print(student['name'])   # 'John'
print(student['age'])    # 20
print(student.get('grade'))  # 'A' (alternative method)

# Adding/updating values
student['city'] = 'New York'  # Add new key-value pair
student['age'] = 21          # Update existing value
```

### No Indexing (Set Types)

Sets don't support indexing - only membership testing:

```python
# Set - No indexing, only membership testing
unique_numbers = {1, 2, 3, 4, 5}
print(1 in unique_numbers)     # True
print(6 in unique_numbers)     # False

# To access elements, convert to list or iterate
numbers_list = list(unique_numbers)
print(numbers_list[0])  # First element (order not guaranteed)

# Or iterate through set
for num in unique_numbers:
    print(num)

# Frozenset - Same as set, no indexing
frozen_numbers = frozenset([1, 2, 3, 4, 5])
print(3 in frozen_numbers)  # True
```

### Direct Access (Single Values)

These types represent single values and don't support indexing:

```python
# Numeric types - Direct access only
age = 25
price = 19.99
complex_num = 3 + 4j

# Boolean - Direct access only
is_active = True

# None - Direct access only
result = None

# Function - Direct access only
def my_function():
    return "Hello"
```

## Examples of Each Data Type

### 1. Text Type (str)

```python
# String examples
single_quote = 'Hello World'
double_quote = "Python Programming"
triple_quote = """This is a
multi-line string"""

print(type(single_quote))  # <class 'str'>
```

### 2. Numeric Types

```python
# Integer
age = 25
print(type(age))  # <class 'int'>

# Float
price = 19.99
print(type(price))  # <class 'float'>

# Complex
complex_num = 3 + 4j
print(type(complex_num))  # <class 'complex'>
```

### 3. Sequence Types

```python
# List (mutable, Changeable) 
fruits = ['apple', 'banana', 'orange']
print(type(fruits))  # <class 'list'>

# Tuple (immutable, Unchangeable)
coordinates = (10, 20)
print(type(coordinates))  # <class 'tuple'>

# Range
numbers = range(1, 6)
print(type(numbers))  # <class 'range'>
print(list(numbers))  # [1, 2, 3, 4, 5]
```

### 4. Mapping Type (dict)

```python
# Dictionary
student = {'name': 'John', 'age': 20, 'grade': 'A'}
print(type(student))  # <class 'dict'>
```

### 5. Set Types

```python
# Set (mutable, Changeable)
unique_numbers = {1, 2, 3, 4, 5}
print(type(unique_numbers))  # <class 'set'>

# Frozenset (immutable, Unchangeable)
frozen_numbers = frozenset([1, 2, 3, 4, 5])
print(type(frozen_numbers))  # <class 'frozenset'>
```

### 6. Boolean Type

```python
# Boolean
is_active = True
is_complete = False
print(type(is_active))  # <class 'bool'>
```

### 7. Binary Types

```python
# Bytes
byte_data = b'Hello'
print(type(byte_data))  # <class 'bytes'>

# Bytearray
byte_array = bytearray(b'Hello')
print(type(byte_array))  # <class 'bytearray'>

# Memoryview
memory_view = memoryview(b'Hello')
print(type(memory_view))  # <class 'memoryview'>
```

### 8. None Type

```python
# None - represents absence of value
result = None
empty_value = None
print(type(result))  # <class 'NoneType'>

# Common use cases
def greet():
    print("Hello")
    # Function returns None implicitly

return_value = greet()
print(type(return_value))  # <class 'NoneType'>
```

### 9. Function Types

```python
# User-defined function
def my_function():
    return "Hello"

print(type(my_function))  # <class 'function'>

# Built-in function
print(type(print))  # <class 'builtin_function_or_method'>
print(type(len))    # <class 'builtin_function_or_method'>

# Lambda function
lambda_func = lambda x: x * 2
print(type(lambda_func))  # <class 'function'>
```

### 10. Other Important Types

```python
# Type of types
print(type(int))  # <class 'type'>
print(type(str))  # <class 'type'>

# Module type
import math
print(type(math))  # <class 'module'>

# Slice object
slice_obj = slice(1, 5, 2)
print(type(slice_obj))  # <class 'slice'>

# Ellipsis
ellipsis_obj = ...
print(type(ellipsis_obj))  # <class 'ellipsis'>

# Class type
class MyClass:
    pass

obj = MyClass()
print(type(obj))        # <class '__main__.MyClass'>
print(type(MyClass))    # <class 'type'>
```
