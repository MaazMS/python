# Data Type Conversion in Python

Data type conversion (also known as type casting) is the process of converting one data type to another. Python provides built-in functions and methods to perform these conversions. This documentation covers all aspects of data type conversion with examples and common errors.

## Table of Contents

1. [All Data Type Conversions](#1-all-data-type-conversions)
2. [Data Type Conversion Operations](#2-data-type-conversion-operations)
3. [Data Type Conversion Methods](#3-data-type-conversion-methods)
4. [Common Errors in Data Type Conversion](#4-common-errors-in-data-type-conversion)

---

## 1. All Data Type Conversions

### 1.1 To Integer (`int()`)

Convert various data types to integer:

```python
# From string to integer
str_num = "123"
int_num = int(str_num)
print(int_num)  # 123
print(type(int_num))  # <class 'int'>

# From float to integer (truncates decimal part)
float_num = 45.67
int_num = int(float_num)
print(int_num)  # 45

# From boolean to integer
bool_true = True
bool_false = False
print(int(bool_true))   # 1
print(int(bool_false))  # 0

# From complex to integer (only real part, must be whole number)
complex_num = 5+0j
print(int(complex_num))  # 5

# From binary, octal, hexadecimal strings
binary_str = "1010"
octal_str = "12"
hex_str = "A"
print(int(binary_str, 2))  # 10 (binary to decimal)
print(int(octal_str, 8))   # 10 (octal to decimal)
print(int(hex_str, 16))    # 10 (hex to decimal)
```

### 1.2 To Float (`float()`)

Convert various data types to float:

```python
# From string to float
str_num = "123.45"
float_num = float(str_num)
print(float_num)  # 123.45
print(type(float_num))  # <class 'float'>

# From integer to float
int_num = 42
float_num = float(int_num)
print(float_num)  # 42.0

# From boolean to float
print(float(True))   # 1.0
print(float(False))  # 0.0

# From complex to float (only real part)
complex_num = 3.14+0j
print(float(complex_num))  # 3.14

# Special float values
print(float('inf'))   # inf (infinity)
print(float('-inf'))  # -inf (negative infinity)
print(float('nan'))   # nan (not a number)
```

### 1.3 To String (`str()`)

Convert any data type to string:

```python
# From integer to string
num = 123
str_num = str(num)
print(str_num)  # "123"
print(type(str_num))  # <class 'str'>

# From float to string
float_num = 3.14
str_num = str(float_num)
print(str_num)  # "3.14"

# From boolean to string
print(str(True))   # "True"
print(str(False))  # "False"

# From list to string
my_list = [1, 2, 3]
str_list = str(my_list)
print(str_list)  # "[1, 2, 3]"

# From dictionary to string
my_dict = {'a': 1, 'b': 2}
str_dict = str(my_dict)
print(str_dict)  # "{'a': 1, 'b': 2}"

# From None to string
none_val = None
str_none = str(none_val)
print(str_none)  # "None"
```

### 1.4 To Boolean (`bool()`)

Convert various data types to boolean:

```python
# From integer to boolean
print(bool(1))    # True (non-zero)
print(bool(0))    # False (zero)
print(bool(-5))   # True (non-zero)

# From float to boolean
print(bool(3.14))  # True (non-zero)
print(bool(0.0))   # False (zero)

# From string to boolean
print(bool("Hello"))  # True (non-empty)
print(bool(""))       # False (empty string)
print(bool("False"))  # True (non-empty string, even if it says "False")

# From list to boolean
print(bool([1, 2, 3]))  # True (non-empty)
print(bool([]))         # False (empty list)

# From dictionary to boolean
print(bool({'a': 1}))  # True (non-empty)
print(bool({}))        # False (empty dict)

# From None to boolean
print(bool(None))  # False
```

### 1.5 To List (`list()`)

Convert iterables to list:

```python
# From string to list
str_val = "hello"
list_val = list(str_val)
print(list_val)  # ['h', 'e', 'l', 'l', 'o']

# From tuple to list
tuple_val = (1, 2, 3)
list_val = list(tuple_val)
print(list_val)  # [1, 2, 3]

# From set to list
set_val = {1, 2, 3}
list_val = list(set_val)
print(list_val)  # [1, 2, 3] (order may vary)

# From range to list
range_val = range(5)
list_val = list(range_val)
print(list_val)  # [0, 1, 2, 3, 4]

# From dictionary to list (keys only)
dict_val = {'a': 1, 'b': 2}
list_val = list(dict_val)
print(list_val)  # ['a', 'b']

# From dictionary values to list
list_val = list(dict_val.values())
print(list_val)  # [1, 2]

# From dictionary items to list
list_val = list(dict_val.items())
print(list_val)  # [('a', 1), ('b', 2)]
```

### 1.6 To Tuple (`tuple()`)

Convert iterables to tuple:

```python
# From list to tuple
list_val = [1, 2, 3]
tuple_val = tuple(list_val)
print(tuple_val)  # (1, 2, 3)

# From string to tuple
str_val = "hello"
tuple_val = tuple(str_val)
print(tuple_val)  # ('h', 'e', 'l', 'l', 'o')

# From set to tuple
set_val = {1, 2, 3}
tuple_val = tuple(set_val)
print(tuple_val)  # (1, 2, 3) (order may vary)

# From range to tuple
range_val = range(3)
tuple_val = tuple(range_val)
print(tuple_val)  # (0, 1, 2)

# From dictionary to tuple (keys only)
dict_val = {'a': 1, 'b': 2}
tuple_val = tuple(dict_val)
print(tuple_val)  # ('a', 'b')
```

### 1.7 To Set (`set()`)

Convert iterables to set (removes duplicates):

```python
# From list to set
list_val = [1, 2, 2, 3, 3, 3]
set_val = set(list_val)
print(set_val)  # {1, 2, 3}

# From string to set
str_val = "hello"
set_val = set(str_val)
print(set_val)  # {'h', 'e', 'l', 'o'} (duplicates removed)

# From tuple to set
tuple_val = (1, 2, 2, 3)
set_val = set(tuple_val)
print(set_val)  # {1, 2, 3}

# From dictionary to set (keys only)
dict_val = {'a': 1, 'b': 2}
set_val = set(dict_val)
print(set_val)  # {'a', 'b'}
```

### 1.8 To Dictionary (`dict()`)

Convert to dictionary:

```python
# From list of tuples to dictionary
list_tuples = [('a', 1), ('b', 2), ('c', 3)]
dict_val = dict(list_tuples)
print(dict_val)  # {'a': 1, 'b': 2, 'c': 3}

# From list of lists to dictionary
list_lists = [['a', 1], ['b', 2], ['c', 3]]
dict_val = dict(list_lists)
print(dict_val)  # {'a': 1, 'b': 2, 'c': 3}

# From zip object to dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_val = dict(zip(keys, values))
print(dict_val)  # {'a': 1, 'b': 2, 'c': 3}

# From keyword arguments to dictionary
dict_val = dict(a=1, b=2, c=3)
print(dict_val)  # {'a': 1, 'b': 2, 'c': 3}
```

### 1.9 To Frozenset (`frozenset()`)

Convert iterables to frozenset (immutable set):

```python
# From list to frozenset
list_val = [1, 2, 2, 3]
frozenset_val = frozenset(list_val)
print(frozenset_val)  # frozenset({1, 2, 3})

# From string to frozenset
str_val = "hello"
frozenset_val = frozenset(str_val)
print(frozenset_val)  # frozenset({'h', 'e', 'l', 'o'})

# From set to frozenset
set_val = {1, 2, 3}
frozenset_val = frozenset(set_val)
print(frozenset_val)  # frozenset({1, 2, 3})
```

### 1.10 To Complex (`complex()`)

Convert to complex number:

```python
# From integer to complex
int_val = 5
complex_val = complex(int_val)
print(complex_val)  # (5+0j)

# From float to complex
float_val = 3.14
complex_val = complex(float_val)
print(complex_val)  # (3.14+0j)

# From string to complex
str_val = "3+4j"
complex_val = complex(str_val)
print(complex_val)  # (3+4j)

# Creating complex with real and imaginary parts
complex_val = complex(3, 4)
print(complex_val)  # (3+4j)
```

---

## 2. Data Type Conversion Operations

### 2.1 Implicit Conversion (Type Coercion)

Python automatically converts data types in certain operations:

```python
# Integer and float operations
int_val = 10
float_val = 3.14
result = int_val + float_val  # int is converted to float
print(result)  # 13.14
print(type(result))  # <class 'float'>

# Boolean in arithmetic operations
bool_val = True
int_val = 5
result = bool_val + int_val  # True becomes 1
print(result)  # 6

# String concatenation with other types requires explicit conversion
name = "John"
age = 25
# message = name + age  # This would cause TypeError
message = name + str(age)  # Explicit conversion required
print(message)  # "John25"

# Division always returns float
result = 10 / 2
print(result)  # 5.0
print(type(result))  # <class 'float'>

# Floor division with mixed types
result = 10 // 3.0  # int // float = float
print(result)  # 3.0
print(type(result))  # <class 'float'>
```

### 2.2 Explicit Conversion Operations

```python
# Using constructors for conversion
str_num = "42"
int_num = int(str_num)
float_num = float(str_num)
bool_num = bool(int_num)

print(f"String: {str_num} ({type(str_num)})")
print(f"Integer: {int_num} ({type(int_num)})")
print(f"Float: {float_num} ({type(float_num)})")
print(f"Boolean: {bool_num} ({type(bool_num)})")

# Chain conversions
original = "123.45"
result = int(float(original))  # str -> float -> int
print(result)  # 123

# Using eval() for string expressions (use with caution)
expr = "2 + 3 * 4"
result = eval(expr)
print(result)  # 14
print(type(result))  # <class 'int'>
```

### 2.3 Mathematical Operations Causing Conversion

```python
# Powers with different types
base = 2
exponent = 3.0
result = base ** exponent  # int ** float = float
print(result)  # 8.0
print(type(result))  # <class 'float'>

# Modulo with different types
result = 10 % 3.0  # int % float = float
print(result)  # 1.0
print(type(result))  # <class 'float'>

# Complex number operations
real = 3
imaginary = 4j
result = real + imaginary  # int + complex = complex
print(result)  # (3+4j)
print(type(result))  # <class 'complex'>
```

---

## 3. Data Type Conversion Methods

### 3.1 String Methods for Conversion

```python
# String methods that return different types
text = "hello world"

# String to list methods
words = text.split()  # Split by whitespace
print(words)  # ['hello', 'world']

chars = list(text)  # Convert to character list
print(chars)  # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# String case conversion methods
print(text.upper())    # "HELLO WORLD"
print(text.lower())    # "hello world"
print(text.title())    # "Hello World"
print(text.capitalize())  # "Hello world"

# String to boolean-like methods
print(text.isdigit())   # False
print(text.isalpha())   # False (contains space)
print(text.isalnum())   # False (contains space)
print("123".isdigit())  # True

# String strip methods
padded = "  hello  "
print(padded.strip())   # "hello"
print(padded.lstrip())  # "hello  "
print(padded.rstrip())  # "  hello"
```

### 3.2 Numeric Methods for Conversion

```python
# Float methods
float_val = 3.14159

# Convert to different representations
print(float_val.hex())  # '0x1.921f9f01b866ep+1'
print(float.fromhex('0x1.921f9f01b866ep+1'))  # 3.14159

# Integer methods
int_val = 42

# Convert to different bases
print(bin(int_val))  # '0b101010' (binary)
print(oct(int_val))  # '0o52' (octal)
print(hex(int_val))  # '0x2a' (hexadecimal)

# Convert back from different bases
print(int('0b101010', 2))   # 42
print(int('0o52', 8))       # 42
print(int('0x2a', 16))      # 42
```

### 3.3 Collection Methods for Conversion

```python
# List methods
my_list = [1, 2, 3, 4, 5]

# Join list elements to string
str_list = ', '.join(map(str, my_list))
print(str_list)  # "1, 2, 3, 4, 5"

# Dictionary methods
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Convert dictionary parts to lists
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
items_list = list(my_dict.items())

print(keys_list)    # ['a', 'b', 'c']
print(values_list)  # [1, 2, 3]
print(items_list)   # [('a', 1), ('b', 2), ('c', 3)]

# Set methods
my_set = {1, 2, 3, 4, 5}

# Convert set to sorted list
sorted_list = sorted(my_set)
print(sorted_list)  # [1, 2, 3, 4, 5]
```

### 3.4 Advanced Conversion Methods

```python
# Using map() for batch conversion
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers))
print(int_numbers)  # [1, 2, 3, 4, 5]

# Using filter() with conversion
mixed_list = ['1', '2', 'hello', '3', 'world', '4']
numbers_only = list(filter(str.isdigit, mixed_list))
print(numbers_only)  # ['1', '2', '3', '4']

# Convert filtered results to integers
int_numbers = list(map(int, numbers_only))
print(int_numbers)  # [1, 2, 3, 4]

# Using list comprehension for conversion
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = [int(x) for x in str_numbers]
print(int_numbers)  # [1, 2, 3, 4, 5]

# Conditional conversion
mixed_values = ['1', '2.5', 'hello', '3', '4.7']
converted = []
for val in mixed_values:
    try:
        if '.' in val:
            converted.append(float(val))
        else:
            converted.append(int(val))
    except ValueError:
        converted.append(val)  # Keep original if conversion fails

print(converted)  # [1, 2.5, 'hello', 3, 4.7]
```

---

## 4. Common Errors in Data Type Conversion

### 4.1 ValueError: Invalid Conversion

```python
# Common ValueError scenarios
try:
    # Invalid string to integer conversion
    result = int("hello")
except ValueError as e:
    print(f"Error: {e}")  # invalid literal for int() with base 10: 'hello'

try:
    # Invalid string to float conversion
    result = float("not_a_number")
except ValueError as e:
    print(f"Error: {e}")  # could not convert string to float: not_a_number

try:
    # Complex number with imaginary part to int/float
    complex_num = 3 + 4j
    result = int(complex_num)
except TypeError as e:
    print(f"Error: {e}")  # can't convert complex to int

# Solution: Check before conversion
def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to integer")
        return None
    except TypeError:
        print(f"Invalid type for conversion: {type(value)}")
        return None

result = safe_int_conversion("123")    # 123
result = safe_int_conversion("hello")  # None
result = safe_int_conversion(3.14)     # 3
```

### 4.2 TypeError: Unsupported Operations

```python
# Common TypeError scenarios
try:
    # Cannot concatenate string and integer
    result = "Age: " + 25
except TypeError as e:
    print(f"Error: {e}")  # can only concatenate str (not "int") to str

# Solution: Explicit conversion
result = "Age: " + str(25)
print(result)  # "Age: 25"

try:
    # Cannot convert unhashable type to set
    list_with_lists = [[1, 2], [3, 4]]
    result = set(list_with_lists)
except TypeError as e:
    print(f"Error: {e}")  # unhashable type: 'list'

# Solution: Convert to hashable type first
list_with_tuples = [tuple(sublist) for sublist in list_with_lists]
result = set(list_with_tuples)
print(result)  # {(1, 2), (3, 4)}
```

### 4.3 Precision Loss in Conversion

```python
# Float to integer conversion loses decimal part
float_val = 3.99
int_val = int(float_val)
print(f"Original: {float_val}, Converted: {int_val}")  # Original: 3.99, Converted: 3

# Large integer to float may lose precision
large_int = 123456789012345678901234567890
float_val = float(large_int)
back_to_int = int(float_val)
print(f"Original: {large_int}")
print(f"Float: {float_val}")
print(f"Back to int: {back_to_int}")
print(f"Precision lost: {large_int != back_to_int}")  # True

# Solution: Use decimal for precise arithmetic
from decimal import Decimal
precise_val = Decimal('3.99')
print(f"Precise value: {precise_val}")
```

### 4.4 Encoding/Decoding Errors

```python
# String to bytes conversion errors
try:
    text = "Hello 世界"  # Contains non-ASCII characters
    bytes_val = text.encode('ascii')
except UnicodeEncodeError as e:
    print(f"Encoding error: {e}")

# Solution: Use appropriate encoding
bytes_val = text.encode('utf-8')
print(f"Encoded: {bytes_val}")

# Bytes to string conversion errors
try:
    bytes_val = b'\xff\xfe\x48\x00'  # Invalid UTF-8 sequence
    text = bytes_val.decode('utf-8')
except UnicodeDecodeError as e:
    print(f"Decoding error: {e}")

# Solution: Handle errors gracefully
text = bytes_val.decode('utf-8', errors='ignore')
print(f"Decoded with ignored errors: {text}")
```

### 4.5 Boolean Conversion Gotchas

```python
# Common boolean conversion mistakes
print(bool("False"))  # True (non-empty string)
print(bool("0"))      # True (non-empty string)
print(bool(""))       # False (empty string)
print(bool(0))        # False (zero)
print(bool([]))       # False (empty list)
print(bool({}))       # False (empty dict)
print(bool(None))     # False

# Correct way to convert string to boolean
def str_to_bool(value):
    if isinstance(value, str):
        return value.lower() in ('true', '1', 'yes', 'on')
    return bool(value)

print(str_to_bool("True"))   # True
print(str_to_bool("false"))  # False
print(str_to_bool("1"))      # True
print(str_to_bool("0"))      # False
```

### 4.6 Dictionary Conversion Errors

```python
# Dictionary conversion requires proper key-value structure
try:
    # Invalid structure for dict conversion
    invalid_list = [1, 2, 3]
    result = dict(invalid_list)
except TypeError as e:
    print(f"Error: {e}")  # cannot convert dictionary update sequence element #0 to a sequence

# Solution: Ensure proper structure
valid_list = [(1, 'a'), (2, 'b'), (3, 'c')]
result = dict(valid_list)
print(result)  # {1: 'a', 2: 'b', 3: 'c'}

# Or use enumerate for indexing
numbers = ['a', 'b', 'c']
result = dict(enumerate(numbers))
print(result)  # {0: 'a', 1: 'b', 2: 'c'}
```

### 4.7 Best Practices for Error Handling

```python
def safe_convert(value, target_type):
    """
    Safely convert value to target type with error handling
    """
    try:
        if target_type == int:
            if isinstance(value, str):
                # Handle binary, octal, hex strings
                if value.startswith('0b'):
                    return int(value, 2)
                elif value.startswith('0o'):
                    return int(value, 8)
                elif value.startswith('0x'):
                    return int(value, 16)
            return int(value)
        
        elif target_type == float:
            return float(value)
        
        elif target_type == str:
            return str(value)
        
        elif target_type == bool:
            if isinstance(value, str):
                return value.lower() in ('true', '1', 'yes', 'on')
            return bool(value)
        
        elif target_type == list:
            return list(value)
        
        elif target_type == tuple:
            return tuple(value)
        
        elif target_type == set:
            return set(value)
        
        elif target_type == dict:
            return dict(value)
        
        else:
            return target_type(value)
    
    except (ValueError, TypeError, OverflowError) as e:
        print(f"Conversion error: {e}")
        return None

# Usage examples
print(safe_convert("123", int))      # 123
print(safe_convert("hello", int))    # None (with error message)
print(safe_convert([1, 2, 3], str))  # "[1, 2, 3]"
print(safe_convert("True", bool))    # True
```

---

## Summary

This documentation covers:

1. **All Data Type Conversions**: Comprehensive examples of converting between all Python data types
2. **Conversion Operations**: Both implicit (automatic) and explicit conversion operations
3. **Conversion Methods**: Built-in methods and advanced techniques for type conversion
4. **Common Errors**: Typical errors encountered during conversion and how to handle them

### Key Takeaways

- Always handle conversion errors with try-except blocks
- Be aware of precision loss in numeric conversions
- Use appropriate encoding for string-bytes conversions
- Understand the difference between implicit and explicit conversions
- Test edge cases and invalid inputs in your conversion logic
- Use type checking functions like `isinstance()` before conversion
- Consider using validation functions for user input conversions

### Further Reading

For more specific information about each data type, refer to:

- `text_type_data/string_documentation.md`
- `number_type_data/numeric_documentation.md`
- `sequence_index_type_data/list_documentation.md`
- `mapping_data_type/dict_documentation.md`
- `set_type_data/set_documentation.md`
- `boolean_type_data/boolean_documentation.md`
