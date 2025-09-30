# List Type Data Documentation

## 1. List Type Data Definition

A **list** is a collection of arbitrary objects that can store different types of data. Lists are one of the most versatile data structures in Python.

**Key Definition Points:**

- Lists are defined by enclosing a comma-separated sequence of objects in square brackets `[]`
- Lists are ordered, mutable, and can contain duplicate values
- Lists can store any Python object (numbers, strings, booleans, other lists, etc.)

**Basic Syntax:**

```python
list_name = [item1, item2, item3, ...]
```

**Important Characteristics:**

1. **Ordered**: Items have a defined order and maintain that order
2. **Mutable**: Items can be changed after creation
3. **Allow duplicates**: Same value can appear multiple times
4. **Dynamic**: Can grow or shrink during runtime
5. **Indexed**: Elements can be accessed by index (starting from 0)
6. **Nested**: Can contain other lists
7. **Heterogeneous**: Can contain different data types

---

## 2. List Type Data Creations

### 2.1 Empty List Creation

```python
# Method 1: Using square brackets
empty_list = []

# Method 2: Using list() constructor
empty_list = list()

# Example
my_list = []
print(my_list)  # Output: []
print(type(my_list))  # Output: <class 'list'>
```

### 2.2 List with Initial Values

```python
# Numbers list
numbers = [1, 2, 3, 4, 5]

# String list
fruits = ['apple', 'banana', 'orange']

# Mixed data types
mixed_list = [1, 'hello', 3.14, True, [1, 2, 3]]

# Boolean list
bool_list = [True, False, True]
```

### 2.3 List Creation Using Range

```python
# Using range() to create list
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
even_numbers = list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]
```

### 2.4 List Creation Using List Comprehension

```python
# Squares of numbers 1-5
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# Even numbers from 1-10
evens = [x for x in range(1, 11) if x % 2 == 0]  # [2, 4, 6, 8, 10]
```

### 2.5 Nested List Creation

```python
# 2D list (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List of lists with different sizes
nested = [['a', 'b'], [1, 2, 3, 4], ['hello']]
```

---

## 3. List Type Data Operations

### 3.1 Indexing Operations

```python
fruits = ['apple', 'banana', 'orange', 'grape']

# Positive indexing (left to right, starts from 0)
print(fruits[0])    # Output: apple
print(fruits[1])    # Output: banana
print(fruits[3])    # Output: grape

# Negative indexing (right to left, starts from -1)
print(fruits[-1])   # Output: grape
print(fruits[-2])   # Output: orange
print(fruits[-4])   # Output: apple
```

### 3.2 Slicing Operations

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic slicing [start:end]
print(numbers[2:5])     # Output: [3, 4, 5]
print(numbers[:3])      # Output: [1, 2, 3]
print(numbers[7:])      # Output: [8, 9, 10]

# Slicing with step [start:end:step]
print(numbers[::2])     # Output: [1, 3, 5, 7, 9]
print(numbers[1::2])    # Output: [2, 4, 6, 8, 10]
print(numbers[::-1])    # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (reverse)
```

### 3.3 Concatenation Operations

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using + operator
combined = list1 + list2    # Output: [1, 2, 3, 4, 5, 6]

# Using += operator
list1 += list2              # list1 becomes [1, 2, 3, 4, 5, 6]
```

### 3.4 Repetition Operations

```python
# Using * operator
repeated = [1, 2] * 3       # Output: [1, 2, 1, 2, 1, 2]
zeros = [0] * 5             # Output: [0, 0, 0, 0, 0]
```

### 3.5 Membership Operations

```python
fruits = ['apple', 'banana', 'orange']

# Check if item exists
print('apple' in fruits)        # Output: True
print('grape' in fruits)        # Output: False
print('grape' not in fruits)    # Output: True
```

### 3.6 Comparison Operations

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

print(list1 == list2)   # Output: True
print(list1 == list3)   # Output: False
print(list1 != list3)   # Output: True
```

---

## 4. List Type Data Methods

### 4.1 Adding Elements Methods

#### append() - Add single element at the end

```python
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'orange']

# Can append any data type
numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers)  # Output: [1, 2, 3, [4, 5]]
```

#### extend() - Add multiple elements at the end

```python
fruits = ['apple', 'banana']
fruits.extend(['orange', 'grape'])
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

# Extend with string (adds each character)
letters = ['a', 'b']
letters.extend('cd')
print(letters)  # Output: ['a', 'b', 'c', 'd']
```

#### insert() - Add element at specific position

```python
fruits = ['apple', 'orange']
fruits.insert(1, 'banana')
print(fruits)  # Output: ['apple', 'banana', 'orange']

