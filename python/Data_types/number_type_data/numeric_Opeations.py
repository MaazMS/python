#!/usr/bin/env python3
"""
Numeric Operations Program - Comprehensive demonstration of Python numeric operations
Author: Python Learning Repository
Description: This program demonstrates all types of numeric operations in Python
"""

import math
import operator

def demonstrate_basic_arithmetic():
    """Demonstrate basic arithmetic operations"""
    print("="*60)
    print("BASIC ARITHMETIC OPERATIONS")
    print("="*60)
    
    # Integer operations
    a = 15
    b = 4
    print(f"Working with integers: a = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")
    print()
    
    # Float operations
    x = 12.5
    y = 3.2
    print(f"Working with floats: x = {x}, y = {y}")
    print(f"Addition: {x} + {y} = {x + y}")
    print(f"Subtraction: {x} - {y} = {x - y}")
    print(f"Multiplication: {x} * {y} = {x * y}")
    print(f"Division: {x} / {y} = {x / y}")
    print(f"Floor Division: {x} // {y} = {x // y}")
    print(f"Modulus: {x} % {y} = {x % y}")
    print(f"Exponentiation: {x} ** {y} = {x ** y}")
    print()
    
    # Negative numbers
    print("Operations with negative numbers:")
    neg_a = -10
    neg_b = -3
    print(f"(-10) + (-3) = {neg_a + neg_b}")
    print(f"(-10) - (-3) = {neg_a - neg_b}")
    print(f"(-10) * (-3) = {neg_a * neg_b}")
    print(f"(-10) / (-3) = {neg_a / neg_b}")
    print(f"(-10) // (-3) = {neg_a // neg_b}")
    print(f"(-10) % (-3) = {neg_a % neg_b}")
    print()

def demonstrate_mixed_type_operations():
    """Demonstrate operations between different numeric types"""
    print("="*60)
    print("MIXED TYPE OPERATIONS")
    print("="*60)
    
    # Integer and float operations
    int_num = 10
    float_num = 3.5
    print(f"Integer and Float operations:")
    print(f"int = {int_num}, float = {float_num}")
    print(f"{int_num} + {float_num} = {int_num + float_num} (type: {type(int_num + float_num)})")
    print(f"{int_num} * {float_num} = {int_num * float_num} (type: {type(int_num * float_num)})")
    print(f"{int_num} / {float_num} = {int_num / float_num} (type: {type(int_num / float_num)})")
    print()
    
    # Float and complex operations
    complex_num = 2 + 3j
    print(f"Float and Complex operations:")
    print(f"float = {float_num}, complex = {complex_num}")
    print(f"{float_num} + {complex_num} = {float_num + complex_num} (type: {type(float_num + complex_num)})")
    print(f"{float_num} * {complex_num} = {float_num * complex_num} (type: {type(float_num * complex_num)})")
    print()
    
    # Integer and complex operations
    print(f"Integer and Complex operations:")
    print(f"int = {int_num}, complex = {complex_num}")
    print(f"{int_num} + {complex_num} = {int_num + complex_num} (type: {type(int_num + complex_num)})")
    print(f"{int_num} * {complex_num} = {int_num * complex_num} (type: {type(int_num * complex_num)})")
    print()
    
    # Type hierarchy demonstration
    print("Type hierarchy in operations:")
    print("int + float → float")
    print("float + complex → complex")
    print("int + complex → complex")
    print()

