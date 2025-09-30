"""
Comparison Operators in Python - Comprehensive Examples
Based on Comparison_documentation.md

This program demonstrates:
1. Basic comparison operations
2. Working with different data types
3. Identity vs Equality comparisons
4. Membership operations
5. Chained comparisons
6. Built-in comparison functions
7. Custom comparison methods
8. Common error handling
9. Practical real-world examples
"""

import math
from decimal import Decimal
from functools import cmp_to_key

print("=" * 60)
print("COMPARISON OPERATORS IN PYTHON - COMPREHENSIVE EXAMPLES")
print("=" * 60)

# ============================================================================
# 1. BASIC COMPARISON OPERATIONS
# ============================================================================
print("\n1. BASIC COMPARISON OPERATIONS")
print("-" * 40)

# Numeric comparisons
a = 10
b = 5

print(f"Given: a = {a}, b = {b}")
print(f"a > b: {a > b}")    # True
print(f"a < b: {a < b}")    # False
print(f"a == b: {a == b}")  # False
print(f"a != b: {a != b}")  # True
print(f"a >= b: {a >= b}")  # True
print(f"a <= b: {a <= b}")  # False

# String comparisons (lexicographic order)
str1 = "apple"
str2 = "banana"
str3 = "Apple"

print(f"\nString Comparisons:")
print(f"'{str1}' < '{str2}': {str1 < str2}")  # True
print(f"'{str1}' > '{str2}': {str1 > str2}")  # False
print(f"'{str1}' == '{str3}': {str1 == str3}")  # False (case sensitive)
print(f"'{str1}'.upper() == '{str3}'.upper(): {str1.upper() == str3.upper()}")  # True

# ============================================================================
# 2. WORKING WITH DIFFERENT DATA TYPES
# ============================================================================
print("\n2. WORKING WITH DIFFERENT DATA TYPES")
print("-" * 40)

# Comparing different numeric types
int_val = 10
float_val = 10.0
print(f"Integer vs Float:")
print(f"int {int_val} == float {float_val}: {int_val == float_val}")  # True
print(f"Type of int_val: {type(int_val).__name__}")
print(f"Type of float_val: {type(float_val).__name__}")

# Boolean comparisons
print(f"\nBoolean Comparisons:")
print(f"True == 1: {True == 1}")    # True
print(f"False == 0: {False == 0}")  # True
print(f"True > False: {True > False}")  # True
print(f"True + True: {True + True}")  # 2

# List comparisons (element by element)
list1 = [1, 2, 3]
list2 = [1, 2, 4]
list3 = [1, 2, 3]
list4 = [1, 2]

print(f"\nList Comparisons:")
print(f"{list1} == {list3}: {list1 == list3}")  # True
print(f"{list1} == {list2}: {list1 == list2}")  # False
print(f"{list1} < {list2}: {list1 < list2}")    # True (3 < 4)
print(f"{list1} > {list4}: {list1 > list4}")    # True (longer list)

# Tuple comparisons
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)

print(f"\nTuple Comparisons:")
print(f"{tuple1} == {tuple2}: {tuple1 == tuple2}")  # True
print(f"{tuple1} < {tuple3}: {tuple1 < tuple3}")    # True

# ============================================================================
# 3. IDENTITY VS EQUALITY COMPARISONS
# ============================================================================
print("\n3. IDENTITY VS EQUALITY COMPARISONS")
print("-" * 40)

# Identity comparison with 'is'
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"Lists: a = {a}, b = {b}")
print(f"a == b: {a == b}")      # True (same values)
print(f"a is b: {a is b}")      # False (different objects)
print(f"a is c: {a is c}")      # True (same object)

# None comparison
value = None
print(f"\nNone Comparison:")
print(f"value is None: {value is None}")      # Correct way
print(f"value == None: {value == None}")      # Works but not recommended

# ============================================================================
# 4. MEMBERSHIP OPERATIONS
# ============================================================================
print("\n4. MEMBERSHIP OPERATIONS")
print("-" * 40)

# List membership
fruits = ['apple', 'banana', 'orange']
print(f"Fruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")      # True
print(f"'grape' in fruits: {'grape' in fruits}")      # False
print(f"'grape' not in fruits: {'grape' not in fruits}")  # True

# String membership
text = "Hello World"
print(f"\nString membership in '{text}':")
print(f"'Hello' in text: {'Hello' in text}")        # True
print(f"'hello' in text: {'hello' in text}")        # False (case sensitive)
print(f"'World' in text: {'World' in text}")        # True

