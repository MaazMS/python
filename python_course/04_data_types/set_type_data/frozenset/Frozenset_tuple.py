# Frozenset with Tuple Program
# This program demonstrates various ways to create and work with frozensets from tuples

from __future__ import annotations

print("=" * 60)
print("FROZENSET WITH TUPLE PROGRAM")
print("=" * 60)

# 1. Basic Frozenset Creation from Tuples
print("\n1. BASIC FROZENSET CREATION FROM TUPLES")
print("-" * 40)

# Creating frozenset from a simple tuple
number_tuple = (1, 2, 3, 4, 5)
frozenset_numbers = frozenset(number_tuple)
print(f"Original tuple: {number_tuple}")
print(f"Frozenset from tuple: {frozenset_numbers}")
print(f"Tuple type: {type(number_tuple)}")
print(f"Frozenset type: {type(frozenset_numbers)}")

# 2. Frozenset from Different Types of Tuples
print("\n2. FROZENSET FROM DIFFERENT TYPES OF TUPLES")
print("-" * 40)

# String tuple
string_tuple = ("apple", "banana", "cherry", "date", "elderberry")
frozenset_strings = frozenset(string_tuple)
print(f"String tuple: {string_tuple}")
print(f"Frozenset from strings: {frozenset_strings}")

# Mixed data type tuple
mixed_tuple = (1, "hello", 3.14, True, "world", 42)
frozenset_mixed = frozenset(mixed_tuple)
print(f"Mixed tuple: {mixed_tuple}")
print(f"Frozenset from mixed: {frozenset_mixed}")

# Tuple with different numeric types
numeric_tuple = (1, 2.5, 3, 4.8, 5)
frozenset_numeric = frozenset(numeric_tuple)
print(f"Numeric tuple: {numeric_tuple}")
print(f"Frozenset from numeric: {frozenset_numeric}")

# 3. Handling Duplicates in Tuples
print("\n3. HANDLING DUPLICATES IN TUPLES")
print("-" * 40)

# Tuple with duplicates
duplicate_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 1, 2, 3)
frozenset_no_duplicates = frozenset(duplicate_tuple)
print(f"Tuple with duplicates: {duplicate_tuple}")
print(f"Frozenset (duplicates removed): {frozenset_no_duplicates}")
print(f"Original tuple length: {len(duplicate_tuple)}")
print(f"Frozenset length: {len(frozenset_no_duplicates)}")

# Character duplicates from string-like tuple
char_tuple = ('a', 'b', 'c', 'a', 'b', 'd', 'e', 'a')
frozenset_chars = frozenset(char_tuple)
print(f"Character tuple: {char_tuple}")
print(f"Frozenset from chars: {frozenset_chars}")

# 4. Empty Tuple to Frozenset
print("\n4. EMPTY TUPLE TO FROZENSET")
print("-" * 40)

empty_tuple = ()
frozenset_empty = frozenset(empty_tuple)
print(f"Empty tuple: {empty_tuple}")
print(f"Frozenset from empty tuple: {frozenset_empty}")
print(f"Is empty frozenset: {len(frozenset_empty) == 0}")

# 5. Nested Tuples (Advantage over Lists)
print("\n5. NESTED TUPLES (ADVANTAGE OVER LISTS)")
print("-" * 40)

# Nested tuples work fine (unlike lists)
nested_tuple = ((1, 2), (3, 4), (5, 6), (7, 8))
print(f"Nested tuple: {nested_tuple}")
frozenset_nested = frozenset(nested_tuple)
print(f"Frozenset from nested tuple: {frozenset_nested}")

# More complex nested structures
complex_nested = ((1, 'a'), (2, 'b'), (3, 'c'), (1, 'a'))  # With duplicate
frozenset_complex = frozenset(complex_nested)
print(f"Complex nested tuple: {complex_nested}")
print(f"Frozenset (duplicates removed): {frozenset_complex}")

# Coordinates example
coordinates = ((0, 0), (1, 1), (2, 2), (3, 3), (0, 0))
frozenset_coords = frozenset(coordinates)
print(f"Coordinate tuple: {coordinates}")
print(f"Unique coordinates: {frozenset_coords}")

# 6. Operations with Frozensets from Tuples
print("\n6. OPERATIONS WITH FROZENSETS FROM TUPLES")
print("-" * 40)

# Create frozensets from different tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
tuple3 = (1, 3, 5, 7, 9)

fs1: frozenset[int] = frozenset(tuple1)
fs2: frozenset[int] = frozenset(tuple2)
fs3: frozenset[int] = frozenset(tuple3)

print(f"Tuple 1: {tuple1} -> Frozenset 1: {fs1}")
print(f"Tuple 2: {tuple2} -> Frozenset 2: {fs2}")
print(f"Tuple 3: {tuple3} -> Frozenset 3: {fs3}")

