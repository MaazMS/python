"""
Logical Operators in Python - Comprehensive Examples
Based on Logical_documentation.md

This program demonstrates:
1. Basic logical operations with truth tables
2. Short-circuit evaluation
3. Truthiness and falsy values
4. Complex conditions and expressions
5. Built-in logical functions
6. Common error handling
7. Practical real-world examples
"""

print("=" * 60)
print("LOGICAL OPERATORS IN PYTHON - COMPREHENSIVE EXAMPLES")
print("=" * 60)

# ============================================================================
# 1. BASIC LOGICAL OPERATIONS - TRUTH TABLES
# ============================================================================
print("\n1. BASIC LOGICAL OPERATIONS - TRUTH TABLES")
print("-" * 40)

# AND operator truth table
print("AND Operator Truth Table:")
print("x     | y     | x and y")
print("------|-------|--------")
print(f"True  | True  | {True and True}")
print(f"True  | False | {True and False}")
print(f"False | True  | {False and True}")
print(f"False | False | {False and False}")

print("\nOR Operator Truth Table:")
print("x     | y     | x or y")
print("------|-------|-------")
print(f"True  | True  | {True or True}")
print(f"True  | False | {True or False}")
print(f"False | True  | {False or True}")
print(f"False | False | {False or False}")

print("\nNOT Operator Truth Table:")
print("x     | not x")
print("------|------")
print(f"True  | {not True}")
print(f"False | {not False}")

# Basic examples with variables
print("\n1.1 Basic Examples with Variables:")
a = True
b = False

print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
print(f"not b: {not b}")

# Combining operations
print(f"\nCombining operations:")
print(f"not a and b: {not a and b}")
print(f"not a or b: {not a or b}")
print(f"not (a and b): {not (a and b)}")
print(f"not (a or b): {not (a or b)}")

# ============================================================================
# 2. WORKING WITH EXPRESSIONS
# ============================================================================
print("\n2. WORKING WITH EXPRESSIONS")
print("-" * 40)

# Numeric comparisons with logical operators
x = 10
y = 5
z = 15

print(f"Given: x = {x}, y = {y}, z = {z}")
print(f"x > y and z > x: {x > y and z > x}")    # True and True = True
print(f"x > y and z < x: {x > y and z < x}")    # True and False = False
print(f"x < y or z > x: {x < y or z > x}")      # False or True = True
print(f"x < y or z < x: {x < y or z < x}")      # False or False = False

# Complex conditions
age = 25
has_license = True
has_insurance = False

print(f"\nComplex condition example:")
print(f"age = {age}, has_license = {has_license}, has_insurance = {has_insurance}")
can_drive = age >= 18 and has_license and has_insurance
print(f"Can drive (age >= 18 and has_license and has_insurance): {can_drive}")

can_apply = age >= 16 and (has_license or not has_insurance)
print(f"Can apply for license: {can_apply}")

# ============================================================================
# 3. SHORT-CIRCUIT EVALUATION
# ============================================================================
print("\n3. SHORT-CIRCUIT EVALUATION")
print("-" * 40)

def check_true():
    print("  check_true() called")
    return True

def check_false():
    print("  check_false() called")
    return False

print("3.1 AND Short-circuit (False and ...):")
result1 = check_false() and check_true()  # Only check_false() is called
print(f"Result: {result1}\n")

print("3.2 OR Short-circuit (True or ...):")
result2 = check_true() or check_false()   # Only check_true() is called
print(f"Result: {result2}\n")

print("3.3 Practical example - Avoiding division by zero:")
x = 10
y = 0
if y != 0 and x / y > 5:  # y != 0 prevents division by zero
    print("Division is greater than 5")
else:
    print("Cannot divide by zero or result <= 5")

# Another practical example
data = []
if data and len(data) > 0:  # data check prevents error on empty list
    print(f"First item: {data[0]}")
else:
    print("No data available")

# ============================================================================
# 4. TRUTHINESS AND FALSY VALUES
# ============================================================================
print("\n4. TRUTHINESS AND FALSY VALUES")
print("-" * 40)

# Falsy values in Python: False, 0, 0.0, '', [], {}, None
falsy_values = [False, 0, 0.0, '', [], {}, None]
truthy_values = [True, 1, 'hello', [1, 2], {'a': 1}, 'False']

print("4.1 Falsy values:")
for value in falsy_values:
    print(f"  {repr(value):12} -> {bool(value)}")

print("\n4.2 Truthy values:")
for value in truthy_values:
    print(f"  {repr(value):12} -> {bool(value)}")

# Practical use of truthiness
print("\n4.3 Practical truthiness examples:")
name = ""
age = 0
email = "user@example.com"

print(f"name = {repr(name)}, age = {age}, email = {repr(email)}")

# Using truthiness in conditions
if name and age and email:
    print("User data is complete")
else:
    print("User data is incomplete (some fields are empty/zero)")

# Better approach with explicit checks
if name != "" and age > 0 and email != "":
    print("User data is complete (explicit check)")
else:
    print("User data is incomplete (explicit check)")

# ============================================================================
# 5. LOGICAL OPERATORS RETURN ACTUAL VALUES
# ============================================================================
print("\n5. LOGICAL OPERATORS RETURN ACTUAL VALUES")
print("-" * 40)

print("5.1 AND operator returns:")
print(f"'hello' and 'world': {repr('hello' and 'world')}")  # 'world'
print(f"'hello' and '': {repr('hello' and '')}")            # ''
print(f"'' and 'world': {repr('' and 'world')}")            # ''

print("\n5.2 OR operator returns:")
print(f"'hello' or 'world': {repr('hello' or 'world')}")    # 'hello'
print(f"'' or 'world': {repr('' or 'world')}")              # 'world'
print(f"'' or None: {repr('' or None)}")                    # None

# Practical use for default values
def greet(name=None):
    display_name = name or "Guest"
    return f"Hello, {display_name}!"

print(f"\n5.3 Default value examples:")
print(greet("Alice"))  # Hello, Alice!
print(greet(""))       # Hello, Guest!
print(greet())         # Hello, Guest!

# ============================================================================
# 6. BUILT-IN LOGICAL FUNCTIONS
# ============================================================================
print("\n6. BUILT-IN LOGICAL FUNCTIONS")
print("-" * 40)

# all() function - Returns True if all elements are truthy
numbers = [1, 2, 3, 4, 5]
print(f"6.1 all() function:")
print(f"all({numbers}): {all(numbers)}")  # True

mixed = [1, 2, 0, 4, 5]
print(f"all({mixed}): {all(mixed)}")      # False (0 is falsy)

# any() function - Returns True if any element is truthy
print(f"\n6.2 any() function:")
print(f"any({mixed}): {any(mixed)}")      # True (1, 2, 4, 5 are truthy)

empty_list = []
print(f"all({empty_list}): {all(empty_list)}")  # True (vacuous truth)
print(f"any({empty_list}): {any(empty_list)}")  # False

# Practical examples
print(f"\n6.3 Practical examples:")
grades = [85, 90, 78, 92, 88]
passing_grades = [grade >= 60 for grade in grades]
print(f"Grades: {grades}")
print(f"All students passed: {all(passing_grades)}")  # True

attendance = [True, True, False, True, True]
print(f"Attendance: {attendance}")
print(f"Perfect attendance: {all(attendance)}")       # False
print(f"Any absence: {any(not day for day in attendance)}")  # True

# bool() function
print(f"\n6.4 bool() function examples:")
values = [0, 1, '', 'text', [], [1], {}, {'a': 1}, None]
for value in values:
    print(f"  bool({repr(value):12}): {bool(value)}")