def demonstrate_complex_operations():
    """Demonstrate complex number operations"""
    print("="*60)
    print("COMPLEX NUMBER OPERATIONS")
    print("="*60)
    
    # Complex number creation and operations
    z1 = 3 + 4j
    z2 = 1 + 2j
    z3 = 2 - 3j
    
    print(f"Working with complex numbers:")
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")
    print(f"z3 = {z3}")
    print()
    
    # Basic operations
    print("Basic complex operations:")
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 - z2 = {z1 - z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1 / z2 = {z1 / z2}")
    print(f"z1 ** 2 = {z1 ** 2}")
    print()
    
    # Complex conjugate and absolute value
    print("Complex number properties:")
    print(f"z1.conjugate() = {z1.conjugate()}")
    print(f"abs(z1) = {abs(z1)}")
    print(f"z1.real = {z1.real}")
    print(f"z1.imag = {z1.imag}")
    print()
    
    # Complex multiplication patterns
    print("Complex multiplication patterns:")
    print(f"z1 * z1.conjugate() = {z1 * z1.conjugate()}")
    print(f"(a + bj) * (a - bj) = a² + b² = {z1.real**2 + z1.imag**2}")
    print()

def demonstrate_comparison_operations():
    """Demonstrate comparison operations"""
    print("="*60)
    print("COMPARISON OPERATIONS")
    print("="*60)
    
    # Integer comparisons
    a = 10
    b = 15
    c = 10
    
    print(f"Integer comparisons (a={a}, b={b}, c={c}):")
    print(f"a == b: {a == b}")
    print(f"a == c: {a == c}")
    print(f"a != b: {a != b}")
    print(f"a < b: {a < b}")
    print(f"a > b: {a > b}")
    print(f"a <= c: {a <= c}")
    print(f"a >= c: {a >= c}")
    print()
    
    # Float comparisons
    x = 3.14
    y = 3.14159
    z = 3.14
    
    print(f"Float comparisons (x={x}, y={y}, z={z}):")
    print(f"x == y: {x == y}")
    print(f"x == z: {x == z}")
    print(f"x < y: {x < y}")
    print(f"x > y: {x > y}")
    print()
    
    # Mixed type comparisons
    print("Mixed type comparisons:")
    print(f"10 == 10.0: {10 == 10.0}")
    print(f"10 < 10.5: {10 < 10.5}")
    print(f"3 > 2.5: {3 > 2.5}")
    print()
    
    # Complex number comparisons (only == and != work)
    print("Complex number comparisons:")
    z1 = 3 + 4j
    z2 = 3 + 4j
    z3 = 2 + 5j
    
    print(f"z1 = {z1}, z2 = {z2}, z3 = {z3}")
    print(f"z1 == z2: {z1 == z2}")
    print(f"z1 != z3: {z1 != z3}")
    print("Note: <, >, <=, >= are not supported for complex numbers")
    print()

def demonstrate_bitwise_operations():
    """Demonstrate bitwise operations (integers only)"""
    print("="*60)
    print("BITWISE OPERATIONS (INTEGERS ONLY)")
    print("="*60)
    
    a = 12  # 1100 in binary
    b = 7   # 0111 in binary
    
    print(f"Working with integers: a = {a} (binary: {bin(a)}), b = {b} (binary: {bin(b)})")
    print()
    
    # Bitwise operations
    print("Bitwise operations:")
    print(f"a & b (AND): {a & b} (binary: {bin(a & b)})")
    print(f"a | b (OR): {a | b} (binary: {bin(a | b)})")
    print(f"a ^ b (XOR): {a ^ b} (binary: {bin(a ^ b)})")
    print(f"~a (NOT): {~a} (binary: {bin(~a)})")
    print(f"a << 2 (Left shift): {a << 2} (binary: {bin(a << 2)})")
    print(f"a >> 2 (Right shift): {a >> 2} (binary: {bin(a >> 2)})")
    print()
    
    # Practical examples
    print("Practical bitwise examples:")
    print(f"Check if number is even: {a} & 1 = {a & 1} ({'even' if (a & 1) == 0 else 'odd'})")
    print(f"Multiply by 2: {a} << 1 = {a << 1}")
    print(f"Divide by 2: {a} >> 1 = {a >> 1}")
    print(f"Toggle bit: {a} ^ 1 = {a ^ 1}")
    print()

def demonstrate_assignment_operations():
    """Demonstrate assignment operations"""
    print("="*60)
    print("ASSIGNMENT OPERATIONS")
    print("="*60)
    
    # Basic assignment
    x = 10
    print(f"Initial value: x = {x}")
    
    # Arithmetic assignment operators
    x += 5
    print(f"After x += 5: x = {x}")
    
    x -= 3
    print(f"After x -= 3: x = {x}")
    
    x *= 2
    print(f"After x *= 2: x = {x}")
    
    x /= 4
    print(f"After x /= 4: x = {x}")
    
    x //= 2
    print(f"After x //= 2: x = {x}")
    
    x %= 3
    print(f"After x %= 3: x = {x}")
    
    x **= 3
    print(f"After x **= 3: x = {x}")
    print()
    
    # Bitwise assignment operators
    y = 12
    print(f"Bitwise assignment operations (starting with y = {y}):")
    
    y &= 7
    print(f"After y &= 7: y = {y}")
    
    y |= 4
    print(f"After y |= 4: y = {y}")
    
    y ^= 2
    print(f"After y ^= 2: y = {y}")
    
    y <<= 1
    print(f"After y <<= 1: y = {y}")
    
    y >>= 2
    print(f"After y >>= 2: y = {y}")
    print()

def demonstrate_special_operations():
    """Demonstrate special numeric operations"""
    print("="*60)
    print("SPECIAL OPERATIONS")
    print("="*60)
    
    # Unary operations
    x = 5
    print(f"Unary operations (x = {x}):")
    print(f"+x = {+x}")
    print(f"-x = {-x}")
    print(f"abs(x) = {abs(x)}")
    print(f"abs(-x) = {abs(-x)}")
    print()
    
    # Divmod operation
    print("Divmod operation:")
    a, b = 17, 5
    quotient, remainder = divmod(a, b)
    print(f"divmod({a}, {b}) = ({quotient}, {remainder})")
    print(f"Verification: {quotient} * {b} + {remainder} = {quotient * b + remainder}")
    print()
    
    # Power with modulus
    print("Power with modulus:")
    base, exp, mod = 2, 10, 1000
    result = pow(base, exp, mod)
    print(f"pow({base}, {exp}, {mod}) = {result}")
    print(f"Equivalent to: ({base}^{exp}) % {mod} = {result}")
    print()
    
    # Round operations
    print("Rounding operations:")
    values = [3.2, 3.7, -2.3, -2.8, 2.5, 3.5]
    for val in values:
        print(f"round({val}) = {round(val)}")
    print()
    
    # Math ceiling and floor
    print("Ceiling and floor operations:")
    for val in [3.2, 3.7, -2.3, -2.8]:
        print(f"math.ceil({val}) = {math.ceil(val)}, math.floor({val}) = {math.floor(val)}")
    print()

def demonstrate_operator_precedence():
    """Demonstrate operator precedence"""
    print("="*60)
    print("OPERATOR PRECEDENCE")
    print("="*60)
    
    # Precedence examples
    print("Operator precedence examples:")
    
    # Arithmetic precedence
    result1 = 2 + 3 * 4
    result2 = (2 + 3) * 4
    print(f"2 + 3 * 4 = {result1}")
    print(f"(2 + 3) * 4 = {result2}")
    
    result3 = 2 ** 3 ** 2
    result4 = (2 ** 3) ** 2
    print(f"2 ** 3 ** 2 = {result3} (right-to-left)")
    print(f"(2 ** 3) ** 2 = {result4}")
    
    # Mixed operations
    result5 = 10 + 2 * 3 - 4 / 2
    print(f"10 + 2 * 3 - 4 / 2 = {result5}")
    
    # Comparison and logical
    result6 = 5 > 3 and 2 < 4
    result7 = 5 > 3 or 2 > 4
    print(f"5 > 3 and 2 < 4 = {result6}")
    print(f"5 > 3 or 2 > 4 = {result7}")
    print()
    
    # Precedence order
    print("Operator precedence order (highest to lowest):")
    print("1. Parentheses ()")
    print("2. Exponentiation **")
    print("3. Unary +x, -x, ~x")
    print("4. Multiplication *, Division /, Floor division //, Modulus %")
    print("5. Addition +, Subtraction -")
    print("6. Bitwise shifts <<, >>")
    print("7. Bitwise AND &")
    print("8. Bitwise XOR ^")
    print("9. Bitwise OR |")
    print("10. Comparisons ==, !=, <, >, <=, >=")
    print("11. Boolean NOT not")
    print("12. Boolean AND and")
    print("13. Boolean OR or")
    print()

def demonstrate_operator_module():
    """Demonstrate operator module functions"""
    print("="*60)
    print("OPERATOR MODULE FUNCTIONS")
    print("="*60)
    
    a = 10
    b = 3
    
    print(f"Using operator module functions (a = {a}, b = {b}):")
    print(f"operator.add(a, b) = {operator.add(a, b)}")
    print(f"operator.sub(a, b) = {operator.sub(a, b)}")
    print(f"operator.mul(a, b) = {operator.mul(a, b)}")
    print(f"operator.truediv(a, b) = {operator.truediv(a, b)}")
    print(f"operator.floordiv(a, b) = {operator.floordiv(a, b)}")
    print(f"operator.mod(a, b) = {operator.mod(a, b)}")
    print(f"operator.pow(a, b) = {operator.pow(a, b)}")
    print()
    
    print("Comparison operators:")
    print(f"operator.eq(a, b) = {operator.eq(a, b)}")
    print(f"operator.ne(a, b) = {operator.ne(a, b)}")
    print(f"operator.lt(a, b) = {operator.lt(a, b)}")
    print(f"operator.le(a, b) = {operator.le(a, b)}")
    print(f"operator.gt(a, b) = {operator.gt(a, b)}")
    print(f"operator.ge(a, b) = {operator.ge(a, b)}")
    print()
    
    print("Bitwise operators:")
    print(f"operator.and_(a, b) = {operator.and_(a, b)}")
    print(f"operator.or_(a, b) = {operator.or_(a, b)}")
    print(f"operator.xor(a, b) = {operator.xor(a, b)}")
    print(f"operator.lshift(a, 2) = {operator.lshift(a, 2)}")
    print(f"operator.rshift(a, 2) = {operator.rshift(a, 2)}")
    print()

def demonstrate_practical_examples():
    """Demonstrate practical examples using numeric operations"""
    print("="*60)
    print("PRACTICAL EXAMPLES")
    print("="*60)
    
    # Example 1: Simple calculator
    print("1. Simple Calculator Function:")
    def calculate(a, b, operation):
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",
            '//': lambda x, y: x // y if y != 0 else "Error: Division by zero",
            '%': lambda x, y: x % y if y != 0 else "Error: Division by zero",
            '**': lambda x, y: x ** y
        }
        return operations.get(operation, lambda x, y: "Invalid operation")(a, b)
    
    test_cases = [
        (10, 3, '+'), (10, 3, '-'), (10, 3, '*'), (10, 3, '/'),
        (10, 3, '//'), (10, 3, '%'), (2, 3, '**')
    ]
    
    for a, b, op in test_cases:
        result = calculate(a, b, op)
        print(f"   {a} {op} {b} = {result}")
    print()
    
    # Example 2: Number base converter
    print("2. Number Base Converter:")
    def convert_base(number, base):
        if base == 2:
            return bin(number)
        elif base == 8:
            return oct(number)
        elif base == 16:
            return hex(number)
        else:
            return str(number)
    
    num = 255
    for base in [2, 8, 10, 16]:
        converted = convert_base(num, base)
        print(f"   {num} in base {base}: {converted}")
    print()
    
    # Example 3: Factorial using operations
    print("3. Factorial Calculator:")
    def factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    for i in range(1, 6):
        print(f"   {i}! = {factorial(i)}")
    print()
    
    # Example 4: Prime number check
    print("4. Prime Number Checker:")
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for num in test_numbers:
        prime_status = "Prime" if is_prime(num) else "Not Prime"
        print(f"   {num}: {prime_status}")
    print()

def main():
    """Main function to run all demonstrations"""
    print("PYTHON NUMERIC OPERATIONS DEMONSTRATION")
    print("="*60)
    print("This program demonstrates various numeric operations in Python")
    print()
    
    # Run all demonstrations
    demonstrate_basic_arithmetic()
    demonstrate_mixed_type_operations()
    demonstrate_complex_operations()
    demonstrate_comparison_operations()
    demonstrate_bitwise_operations()
    demonstrate_assignment_operations()
    demonstrate_special_operations()
    demonstrate_operator_precedence()
    demonstrate_operator_module()
    demonstrate_practical_examples()
    
    print("="*60)
    print("PROGRAM COMPLETED SUCCESSFULLY")
    print("="*60)

if __name__ == "__main__":
    main()
