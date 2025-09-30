# Numeric Data Types in Python

Python supports three main numeric data types: integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`). This documentation provides comprehensive examples for each aspect of numeric data types.

## 1. Numeric Data Types Definitions

### Integer (int)

Integers are whole numbers without decimal points. Python 3 has unlimited precision for integers.

**Example:**

```python
# Integer examples
positive_int = 42
negative_int = -17
zero = 0
large_int = 999999999999999999999999999999

print(f"Type of {positive_int}: {type(positive_int)}")  # <class 'int'>
print(f"Type of {negative_int}: {type(negative_int)}")  # <class 'int'>
```

### Float (float)

Floating-point numbers contain decimal points. They have limited precision (approximately 15-17 decimal digits).

**Example:**

```python
# Float examples
positive_float = 3.14
negative_float = -2.5
scientific_notation = 1.5e2  # 150.0
small_number = 1e-10  # 0.0000000001

print(f"Type of {positive_float}: {type(positive_float)}")  # <class 'float'>
print(f"Scientific notation: {scientific_notation}")  # 150.0
```

### Complex (complex)

Complex numbers have real and imaginary parts, written as `x + yj` where `x` is real and `y` is imaginary.

**Example:**

```python

# Complex examples
complex_num1 = 3 + 4j
complex_num2 = 2 - 5j
pure_imaginary = 7j
pure_real = 5 + 0j

print(f"Type of {complex_num1}: {type(complex_num1)}")  # <class 'complex'>
print(f"Real part: {complex_num1.real}")  # 3.0
print(f"Imaginary part: {complex_num1.imag}")  # 4.0
```

## 2. Numeric Data Types Creation

### Creating Integers

```python
# Direct assignment
age = 25
year = 2024

# From strings
str_number = "123"
converted_int = int(str_number)

# From floats (truncates decimal part)
float_to_int = int(3.8)  # Result: 3

# Binary, octal, and hexadecimal
binary = 0b1010      # 10 in decimal
octal = 0o12         # 10 in decimal
hexadecimal = 0xa    # 10 in decimal

print(f"Binary {binary}, Octal {octal}, Hex {hexadecimal}")
```

### Creating Floats

```python
# Direct assignment
pi = 3.14159
temperature = -15.5

# From strings
str_float = "12.34"
converted_float = float(str_float)

# From integers
int_to_float = float(25)  # Result: 25.0

# Scientific notation
large_number = 1.5e6      # 1500000.0
small_number = 2.5e-3     # 0.0025

print(f"Large: {large_number}, Small: {small_number}")
```

### Creating Complex Numbers

```python
# Direct assignment
z1 = 3 + 4j
z2 = 2 - 5j

# Using complex() function
z3 = complex(3, 4)        # 3 + 4j
z4 = complex(2)           # 2 + 0j
z5 = complex(0, 1)        # 1j

# From strings
str_complex = "3+4j"
z6 = complex(str_complex)

print(f"z1: {z1}, z3: {z3}, z6: {z6}")
```

## 3. Numeric Data Types Operations

### Arithmetic Operations

```python
# Basic arithmetic
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
floor_division = a // b # 3
modulus = a % b         # 1
exponentiation = a ** b # 1000

print(f"Addition: {addition}")
print(f"Floor division: {floor_division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")
```

### Float Operations

```python
# Float arithmetic
x = 10.5
y = 3.2

result1 = x + y         # 13.7
result2 = x * y         # 33.6
result3 = x / y         # 3.28125
result4 = x ** 2        # 110.25

print(f"Float results: {result1}, {result2}, {result3}, {result4}")
```

### Complex Operations

```python
# Complex arithmetic
z1 = 3 + 4j
z2 = 1 + 2j

addition = z1 + z2      # (4+6j)
subtraction = z1 - z2   # (2+2j)
multiplication = z1 * z2 # (-5+10j)
division = z1 / z2      # (2.2+0.4j)

print(f"Complex addition: {addition}")
print(f"Complex multiplication: {multiplication}")
```

### Mixed Type Operations

```python
# Operations between different numeric types
integer = 5
floating = 2.5
complex_num = 1 + 2j

# Integer and float
mixed1 = integer + floating     # 7.5 (result is float)
mixed2 = integer * floating     # 12.5 (result is float)

# Float and complex
mixed3 = floating + complex_num # (3.5+2j) (result is complex)
mixed4 = floating * complex_num # (2.5+5j) (result is complex)

print(f"Mixed operations: {mixed1}, {mixed2}, {mixed3}, {mixed4}")
```

## 4. Numeric Data Types Methods

### Built-in Functions for Numbers

```python
# Common built-in functions
numbers = [1, 2, 3, 4, 5]
float_num = 3.7
negative = -15

