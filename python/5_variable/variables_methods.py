#!/usr/bin/env python3
"""
Python Variable Methods - Comprehensive Demo
This script demonstrates all possible methods that can be used with different variable types
"""

print("=" * 70)
print("PYTHON VARIABLE METHODS - COMPREHENSIVE DEMO")
print("=" * 70)

# ============================================================================
# 1. STRING VARIABLE METHODS
# ============================================================================
print("\n1. STRING VARIABLE METHODS")
print("-" * 40)

text = "Hello World Python Programming"
sample_text = "  python programming  "
mixed_case = "PyThOn PrOgRaMmInG"

print(f"Original text: '{text}'")
print(f"Sample text: '{sample_text}'")
print(f"Mixed case: '{mixed_case}'")

# Case conversion methods
print(f"\nCASE CONVERSION METHODS:")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"title(): '{text.title()}'")
print(f"swapcase(): '{mixed_case.swapcase()}'")
print(f"casefold(): '{mixed_case.casefold()}'")

# Whitespace methods
print(f"\nWHITESPACE METHODS:")
print(f"strip(): '{sample_text.strip()}'")
print(f"lstrip(): '{sample_text.lstrip()}'")
print(f"rstrip(): '{sample_text.rstrip()}'")
print(f"center(30): '{text.center(30, '*')}'")
print(f"ljust(20): '{text.ljust(20, '-')}'")
print(f"rjust(20): '{text.rjust(20, '-')}'")
print(f"zfill(10): '{'123'.zfill(10)}'")

# Search and check methods
print(f"\nSEARCH AND CHECK METHODS:")
print(f"find('World'): {text.find('World')}")
print(f"rfind('o'): {text.rfind('o')}")
print(f"index('Python'): {text.index('Python')}")
print(f"count('o'): {text.count('o')}")
print(f"startswith('Hello'): {text.startswith('Hello')}")
print(f"endswith('Programming'): {text.endswith('Programming')}")

# Boolean check methods
print(f"\nBOOLEAN CHECK METHODS:")
digit_text = "12345"
alpha_text = "Hello"
alnum_text = "Hello123"
print(f"'{digit_text}'.isdigit(): {digit_text.isdigit()}")
print(f"'{alpha_text}'.isalpha(): {alpha_text.isalpha()}")
print(f"'{alnum_text}'.isalnum(): {alnum_text.isalnum()}")
print(f"'{text}'.islower(): {text.islower()}")
print(f"'{text}'.isupper(): {text.isupper()}")
print(f"'{text}'.isspace(): {text.isspace()}")
print(f"'{text}'.istitle(): {text.istitle()}")

# String modification methods
print(f"\nSTRING MODIFICATION METHODS:")
print(f"replace('World', 'Universe'): '{text.replace('World', 'Universe')}'")
print(f"split(' '): {text.split(' ')}")
print(f"rsplit(' ', 2): {text.rsplit(' ', 2)}")
multiline = "Line1\nLine2\nLine3"
print(f"splitlines(): {multiline.splitlines()}")
join_list = ["Python", "is", "awesome"]
print(f"' '.join({join_list}): '{' '.join(join_list)}'")

# Encoding methods
print(f"\nENCODING METHODS:")
print(f"encode('utf-8'): {text.encode('utf-8')}")
encoded = text.encode('utf-8')
print(f"decode('utf-8'): {encoded.decode('utf-8')}")

# Format methods
print(f"\nFORMAT METHODS:")
template = "Hello {name}, you are {age} years old"
print(f"format(): '{template.format(name='Maaz', age=25)}'")
tab_text = "Hello\tWorld"
print(f"expandtabs(): {tab_text.expandtabs(8)}")

# ============================================================================
# 2. NUMERIC VARIABLE METHODS (int, float)
# ============================================================================
print("\n" + "=" * 70)
print("2. NUMERIC VARIABLE METHODS")
print("-" * 40)

integer_num = 42
float_num = 3.14159
negative_num = -17

print(f"Integer: {integer_num}")
print(f"Float: {float_num}")
print(f"Negative: {negative_num}")

