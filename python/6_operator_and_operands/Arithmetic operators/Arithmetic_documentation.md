# Arithmetic Operators in Python

## 1. Arithmetic Definition and Characteristics

Arithmetic operators are symbols used to perform mathematical operations on numeric values (operands). In Python, arithmetic operators work with various numeric data types including integers, floats, and complex numbers.

### Characteristics:

- **Binary Operations**: Most arithmetic operators require two operands (except unary operators like negation)
- **Type Coercion**: Python automatically converts between compatible numeric types during operations
- **Precedence Rules**: Operations follow mathematical precedence (PEMDAS/BODMAS)
- **Left-to-Right Associativity**: Operations of equal precedence are evaluated from left to right
- **Return Types**: Result type depends on operand types (int + int = int, int + float = float)

## 2. Arithmetic Operations

| Operator | Description | Syntax | Example | Result |
|----------|-------------|--------|---------|--------|
| + | Addition: adds two operands | x + y | 5 + 3 | 8 |
| - | Subtraction: subtracts two operands | x - y | 10 - 4 | 6 |
| * | Multiplication: multiplies two operands | x * y | 7 * 6 | 42 |
| / | Division (float): divides two operands | x / y | 15 / 4 | 3.75 |
| // | Floor Division: divides and returns floor value | x // y | 15 // 4 | 3 |
| % | Modulus: returns remainder after division | x % y | 17 % 5 | 2 |
| ** | Exponentiation: raises x to power of y | x ** y | 2 ** 3 | 8 |

### Detailed Examples

```python
# Basic arithmetic operations
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")        # 13
print(f"Subtraction: {a} - {b} = {a - b}")    # 7
print(f"Multiplication: {a} * {b} = {a * b}") # 30
print(f"Division: {a} / {b} = {a / b}")       # 3.3333...
print(f"Floor Division: {a} // {b} = {a // b}") # 3
print(f"Modulus: {a} % {b} = {a % b}")        # 1
print(f"Power: {a} ** {b} = {a ** b}")        # 1000

# Working with different data types
int_val = 10
float_val = 3.5

result1 = int_val + float_val    # 13.5 (float)
result2 = int_val * float_val    # 35.0 (float)
result3 = int_val // float_val   # 2.0 (float)

# Complex number arithmetic
complex1 = 3 + 4j
complex2 = 1 + 2j
complex_sum = complex1 + complex2  # (4+6j)
```

## 3. Arithmetic Methods

Python provides several built-in functions and methods for arithmetic operations:

### Built-in Functions

```python
# abs() - Absolute value
print(abs(-5))          # 5
print(abs(-3.14))       # 3.14
print(abs(3+4j))        # 5.0 (magnitude of complex number)

# pow() - Power function
print(pow(2, 3))        # 8 (equivalent to 2 ** 3)
print(pow(2, 3, 5))     # 3 (2^3 % 5 = 8 % 5 = 3)

# divmod() - Division and modulus
quotient, remainder = divmod(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")  # 3 remainder 2

# round() - Rounding numbers
print(round(3.14159, 2))    # 3.14
print(round(2.5))           # 2 (banker's rounding)
print(round(3.5))           # 4

# min() and max() - Minimum and maximum
numbers = [1, 5, 3, 9, 2]
print(min(numbers))         # 1
print(max(numbers))         # 9
print(min(10, 20, 5))       # 5

# sum() - Sum of iterable
print(sum([1, 2, 3, 4, 5])) # 15
print(sum([1, 2, 3], 10))   # 16 (start value = 10)
```

### Math Module Functions

```python
import math

# Mathematical functions
print(math.sqrt(16))        # 4.0
print(math.ceil(3.2))       # 4 (ceiling)
print(math.floor(3.8))      # 3 (floor)
print(math.factorial(5))    # 120
print(math.gcd(48, 18))     # 6 (greatest common divisor)
print(math.lcm(4, 6))       # 12 (least common multiple)

# Trigonometric functions
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
print(math.tan(math.pi/4))  # 1.0

# Logarithmic functions
print(math.log(10))         # 2.302... (natural log)
print(math.log10(100))      # 2.0 (base 10)
print(math.log(8, 2))       # 3.0 (log base 2)
```

### Operator Module

```python
import operator

# Using operator module for arithmetic
a, b = 10, 3

print(operator.add(a, b))      # 13
print(operator.sub(a, b))      # 7
print(operator.mul(a, b))      # 30
print(operator.truediv(a, b))  # 3.333...
print(operator.floordiv(a, b)) # 3
print(operator.mod(a, b))      # 1
print(operator.pow(a, b))      # 1000
```

## 4. Common Errors in Arithmetic

### 4.1 Division by Zero

```python
# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # division by zero

try:
    result = 10 // 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # integer division or modulo by zero

try:
    result = 10 % 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # integer division or modulo by zero
```

### 4.2 Type Errors

```python
# TypeError - Unsupported operand types
try:
    result = "5" + 3  # Can't add string and integer
except TypeError as e:
    print(f"Error: {e}")

try:
    result = [1, 2, 3] * "2"  # Can't multiply list by string
except TypeError as e:
    print(f"Error: {e}")

# Correct approaches:
result1 = int("5") + 3      # Convert string to int: 8
result2 = "5" + str(3)      # Convert int to string: "53"
result3 = [1, 2, 3] * 2     # Multiply list by int: [1, 2, 3, 1, 2, 3]
```

### 4.3 Overflow Errors (Rare in Python)

```python
# Python handles large integers automatically
large_number = 10 ** 1000  # This works fine in Python
print(f"Large number has {len(str(large_number))} digits")

# However, floating-point overflow can occur
import math
try:
    result = math.exp(1000)  # May cause OverflowError
except OverflowError as e:
    print(f"Error: {e}")
```

### 4.4 Precision Issues with Floating Point

```python
# Floating-point precision issues
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (not exactly 0.3)

# Solutions:
from decimal import Decimal
decimal_result = Decimal('0.1') + Decimal('0.2')
print(decimal_result)  # 0.3 (exact)

# Or use round()
rounded_result = round(0.1 + 0.2, 1)
print(rounded_result)  # 0.3

# For comparisons, use math.isclose()
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

### 4.5 Modulus with Negative Numbers

```python
# Understanding modulus with negative numbers
print(7 % 3)    # 1
print(-7 % 3)   # 2 (not -1)
print(7 % -3)   # -2 (not 1)
print(-7 % -3)  # -1

# The result takes the sign of the divisor in Python
# For consistent positive results, use abs():
def positive_mod(a, b):
    return ((a % b) + b) % b

print(positive_mod(-7, 3))  # 2
```

### 4.6 Integer Division Confusion

```python
# Difference between / and //
print(7 / 2)   # 3.5 (true division)
print(7 // 2)  # 3 (floor division)

# With negative numbers, floor division can be surprising
print(-7 / 2)   # -3.5 (true division)
print(-7 // 2)  # -4 (floor division, not -3!)

# If you want truncation towards zero, use int():
print(int(-7 / 2))  # -3 (truncates towards zero)
```

### Best Practices to Avoid Errors

1. **Always validate input** before arithmetic operations
2. **Use try-except blocks** for operations that might fail
3. **Be aware of data types** and convert when necessary
4. **Use appropriate precision** for floating-point operations
5. **Test edge cases** like zero, negative numbers, and very large numbers
6. **Use math.isclose()** for floating-point comparisons
7. **Document assumptions** about input ranges and types
