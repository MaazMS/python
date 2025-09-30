# Frozenset Type Data Documentation

## 1. Frozenset Type Data Definition and Characteristics

### Definition

A **frozenset** is an immutable version of a Python set. It is a built-in data type that represents an unordered collection of unique elements that cannot be changed after creation.

### Key Characteristics

- **Immutable**: Once created, frozenset cannot be modified (no add, remove, or update operations)
- **Unordered**: Elements have no defined order or index
- **Unique Elements**: All elements in a frozenset are unique (no duplicates)
- **Hashable**: Frozensets can be used as dictionary keys or elements in other sets
- **Iterable**: You can iterate through frozenset elements
- **Built-in Type**: Native Python data type, no imports required

### Syntax

```python
frozenset([iterable])
```

## 2. Frozenset Type Data Creation

### Creating Empty Frozenset

```python
# Empty frozenset
empty_frozenset = frozenset()
print(empty_frozenset)  # Output: frozenset()
```

### Creating Frozenset from Different Data Types

#### From List

```python
# From list
list_numbers = [1, 2, 3, 4, 5, 2, 3]  # Duplicates will be removed
frozenset_from_list = frozenset(list_numbers)
print(frozenset_from_list)  # Output: frozenset({1, 2, 3, 4, 5})
```

#### From Tuple

```python
# From tuple
tuple_numbers = (1, 2, 3, 4, 5, 6)
frozenset_from_tuple = frozenset(tuple_numbers)
print(frozenset_from_tuple)  # Output: frozenset({1, 2, 3, 4, 5, 6})
```

#### From Dictionary

```python
# From dictionary (keys only)
dictionary = {1: 'a', 2: 'b', 3: 'c'}
frozenset_from_dict = frozenset(dictionary)
print(frozenset_from_dict)  # Output: frozenset({1, 2, 3})

# From dictionary values
frozenset_from_dict_values = frozenset(dictionary.values())
print(frozenset_from_dict_values)  # Output: frozenset({'a', 'b', 'c'})
```

#### From String

```python
# From string
string_data = "hello"
frozenset_from_string = frozenset(string_data)
print(frozenset_from_string)  # Output: frozenset({'h', 'e', 'l', 'o'})
```

#### From Set

```python
# From set
normal_set = {1, 2, 3, 4, 5}
frozenset_from_set = frozenset(normal_set)
print(frozenset_from_set)  # Output: frozenset({1, 2, 3, 4, 5})
```

## 3. Frozenset Type Data Operations

### Mathematical Set Operations

#### Union (|)

```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
union_result = fs1 | fs2
print(union_result)  # Output: frozenset({1, 2, 3, 4, 5})
```

#### Intersection (&)

```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
intersection_result = fs1 & fs2
print(intersection_result)  # Output: frozenset({3, 4})
```

#### Difference (-)

```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
difference_result = fs1 - fs2
print(difference_result)  # Output: frozenset({1, 2})
```

#### Symmetric Difference (^)

```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
symmetric_diff = fs1 ^ fs2
print(symmetric_diff)  # Output: frozenset({1, 2, 5, 6})
```

### Comparison Operations

#### Subset and Superset

```python
fs1 = frozenset([1, 2])
fs2 = frozenset([1, 2, 3, 4])

# Check if fs1 is subset of fs2
is_subset = fs1 <= fs2
print(is_subset)  # Output: True

# Check if fs2 is superset of fs1
is_superset = fs2 >= fs1
print(is_superset)  # Output: True

# Check if disjoint (no common elements)
fs3 = frozenset([5, 6])
are_disjoint = fs1.isdisjoint(fs3)
print(are_disjoint)  # Output: True
```

### Membership Testing

```python
fs = frozenset([1, 2, 3, 4, 5])
print(3 in fs)      # Output: True
print(6 in fs)      # Output: False
print(7 not in fs)  # Output: True
```

## 4. Frozenset Type Data Methods

### Basic Methods

#### `copy()`

```python
fs = frozenset([1, 2, 3])
fs_copy = fs.copy()
print(fs_copy)  # Output: frozenset({1, 2, 3})
```

#### `len()`