# Absolute value
abs_value = abs(negative)        # 15
abs_float = abs(-3.7)           # 3.7

# Min and max
minimum = min(numbers)           # 1
maximum = max(numbers)           # 5

# Sum
total = sum(numbers)             # 15

# Round
rounded = round(float_num)       # 4
rounded_precision = round(3.14159, 2)  # 3.14

# Divmod (quotient and remainder)
quotient, remainder = divmod(17, 5)  # (3, 2)

print(f"Absolute: {abs_value}, Min: {minimum}, Max: {maximum}")
print(f"Sum: {total}, Rounded: {rounded}, Rounded precision: {rounded_precision}")
print(f"Divmod: quotient={quotient}, remainder={remainder}")
```

### Mathematical Functions (from math module)

```python
import math

# Mathematical functions
num = 16
angle = math.pi / 4  # 45 degrees in radians

# Power and logarithm
sqrt_val = math.sqrt(num)           # 4.0
log_val = math.log(num)             # Natural log
log10_val = math.log10(num)         # Base 10 log
pow_val = math.pow(2, 3)            # 8.0

# Trigonometric functions
sin_val = math.sin(angle)           # 0.707...
cos_val = math.cos(angle)           # 0.707...
tan_val = math.tan(angle)           # 1.0

# Ceiling and floor
ceil_val = math.ceil(3.2)           # 4
floor_val = math.floor(3.8)         # 3

print(f"Square root: {sqrt_val}, Log: {log_val:.2f}")
print(f"Sin: {sin_val:.3f}, Cos: {cos_val:.3f}, Tan: {tan_val:.3f}")
print(f"Ceil: {ceil_val}, Floor: {floor_val}")
```

## 5. Common Errors in Numeric Data Types

### Division by Zero

```python
# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Error: division by zero

try:
    result = 10 % 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Error: integer division or modulo by zero
```

### Overflow and Precision Issues

```python
# Float precision issues
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")  # 0.30000000000000004 (not exactly 0.3)

# Better approach for precise decimal arithmetic
from decimal import Decimal
precise_result = Decimal('0.1') + Decimal('0.2')
print(f"Precise result: {precise_result}")  # 0.3

# Float overflow
import sys
print(f"Max float: {sys.float_info.max}")
try:
    overflow = 1.8e308 * 10
    print(overflow)  # inf (infinity)
except OverflowError as e:
    print(f"Overflow error: {e}")
```

### Complex Number Limitations

```python
# Comparison errors with complex numbers
try:
    result = (3 + 4j) > (1 + 2j)
except TypeError as e:
    print(f"Error: {e}")  # Error: '>' not supported between instances of 'complex' and 'complex'

# Complex numbers don't support comparison operators except == and !=
z1 = 3 + 4j
z2 = 1 + 2j
print(f"Equal: {z1 == z2}")        # False
print(f"Not equal: {z1 != z2}")    # True
```

### Integer Division Confusion

```python
# Python 2 vs Python 3 division behavior
a = 7
b = 3

# True division (Python 3 default)
true_division = a / b       # 2.333... (float result)

# Floor division
floor_division = a // b     # 2 (integer result)

print(f"True division: {true_division}")
print(f"Floor division: {floor_division}")

# Common mistake: expecting integer division
# In Python 2: 7 / 3 = 2 (integer)
# In Python 3: 7 / 3 = 2.333... (float)
```

### Underflow and Special Values

```python
# Very small numbers become zero
very_small = 1e-400
print(f"Very small number: {very_small}")  # 0.0

# Special float values
positive_infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(f"Positive infinity: {positive_infinity}")
print(f"Negative infinity: {negative_infinity}")
print(f"Not a number: {not_a_number}")

# Checking for special values
import math
print(f"Is inf: {math.isinf(positive_infinity)}")   # True
print(f"Is nan: {math.isnan(not_a_number)}")        # True
print(f"Is finite: {math.isfinite(42.0)}")          # True
```

### Best Practices to Avoid Errors

1. **Use appropriate data types**: Choose `int` for whole numbers, `float` for decimals, `complex` for complex mathematics.

2. **Handle precision issues**: Use `decimal.Decimal` for financial calculations requiring exact precision.

3. **Check for special values**: Always validate inputs, especially when dealing with user input or calculations that might result in infinity or NaN.

4. **Use proper error handling**: Wrap potentially problematic operations in try-except blocks.

5. **Be aware of type coercion**: Understand how Python handles operations between different numeric types.

---

**Note**: This documentation covers the essential aspects of numeric data types in Python. For advanced mathematical operations, consider using specialized libraries like NumPy, SciPy, or SymPy.
