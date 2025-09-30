# Assignment Operators in Python

## 1. Assignment Definition and Characteristics

Assignment operators are used to assign values to variables and perform operations simultaneously. They provide a shorthand way to modify variables by combining an arithmetic, bitwise, or logical operation with assignment.

### Characteristics

- **In-place Operations**: Modify the variable directly without creating a new object (when possible)
- **Shorthand Notation**: Combine operation and assignment in a single statement
- **Right-to-Left Associativity**: Assignment operations are evaluated from right to left
- **Return Value**: Assignment expressions return the assigned value
- **Mutable vs Immutable**: Behavior differs between mutable and immutable objects
- **Chaining Support**: Multiple assignments can be chained (e.g., `a = b = c = 5`)

## 2. Assignment Operations

| Operator | Description | Example | Equivalent to | Result |
|----------|-------------|---------|---------------|--------|
| = | Simple assignment | x = 5 | x = 5 | x becomes 5 |
| += | Addition assignment | x += 3 | x = x + 3 | Adds 3 to x |
| -= | Subtraction assignment | x -= 2 | x = x - 2 | Subtracts 2 from x |
| *= | Multiplication assignment | x *= 4 | x = x * 4 | Multiplies x by 4 |
| /= | Division assignment | x /= 2 | x = x / 2 | Divides x by 2 |
| //= | Floor division assignment | x //= 3 | x = x // 3 | Floor divides x by 3 |
| %= | Modulus assignment | x %= 3 | x = x % 3 | x becomes remainder |
| **= | Exponentiation assignment | x **= 2 | x = x ** 2 | x becomes x squared |
| &= | Bitwise AND assignment | x &= 3 | x = x & 3 | Bitwise AND with 3 |
| \|= | Bitwise OR assignment | x \|= 2 | x = x \| 2 | Bitwise OR with 2 |
| ^= | Bitwise XOR assignment | x ^= 1 | x = x ^ 1 | Bitwise XOR with 1 |
| >>= | Right shift assignment | x >>= 2 | x = x >> 2 | Right shift by 2 bits |
| <<= | Left shift assignment | x <<= 1 | x = x << 1 | Left shift by 1 bit |

### Detailed Examples

#### Basic Assignment Operations

```python
# Simple assignment
x = 10
print(f"x = {x}")  # 10

# Arithmetic assignment operators
x += 5    # x = x + 5
print(f"After x += 5: {x}")  # 15

x -= 3    # x = x - 3
print(f"After x -= 3: {x}")  # 12

x *= 2    # x = x * 2
print(f"After x *= 2: {x}")  # 24

x /= 4    # x = x / 4
print(f"After x /= 4: {x}")  # 6.0

x //= 2   # x = x // 2
print(f"After x //= 2: {x}")  # 3.0

x %= 2    # x = x % 2
print(f"After x %= 2: {x}")  # 1.0

x = 3
x **= 2   # x = x ** 2
print(f"After x **= 2: {x}")  # 9
```

#### Working with Different Data Types

```python
# String concatenation
text = "Hello"
text += " World"
print(text)  # "Hello World"

text *= 2
print(text)  # "Hello WorldHello World"

# List operations
numbers = [1, 2, 3]
numbers += [4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

numbers *= 2
print(numbers)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Dictionary update
data = {'a': 1, 'b': 2}
data |= {'c': 3, 'd': 4}  # Python 3.9+
print(data)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

#### Bitwise Assignment Operations

```python
# Bitwise operations with binary representation
x = 12  # Binary: 1100
print(f"Initial x = {x} (binary: {bin(x)})")

x &= 10  # Binary: 1010, Result: 1000 = 8
print(f"x &= 10: {x} (binary: {bin(x)})")

x |= 5   # Binary: 0101, Result: 1101 = 13
print(f"x |= 5: {x} (binary: {bin(x)})")

x ^= 3   # Binary: 0011, Result: 1110 = 14
print(f"x ^= 3: {x} (binary: {bin(x)})")

x >>= 2  # Right shift by 2: 0011 = 3
print(f"x >>= 2: {x} (binary: {bin(x)})")

x <<= 1  # Left shift by 1: 0110 = 6
print(f"x <<= 1: {x} (binary: {bin(x)})")
```

## 3. Assignment Methods

### Multiple Assignment

```python
# Multiple assignment (tuple unpacking)
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")  # a=1, b=2, c=3

# Swapping variables
a, b = b, a
print(f"After swap: a={a}, b={b}")  # a=2, b=1

# Chain assignment
x = y = z = 10
print(f"x={x}, y={y}, z={z}")  # x=10, y=10, z=10
```

### Augmented Assignment with Methods

```python
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

# Using custom augmented assignment
counter = Counter(5)
print(f"Initial: {counter}")  # 5

counter += 3
print(f"After += 3: {counter}")  # 8

