#!/usr/bin/env python3
"""
Numeric Methods Program - Comprehensive demonstration of Python numeric data types and methods
Author: Python Learning Repository
Description: This program demonstrates various numeric methods, operations, and error handling
"""

import math
import sys
from decimal import Decimal

def demonstrate_builtin_functions():
    """Demonstrate built-in functions for numeric operations"""
    print("="*60)
    print("BUILT-IN NUMERIC FUNCTIONS")
    print("="*60)
    
    # Sample data
    numbers = [1, 2, 3, 4, 5, -10, 25]
    float_num = 3.7
    negative = -15
    
    print(f"Sample numbers: {numbers}")
    print(f"Float number: {float_num}")
    print(f"Negative number: {negative}")
    print()
    
    # Absolute value
    abs_value = abs(negative)
    abs_float = abs(-3.7)
    print(f"abs({negative}) = {abs_value}")
    print(f"abs(-3.7) = {abs_float}")
    
    # Min and max
    minimum = min(numbers)
    maximum = max(numbers)
    print(f"min({numbers}) = {minimum}")
    print(f"max({numbers}) = {maximum}")
    
    # Sum
    total = sum(numbers)
    print(f"sum({numbers}) = {total}")
    
    # Round
    rounded = round(float_num)
    rounded_precision = round(3.14159, 2)
    rounded_negative = round(-2.675, 2)
    print(f"round({float_num}) = {rounded}")
    print(f"round(3.14159, 2) = {rounded_precision}")
    print(f"round(-2.675, 2) = {rounded_negative}")
    
    # Divmod (quotient and remainder)
    quotient, remainder = divmod(17, 5)
    print(f"divmod(17, 5) = ({quotient}, {remainder})")
    
    # Power
    power_result = pow(2, 3)
    power_with_mod = pow(2, 3, 5)  # (2^3) % 5
    print(f"pow(2, 3) = {power_result}")
    print(f"pow(2, 3, 5) = {power_with_mod}")
    
    print()

def demonstrate_mathematical_functions():
    """Demonstrate mathematical functions from math module"""
    print("="*60)
    print("MATHEMATICAL FUNCTIONS (math module)")
    print("="*60)
    
    # Mathematical constants
    print(f"math.pi = {math.pi}")
    print(f"math.e = {math.e}")
    print(f"math.tau = {math.tau}")
    print()
    
    # Power and logarithm functions
    num = 16
    print(f"Working with number: {num}")
    print(f"math.sqrt({num}) = {math.sqrt(num)}")
    print(f"math.log({num}) = {math.log(num):.4f}")
    print(f"math.log10({num}) = {math.log10(num):.4f}")
    print(f"math.log2({num}) = {math.log2(num):.4f}")
    print(f"math.pow(2, 3) = {math.pow(2, 3)}")
    print()
    
    # Trigonometric functions
    angle = math.pi / 4  # 45 degrees in radians
    print(f"Trigonometric functions (angle = π/4):")
    print(f"math.sin({angle:.4f}) = {math.sin(angle):.4f}")
    print(f"math.cos({angle:.4f}) = {math.cos(angle):.4f}")
    print(f"math.tan({angle:.4f}) = {math.tan(angle):.4f}")
    print()
    
    # Hyperbolic functions
    print(f"Hyperbolic functions:")
    print(f"math.sinh(1) = {math.sinh(1):.4f}")
    print(f"math.cosh(1) = {math.cosh(1):.4f}")
    print(f"math.tanh(1) = {math.tanh(1):.4f}")
    print()
    
    # Ceiling and floor
    test_float = 3.7
    print(f"Ceiling and floor functions:")
    print(f"math.ceil({test_float}) = {math.ceil(test_float)}")
    print(f"math.floor({test_float}) = {math.floor(test_float)}")
    print(f"math.trunc({test_float}) = {math.trunc(test_float)}")
    print()
    
    # Factorial and combinations
    print(f"Factorial and combinations:")
    print(f"math.factorial(5) = {math.factorial(5)}")
    print(f"math.comb(5, 2) = {math.comb(5, 2)}")
    print(f"math.perm(5, 2) = {math.perm(5, 2)}")
    print()

