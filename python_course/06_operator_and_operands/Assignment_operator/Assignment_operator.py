"""
Assignment Operators in Python - Comprehensive Examples
Based on Assignment_documentation.md

This program demonstrates:
1. Basic assignment operations
2. Working with different data types
3. Bitwise assignment operations
4. Multiple assignment and unpacking
5. Advanced assignment patterns
6. Common error handling
7. Practical real-world examples
"""

import copy
import operator

print("=" * 60)
print("ASSIGNMENT OPERATORS IN PYTHON - COMPREHENSIVE EXAMPLES")
print("=" * 60)

# ============================================================================
# 1. BASIC ASSIGNMENT OPERATIONS
# ============================================================================
print("\n1. BASIC ASSIGNMENT OPERATIONS")
print("-" * 40)

# Simple assignment
x = 10
print(f"Simple assignment: x = {x}")

# Arithmetic assignment operators
print(f"\nStarting with x = {x}")

x += 5    # x = x + 5
print(f"After x += 5: x = {x}")

x -= 3    # x = x - 3
print(f"After x -= 3: x = {x}")

x *= 2    # x = x * 2
print(f"After x *= 2: x = {x}")

x /= 4    # x = x / 4
print(f"After x /= 4: x = {x}")

x //= 2   # x = x // 2
print(f"After x //= 2: x = {x}")

x %= 3    # x = x % 3
print(f"After x %= 3: x = {x}")

x = 3     # Reset for exponentiation
x **= 2   # x = x ** 2
print(f"After x = 3, x **= 2: x = {x}")

# ============================================================================
# 2. WORKING WITH DIFFERENT DATA TYPES
# ============================================================================
print("\n2. WORKING WITH DIFFERENT DATA TYPES")
print("-" * 40)

# String operations
text = "Hello"
print(f"Initial string: '{text}'")
text += " World"
print(f"After += ' World': '{text}'")
text *= 2
print(f"After *= 2: '{text}'")

# List operations
numbers = [1, 2, 3]
print(f"\nInitial list: {numbers}")
numbers += [4, 5]
print(f"After += [4, 5]: {numbers}")
numbers *= 2
print(f"After *= 2: {numbers}")

# Dictionary operations (Python 3.9+)
data = {'a': 1, 'b': 2}
print(f"\nInitial dict: {data}")
try:
    data |= {'c': 3, 'd': 4}  # Union operator for dicts
    print(f"After |= {{'c': 3, 'd': 4}}: {data}")
except TypeError:
    # For older Python versions
    data.update({'c': 3, 'd': 4})
    print(f"After .update({{'c': 3, 'd': 4}}): {data}")

# Set operations
set1 = {1, 2, 3}
print(f"\nInitial set: {set1}")
set1 |= {4, 5}  # Union assignment
print(f"After |= {{4, 5}}: {set1}")
set1 &= {1, 2, 3, 4}  # Intersection assignment
print(f"After &= {{1, 2, 3, 4}}: {set1}")

# ============================================================================
# 3. BITWISE ASSIGNMENT OPERATIONS
# ============================================================================
print("\n3. BITWISE ASSIGNMENT OPERATIONS")
print("-" * 40)

# Bitwise operations with binary representation
x = 12  # Binary: 1100
print(f"Initial: x = {x} (binary: {bin(x)})")

x &= 10  # Binary: 1010, Result: 1000 = 8
print(f"After x &= 10: x = {x} (binary: {bin(x)})")

x |= 5   # Binary: 0101, Result: 1101 = 13
print(f"After x |= 5: x = {x} (binary: {bin(x)})")

x ^= 3   # Binary: 0011, Result: 1110 = 14
print(f"After x ^= 3: x = {x} (binary: {bin(x)})")

x >>= 2  # Right shift by 2: 0011 = 3
print(f"After x >>= 2: x = {x} (binary: {bin(x)})")

x <<= 1  # Left shift by 1: 0110 = 6
print(f"After x <<= 1: x = {x} (binary: {bin(x)})")

# ============================================================================
# 4. MULTIPLE ASSIGNMENT AND UNPACKING
# ============================================================================
print("\n4. MULTIPLE ASSIGNMENT AND UNPACKING")
print("-" * 40)

# Multiple assignment (tuple unpacking)
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Swapping variables
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Chain assignment
x = y = z = 10
print(f"Chain assignment: x={x}, y={y}, z={z}")

# Unpacking with starred expressions
numbers = [1, 2, 3, 4, 5, 6]
first, *middle, last = numbers
print(f"Unpacking: first={first}, middle={middle}, last={last}")

# Dictionary unpacking
defaults = {'timeout': 30, 'retries': 3}
config = {'host': 'localhost', **defaults, 'port': 8080}
print(f"Dict unpacking: {config}")

# ============================================================================
# 5. ADVANCED ASSIGNMENT PATTERNS
# ============================================================================
print("\n5. ADVANCED ASSIGNMENT PATTERNS")
print("-" * 40)

# Conditional assignment (ternary operator)
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"Score: {score}, Grade: {grade}")

# Default value assignment
name = None
name = name or "Anonymous"
print(f"Default assignment: name = '{name}'")

# Walrus operator (Python 3.8+)
data_list = [1, 2, 3, 4, 5]
try:
    if (n := len(data_list)) > 3:
        print(f"Walrus operator: List has {n} elements (more than 3)")
except SyntaxError:
    # For Python < 3.8
    n = len(data_list)
    if n > 3:
        print(f"List has {n} elements (more than 3)")