# Built-in functions for numbers
print(f"\nBUILT-IN FUNCTIONS FOR NUMBERS:")
numbers = [10, 5, 8, 15, 3]
print(f"abs({negative_num}): {abs(negative_num)}")
print(f"round({float_num}, 2): {round(float_num, 2)}")
print(f"max({numbers}): {max(numbers)}")
print(f"min({numbers}): {min(numbers)}")
print(f"sum({numbers}): {sum(numbers)}")
print(f"pow(2, 3): {pow(2, 3)}")
print(f"divmod(17, 5): {divmod(17, 5)}")

# Integer specific methods
print(f"\nINTEGER SPECIFIC METHODS:")
binary_num = 0b1010  # 10 in binary
print(f"bit_length(): {integer_num.bit_length()}")
print(f"to_bytes(4, 'big'): {integer_num.to_bytes(4, 'big')}")
byte_data = b'\x00\x00\x00*'
print(f"from_bytes: {int.from_bytes(byte_data, 'big')}")

# Float specific methods
print(f"\nFLOAT SPECIFIC METHODS:")
print(f"is_integer(): {float_num.is_integer()}")
print(f"as_integer_ratio(): {float_num.as_integer_ratio()}")
print(f"hex(): {float_num.hex()}")
special_float = 3.0
print(f"{special_float}.is_integer(): {special_float.is_integer()}")

# Math module functions (if available)
try:
    import math
    print(f"\nMATH MODULE FUNCTIONS:")
    print(f"math.ceil({float_num}): {math.ceil(float_num)}")
    print(f"math.floor({float_num}): {math.floor(float_num)}")
    print(f"math.sqrt(16): {math.sqrt(16)}")
    print(f"math.factorial(5): {math.factorial(5)}")
except ImportError:
    print("\nMath module not available")

# ============================================================================
# 3. LIST VARIABLE METHODS
# ============================================================================
print("\n" + "=" * 70)
print("3. LIST VARIABLE METHODS")
print("-" * 40)

fruits = ["apple", "banana", "orange"]
numbers_list = [3, 1, 4, 1, 5, 9, 2, 6]
mixed_list = [1, "hello", 3.14, True]

print(f"Original fruits: {fruits}")
print(f"Numbers list: {numbers_list}")
print(f"Mixed list: {mixed_list}")

# Modification methods
print(f"\nMODIFICATION METHODS:")
test_list = fruits.copy()
print(f"append('grape'): {test_list.append('grape')} -> {test_list}")

test_list = fruits.copy()
test_list.extend(['mango', 'kiwi'])
print(f"extend(['mango', 'kiwi']): {test_list}")

test_list = fruits.copy()
test_list.insert(1, 'strawberry')
print(f"insert(1, 'strawberry'): {test_list}")

test_list = fruits.copy()
removed = test_list.remove('banana')
print(f"remove('banana'): {test_list}")

test_list = fruits.copy()
popped = test_list.pop()
print(f"pop(): removed '{popped}' -> {test_list}")

test_list = fruits.copy()
popped = test_list.pop(0)
print(f"pop(0): removed '{popped}' -> {test_list}")

# Search and count methods
print(f"\nSEARCH AND COUNT METHODS:")
print(f"index('banana'): {fruits.index('banana')}")
print(f"count('apple'): {fruits.count('apple')}")
print(f"count(1) in numbers: {numbers_list.count(1)}")

# Sorting methods
print(f"\nSORTING METHODS:")
test_list = numbers_list.copy()
test_list.sort()
print(f"sort(): {test_list}")

test_list = numbers_list.copy()
test_list.sort(reverse=True)
print(f"sort(reverse=True): {test_list}")

test_list = fruits.copy()
test_list.reverse()
print(f"reverse(): {test_list}")

# Copy and clear methods
print(f"\nCOPY AND CLEAR METHODS:")
copied_list = fruits.copy()
print(f"copy(): {copied_list}")

test_list = fruits.copy()
test_list.clear()
print(f"clear(): {test_list}")

# ============================================================================
# 4. DICTIONARY VARIABLE METHODS
# ============================================================================
print("\n" + "=" * 70)
print("4. DICTIONARY VARIABLE METHODS")
print("-" * 40)

