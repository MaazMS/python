# Frozenset with Dictionary Program
# This program demonstrates various ways to create and work with frozensets from dictionaries

from __future__ import annotations

print("=" * 60)
print("FROZENSET WITH DICTIONARY PROGRAM")
print("=" * 60)

# 1. Basic Frozenset Creation from Dictionaries
print("\n1. BASIC FROZENSET CREATION FROM DICTIONARIES")
print("-" * 40)

# Creating frozenset from dictionary keys (default behavior)
sample_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
frozenset_keys = frozenset(sample_dict)
print(f"Original dictionary: {sample_dict}")
print(f"Frozenset from dict (keys): {frozenset_keys}")
print(f"Type: {type(frozenset_keys)}")

# Creating frozenset from dictionary keys explicitly
frozenset_keys_explicit = frozenset(sample_dict.keys())
print(f"Frozenset from dict.keys(): {frozenset_keys_explicit}")

# Creating frozenset from dictionary values
frozenset_values = frozenset(sample_dict.values())
print(f"Frozenset from dict.values(): {frozenset_values}")

# Creating frozenset from dictionary items (key-value pairs)
frozenset_items = frozenset(sample_dict.items())
print(f"Frozenset from dict.items(): {frozenset_items}")

# 2. Frozenset from Different Types of Dictionaries
print("\n2. FROZENSET FROM DIFFERENT TYPES OF DICTIONARIES")
print("-" * 40)

# String keys dictionary
string_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}
frozenset_string_keys = frozenset(string_dict.keys())
frozenset_string_values = frozenset(string_dict.values())
frozenset_string_items = frozenset(string_dict.items())

print(f"String dict: {string_dict}")
print(f"Keys frozenset: {frozenset_string_keys}")
print(f"Values frozenset: {frozenset_string_values}")
print(f"Items frozenset: {frozenset_string_items}")

# Mixed data type dictionary
mixed_dict = {1: 'one', 'two': 2, 3.0: 'three', True: 'boolean'}
frozenset_mixed_keys = frozenset(mixed_dict.keys())
frozenset_mixed_values = frozenset(mixed_dict.values())
frozenset_mixed_items = frozenset(mixed_dict.items())

print(f"\nMixed dict: {mixed_dict}")
print(f"Keys frozenset: {frozenset_mixed_keys}")
print(f"Values frozenset: {frozenset_mixed_values}")
print(f"Items frozenset: {frozenset_mixed_items}")

# 3. Handling Duplicates in Dictionary Values
print("\n3. HANDLING DUPLICATES IN DICTIONARY VALUES")
print("-" * 40)

# Dictionary with duplicate values
duplicate_values_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 1}
frozenset_duplicate_values = frozenset(duplicate_values_dict.values())
print(f"Dict with duplicate values: {duplicate_values_dict}")
print(f"Frozenset from values (duplicates removed): {frozenset_duplicate_values}")
print(f"Original values count: {len(duplicate_values_dict.values())}")
print(f"Frozenset values count: {len(frozenset_duplicate_values)}")

# Dictionary with duplicate keys (impossible, but showing overwrite behavior)
print(f"\nNote: Dictionary keys are always unique by definition")
overwrite_demo = {'key': 'first', 'key': 'second', 'key': 'third'}
print(f"Overwrite example: {overwrite_demo}")
print(f"Frozenset from keys: {frozenset(overwrite_demo.keys())}")

# 4. Empty Dictionary to Frozenset
print("\n4. EMPTY DICTIONARY TO FROZENSET")
print("-" * 40)

empty_dict = {}
frozenset_empty_keys = frozenset(empty_dict.keys())
frozenset_empty_values = frozenset(empty_dict.values())
frozenset_empty_items = frozenset(empty_dict.items())

print(f"Empty dictionary: {empty_dict}")
print(f"Frozenset from empty keys: {frozenset_empty_keys}")
print(f"Frozenset from empty values: {frozenset_empty_values}")
print(f"Frozenset from empty items: {frozenset_empty_items}")
print(f"All empty frozensets equal: {frozenset_empty_keys == frozenset_empty_values == frozenset_empty_items}")

