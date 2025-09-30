# Range Type Data Documentation

## 1. Range Type Data Definition and Characteristics

### Definition

The `range` type in Python is an immutable sequence type that represents a sequence of numbers. It is commonly used for looping a specific number of times in for loops.

### Characteristics

- **Immutable**: Once created, range objects cannot be modified
- **Memory Efficient**: Range objects don't store all values in memory, they generate values on-demand
- **Lazy Evaluation**: Values are computed only when needed
- **Sequence Type**: Supports indexing, slicing, and iteration
- **Integer Only**: Can only represent sequences of integers
- **Step Support**: Supports custom step values (increment/decrement)

### Syntax

```python
range(stop)                    # range(5) -> 0, 1, 2, 3, 4
range(start, stop)             # range(1, 5) -> 1, 2, 3, 4
range(start, stop, step)       # range(1, 10, 2) -> 1, 3, 5, 7, 9
```

## 2. Range Type Data Creations

### Basic Range Creation

#### Single Parameter (stop)

```python
# Creates range from 0 to n-1
numbers = range(5)
print(list(numbers))  # Output: [0, 1, 2, 3, 4]

# Example usage in loop
for i in range(3):
    print(f"Iteration {i}")
```

#### Two Parameters (start, stop)

```python
# Creates range from start to stop-1
numbers = range(2, 8)
print(list(numbers))  # Output: [2, 3, 4, 5, 6, 7]

# Example with negative start
numbers = range(-3, 3)
print(list(numbers))  # Output: [-3, -2, -1, 0, 1, 2]
```

#### Three Parameters (start, stop, step)

```python
# Positive step
numbers = range(1, 10, 2)
print(list(numbers))  # Output: [1, 3, 5, 7, 9]

# Negative step (countdown)
numbers = range(10, 0, -2)
print(list(numbers))  # Output: [10, 8, 6, 4, 2]

# Decimal step is not allowed - use numpy.arange() instead
```

### Special Range Creations

#### Empty Range

```python
# When start >= stop (with positive step)
empty_range = range(5, 5)
print(list(empty_range))  # Output: []

# When start <= stop (with negative step)
empty_range = range(5, 10, -1)
print(list(empty_range))  # Output: []
```

#### Large Range

```python
# Memory efficient for large ranges
large_range = range(1000000)
print(len(large_range))  # Output: 1000000
# Only 48 bytes in memory regardless of size
```

## 3. Range Type Data Operations

### Indexing

```python
r = range(10, 20)
print(r[0])    # Output: 10 (first element)
print(r[-1])   # Output: 19 (last element)
print(r[3])    # Output: 13 (fourth element)
```

### Slicing

```python
r = range(0, 10)
print(r[2:5])     # Output: range(2, 5)
print(list(r[2:5]))  # Output: [2, 3, 4]
print(r[::2])     # Output: range(0, 10, 2)
print(list(r[::2]))  # Output: [0, 2, 4, 6, 8]
```

### Membership Testing

```python
r = range(1, 10, 2)
print(5 in r)     # Output: True
print(6 in r)     # Output: False
print(1 in r)     # Output: True
```

### Iteration

```python
# Using for loop
for num in range(3, 8):
    print(num)  # Output: 3, 4, 5, 6, 7

# Using while loop with range
r = range(5)
i = 0
while i < len(r):
    print(r[i])
    i += 1
```

### Concatenation and Repetition

```python
# Note: Direct concatenation not supported
r1 = range(3)
r2 = range(3, 6)
# r1 + r2  # This will raise TypeError

# Workaround using itertools
import itertools
combined = itertools.chain(r1, r2)
print(list(combined))  # Output: [0, 1, 2, 3, 4, 5]
```

## 4. Range Type Data Methods

### Built-in Methods

#### `count(value)`

```python
r = range(1, 10, 2)  # [1, 3, 5, 7, 9]
print(r.count(5))    # Output: 1
print(r.count(4))    # Output: 0 (4 is not in range)
```

#### `index(value)`

```python
r = range(10, 50, 5)  # [10, 15, 20, 25, 30, 35, 40, 45]
print(r.index(25))    # Output: 3 (index of 25)
print(r.index(30))    # Output: 4 (index of 30)
# print(r.index(12))  # ValueError: 12 is not in range
```

### Properties

#### `start`, `stop`, `step`

