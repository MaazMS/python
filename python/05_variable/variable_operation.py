#!/usr/bin/env python3
"""
Python Variable Operations - Comprehensive Demo
This script demonstrates all possible variable operations in Python
"""

print("=" * 60)
print("PYTHON VARIABLE OPERATIONS - COMPREHENSIVE DEMO")
print("=" * 60)

# ============================================================================
# 1. BASIC ASSIGNMENT
# ============================================================================
print("\n1. BASIC ASSIGNMENT")
print("-" * 30)

# Simple variable assignment
name = "Maaz"
age = 25
height = 5.9
is_student = True

print(f"Name: {name} (Type: {type(name).__name__})")
print(f"Age: {age} (Type: {type(age).__name__})")
print(f"Height: {height} (Type: {type(height).__name__})")
print(f"Is Student: {is_student} (Type: {type(is_student).__name__})")

# ============================================================================
# 2. MULTIPLE ASSIGNMENT
# ============================================================================
print("\n2. MULTIPLE ASSIGNMENT")
print("-" * 30)

# Assign values to multiple variables in one line
first_name, last_name, birth_year = "Maaz", "Shaikh", 1999
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Birth Year: {birth_year}")

# Assign same value to multiple variables
x = y = z = 100
print(f"x = {x}, y = {y}, z = {z}")

# ============================================================================
# 3. VARIABLE SWAPPING
# ============================================================================
print("\n3. VARIABLE SWAPPING")
print("-" * 30)

a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")

# Python way of swapping (tuple unpacking)
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# Multiple variable swapping
p, q, r = 1, 2, 3
print(f"Before: p = {p}, q = {q}, r = {r}")
p, q, r = r, p, q
print(f"After rotation: p = {p}, q = {q}, r = {r}")

# ============================================================================
# 4. ARITHMETIC OPERATIONS
# ============================================================================
print("\n4. ARITHMETIC OPERATIONS")
print("-" * 30)