person = {"name": "Maaz", "age": 25, "city": "Mumbai"}
scores = {"math": 95, "english": 87, "science": 92}

print(f"Person dict: {person}")
print(f"Scores dict: {scores}")

# Access methods
print(f"\nACCESS METHODS:")
print(f"get('name'): {person.get('name')}")
print(f"get('country', 'India'): {person.get('country', 'India')}")
print(f"keys(): {list(person.keys())}")
print(f"values(): {list(person.values())}")
print(f"items(): {list(person.items())}")

# Modification methods
print(f"\nMODIFICATION METHODS:")
test_dict = person.copy()
test_dict.update({"profession": "Developer", "age": 26})
print(f"update(): {test_dict}")

test_dict = person.copy()
popped_value = test_dict.pop('age')
print(f"pop('age'): removed {popped_value} -> {test_dict}")

test_dict = person.copy()
popped_item = test_dict.popitem()
print(f"popitem(): removed {popped_item} -> {test_dict}")

test_dict = person.copy()
default_value = test_dict.setdefault('country', 'India')
print(f"setdefault('country', 'India'): {default_value} -> {test_dict}")

# Copy and clear methods
print(f"\nCOPY AND CLEAR METHODS:")
copied_dict = person.copy()
print(f"copy(): {copied_dict}")

test_dict = person.copy()
test_dict.clear()
print(f"clear(): {test_dict}")

# Dictionary creation methods
print(f"\nDICTIONARY CREATION METHODS:")
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)
print(f"fromkeys({keys}, 0): {default_dict}")

# ============================================================================
# 5. SET VARIABLE METHODS
# ============================================================================
print("\n" + "=" * 70)
print("5. SET VARIABLE METHODS")
print("-" * 40)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
fruits_set = {"apple", "banana", "orange"}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Fruits set: {fruits_set}")

# Modification methods
print(f"\nMODIFICATION METHODS:")
test_set = set1.copy()
test_set.add(6)
print(f"add(6): {test_set}")

test_set = set1.copy()
test_set.update([6, 7, 8])
print(f"update([6, 7, 8]): {test_set}")

test_set = set1.copy()
test_set.remove(3)
print(f"remove(3): {test_set}")

test_set = set1.copy()
test_set.discard(10)  # Won't raise error if element doesn't exist
print(f"discard(10): {test_set}")

test_set = set1.copy()
popped = test_set.pop()
print(f"pop(): removed {popped} -> {test_set}")

# Set operations
print(f"\nSET OPERATIONS:")
print(f"union(set2): {set1.union(set2)}")
print(f"intersection(set2): {set1.intersection(set2)}")
print(f"difference(set2): {set1.difference(set2)}")
print(f"symmetric_difference(set2): {set1.symmetric_difference(set2)}")

# Boolean set methods
print(f"\nBOOLEAN SET METHODS:")
subset = {1, 2}
superset = {1, 2, 3, 4, 5, 6}
print(f"{subset}.issubset({set1}): {subset.issubset(set1)}")
print(f"{superset}.issuperset({set1}): {superset.issuperset(set1)}")
print(f"{set1}.isdisjoint({set2}): {set1.isdisjoint(set2)}")

# Copy and clear methods
print(f"\nCOPY AND CLEAR METHODS:")
copied_set = set1.copy()
print(f"copy(): {copied_set}")

test_set = set1.copy()
test_set.clear()
print(f"clear(): {test_set}")

# ============================================================================
# 6. TUPLE VARIABLE METHODS (Limited - Immutable)
# ============================================================================
print("\n" + "=" * 70)
print("6. TUPLE VARIABLE METHODS")
print("-" * 40)

coordinates = (10, 20, 30, 20, 40)
mixed_tuple = (1, "hello", 3.14, True, "hello")

print(f"Coordinates: {coordinates}")
print(f"Mixed tuple: {mixed_tuple}")

# Tuple methods (limited since immutable)
print(f"\nTUPLE METHODS:")
print(f"count(20): {coordinates.count(20)}")
print(f"index(30): {coordinates.index(30)}")
print(f"count('hello'): {mixed_tuple.count('hello')}")