counter *= 2
print(f"After *= 2: {counter}")  # 16
```

### Conditional Assignment

```python
# Walrus operator (Python 3.8+)
data = [1, 2, 3, 4, 5]
if (n := len(data)) > 3:
    print(f"List has {n} elements, which is more than 3")

# Ternary operator for conditional assignment
x = 10
result = "positive" if x > 0 else "non-positive"
print(result)  # positive

# Default value assignment
name = None
name = name or "Anonymous"
print(name)  # Anonymous
```

### Advanced Assignment Patterns

```python
# Unpacking with starred expressions
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"first={first}, middle={middle}, last={last}")
# first=1, middle=[2, 3, 4], last=5

# Dictionary unpacking
defaults = {'timeout': 30, 'retries': 3}
config = {'host': 'localhost', **defaults, 'port': 8080}
print(config)
# {'host': 'localhost', 'timeout': 30, 'retries': 3, 'port': 8080}

# Nested unpacking
data = [(1, 2), (3, 4), (5, 6)]
for (a, b) in data:
    print(f"a={a}, b={b}")
```

## 4. Common Errors in Assignment

### 4.1 Mutable Default Arguments

```python
# WRONG: Mutable default argument
def append_to_list(item, target_list=[]):
    target_list.append(item)
    return target_list

list1 = append_to_list(1)
list2 = append_to_list(2)
print(list1)  # [1, 2] - Unexpected!
print(list2)  # [1, 2] - Same list!

# CORRECT: Use None and create new list
def append_to_list_correct(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

list3 = append_to_list_correct(1)
list4 = append_to_list_correct(2)
print(list3)  # [1]
print(list4)  # [2]
```

### 4.2 Assignment vs Equality Confusion

```python
# WRONG: Using = instead of ==
x = 5
# if x = 10:  # SyntaxError: invalid syntax
#     print("x is 10")

# CORRECT: Use == for comparison
if x == 5:
    print("x is 5")  # This works

# Be careful with assignment in conditions (walrus operator)
data = [1, 2, 3]
if length := len(data):  # This assigns AND checks truthiness
    print(f"Length is {length}")  # Length is 3
```

### 4.3 Shallow vs Deep Copy Issues

```python
# Shallow copy problem
original = [[1, 2], [3, 4]]
copy = original
copy[0][0] = 99

print(original)  # [[99, 2], [3, 4]] - Original changed!
print(copy)      # [[99, 2], [3, 4]]

# Correct approaches:
import copy

# Shallow copy
shallow = original.copy()  # or list(original)
shallow[0] = [100, 200]  # This won't affect original's nested lists

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print(original)  # [[1, 2], [3, 4]] - Original unchanged
print(deep)      # [[999, 2], [3, 4]]
```

### 4.4 Augmented Assignment with Immutable Types

```python
# Understanding the difference
# With immutable types (int, str, tuple)
a = [1, 2, 3]
b = a
a += [4, 5]  # Modifies the existing list
print(b)     # [1, 2, 3, 4, 5] - b is affected

# vs
a = [1, 2, 3]
b = a
a = a + [4, 5]  # Creates a new list
print(b)        # [1, 2, 3] - b is not affected

# With tuples (immutable)
t1 = (1, 2, 3)
t2 = t1
t1 += (4, 5)  # Creates new tuple, reassigns t1
print(t1)     # (1, 2, 3, 4, 5)
print(t2)     # (1, 2, 3) - t2 unchanged
```

### 4.5 Variable Scope and Assignment

```python
# Global vs local variable confusion
counter = 0

def increment():
    # This creates a local variable, doesn't modify global
    counter = counter + 1  # UnboundLocalError!

# Correct approaches:
def increment_global():
    global counter
    counter += 1

def increment_return():
    return counter + 1

# Using nonlocal in nested functions
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x += 1
        return x
    
    return inner

func = outer()
print(func())  # 11
print(func())  # 12
```

### 4.6 Chained Assignment Pitfalls

```python
# Problem with mutable objects
a = b = []
a.append(1)
print(b)  # [1] - b is affected because both reference same list

# Correct approach
a, b = [], []
a.append(1)
print(b)  # [] - b is not affected

# Or use list() constructor
a = b = list()  # Still same problem
a = list()      # Create separate lists
b = list()
```

### Best Practices to Avoid Assignment Errors

1. **Use `is` for None comparisons**: `if x is None:` instead of `if x == None:`
2. **Avoid mutable default arguments**: Use `None` and create objects inside function
3. **Be explicit about copying**: Use `copy()` or `deepcopy()` when needed
4. **Understand augmented assignment**: Know when it modifies vs creates new objects
5. **Use proper variable scoping**: Declare `global` or `nonlocal` when needed
6. **Test assignment behavior**: Especially with mutable objects and references
7. **Use type hints**: Help catch assignment type mismatches early
8. **Prefer immutable types**: When possible, use tuples instead of lists for fixed data