```python
fs = frozenset([1, 2, 3, 4, 5])
print(len(fs))  # Output: 5
```

### Set Operation Methods

#### `union(*others)`

```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
fs3 = frozenset([5, 6, 7])
union_result = fs1.union(fs2, fs3)
print(union_result)  # Output: frozenset({1, 2, 3, 4, 5, 6, 7})
```

#### `intersection(*others)`

```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([2, 3, 4, 5])
fs3 = frozenset([3, 4, 5, 6])
intersection_result = fs1.intersection(fs2, fs3)
print(intersection_result)  # Output: frozenset({3, 4})
```

#### `difference(*others)`

```python
fs1 = frozenset([1, 2, 3, 4, 5])
fs2 = frozenset([3, 4])
fs3 = frozenset([5, 6])
difference_result = fs1.difference(fs2, fs3)
print(difference_result)  # Output: frozenset({1, 2})
```

#### `symmetric_difference(other)`

```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
symmetric_diff = fs1.symmetric_difference(fs2)
print(symmetric_diff)  # Output: frozenset({1, 2, 5, 6})
```

### Comparison Methods

#### `issubset(other)`

```python
fs1 = frozenset([1, 2])
fs2 = frozenset([1, 2, 3, 4])
print(fs1.issubset(fs2))  # Output: True
```

#### `issuperset(other)`

```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([1, 2])
print(fs1.issuperset(fs2))  # Output: True
```

#### `isdisjoint(other)`

```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])
print(fs1.isdisjoint(fs2))  # Output: True
```

## 5. Common Errors in Frozenset Type Data

### 1. Attempting to Modify Frozenset

```python
# ERROR: Frozensets are immutable
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'
# fs.update([4, 5])  # AttributeError: 'frozenset' object has no attribute 'update'
```

### 2. Indexing Frozenset

```python
# ERROR: Frozensets don't support indexing
fs = frozenset([1, 2, 3])
# element = fs[0]  # TypeError: 'frozenset' object is not subscriptable
```

### 3. Creating Frozenset with Unhashable Elements

```python
# ERROR: Lists are unhashable
try:
    fs = frozenset([[1, 2], [3, 4]])  # TypeError: unhashable type: 'list'
except TypeError as e:
    print(f"Error: {e}")

# CORRECT: Use tuples instead
fs = frozenset([(1, 2), (3, 4)])  # Works fine
print(fs)  # Output: frozenset({(1, 2), (3, 4)})
```

### 4. Confusion with Set Methods

```python
# ERROR: Using set methods on frozenset
fs = frozenset([1, 2, 3])
# fs.discard(1)  # AttributeError: 'frozenset' object has no attribute 'discard'
# fs.pop()  # AttributeError: 'frozenset' object has no attribute 'pop'
# fs.clear()  # AttributeError: 'frozenset' object has no attribute 'clear'
```

### 5. Type Confusion

```python
# ERROR: Expecting mutable behavior
def modify_set(s):
    return s.add(4)  # This will fail for frozenset

regular_set = {1, 2, 3}
frozen_set = frozenset([1, 2, 3])

# modify_set(frozen_set)  # AttributeError: 'frozenset' object has no attribute 'add'
```

## Best Practices

1. **Use frozenset as dictionary keys**: Since frozensets are hashable

   ```python
   fs1 = frozenset([1, 2, 3])
   fs2 = frozenset([4, 5, 6])
   my_dict = {fs1: "first set", fs2: "second set"}
   ```

2. **Convert to regular set for modifications**:

   ```python
   fs = frozenset([1, 2, 3])
   regular_set = set(fs)
   regular_set.add(4)
   new_frozenset = frozenset(regular_set)
   ```

3. **Use frozenset for constant collections**:

   ```python
   VALID_STATUSES = frozenset(['active', 'inactive', 'pending'])
   ```

4. **Memory efficiency**: Frozensets are more memory-efficient than regular sets for read-only operations.

## Summary

Frozensets are powerful immutable collections that provide all the mathematical set operations while being hashable and memory-efficient. They are ideal for situations where you need an unchangeable set of unique elements, especially when used as dictionary keys or for constant collections in your applications.