```python
r = range(2, 20, 3)
print(r.start)  # Output: 2
print(r.stop)   # Output: 20
print(r.step)   # Output: 3

# Default values
r2 = range(5)
print(r2.start)  # Output: 0
print(r2.stop)   # Output: 5
print(r2.step)   # Output: 1
```

### Utility Functions

#### `len()`

```python
r = range(1, 11)
print(len(r))  # Output: 10

r2 = range(5, 50, 5)
print(len(r2))  # Output: 9
```

#### `reversed()`

```python
r = range(1, 6)
print(list(reversed(r)))  # Output: [5, 4, 3, 2, 1]

# Equivalent to negative step
r2 = range(5, 0, -1)
print(list(r2))  # Output: [5, 4, 3, 2, 1]
```

#### `min()` and `max()`

```python
r = range(10, 100, 10)
print(min(r))  # Output: 10
print(max(r))  # Output: 90

# Empty range will raise ValueError
# print(min(range(0)))  # ValueError
```

## 5. Common Errors in Range Type Data

### Error 1: Expecting Float/Decimal Step

```python
# ❌ INCORRECT - Will raise TypeError
# r = range(0, 10, 0.5)  # TypeError: 'float' object cannot be interpreted as an integer

# ✅ CORRECT - Use numpy.arange() or list comprehension
import numpy as np
r = np.arange(0, 10, 0.5)
print(list(r))  # Output: [0.0, 0.5, 1.0, 1.5, ...]

# Alternative with list comprehension
r = [x * 0.5 for x in range(20)]
print(r)  # Output: [0.0, 0.5, 1.0, 1.5, ...]
```

### Error 2: Modifying Range Object

```python
# ❌ INCORRECT - Range objects are immutable
r = range(5)
# r[0] = 10  # TypeError: 'range' object does not support item assignment

# ✅ CORRECT - Convert to list first
r_list = list(range(5))
r_list[0] = 10
print(r_list)  # Output: [10, 1, 2, 3, 4]
```

### Error 3: Using range() with Non-Integer Arguments

```python
# ❌ INCORRECT
# r = range("5")  # TypeError: 'str' object cannot be interpreted as an integer
# r = range(5.0)  # TypeError: 'float' object cannot be interpreted as an integer

# ✅ CORRECT
r = range(int("5"))  # Convert string to int
r = range(int(5.0))  # Convert float to int
```

### Error 4: Infinite Loop with Wrong Step

```python
# ❌ INCORRECT - Will create empty range
r = range(10, 0, 1)  # Empty range because step is positive
print(list(r))  # Output: []

# ✅ CORRECT - Use negative step for countdown
r = range(10, 0, -1)
print(list(r))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### Error 5: Zero Step Value

```python
# ❌ INCORRECT - Will raise ValueError
# r = range(1, 10, 0)  # ValueError: range() arg 3 must not be zero

# ✅ CORRECT - Use non-zero step
r = range(1, 10, 1)
print(list(r))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Error 6: Index Out of Range

```python
r = range(5)  # [0, 1, 2, 3, 4]
print(r[4])   # Output: 4 (valid)
# print(r[5])  # IndexError: range object index out of range

# ✅ CORRECT - Check bounds
if 5 < len(r):
    print(r[5])
else:
    print("Index out of range")
```

### Error 7: Assuming range() Returns a List

```python
# ❌ INCORRECT - Assuming it's a list
r = range(5)
# print(r + [6, 7])  # TypeError: unsupported operand type(s)

# ✅ CORRECT - Convert to list when needed
r_list = list(range(5))
print(r_list + [6, 7])  # Output: [0, 1, 2, 3, 4, 6, 7]
```

## Best Practices

1. **Use range() for loops**: Most efficient way to iterate a specific number of times
2. **Convert to list only when necessary**: Keep as range object for memory efficiency
3. **Use enumerate() for index-value pairs**: Better than range(len(sequence))
4. **Understand lazy evaluation**: Range objects generate values on demand
5. **Use negative steps for countdown**: More intuitive than complex calculations

## Examples in Real-World Scenarios

### Example 1: Processing Array Indices

```python
data = ['a', 'b', 'c', 'd', 'e']
for i in range(len(data)):
    print(f"Index {i}: {data[i]}")
```

### Example 2: Creating Multiplication Table

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
```

### Example 3: Reverse Iteration

```python
for i in range(10, 0, -1):
    print(f"Countdown: {i}")
```
