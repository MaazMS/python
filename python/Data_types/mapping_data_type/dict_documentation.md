# Dictionary Type Data Documentation

## 1. Dict Type Data Definition and Characteristics

### Definition

A dictionary is a collection of key-value pairs enclosed in curly braces `{}`. It's also known as an associative array or hash map in other programming languages.

### Characteristics

- **Mutable**: Dictionary contents can be modified after creation
- **Dynamic**: Can grow or shrink in size during runtime
- **Nested**: Can contain other dictionaries, lists, or complex data structures
- **Unordered**: Prior to Python 3.7, dictionaries were unordered. From Python 3.7+, they maintain insertion order
- **Key-Value Pairs**: Each element consists of a key and its associated value
- **Unique Keys**: Keys must be unique within a dictionary
- **Immutable Keys**: Keys must be immutable (strings, numbers, tuples)

### Key Features

- **Fast Lookup**: O(1) average time complexity for access operations
- **Flexible Values**: Values can be of any data type
- **Memory Efficient**: Optimized for frequent lookups and modifications

### Dictionaries vs Lists

| Feature | Dictionary | List |
|---------|------------|------|
| Access Method | Via keys | Via index (position) |
| Ordering | Insertion order (Python 3.7+) | Positional order |
| Lookup Speed | O(1) average | O(n) for search |
| Key Types | Immutable types only | Integer indices only |

## 2. Dict Type Data Creation

### Method 1: Using Curly Braces

```python
# Empty dictionary
empty_dict = {}

# Dictionary with initial values
student = {'name': 'John', 'age': 20, 'grade': 'A'}

# Mixed data types
mixed_dict = {'name': 'Alice', 'scores': [85, 92, 78], 'passed': True}

# Nested dictionary
nested_dict = {
    'person': {
        'name': 'Bob',
        'address': {'city': 'New York', 'zip': '10001'}
    }
}
```

### Method 2: Using dict() Constructor

```python
# From keyword arguments
d1 = dict(name='John', age=25, city='Boston')

# From key-value pairs (tuples)
d2 = dict([('a', 1), ('b', 2), ('c', 3)])

# From another dictionary
d3 = dict({'x': 10, 'y': 20})

# From zip of two lists
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'Seattle']
d4 = dict(zip(keys, values))
```

### Method 3: Dictionary Comprehension

```python
# Square numbers
squares = {x: x**2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conditional comprehension
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# Result: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# From string
char_count = {char: word.count(char) for char in 'hello'}
# Result: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

## 3. Dict Type Data Operations

### Basic Operations

#### Adding Elements

```python
student = {'name': 'John', 'age': 20}

# Add new key-value pair
student['grade'] = 'A'
student['subjects'] = ['Math', 'Physics']

print(student)
# Output: {'name': 'John', 'age': 20, 'grade': 'A', 'subjects': ['Math', 'Physics']}
```

#### Accessing Elements

```python
student = {'name': 'John', 'age': 20, 'grade': 'A'}

# Direct access
print(student['name'])  # Output: John

# Using get() method (safer)
print(student.get('name'))  # Output: John
print(student.get('phone', 'Not found'))  # Output: Not found
```

#### Updating Elements

```python
student = {'name': 'John', 'age': 20}

# Update single value
student['age'] = 21

# Update multiple values
student.update({'grade': 'B', 'city': 'Boston'})

print(student)
# Output: {'name': 'John', 'age': 21, 'grade': 'B', 'city': 'Boston'}
```

#### Removing Elements

```python
student = {'name': 'John', 'age': 20, 'grade': 'A', 'city': 'Boston'}

# Remove specific key-value pair
del student['city']

# Remove and return value
grade = student.pop('grade')  # Returns 'A'

# Remove last inserted item (Python 3.7+)
last_item = student.popitem()

# Clear all elements
student.clear()
```

### Advanced Operations

#### Merging Dictionaries

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Using update()
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using ** operator (Python 3.5+)
merged = {**dict1, **dict2}

# Using | operator (Python 3.9+)
merged = dict1 | dict2
```

