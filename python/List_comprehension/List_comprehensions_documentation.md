# List Comprehensions Documentation

## 1. List Comprehension Definition and Characteristics

### Definition

List comprehension is a concise and readable way to create lists in Python. It provides a shorter syntax when you want to create a new list based on the values of an existing list or any iterable.

### Characteristics

- **Concise**: Reduces multiple lines of code into a single line
- **Readable**: More Pythonic and easier to understand
- **Efficient**: Generally faster than traditional for loops
- **Flexible**: Can include conditions and transformations

### Basic Syntax

```python
new_list = [expression for item in iterable if condition]
```

### Examples

```python
# Basic list comprehension
numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# With condition
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

# With transformation
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

## 2. List Comprehensions Operations

### Arithmetic Operations

```python
# Addition
numbers = [1, 2, 3, 4, 5]
add_ten = [x + 10 for x in numbers]
print(add_ten)  # [11, 12, 13, 14, 15]

# Multiplication
multiply_by_two = [x * 2 for x in numbers]
print(multiply_by_two)  # [2, 4, 6, 8, 10]

# Power operations
powers_of_two = [2**x for x in range(5)]
print(powers_of_two)  # [1, 2, 4, 8, 16]
```

### String Operations

```python
# String transformation
words = ['hello', 'world', 'python']
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # ['HELLO', 'WORLD', 'PYTHON']

# String length
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 5, 6]

# String filtering
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['python']
```

### Nested List Operations

```python
# Flattening nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6]

# Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Conditional Operations

```python
# If-else in list comprehension
numbers = [1, 2, 3, 4, 5, 6]
result = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(result)  # ['odd', 'even', 'odd', 'even', 'odd', 'even']

# Multiple conditions
filtered_numbers = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(filtered_numbers)  # [0, 6, 12, 18]
```

## 3. List Comprehensions Methods

### Using Built-in Functions

```python
# Using abs() function
numbers = [-5, -3, 0, 3, 5]
absolute_values = [abs(x) for x in numbers]
print(absolute_values)  # [5, 3, 0, 3, 5]

# Using round() function
decimals = [3.14159, 2.71828, 1.41421]
rounded = [round(x, 2) for x in decimals]
print(rounded)  # [3.14, 2.72, 1.41]

# Using str() function
numbers = [1, 2, 3, 4, 5]
string_numbers = [str(x) for x in numbers]
print(string_numbers)  # ['1', '2', '3', '4', '5']
```

### String Methods

```python
# Using string methods
words = ['  hello  ', '  world  ', '  python  ']
cleaned_words = [word.strip().title() for word in words]
print(cleaned_words)  # ['Hello', 'World', 'Python']

# Using split() method
sentences = ['hello world', 'python programming', 'list comprehension']
word_lists = [sentence.split() for sentence in sentences]
print(word_lists)  # [['hello', 'world'], ['python', 'programming'], ['list', 'comprehension']]

# Using replace() method
texts = ['hello world', 'good morning', 'nice day']
replaced_texts = [text.replace(' ', '_') for text in texts]
print(replaced_texts)  # ['hello_world', 'good_morning', 'nice_day']
```

### Custom Functions

```python
# Using custom functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Finding prime numbers
primes = [x for x in range(2, 20) if is_prime(x)]
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19]

# Using lambda functions
numbers = [1, 2, 3, 4, 5]
squared = [(lambda x: x**2)(x) for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]
```

### Working with Dictionaries

```python
# Dictionary values to list
student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
grades_list = [grade for grade in student_grades.values()]
print(grades_list)  # [85, 90, 78]

# Dictionary keys to list
names_list = [name.upper() for name in student_grades.keys()]
print(names_list)  # ['ALICE', 'BOB', 'CHARLIE']

# Dictionary items with conditions
high_performers = [name for name, grade in student_grades.items() if grade >= 80]
print(high_performers)  # ['Alice', 'Bob']
```

## 4. Common Errors in List Comprehensions

### 1. Syntax Errors

```python
# ❌ WRONG: Missing brackets
# numbers = x for x in range(5)

# ✅ CORRECT:
numbers = [x for x in range(5)]

# ❌ WRONG: Incorrect order of elements
# result = [for x in range(5) x * 2]

# ✅ CORRECT:
result = [x * 2 for x in range(5)]
```

### 2. Variable Scope Issues

```python
# ❌ WRONG: Using undefined variable
# result = [x * y for x in range(5)]  # NameError: name 'y' is not defined

# ✅ CORRECT: Define all variables
y = 10
result = [x * y for x in range(5)]

# ❌ WRONG: Variable leakage (Python 2 issue, fixed in Python 3)
# In Python 2, loop variables would leak into surrounding scope
```

### 3. Performance Issues

```python
# ❌ INEFFICIENT: Calling expensive function multiple times
def expensive_function(x):
    # Simulate expensive operation
    import time
    time.sleep(0.01)
    return x * 2

# Don't do this:
# numbers = [expensive_function(x) for x in range(10) if expensive_function(x) > 5]

# ✅ BETTER: Store result in variable first
numbers = [result for x in range(10) if (result := expensive_function(x)) > 5]
# Or use traditional loop for complex cases
```

### 4. Readability Issues

```python
# ❌ TOO COMPLEX: Hard to read nested comprehensions
# result = [[y for y in x if y % 2 == 0] for x in [[1,2,3,4], [5,6,7,8]] if len(x) > 3]

# ✅ BETTER: Break it down
lists = [[1,2,3,4], [5,6,7,8]]
filtered_lists = [x for x in lists if len(x) > 3]
result = [[y for y in x if y % 2 == 0] for x in filtered_lists]
```

### 5. Type Errors

```python
# ❌ WRONG: Mixing incompatible types
mixed_list = [1, '2', 3.0, '4']
# This will cause TypeError:
# result = [x + 1 for x in mixed_list]

# ✅ CORRECT: Handle type conversion
result = [int(x) + 1 for x in mixed_list if str(x).isdigit()]
# Or filter by type:
numbers_only = [x + 1 for x in mixed_list if isinstance(x, (int, float))]
```

### 6. Memory Issues with Large Datasets

```python
# ❌ MEMORY INTENSIVE: Creating large lists in memory
# large_list = [x**2 for x in range(10000000)]  # Uses lots of memory

# ✅ BETTER: Use generator expression for large datasets
large_gen = (x**2 for x in range(10000000))  # Uses minimal memory

# Convert to list only when needed
# large_list = list(large_gen)
```

### 7. Mutating Lists During Iteration

```python
# ❌ DANGEROUS: Don't modify the original list being iterated
original_list = [1, 2, 3, 4, 5]
# Don't do this while iterating:
# result = [original_list.pop() for x in original_list]  # Unpredictable behavior

# ✅ SAFE: Work with a copy or use different approach
result = [x for x in original_list.copy() if x % 2 == 0]
```

### Best Practices Summary

1. Keep list comprehensions simple and readable
2. Use traditional loops for complex logic
3. Be mindful of memory usage with large datasets
4. Handle type errors gracefully
5. Avoid side effects within comprehensions
6. Use meaningful variable names
7. Consider using generator expressions for large datasets