# Union
union_result = fs1.union(fs2)
print(f"Union of fs1 and fs2: {union_result}")

# Intersection
intersection_result = fs1.intersection(fs2)
print(f"Intersection of fs1 and fs2: {intersection_result}")

# Difference
difference_result = fs1.difference(fs2)
print(f"Difference of fs1 and fs2: {difference_result}")

# Symmetric difference
symmetric_diff = fs1.symmetric_difference(fs2)
print(f"Symmetric difference of fs1 and fs2: {symmetric_diff}")

# Triple intersection
triple_intersection = fs1.intersection(fs2, fs3)
print(f"Triple intersection (fs1, fs2, fs3): {triple_intersection}")

# 7. Membership Testing
print("\n7. MEMBERSHIP TESTING")
print("-" * 40)

test_tuple = (10, 20, 30, 40, 50, 60)
test_frozenset = frozenset(test_tuple)
print(f"Test frozenset: {test_frozenset}")

# Test membership
test_values = (10, 25, 30, 35, 50, 75)
print(f"Testing values: {test_values}")
for value in test_values:
    status = "✓" if value in test_frozenset else "✗"
    print(f"{status} {value} {'is' if value in test_frozenset else 'is NOT'} in the frozenset")

# 8. Comparison Operations
print("\n8. COMPARISON OPERATIONS")
print("-" * 40)

small_tuple = (1, 2, 3)
large_tuple = (1, 2, 3, 4, 5, 6)
different_tuple = (7, 8, 9)
overlapping_tuple = (2, 3, 4)

small_fs: frozenset[int] = frozenset(small_tuple)
large_fs: frozenset[int] = frozenset(large_tuple)
different_fs: frozenset[int] = frozenset(different_tuple)
overlapping_fs: frozenset[int] = frozenset(overlapping_tuple)

print(f"Small frozenset: {small_fs}")
print(f"Large frozenset: {large_fs}")
print(f"Different frozenset: {different_fs}")
print(f"Overlapping frozenset: {overlapping_fs}")

# Various comparisons
print(f"Is small_fs subset of large_fs? {small_fs.issubset(large_fs)}")
print(f"Is large_fs superset of small_fs? {large_fs.issuperset(small_fs)}")
print(f"Are small_fs and different_fs disjoint? {small_fs.isdisjoint(different_fs)}")
print(f"Are small_fs and overlapping_fs disjoint? {small_fs.isdisjoint(overlapping_fs)}")