# Tuple operations
print(f"\nTUPLE OPERATIONS:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(f"Concatenation: {tuple1 + tuple2}")
print(f"Repetition: {tuple1 * 3}")

# ============================================================================
# 7. BOOLEAN VARIABLE METHODS
# ============================================================================
print("\n" + "=" * 70)
print("7. BOOLEAN VARIABLE METHODS")
print("-" * 40)

bool_true = True
bool_false = False

print(f"Boolean True: {bool_true}")
print(f"Boolean False: {bool_false}")

# Boolean operations
print(f"\nBOOLEAN OPERATIONS:")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")

# Boolean methods (inherited from int)
print(f"\nBOOLEAN METHODS (inherited from int):")
print(f"bit_length(): {bool_true.bit_length()}")
print(f"conjugate(): {bool_true.conjugate()}")
print(f"to_bytes(1, 'big'): {bool_true.to_bytes(1, 'big')}")

# ============================================================================
# 8. BUILT-IN FUNCTIONS FOR ALL VARIABLE TYPES
# ============================================================================
print("\n" + "=" * 70)
print("8. BUILT-IN FUNCTIONS FOR ALL VARIABLE TYPES")
print("-" * 40)

sample_vars = [
    42,                    # int
    3.14,                  # float
    "Hello",               # str
    [1, 2, 3],            # list
    {"key": "value"},      # dict
    {1, 2, 3},            # set
    (1, 2, 3),            # tuple
    True                   # bool
]

print("UNIVERSAL BUILT-IN FUNCTIONS:")
for var in sample_vars:
    print(f"\nVariable: {var} ({type(var).__name__})")
    print(f"  type(): {type(var)}")
    print(f"  id(): {id(var)}")
    # Hash (only for hashable types)
    try:
        print(f"  hash(): {hash(var)}")
    except TypeError:
        print(f"  hash(): unhashable")
    
    # Length for collections
    if hasattr(var, '__len__'):
        print(f"  len(): {len(var)}")
    
    # String representation
    print(f"  str(): '{str(var)}'")
    print(f"  repr(): {repr(var)}")
    
    # Boolean conversion
    print(f"  bool(): {bool(var)}")

# Type checking functions
print(f"\nTYPE CHECKING:")
test_value = "Hello"
print(f"isinstance('{test_value}', str): {isinstance(test_value, str)}")
print(f"isinstance('{test_value}', (str, int)): {isinstance(test_value, (str, int))}")
print(f"issubclass(bool, int): {issubclass(bool, int)}")

# Attribute checking
print(f"\nATTRIBUTE CHECKING:")
test_obj = "Hello"
print(f"hasattr('{test_obj}', 'upper'): {hasattr(test_obj, 'upper')}")
print(f"getattr('{test_obj}', 'upper', None): {getattr(test_obj, 'upper', None)}")
print(f"dir('{test_obj}') methods: {[m for m in dir(test_obj) if not m.startswith('_')]}")

# ============================================================================
# 9. ADVANCED VARIABLE METHODS AND FUNCTIONS
# ============================================================================
print("\n" + "=" * 70)
print("9. ADVANCED VARIABLE METHODS AND FUNCTIONS")
print("-" * 40)

# Variable introspection
print("VARIABLE INTROSPECTION:")
sample = [1, 2, 3]
print(f"vars() in local scope: {len(locals())} variables")
print(f"globals() keys: {len(globals())} global variables")

# Memory and performance
print(f"\nMEMORY AND PERFORMANCE:")
import sys
print(f"sys.getsizeof('Hello'): {sys.getsizeof('Hello')} bytes")
print(f"sys.getsizeof([1,2,3]): {sys.getsizeof([1,2,3])} bytes")
print(f"sys.getsizeof({{1,2,3}}): {sys.getsizeof({1,2,3})} bytes")

# Callable check
print(f"\nCALLABLE CHECK:")
print(f"callable(len): {callable(len)}")
print(f"callable('hello'): {callable('hello')}")
print(f"callable(lambda x: x): {callable(lambda x: x)}")

print("\n" + "=" * 70)
print("VARIABLE METHODS DEMO COMPLETED")
print("=" * 70)