# 5. Nested Dictionaries and Complex Structures
print("\n5. NESTED DICTIONARIES AND COMPLEX STRUCTURES")
print("-" * 40)

# Dictionary with tuple keys (hashable)
tuple_key_dict = {(1, 2): 'pair1', (3, 4): 'pair2', (5, 6): 'pair3'}
frozenset_tuple_keys = frozenset(tuple_key_dict.keys())
print(f"Dict with tuple keys: {tuple_key_dict}")
print(f"Frozenset from tuple keys: {frozenset_tuple_keys}")

# Dictionary with nested structure as values
nested_dict = {
    'user1': {'name': 'Alice', 'age': 30},
    'user2': {'name': 'Bob', 'age': 25},
    'user3': {'name': 'Charlie', 'age': 35}
}
frozenset_nested_keys = frozenset(nested_dict.keys())
print(f"\nNested dict keys: {frozenset_nested_keys}")

# Extract nested values (can't directly make frozenset from nested dicts)
try:
    frozenset_nested_values = frozenset(nested_dict.values())
    print(f"Nested values frozenset: {frozenset_nested_values}")
except TypeError as e:
    print(f"Error with nested dict values: {e}")
    print("Solution: Extract specific nested values")
    ages = [user_data['age'] for user_data in nested_dict.values()]
    names = [user_data['name'] for user_data in nested_dict.values()]
    frozenset_ages = frozenset(ages)
    frozenset_names = frozenset(names)
    print(f"Ages frozenset: {frozenset_ages}")
    print(f"Names frozenset: {frozenset_names}")

# 6. Operations with Frozensets from Dictionaries
print("\n6. OPERATIONS WITH FROZENSETS FROM DICTIONARIES")
print("-" * 40)

# Create different dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'c': 3, 'd': 4, 'e': 5, 'f': 6}
dict3 = {'a': 10, 'c': 30, 'e': 50, 'g': 70}

# Create frozensets from keys
fs_keys1: frozenset[str] = frozenset(dict1.keys())
fs_keys2: frozenset[str] = frozenset(dict2.keys())
fs_keys3: frozenset[str] = frozenset(dict3.keys())

# Create frozensets from values
fs_values1: frozenset[int] = frozenset(dict1.values())
fs_values2: frozenset[int] = frozenset(dict2.values())
fs_values3: frozenset[int] = frozenset(dict3.values())

print(f"Dict1 keys: {fs_keys1}")
print(f"Dict2 keys: {fs_keys2}")
print(f"Dict3 keys: {fs_keys3}")

# Key operations
print(f"\nKey Operations:")
print(f"Common keys (dict1 ∩ dict2): {fs_keys1.intersection(fs_keys2)}")
print(f"All keys (dict1 ∪ dict2): {fs_keys1.union(fs_keys2)}")
print(f"Keys only in dict1: {fs_keys1.difference(fs_keys2)}")
print(f"Keys only in dict2: {fs_keys2.difference(fs_keys1)}")

# Value operations
print(f"\nValue Operations:")
print(f"Common values: {fs_values1.intersection(fs_values2)}")
print(f"All values: {fs_values1.union(fs_values2)}")
print(f"Values only in dict1: {fs_values1.difference(fs_values2)}")

# Triple intersection
common_keys_all = fs_keys1.intersection(fs_keys2, fs_keys3)
print(f"Common keys in all three dicts: {common_keys_all}")

# 7. Membership Testing
print("\n7. MEMBERSHIP TESTING")
print("-" * 40)

test_dict = {'apple': 10, 'banana': 20, 'cherry': 30, 'date': 40}
test_keys_fs = frozenset(test_dict.keys())
test_values_fs = frozenset(test_dict.values())

print(f"Test dictionary: {test_dict}")
print(f"Keys frozenset: {test_keys_fs}")
print(f"Values frozenset: {test_values_fs}")