# Nested unpacking
coordinates = [(1, 2), (3, 4), (5, 6)]
print("Nested unpacking:")
for i, (x, y) in enumerate(coordinates):
    print(f"  Point {i+1}: x={x}, y={y}")

# ============================================================================
# 6. CUSTOM ASSIGNMENT METHODS
# ============================================================================
print("\n6. CUSTOM ASSIGNMENT METHODS")
print("-" * 40)

class Counter:
    def __init__(self, value=0):
        self.value = value
    
    def __iadd__(self, other):
        """Implements += operator"""
        self.value += other
        return self
    
    def __imul__(self, other):
        """Implements *= operator"""
        self.value *= other
        return self
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"Counter({self.value})"

# Using custom augmented assignment
counter = Counter(5)
print(f"Initial counter: {counter}")

counter += 3
print(f"After counter += 3: {counter}")

counter *= 2
print(f"After counter *= 2: {counter}")

# ============================================================================
# 7. COMMON ERROR HANDLING EXAMPLES
# ============================================================================
print("\n7. COMMON ERROR HANDLING EXAMPLES")
print("-" * 40)

# 7.1 Mutable Default Arguments
print("7.1 Mutable Default Arguments:")

def append_wrong(item, target_list=[]):
    """WRONG: Mutable default argument"""
    target_list.append(item)
    return target_list

def append_correct(item, target_list=None):
    """CORRECT: Use None and create new list"""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

# Demonstrate the problem
list1 = append_wrong(1)
list2 = append_wrong(2)
print(f"Wrong approach - list1: {list1}, list2: {list2}")  # Both have [1, 2]!

# Demonstrate the solution
list3 = append_correct(1)
list4 = append_correct(2)
print(f"Correct approach - list3: {list3}, list4: {list4}")

# 7.2 Shallow vs Deep Copy Issues
print("\n7.2 Shallow vs Deep Copy Issues:")

original = [[1, 2], [3, 4]]
shallow_copy = original.copy()
deep_copy = copy.deepcopy(original)

# Modify nested list
original[0][0] = 99

print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")  # Also affected!
print(f"Deep copy: {deep_copy}")        # Not affected

# 7.3 Augmented Assignment Behavior
print("\n7.3 Augmented Assignment vs Regular Assignment:")

# With lists (mutable)
a = [1, 2, 3]
b = a
print(f"Before: a={a}, b={b}")

a += [4, 5]  # Modifies existing list
print(f"After a += [4, 5]: a={a}, b={b}")  # b is affected

# Reset and try regular assignment
a = [1, 2, 3]
b = a
a = a + [4, 5]  # Creates new list
print(f"After a = a + [4, 5]: a={a}, b={b}")  # b not affected

# 7.4 Variable Scope Issues
print("\n7.4 Variable Scope Issues:")

global_counter = 0

def increment_wrong():
    """This will cause UnboundLocalError"""
    try:
        global_counter = global_counter + 1  # Error!
    except UnboundLocalError as e:
        print(f"Error caught: {e}")

def increment_correct():
    """Correct way using global keyword"""
    global global_counter
    global_counter += 1

print(f"Initial global_counter: {global_counter}")
increment_wrong()  # Shows error
increment_correct()
print(f"After correct increment: {global_counter}")

# ============================================================================
# 8. PRACTICAL REAL-WORLD EXAMPLES
# ============================================================================
print("\n8. PRACTICAL REAL-WORLD EXAMPLES")
print("-" * 40)

# Example 1: Shopping Cart
print("8.1 Shopping Cart Example:")
cart = {}
cart['apples'] = cart.get('apples', 0) + 5
cart['bananas'] = cart.get('bananas', 0) + 3
cart['oranges'] = cart.get('oranges', 0) + 2

print(f"Shopping cart: {cart}")

# Add more items
cart['apples'] += 2
cart.setdefault('grapes', 0)
cart['grapes'] += 4

print(f"Updated cart: {cart}")

# Example 2: Score Accumulator
print("\n8.2 Score Accumulator:")
scores = {'Alice': 0, 'Bob': 0, 'Charlie': 0}
rounds = [
    {'Alice': 10, 'Bob': 8, 'Charlie': 12},
    {'Alice': 15, 'Bob': 11, 'Charlie': 9},
    {'Alice': 12, 'Bob': 14, 'Charlie': 16}
]

for round_num, round_scores in enumerate(rounds, 1):
    print(f"Round {round_num} scores: {round_scores}")
    for player, score in round_scores.items():
        scores[player] += score

print(f"Final scores: {scores}")
winner = max(scores, key=scores.get)
print(f"Winner: {winner} with {scores[winner]} points!")

# Example 3: Configuration Management
print("\n8.3 Configuration Management:")
default_config = {
    'debug': False,
    'timeout': 30,
    'retries': 3,
    'host': 'localhost'
}

user_config = {
    'debug': True,
    'timeout': 60,
    'port': 8080
}

# Merge configurations
final_config = default_config.copy()
final_config.update(user_config)

print(f"Default config: {default_config}")
print(f"User config: {user_config}")
print(f"Final config: {final_config}")

# Example 4: Text Processing
print("\n8.4 Text Processing:")
text = "Hello World"
text = text.lower()
text = text.replace(' ', '_')
text += "_processed"

print(f"Processed text: '{text}'")

# Using augmented assignment for efficiency
words = []
for word in ["Python", "is", "awesome"]:
    words.append(word.upper())

sentence = ""
for word in words:
    sentence += word + " "
sentence = sentence.strip()

print(f"Built sentence: '{sentence}'")

print("\n" + "=" * 60)
print("ASSIGNMENT OPERATORS PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)