def demonstrate_complex_methods():
    """Demonstrate complex number specific methods"""
    print("="*60)
    print("COMPLEX NUMBER METHODS")
    print("="*60)
    
    # Complex number creation
    z1 = 3 + 4j
    z2 = 2 - 5j
    z3 = complex(1, 2)
    
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")
    print(f"z3 = {z3}")
    print()
    
    # Complex number properties
    print("Complex number properties:")
    print(f"z1.real = {z1.real}")
    print(f"z1.imag = {z1.imag}")
    print(f"z1.conjugate() = {z1.conjugate()}")
    print(f"abs(z1) = {abs(z1):.4f}")
    print()
    
    # Complex arithmetic
    print("Complex arithmetic:")
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 - z2 = {z1 - z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1 / z2 = {z1 / z2}")
    print(f"z1 ** 2 = {z1 ** 2}")
    print()

def demonstrate_precision_issues():
    """Demonstrate floating point precision issues and solutions"""
    print("="*60)
    print("PRECISION ISSUES AND SOLUTIONS")
    print("="*60)
    
    # Floating point precision issue
    result = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result}")
    print(f"0.1 + 0.2 == 0.3: {result == 0.3}")
    print()
    
    # Solution using decimal module
    print("Using decimal module for precision:")
    decimal_result = Decimal('0.1') + Decimal('0.2')
    print(f"Decimal('0.1') + Decimal('0.2') = {decimal_result}")
    print(f"Decimal result == 0.3: {decimal_result == Decimal('0.3')}")
    print()
    
    # Alternative: using round for comparison
    print("Using round for comparison:")
    rounded_result = round(result, 1)
    print(f"round(0.1 + 0.2, 1) = {rounded_result}")
    print(f"round(0.1 + 0.2, 1) == 0.3: {rounded_result == 0.3}")
    print()
    
    # System float info
    print("System float information:")
    print(f"sys.float_info.max = {sys.float_info.max}")
    print(f"sys.float_info.min = {sys.float_info.min}")
    print(f"sys.float_info.epsilon = {sys.float_info.epsilon}")
    print()

def demonstrate_error_handling():
    """Demonstrate common numeric errors and how to handle them"""
    print("="*60)
    print("ERROR HANDLING")
    print("="*60)
    
    # Division by zero
    print("1. Division by Zero:")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"   Error: {e}")
    
    try:
        result = 10 % 0
    except ZeroDivisionError as e:
        print(f"   Error: {e}")
    print()
    
    # Type conversion errors
    print("2. Type Conversion Errors:")
    invalid_strings = ["123abc", "3.14.15", "3+4k", "hello"]
    
    for invalid_str in invalid_strings:
        try:
            result = int(invalid_str)
            print(f"   int('{invalid_str}') = {result}")
        except ValueError as e:
            print(f"   int('{invalid_str}') -> Error: {e}")
    print()
    
    # Complex number comparison
    print("3. Complex Number Comparison:")
    try:
        result = (3 + 4j) > (1 + 2j)
    except TypeError as e:
        print(f"   Error: {e}")
    print()
    
    # Overflow handling
    print("4. Overflow Handling:")
    try:
        large_number = 1.8e308
        overflow = large_number * 10
        print(f"   Large number * 10 = {overflow}")
    except OverflowError as e:
        print(f"   Overflow error: {e}")
    print()
    
    # Special values
    print("5. Special Float Values:")
    inf_pos = float('inf')
    inf_neg = float('-inf')
    nan_val = float('nan')
    
    print(f"   Positive infinity: {inf_pos}")
    print(f"   Negative infinity: {inf_neg}")
    print(f"   Not a number: {nan_val}")
    print(f"   math.isinf(inf_pos): {math.isinf(inf_pos)}")
    print(f"   math.isnan(nan_val): {math.isnan(nan_val)}")
    print(f"   math.isfinite(42.0): {math.isfinite(42.0)}")
    print()

def demonstrate_practical_examples():
    """Demonstrate practical examples using numeric methods"""
    print("="*60)
    print("PRACTICAL EXAMPLES")
    print("="*60)
    
    # Example 1: Calculate compound interest
    print("1. Compound Interest Calculator:")
    principal = 1000
    rate = 0.05  # 5%
    time = 5
    n = 12  # monthly compounding
    
    amount = principal * (1 + rate/n) ** (n * time)
    print(f"   Principal: ${principal}")
    print(f"   Rate: {rate*100}%")
    print(f"   Time: {time} years")
    print(f"   Compounding: {n} times per year")
    print(f"   Final amount: ${amount:.2f}")
    print()
    
    # Example 2: Distance between two points
    print("2. Distance Between Two Points:")
    x1, y1 = 1, 2
    x2, y2 = 4, 6
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"   Point 1: ({x1}, {y1})")
    print(f"   Point 2: ({x2}, {y2})")
    print(f"   Distance: {distance:.4f}")
    print()
    
    # Example 3: Temperature conversion
    print("3. Temperature Conversion:")
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    
    print(f"   {celsius}°C = {fahrenheit}°F = {kelvin}K")
    print()
    
    # Example 4: Quadratic formula
    print("4. Quadratic Formula (ax² + bx + c = 0):")
    a, b, c = 1, -5, 6  # x² - 5x + 6 = 0
    
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"   Equation: {a}x² + {b}x + {c} = 0")
        print(f"   Solutions: x1 = {x1}, x2 = {x2}")
    else:
        print(f"   Complex solutions (discriminant = {discriminant})")
    print()

def main():
    """Main function to run all demonstrations"""
    print("PYTHON NUMERIC METHODS DEMONSTRATION")
    print("="*60)
    print("This program demonstrates various numeric methods and operations in Python")
    print()
    
    # Run all demonstrations
    demonstrate_builtin_functions()
    demonstrate_mathematical_functions()
    demonstrate_complex_methods()
    demonstrate_precision_issues()
    demonstrate_error_handling()
    demonstrate_practical_examples()
    
    print("="*60)
    print("PROGRAM COMPLETED SUCCESSFULLY")
    print("="*60)

if __name__ == "__main__":
    main()