# Test key membership
test_keys = ['apple', 'grape', 'banana', 'orange']
print(f"\nTesting key membership:")
for key in test_keys:
    status = "✓" if key in test_keys_fs else "✗"
    print(f"{status} '{key}' {'is' if key in test_keys_fs else 'is NOT'} in keys")

# Test value membership
test_values = [10, 15, 20, 25, 30]
print(f"\nTesting value membership:")
for value in test_values:
    status = "✓" if value in test_values_fs else "✗"
    print(f"{status} {value} {'is' if value in test_values_fs else 'is NOT'} in values")

# 8. Comparison Operations
print("\n8. COMPARISON OPERATIONS")
print("-" * 40)

# Create dictionaries for comparison
small_dict = {'a': 1, 'b': 2}
large_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
different_dict = {'x': 100, 'y': 200}

small_keys_fs: frozenset[str] = frozenset(small_dict.keys())
large_keys_fs: frozenset[str] = frozenset(large_dict.keys())
different_keys_fs: frozenset[str] = frozenset(different_dict.keys())

print(f"Small dict keys: {small_keys_fs}")
print(f"Large dict keys: {large_keys_fs}")
print(f"Different dict keys: {different_keys_fs}")

# Key comparisons
print(f"Is small subset of large? {small_keys_fs.issubset(large_keys_fs)}")
print(f"Is large superset of small? {large_keys_fs.issuperset(small_keys_fs)}")
print(f"Are small and different disjoint? {small_keys_fs.isdisjoint(different_keys_fs)}")

# 9. Practical Examples
print("\n9. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: User permissions by role
user_permissions = {
    'admin': {'read', 'write', 'delete', 'execute'},
    'editor': {'read', 'write'},
    'viewer': {'read'},
    'guest': set()
}

# Convert to frozensets for immutability
frozen_permissions = {role: frozenset(perms) for role, perms in user_permissions.items()}
print(f"User permissions (frozen): {frozen_permissions}")

# Get all unique permissions
all_permissions = frozenset().union(*frozen_permissions.values())
print(f"All unique permissions: {all_permissions}")

# Find roles with specific permissions
write_roles = [role for role, perms in frozen_permissions.items() if 'write' in perms]
print(f"Roles with write permission: {write_roles}")

# Example 2: Product inventory
inventory = {
    'laptop': 50,
    'mouse': 100,
    'keyboard': 75,
    'monitor': 25,
    'headphones': 80
}

# Create frozensets for analysis
product_names = frozenset(inventory.keys())
stock_levels = frozenset(inventory.values())

print(f"\nProduct inventory:")
print(f"Product names: {product_names}")
print(f"Stock levels: {stock_levels}")

# Find products with specific stock levels
high_stock_products = [product for product, stock in inventory.items() if stock >= 75]
low_stock_products = [product for product, stock in inventory.items() if stock < 50]

print(f"High stock products (≥75): {high_stock_products}")
print(f"Low stock products (<50): {low_stock_products}")

# Example 3: Configuration settings
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'mydb'
    },
    'server': {
        'host': 'localhost',
        'port': 8080,
        'debug': True
    }
}

# Extract configuration keys
config_sections = frozenset(config.keys())
db_settings = frozenset(config['database'].keys())
server_settings = frozenset(config['server'].keys())

print(f"\nConfiguration sections: {config_sections}")
print(f"Database settings: {db_settings}")
print(f"Server settings: {server_settings}")

# Find common settings
common_settings = db_settings.intersection(server_settings)
print(f"Common settings: {common_settings}")

# 10. Converting Back to Dictionary
print("\n10. CONVERTING BACK TO DICTIONARY")
print("-" * 40)

original_dict = {'x': 10, 'y': 20, 'z': 30}
keys_fs = frozenset(original_dict.keys())
values_fs = frozenset(original_dict.values())
items_fs = frozenset(original_dict.items())

print(f"Original dictionary: {original_dict}")
print(f"Keys frozenset: {keys_fs}")
print(f"Values frozenset: {values_fs}")
print(f"Items frozenset: {items_fs}")

