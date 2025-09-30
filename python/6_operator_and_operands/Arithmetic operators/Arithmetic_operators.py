"""
Arithmetic Operators in Python - Comprehensive Examples
Based on Arithmetic_documentation.md

This program demonstrates:
1. Basic arithmetic operations
2. Working with different data types
3. Built-in arithmetic functions
4. Math module functions
5. Operator module usage
6. Common error handling
"""

import math
import operator

print("=" * 60)
print("ARITHMETIC OPERATORS IN PYTHON - COMPREHENSIVE EXAMPLES")
print("=" * 60)

# ============================================================================
# 1. BASIC ARITHMETIC OPERATIONS
# ============================================================================
print("\n1. BASIC ARITHMETIC OPERATIONS")
print("-" * 40)

# Using more meaningful examples
a = 15
b = 4

print(f"Given: a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division (float): {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# ============================================================================
# 2. WORKING WITH DIFFERENT DATA TYPES
# ============================================================================
print("\n2. WORKING WITH DIFFERENT DATA TYPES")
print("-" * 40)

# Integer and Float operations
int_val = 10
float_val = 3.5

print(f"Integer: {int_val}, Float: {float_val}")
print(f"int + float = {int_val + float_val} (result type: {type(int_val + float_val).__name__})")
print(f"int * float = {int_val * float_val} (result type: {type(int_val * float_val).__name__})")
print(f"int // float = {int_val // float_val} (result type: {type(int_val // float_val).__name__})")

# Complex number arithmetic
complex1 = 3 + 4j
complex2 = 1 + 2j
complex_sum = complex1 + complex2

print(f"\nComplex Numbers:")
print(f"({complex1}) + ({complex2}) = {complex_sum}")
print(f"({complex1}) * ({complex2}) = {complex1 * complex2}")

# ============================================================================
# 3. BUILT-IN ARITHMETIC FUNCTIONS
# ============================================================================
print("\n3. BUILT-IN ARITHMETIC FUNCTIONS")
print("-" * 40)

# abs() - Absolute value
print(f"abs(-15) = {abs(-15)}")
print(f"abs(-3.14) = {abs(-3.14)}")
print(f"abs(3+4j) = {abs(3+4j)} (magnitude)")

# pow() - Power function
print(f"pow(2, 3) = {pow(2, 3)}")
print(f"pow(2, 3, 5) = {pow(2, 3, 5)} (2^3 % 5)")

# divmod() - Division and modulus
quotient, remainder = divmod(17, 5)
print(f"divmod(17, 5) = ({quotient}, {remainder})")

# round() - Rounding numbers
print(f"round(3.14159, 2) = {round(3.14159, 2)}")
print(f"round(2.5) = {round(2.5)} (banker's rounding)")
print(f"round(3.5) = {round(3.5)}")

# min(), max(), sum()
numbers = [1, 5, 3, 9, 2, 7]
print(f"Numbers: {numbers}")
print(f"min(numbers) = {min(numbers)}")
print(f"max(numbers) = {max(numbers)}")
print(f"sum(numbers) = {sum(numbers)}")
print(f"sum(numbers, 10) = {sum(numbers, 10)} (with start value)")

# ============================================================================
# 4. MATH MODULE FUNCTIONS
# ============================================================================
print("\n4. MATH MODULE FUNCTIONS")
print("-" * 40)

# Mathematical functions
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.ceil(3.2) = {math.ceil(3.2)}")
print(f"math.floor(3.8) = {math.floor(3.8)}")
print(f"math.factorial(5) = {math.factorial(5)}")
print(f"math.gcd(48, 18) = {math.gcd(48, 18)}")

# Check if lcm is available (Python 3.9+)
if hasattr(math, 'lcm'):
    print(f"math.lcm(4, 6) = {math.lcm(4, 6)}")

# Trigonometric functions
print(f"math.sin(π/2) = {math.sin(math.pi/2):.1f}")
print(f"math.cos(0) = {math.cos(0):.1f}")
print(f"math.tan(π/4) = {math.tan(math.pi/4):.1f}")

# Logarithmic functions
print(f"math.log(10) = {math.log(10):.3f} (natural log)")
print(f"math.log10(100) = {math.log10(100)}")
print(f"math.log(8, 2) = {math.log(8, 2)} (log base 2)")

# ============================================================================
# 5. OPERATOR MODULE USAGE
# ============================================================================
print("\n5. OPERATOR MODULE USAGE")
print("-" * 40)

x, y = 12, 5
print(f"Using operator module with x = {x}, y = {y}:")
print(f"operator.add(x, y) = {operator.add(x, y)}")
print(f"operator.sub(x, y) = {operator.sub(x, y)}")
print(f"operator.mul(x, y) = {operator.mul(x, y)}")
print(f"operator.truediv(x, y) = {operator.truediv(x, y)}")
print(f"operator.floordiv(x, y) = {operator.floordiv(x, y)}")
print(f"operator.mod(x, y) = {operator.mod(x, y)}")
print(f"operator.pow(x, y) = {operator.pow(x, y)}")

# ============================================================================
# 6. COMMON ERROR HANDLING EXAMPLES
# ============================================================================
print("\n6. COMMON ERROR HANDLING EXAMPLES")
print("-" * 40)

# Division by Zero
print("6.1 Division by Zero:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error caught: {e}")

try:
    result = 10 % 0
except ZeroDivisionError as e:
    print(f"Error caught: {e}")

# Type Errors
print("\n6.2 Type Errors:")
try:
    result = "5" + 3  # Can't add string and integer
except TypeError as e:
    print(f"Error caught: {e}")
    print(f"Correct approach: int('5') + 3 = {int('5') + 3}")

# Floating-point precision issues
print("\n6.3 Floating-point Precision:")
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result} (not exactly 0.3)")
print(f"Rounded: {round(0.1 + 0.2, 1)}")
print(f"Using math.isclose(): {math.isclose(0.1 + 0.2, 0.3)}")

# Modulus with negative numbers
print("\n6.4 Modulus with Negative Numbers:")
print(f"7 % 3 = {7 % 3}")
print(f"-7 % 3 = {-7 % 3} (result takes sign of divisor)")
print(f"7 % -3 = {7 % -3}")
print(f"-7 % -3 = {-7 % -3}")

# Integer division behavior
print("\n6.5 Integer Division with Negative Numbers:")
print(f"7 / 2 = {7 / 2} (true division)")
print(f"7 // 2 = {7 // 2} (floor division)")
print(f"-7 / 2 = {-7 / 2} (true division)")
print(f"-7 // 2 = {-7 // 2} (floor division - floors towards negative infinity)")
print(f"int(-7 / 2) = {int(-7 / 2)} (truncates towards zero)")

# ============================================================================
# 7. PRACTICAL EXAMPLES
# ============================================================================
print("\n7. PRACTICAL EXAMPLES")
print("-" * 40)

# Calculate area and circumference of a circle
radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Circle with radius {radius}:")
print(f"Area = π × r² = {area:.2f}")
print(f"Circumference = 2πr = {circumference:.2f}")

# Calculate compound interest
principal = 1000
rate = 0.05  # 5%
time = 3
amount = principal * (1 + rate) ** time
compound_interest = amount - principal
print(f"\nCompound Interest Calculation:")
print(f"Principal: ${principal}")
print(f"Rate: {rate*100}% per year")
print(f"Time: {time} years")
print(f"Final Amount: ${amount:.2f}")
print(f"Compound Interest: ${compound_interest:.2f}")

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"\nTemperature Conversion:")
print(f"{celsius}°C = {fahrenheit}°F = {kelvin}K")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)