# 9. Practical Examples
print("\n9. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Database status codes
success_codes = (200, 201, 202, 204)
client_error_codes = (400, 401, 403, 404, 409)
server_error_codes = (500, 501, 502, 503, 504)

success_fs = frozenset(success_codes)
client_error_fs = frozenset(client_error_codes)
server_error_fs = frozenset(server_error_codes)

print(f"Success codes: {success_fs}")
print(f"Client error codes: {client_error_fs}")
print(f"Server error codes: {server_error_fs}")

# Test some status codes
test_codes = (200, 404, 500, 301, 403)
print(f"\nTesting status codes: {test_codes}")
for code in test_codes:
    if code in success_fs:
        print(f"✓ {code}: Success")
    elif code in client_error_fs:
        print(f"⚠ {code}: Client Error")
    elif code in server_error_fs:
        print(f"✗ {code}: Server Error")
    else:
        print(f"? {code}: Unknown status")

# Example 2: Valid chess positions
valid_files = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
valid_ranks = ('1', '2', '3', '4', '5', '6', '7', '8')

files_fs = frozenset(valid_files)
ranks_fs = frozenset(valid_ranks)

print(f"\nValid chess files: {files_fs}")
print(f"Valid chess ranks: {ranks_fs}")

# Test chess positions
test_positions = (('a', '1'), ('h', '8'), ('i', '1'), ('a', '9'), ('d', '4'))
print(f"Testing chess positions: {test_positions}")
for file, rank in test_positions:
    if file in files_fs and rank in ranks_fs:
        print(f"✓ {file}{rank}: Valid position")
    else:
        print(f"✗ {file}{rank}: Invalid position")

# Example 3: Color combinations
primary_colors = ('red', 'blue', 'yellow')
secondary_colors = ('green', 'orange', 'purple')
warm_colors = ('red', 'orange', 'yellow')
cool_colors = ('blue', 'green', 'purple')

primary_fs = frozenset(primary_colors)
secondary_fs = frozenset(secondary_colors)
warm_fs = frozenset(warm_colors)
cool_fs = frozenset(cool_colors)

print(f"\nPrimary colors: {primary_fs}")
print(f"Secondary colors: {secondary_fs}")
print(f"Warm colors: {warm_fs}")
print(f"Cool colors: {cool_fs}")

# Color analysis
all_colors = primary_fs.union(secondary_fs)
warm_primary = primary_fs.intersection(warm_fs)
cool_secondary = secondary_fs.intersection(cool_fs)

print(f"All colors: {all_colors}")
print(f"Warm primary colors: {warm_primary}")
print(f"Cool secondary colors: {cool_secondary}")

# 10. Converting Back to Tuple
print("\n10. CONVERTING FROZENSET BACK TO TUPLE")
print("-" * 40)

original_tuple = (9, 3, 7, 1, 5, 8, 2, 6, 4)
fs_from_tuple = frozenset(original_tuple)
back_to_tuple = tuple(fs_from_tuple)
sorted_tuple = tuple(sorted(fs_from_tuple))

print(f"Original tuple: {original_tuple}")
print(f"Frozenset: {fs_from_tuple}")
print(f"Back to tuple: {back_to_tuple}")
print(f"Sorted tuple: {sorted_tuple}")

# Preserving nested structure
nested_original = ((1, 2), (3, 4), (5, 6), (1, 2))
nested_fs = frozenset(nested_original)
nested_back = tuple(nested_fs)
nested_sorted = tuple(sorted(nested_fs))

print(f"\nNested original: {nested_original}")
print(f"Nested frozenset: {nested_fs}")
print(f"Nested back to tuple: {nested_back}")
print(f"Nested sorted: {nested_sorted}")

# 11. Tuple vs List Performance Comparison
print("\n11. TUPLE VS LIST PERFORMANCE COMPARISON")
print("-" * 40)

import time

# Create large tuple and list
size = 100000
large_tuple = tuple(range(size))
large_list = list(range(size))

print(f"Testing with {size} elements...")

# Time frozenset creation from tuple
start_time = time.time()
frozenset_from_tuple = frozenset(large_tuple)
tuple_time = time.time() - start_time

# Time frozenset creation from list
start_time = time.time()
frozenset_from_list = frozenset(large_list)
list_time = time.time() - start_time

print(f"Frozenset creation from tuple: {tuple_time:.6f} seconds")
print(f"Frozenset creation from list: {list_time:.6f} seconds")
print(f"Tuple is {list_time/tuple_time:.2f}x faster" if tuple_time < list_time else f"List is {tuple_time/list_time:.2f}x faster")

# Memory usage comparison (approximate)
import sys
tuple_memory = sys.getsizeof(large_tuple)
list_memory = sys.getsizeof(large_list)
frozenset_memory = sys.getsizeof(frozenset_from_tuple)

print(f"\nMemory usage:")
print(f"Tuple: {tuple_memory:,} bytes")
print(f"List: {list_memory:,} bytes")
print(f"Frozenset: {frozenset_memory:,} bytes")

# 12. Advantages of Tuples for Frozensets
print("\n12. ADVANTAGES OF TUPLES FOR FROZENSETS")
print("-" * 40)

print("✓ Tuples are immutable (like frozensets)")
print("✓ Tuples are hashable (can be frozenset elements)")
print("✓ Tuples are generally faster to create")
print("✓ Tuples use less memory")
print("✓ Tuples can contain nested structures")
print("✓ Tuples are perfect for coordinate pairs, database records")

# Example: Using tuples as frozenset elements
coordinate_tuples = ((0, 0), (1, 1), (2, 2), (3, 3))
coordinate_frozenset = frozenset(coordinate_tuples)
print(f"\nCoordinate frozenset: {coordinate_frozenset}")

# This wouldn't work with lists:
# coordinate_lists = [[0, 0], [1, 1], [2, 2], [3, 3]]
# coordinate_frozenset = frozenset(coordinate_lists)  # ERROR!

# 13. Real-world Use Cases
print("\n13. REAL-WORLD USE CASES")
print("-" * 40)

# Database connection parameters
db_configs = (
    ('host', 'localhost'),
    ('port', 5432),
    ('database', 'mydb'),
    ('user', 'admin')
)
required_params = frozenset(db_configs)
print(f"Required DB parameters: {required_params}")

# API endpoint methods
get_methods = ('GET', 'HEAD', 'OPTIONS')
post_methods = ('POST', 'PUT', 'PATCH')
delete_methods = ('DELETE',)

safe_methods = frozenset(get_methods)
unsafe_methods = frozenset(post_methods + delete_methods)

print(f"Safe HTTP methods: {safe_methods}")
print(f"Unsafe HTTP methods: {unsafe_methods}")

# Geographic coordinates
cities = (
    ('New York', 40.7128, -74.0060),
    ('London', 51.5074, -0.1278),
    ('Tokyo', 35.6762, 139.6503),
    ('Sydney', -33.8688, 151.2093)
)
city_locations = frozenset(cities)
print(f"City locations: {city_locations}")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)