# Dictionary membership (checks keys by default)
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"\nDictionary membership:")
print(f"'name' in person: {'name' in person}")          # True
print(f"'Alice' in person.values(): {'Alice' in person.values()}")  # True

# ============================================================================
# 5. CHAINED COMPARISONS
# ============================================================================
print("\n5. CHAINED COMPARISONS")
print("-" * 40)

# Chained comparisons
x = 5
print(f"x = {x}")
print(f"1 < x < 10: {1 < x < 10}")           # True
print(f"10 < x < 20: {10 < x < 20}")         # False
print(f"1 <= x <= 5: {1 <= x <= 5}")        # True

# More complex chaining
a, b, c = 2, 5, 8
print(f"\na = {a}, b = {b}, c = {c}")
print(f"a < b < c: {a < b < c}")             # True
print(f"a < b > c: {a < b > c}")             # False (5 > 8 is False)

# Age range checking example
age = 25
print(f"\nAge validation (age = {age}):")
print(f"18 <= age <= 65: {18 <= age <= 65}")  # True (working age)

# ============================================================================
# 6. BUILT-IN COMPARISON FUNCTIONS
# ============================================================================
print("\n6. BUILT-IN COMPARISON FUNCTIONS")
print("-" * 40)

# max() and min() functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Numbers: {numbers}")
print(f"max(numbers): {max(numbers)}")       # 9
print(f"min(numbers): {min(numbers)}")       # 1

# With strings
words = ['apple', 'banana', 'cherry', 'date']
print(f"\nWords: {words}")
print(f"max(words): {max(words)}")           # 'date' (lexicographic)
print(f"min(words): {min(words)}")           # 'apple'

# Custom key function
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('Diana', 95)]
print(f"\nStudents: {students}")
best_student = max(students, key=lambda x: x[1])
print(f"Best student: {best_student}")       # ('Diana', 95)

# Sorting with comparison
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by grade (desc): {sorted_students}")

# ============================================================================
# 7. COMMON ERROR HANDLING EXAMPLES
# ============================================================================
print("\n7. COMMON ERROR HANDLING EXAMPLES")
print("-" * 40)

# 7.1 Floating Point Precision Issues
print("7.1 Floating Point Precision Issues:")
a = 0.1 + 0.2
b = 0.3

print(f"a = 0.1 + 0.2 = {a}")
print(f"b = 0.3 = {b}")
print(f"a == b: {a == b}")  # False! Due to floating point precision
print(f"math.isclose(a, b): {math.isclose(a, b)}")  # True

# 7.2 Type Comparison Issues
print("\n7.2 Type Comparison Issues:")
try:
    result = "5" > 3  # TypeError in Python 3
    print(result)
except TypeError as e:
    print(f"Error comparing string and int: {e}")
    # Correct approaches:
    print(f"int('5') > 3: {int('5') > 3}")  # True
    print(f"'5' > str(3): {'5' > str(3)}")  # True

# 7.3 Case Sensitivity Issues
print("\n7.3 Case Sensitivity Issues:")
name1 = "Alice"
name2 = "alice"

print(f"'{name1}' == '{name2}': {name1 == name2}")  # False
print(f"Case-insensitive: {name1.lower() == name2.lower()}")  # True

# ============================================================================
# 8. PRACTICAL REAL-WORLD EXAMPLES
# ============================================================================
print("\n8. PRACTICAL REAL-WORLD EXAMPLES")
print("-" * 40)

# Example 1: Grade Classification
print("8.1 Grade Classification:")
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

test_scores = [95, 87, 72, 58, 91]
print(f"Test scores: {test_scores}")
for score in test_scores:
    grade = classify_grade(score)
    print(f"  Score {score}: Grade {grade}")

# Example 2: Password Strength Checker
print("\n8.2 Password Strength Checker:")
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    
    if score >= 4:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

passwords = ["password", "Password1", "P@ssw0rd!", "abc"]
print("Password strength analysis:")
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"  '{pwd}': {strength}")

# Example 3: Data Validation
print("\n8.3 Data Validation:")
def validate_email(email):
    return '@' in email and email.count('@') == 1 and len(email) > 5

emails = ["test@email.com", "invalid-email", "user@domain.org", "@invalid"]
print("Email validation:")
for email in emails:
    is_valid = validate_email(email)
    print(f"  '{email}': {'Valid' if is_valid else 'Invalid'}")

print("\n" + "=" * 60)
print("COMPARISON OPERATORS PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)