#### Copying Dictionaries

```python
original = {'a': 1, 'b': [2, 3]}

# Shallow copy
copy1 = original.copy()
copy2 = dict(original)

# Deep copy (for nested structures)
import copy
deep_copy = copy.deepcopy(original)
```

## 4. Dict Type Data Methods

### Essential Methods

#### 1. `get(key, default=None)`

Safely access dictionary values with optional default.

```python
student = {'name': 'John', 'age': 20}

print(student.get('name'))        # Output: John
print(student.get('phone'))       # Output: None
print(student.get('phone', 'N/A')) # Output: N/A
```

#### 2. `keys()`

Returns a view of all keys in the dictionary.

```python
student = {'name': 'John', 'age': 20, 'grade': 'A'}

keys = student.keys()
print(list(keys))  # Output: ['name', 'age', 'grade']

# Iterate through keys
for key in student.keys():
    print(f"Key: {key}")
```

#### 3. `values()`

Returns a view of all values in the dictionary.

```python
student = {'name': 'John', 'age': 20, 'grade': 'A'}

values = student.values()
print(list(values))  # Output: ['John', 20, 'A']

# Iterate through values
for value in student.values():
    print(f"Value: {value}")
```

#### 4. `items()`

Returns a view of all key-value pairs as tuples.

```python
student = {'name': 'John', 'age': 20, 'grade': 'A'}

items = student.items()
print(list(items))  # Output: [('name', 'John'), ('age', 20), ('grade', 'A')]

# Iterate through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

#### 5. `pop(key, default=None)`

Removes and returns the value for a specified key.

```python
student = {'name': 'John', 'age': 20, 'grade': 'A'}

# Remove and return value
age = student.pop('age')  # Returns 20
print(student)  # Output: {'name': 'John', 'grade': 'A'}

# With default value
phone = student.pop('phone', 'Not found')  # Returns 'Not found'
```

#### 6. `popitem()`

Removes and returns the last inserted key-value pair.

```python
student = {'name': 'John', 'age': 20, 'grade': 'A'}

last_item = student.popitem()  # Returns ('grade', 'A')
print(student)  # Output: {'name': 'John', 'age': 20}
```

#### 7. `clear()`

Removes all elements from the dictionary.

```python
student = {'name': 'John', 'age': 20, 'grade': 'A'}

student.clear()
print(student)  # Output: {}
```

#### 8. `update(other)`

Updates dictionary with key-value pairs from another dictionary or iterable.

```python
student = {'name': 'John', 'age': 20}

# Update with another dictionary
student.update({'grade': 'A', 'city': 'Boston'})

# Update with keyword arguments
student.update(phone='123-456-7890', email='john@email.com')

print(student)
# Output: {'name': 'John', 'age': 20, 'grade': 'A', 'city': 'Boston', 'phone': '123-456-7890', 'email': 'john@email.com'}
```

#### 9. `setdefault(key, default=None)`

Returns the value of a key if it exists, otherwise sets and returns the default value.

```python
student = {'name': 'John', 'age': 20}

# Key exists
name = student.setdefault('name', 'Unknown')  # Returns 'John'

# Key doesn't exist
grade = student.setdefault('grade', 'A')  # Returns 'A' and adds to dict

print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'A'}
```

### Utility Methods

#### 10. `fromkeys(iterable, value=None)`

Creates a dictionary from an iterable with the same value for all keys.

```python
# Create dictionary with default value
keys = ['name', 'age', 'grade']
student_template = dict.fromkeys(keys, 'Unknown')
print(student_template)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'grade': 'Unknown'}

# Create dictionary with None values
empty_fields = dict.fromkeys(['email', 'phone', 'address'])
print(empty_fields)  # Output: {'email': None, 'phone': None, 'address': None}
```

## 5. Common Errors in Dict Type Data

### Error 1: KeyError - Accessing Non-existent Keys

```python
# ❌ Wrong way
student = {'name': 'John', 'age': 20}
try:
    print(student['grade'])  # Raises KeyError
except KeyError as e:
    print(f"KeyError: {e}")