# Insert at beginning
numbers = [2, 3, 4]
numbers.insert(0, 1)
print(numbers)  # Output: [1, 2, 3, 4]
```

### 4.2 Removing Elements Methods

#### remove() - Remove first occurrence of value

```python
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange', 'banana']

# Raises ValueError if item not found
# fruits.remove('grape')  # This would raise ValueError
```

#### pop() - Remove and return element by index

```python
fruits = ['apple', 'banana', 'orange']

# Remove last element
last_fruit = fruits.pop()
print(last_fruit)  # Output: orange
print(fruits)      # Output: ['apple', 'banana']

# Remove element at specific index
first_fruit = fruits.pop(0)
print(first_fruit)  # Output: apple
print(fruits)       # Output: ['banana']
```

#### clear() - Remove all elements

```python
fruits = ['apple', 'banana', 'orange']
fruits.clear()
print(fruits)  # Output: []
```

### 4.3 Searching Methods

#### index() - Find index of first occurrence

```python
fruits = ['apple', 'banana', 'orange', 'banana']
print(fruits.index('banana'))  # Output: 1

# With start and end parameters
print(fruits.index('banana', 2))  # Output: 3 (search from index 2)
```

#### count() - Count occurrences of value

```python
numbers = [1, 2, 3, 2, 4, 2, 5]
print(numbers.count(2))  # Output: 3
print(numbers.count(6))  # Output: 0
```

### 4.4 Sorting Methods

#### sort() - Sort list in place

```python
# Sort numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# Sort in reverse order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

# Sort strings
fruits = ['banana', 'apple', 'orange']
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'orange']
```

#### reverse() - Reverse list in place

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]
```

### 4.5 Copying Methods

#### copy() - Create shallow copy

```python
original = [1, 2, 3, [4, 5]]
copied = original.copy()
print(copied)  # Output: [1, 2, 3, [4, 5]]

# Modify original
original[0] = 10
print(original)  # Output: [10, 2, 3, [4, 5]]
print(copied)    # Output: [1, 2, 3, [4, 5]]
```

---

## 5. Common Errors in List Type Data

### 5.1 IndexError - Index out of range

```python
# ERROR EXAMPLE
fruits = ['apple', 'banana', 'orange']
# print(fruits[3])  # IndexError: list index out of range

# CORRECT APPROACH
if len(fruits) > 3:
    print(fruits[3])
else:
    print("Index out of range")
```

### 5.2 ValueError - Value not in list

```python
# ERROR EXAMPLE
fruits = ['apple', 'banana', 'orange']
# fruits.remove('grape')  # ValueError: list.remove(x): x not in list

# CORRECT APPROACH
if 'grape' in fruits:
    fruits.remove('grape')
else:
    print("Item not found in list")
```

### 5.3 TypeError - Unsupported operand types

```python
# ERROR EXAMPLE
numbers = [1, 2, 3]
# result = numbers + 4  # TypeError: can only concatenate list (not "int") to list

# CORRECT APPROACH
result = numbers + [4]  # Output: [1, 2, 3, 4]
# OR
numbers.append(4)       # numbers becomes [1, 2, 3, 4]
```

### 5.4 Modifying list during iteration

```python
# ERROR EXAMPLE - Can cause unexpected behavior
numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # Modifying list during iteration

# CORRECT APPROACH
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # Output: [1, 3, 5]
```

### 5.5 Shallow vs Deep Copy Issues

```python
# PROBLEM WITH SHALLOW COPY
original = [[1, 2], [3, 4]]
copied = original.copy()
copied[0][0] = 'X'
print(original)  # Output: [['X', 2], [3, 4]] - Original affected!

# SOLUTION - Deep copy
import copy
original = [[1, 2], [3, 4]]
deep_copied = copy.deepcopy(original)
deep_copied[0][0] = 'X'
print(original)     # Output: [[1, 2], [3, 4]] - Original unchanged
print(deep_copied)  # Output: [['X', 2], [3, 4]]
```

### 5.6 Mutable Default Arguments

```python
# ERROR EXAMPLE
def add_item(item, my_list=[]):  # Dangerous!
    my_list.append(item)
    return my_list

# This causes issues
list1 = add_item(1)     # [1]
list2 = add_item(2)     # [1, 2] - Unexpected!

# CORRECT APPROACH
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

---

## Summary

Lists are fundamental data structures in Python that provide:

- **Flexibility**: Can store any type of data
- **Mutability**: Can be modified after creation  
- **Ordering**: Maintain insertion order
- **Rich methods**: Comprehensive set of built-in methods
- **Versatility**: Support for various operations

Understanding these concepts and common pitfalls will help you use lists effectively in your Python programs.  
  