# Convert back to dictionary from items
back_to_dict = dict(items_fs)
print(f"Back to dictionary: {back_to_dict}")

# Create dictionary from separate key and value frozensets (if they match)
if len(keys_fs) == len(values_fs):
    # Note: This only works if order is preserved and lengths match
    reconstructed_dict = dict(zip(sorted(keys_fs), sorted(values_fs)))
    print(f"Reconstructed dict (may not match original): {reconstructed_dict}")

# 11. Dictionary Comprehensions with Frozensets
print("\n11. DICTIONARY COMPREHENSIONS WITH FROZENSETS")
print("-" * 40)

# Create dictionary with frozenset values
categories = {
    'fruits': ['apple', 'banana', 'orange'],
    'vegetables': ['carrot', 'lettuce', 'tomato'],
    'grains': ['rice', 'wheat', 'oats']
}

# Convert lists to frozensets
frozen_categories = {category: frozenset(items) for category, items in categories.items()}
print(f"Categories with frozenset values: {frozen_categories}")

# Create frozenset from dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
squared_values = frozenset(squared_dict.values())
print(f"Squared values: {squared_values}")

# 12. Performance Comparison
print("\n12. PERFORMANCE COMPARISON")
print("-" * 40)

import time

# Create large dictionary
size = 10000
large_dict = {f'key_{i}': i for i in range(size)}

print(f"Testing with {size} key-value pairs...")

# Time different frozenset creations
operations = [
    ('keys', lambda d: frozenset(d.keys())),
    ('values', lambda d: frozenset(d.values())),
    ('items', lambda d: frozenset(d.items()))
]

for op_name, op_func in operations:
    start_time = time.time()
    result_fs = op_func(large_dict)
    end_time = time.time()
    print(f"Frozenset from {op_name}: {end_time - start_time:.6f} seconds")

# Memory usage comparison
import sys
keys_fs = frozenset(large_dict.keys())
values_fs = frozenset(large_dict.values())
items_fs = frozenset(large_dict.items())

print(f"\nMemory usage:")
print(f"Original dict: {sys.getsizeof(large_dict):,} bytes")
print(f"Keys frozenset: {sys.getsizeof(keys_fs):,} bytes")
print(f"Values frozenset: {sys.getsizeof(values_fs):,} bytes")
print(f"Items frozenset: {sys.getsizeof(items_fs):,} bytes")

# 13. Real-world Use Cases
print("\n13. REAL-WORLD USE CASES")
print("-" * 40)

# Use case 1: API endpoint validation
api_endpoints = {
    '/users': ['GET', 'POST'],
    '/users/{id}': ['GET', 'PUT', 'DELETE'],
    '/products': ['GET', 'POST'],
    '/orders': ['GET', 'POST']
}

# Convert to frozensets for validation
frozen_endpoints = {endpoint: frozenset(methods) for endpoint, methods in api_endpoints.items()}
all_endpoints = frozenset(frozen_endpoints.keys())
all_methods = frozenset().union(*frozen_endpoints.values())

print(f"All API endpoints: {all_endpoints}")
print(f"All HTTP methods: {all_methods}")

# Use case 2: Database table relationships
table_relationships = {
    'users': frozenset(['orders', 'profiles']),
    'orders': frozenset(['products', 'users']),
    'products': frozenset(['categories', 'orders']),
    'categories': frozenset(['products'])
}

print(f"\nTable relationships: {table_relationships}")

# Find tables with most relationships
max_relationships = max(len(relations) for relations in table_relationships.values())
most_connected = [table for table, relations in table_relationships.items() 
                 if len(relations) == max_relationships]
print(f"Most connected tables: {most_connected}")

# Use case 3: Feature flags
feature_flags = {
    'development': frozenset(['debug_mode', 'test_data', 'mock_services']),
    'staging': frozenset(['test_data', 'analytics']),
    'production': frozenset(['analytics', 'monitoring'])
}

print(f"\nFeature flags by environment: {feature_flags}")

# Find common features across environments
common_features = frozenset.intersection(*feature_flags.values())
print(f"Common features: {common_features}")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)