# ✅ Correct ways
# Method 1: Using get()
print(student.get('grade', 'Not assigned'))

# Method 2: Check if key exists
if 'grade' in student:
    print(student['grade'])
else:
    print('Grade not found')

# Method 3: Use try-except
try:
    print(student['grade'])
except KeyError:
    print('Grade not found')
```

### Error 2: TypeError - Using Mutable Objects as Keys

```python
# ❌ Wrong way - Lists are mutable
try:
    invalid_dict = {[1, 2]: 'value'}  # Raises TypeError
except TypeError as e:
    print(f"TypeError: {e}")

# ✅ Correct way - Use immutable types
valid_dict = {
    'string_key': 'value1',
    42: 'value2',
    (1, 2): 'value3',  # Tuples are immutable
    True: 'value4'
}
```

### Error 3: UnboundLocalError - Modifying Dictionary While Iterating

```python
# ❌ Wrong way
student = {'name': 'John', 'age': 20, 'grade': 'A', 'city': 'Boston'}

# Don't modify dictionary while iterating
for key in student:
    if key == 'city':
        del student[key]  # Can cause RuntimeError

# ✅ Correct way
# Method 1: Create a copy of keys
for key in list(student.keys()):
    if key == 'city':
        del student[key]

# Method 2: Use dictionary comprehension
student = {k: v for k, v in student.items() if k != 'city'}
```

### Error 4: AttributeError - Incorrect Method Usage

```python
# ❌ Wrong way
student = {'name': 'John', 'age': 20}

# Trying to use list methods on dictionary
try:
    student.append({'grade': 'A'})  # Raises AttributeError
except AttributeError as e:
    print(f"AttributeError: {e}")

# ✅ Correct way
student.update({'grade': 'A'})
# or
student['grade'] = 'A'
```

### Error 5: Memory Issues with Large Dictionaries

```python
# ❌ Inefficient way
large_dict = {}
for i in range(1000000):
    large_dict[f'key_{i}'] = f'value_{i}'

# ✅ More efficient way
large_dict = {f'key_{i}': f'value_{i}' for i in range(1000000)}

# ✅ For very large datasets, consider using slots or named tuples
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])
people = [Person('John', 20, 'Boston') for _ in range(1000000)]
```

### Error 6: Unexpected Behavior with Mutable Default Values

```python
# ❌ Wrong way
def add_student(name, subjects={}):  # Mutable default argument
    subjects[name] = []
    return subjects

# This will cause unexpected behavior
students1 = add_student('John')
students2 = add_student('Alice')
print(students1)  # Both dictionaries are the same object!

# ✅ Correct way
def add_student(name, subjects=None):
    if subjects is None:
        subjects = {}
    subjects[name] = []
    return subjects
```

### Error 7: Comparison and Sorting Issues

```python
# ❌ Wrong way - Dictionaries can't be compared with < or >
try:
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    print(dict1 < dict2)  # Raises TypeError
except TypeError as e:
    print(f"TypeError: {e}")

# ✅ Correct way - Compare specific aspects
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Compare lengths
print(len(dict1) == len(dict2))

# Compare keys
print(set(dict1.keys()) == set(dict2.keys()))

# Sort by values
sorted_items = sorted(dict1.items(), key=lambda x: x[1])
print(sorted_items)
```

### Best Practices to Avoid Errors

1. **Always use `get()` for uncertain keys**
2. **Use immutable objects as keys**
3. **Don't modify dictionaries while iterating**
4. **Use appropriate methods for dictionary operations**
5. **Be careful with default arguments**
6. **Consider memory usage for large dictionaries**
7. **Use meaningful key names**
8. **Handle exceptions appropriately**

### Performance Tips

```python
# Fast membership testing
if 'key' in dictionary:  # O(1) average case
    pass

# Efficient iteration
for key, value in dictionary.items():  # Better than separate key/value access
    pass

# Batch operations
dictionary.update(other_dict)  # Better than multiple individual assignments
```

This comprehensive documentation covers all the essential aspects of Python dictionaries with practical examples and common pitfalls to avoid.