num1 = 15
num2 = 4

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
power = num1 ** num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {floor_division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {power}")

# ============================================================================
# 5. STRING OPERATIONS
# ============================================================================
print("\n5. STRING OPERATIONS")
print("-" * 30)

greeting = "Hello"
target = "World"

# String concatenation
message = greeting + " " + target + "!"
print(f"Concatenation: {message}")

# String repetition
repeated = greeting * 3
print(f"Repetition: {repeated}")

# String formatting
formatted = f"{greeting}, {target}!"
print(f"F-string: {formatted}")

# String methods
upper_greeting = greeting.upper()
lower_target = target.lower()
print(f"Upper: {upper_greeting}, Lower: {lower_target}")

# ============================================================================
# 6. AUGMENTED ASSIGNMENT OPERATIONS
# ============================================================================
print("\n6. AUGMENTED ASSIGNMENT OPERATIONS")
print("-" * 30)

# Numeric augmented assignment
counter = 10
print(f"Initial counter: {counter}")

counter += 5    # counter = counter + 5
print(f"After += 5: {counter}")

counter -= 3    # counter = counter - 3
print(f"After -= 3: {counter}")

counter *= 2    # counter = counter * 2
print(f"After *= 2: {counter}")

counter //= 4   # counter = counter // 4
print(f"After //= 4: {counter}")

# String augmented assignment
text = "Python"
print(f"Initial text: {text}")
text += " Programming"
print(f"After += ' Programming': {text}")

# List augmented assignment
numbers = [1, 2, 3]
print(f"Initial list: {numbers}")
numbers += [4, 5]
print(f"After += [4, 5]: {numbers}")

# ============================================================================
# 7. TYPE CONVERSION OPERATIONS
# ============================================================================
print("\n7. TYPE CONVERSION OPERATIONS")
print("-" * 30)

# String to numeric conversions
str_number = "42"
str_float = "3.14"
str_bool = "True"

int_from_str = int(str_number)
float_from_str = float(str_float)
bool_from_str = bool(str_bool)

print(f"String '{str_number}' to int: {int_from_str}")
print(f"String '{str_float}' to float: {float_from_str}")
print(f"String '{str_bool}' to bool: {bool_from_str}")

# Numeric to string conversions
number = 123
float_num = 45.67

str_from_int = str(number)
str_from_float = str(float_num)

print(f"Int {number} to string: '{str_from_int}'")
print(f"Float {float_num} to string: '{str_from_float}'")

# ============================================================================
# 8. COLLECTION OPERATIONS
# ============================================================================
print("\n8. COLLECTION OPERATIONS")
print("-" * 30)

# List operations
fruits = ["apple", "banana", "orange"]
print(f"Original list: {fruits}")

fruits.append("grape")
print(f"After append: {fruits}")

fruits.extend(["mango", "kiwi"])
print(f"After extend: {fruits}")

# Dictionary operations
person = {"name": "Maaz", "age": 25}
print(f"Original dict: {person}")

person["city"] = "Mumbai"
person.update({"profession": "Developer"})
print(f"After updates: {person}")

# Tuple operations (immutable)
coordinates = (10, 20)
print(f"Tuple: {coordinates}")
x_coord, y_coord = coordinates  # Tuple unpacking
print(f"Unpacked: x = {x_coord}, y = {y_coord}")

# ============================================================================
# 9. VARIABLE INFORMATION OPERATIONS
# ============================================================================
print("\n9. VARIABLE INFORMATION OPERATIONS")
print("-" * 30)

sample_var = "Hello World"
sample_list = [1, 2, 3, 4, 5]

# Get variable type
print(f"Type of '{sample_var}': {type(sample_var)}")
print(f"Type of {sample_list}: {type(sample_list)}")

# Check variable type
print(f"Is '{sample_var}' a string? {isinstance(sample_var, str)}")
print(f"Is {sample_list} a list? {isinstance(sample_list, list)}")

# Get variable length
print(f"Length of '{sample_var}': {len(sample_var)}")
print(f"Length of {sample_list}: {len(sample_list)}")

# Get variable ID (memory address)
print(f"ID of sample_var: {id(sample_var)}")
print(f"ID of sample_list: {id(sample_list)}")

# ============================================================================
# 10. GLOBAL AND LOCAL VARIABLE OPERATIONS
# ============================================================================
print("\n10. GLOBAL AND LOCAL VARIABLE OPERATIONS")
print("-" * 30)

# Global variable
global_counter = 0

def demonstrate_local_variables():
    """Demonstrate local variable operations"""
    local_var = "I am local"
    print(f"Local variable: {local_var}")
    
    # Access global variable
    print(f"Global counter (read): {global_counter}")

def demonstrate_global_modification():
    """Demonstrate global variable modification"""
    global global_counter
    global_counter += 1
    print(f"Global counter (modified): {global_counter}")

def demonstrate_variable_scope():
    """Demonstrate variable scope operations"""
    local_name = "Local Maaz"
    
    # Show local variables
    local_vars = locals()
    print(f"Local variables: {list(local_vars.keys())}")
    
    return local_name

# Call functions to demonstrate operations
demonstrate_local_variables()
demonstrate_global_modification()
returned_value = demonstrate_variable_scope()
print(f"Returned value: {returned_value}")

# ============================================================================
# 11. ADVANCED VARIABLE OPERATIONS
# ============================================================================
print("\n11. ADVANCED VARIABLE OPERATIONS")
print("-" * 30)

# Variable copying vs referencing
original_list = [1, 2, 3]
reference_list = original_list      # Reference (same object)
copied_list = original_list.copy()  # Copy (different object)

print(f"Original: {original_list}")
print(f"Reference: {reference_list}")
print(f"Copy: {copied_list}")

original_list.append(4)
print(f"After modifying original:")
print(f"Original: {original_list}")
print(f"Reference: {reference_list}")  # Changed (same object)
print(f"Copy: {copied_list}")          # Unchanged (different object)

# Variable deletion
temp_var = "Temporary"
print(f"Temp variable exists: {temp_var}")
del temp_var
# print(temp_var)  # This would cause NameError

# Dynamic variable creation
var_name = "dynamic_var"
var_value = "Dynamic Value"
globals()[var_name] = var_value
print(f"Dynamic variable {var_name}: {globals()[var_name]}")

# ============================================================================
# 12. VARIABLE COMPARISON OPERATIONS
# ============================================================================
print("\n12. VARIABLE COMPARISON OPERATIONS")
print("-" * 30)

val1 = 10
val2 = 20
val3 = 10

print(f"val1 = {val1}, val2 = {val2}, val3 = {val3}")
print(f"val1 == val3: {val1 == val3}")
print(f"val1 != val2: {val1 != val2}")
print(f"val1 < val2: {val1 < val2}")
print(f"val2 > val1: {val2 > val1}")
print(f"val1 <= val3: {val1 <= val3}")
print(f"val2 >= val3: {val2 >= val3}")

# Identity comparison
print(f"val1 is val3: {val1 is val3}")  # True for small integers
print(f"val1 is not val2: {val1 is not val2}")

# ============================================================================
# 13. CONDITIONAL VARIABLE OPERATIONS
# ============================================================================
print("\n13. CONDITIONAL VARIABLE OPERATIONS")
print("-" * 30)

# Conditional assignment
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(f"Score: {score}, Grade: {grade}")

# Default value assignment
user_input = None
default_name = user_input or "Anonymous"
print(f"Name: {default_name}")

# Walrus operator (Python 3.8+)
data = [1, 2, 3, 4, 5]
if (data_length := len(data)) > 3:
    print(f"Data has {data_length} items (more than 3)")

print("\n" + "=" * 60)
print("VARIABLE OPERATIONS DEMO COMPLETED")
print("=" * 60)


