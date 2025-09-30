# Frozenset with List Program
# This program demonstrates various ways to create and work with frozensets from lists

print("=" * 60)
print("FROZENSET WITH LIST PROGRAM")
print("=" * 60)

# 1. Basic Frozenset Creation from Lists
print("\n1. BASIC FROZENSET CREATION FROM LISTS")
print("-" * 40)

# Creating frozenset from a simple list
number_list = [1, 2, 3, 4, 5]
frozenset_numbers = frozenset(number_list)
print(f"Original list: {number_list}")
print(f"Frozenset from list: {frozenset_numbers}")
print(f"Type: {type(frozenset_numbers)}")

# 2. Frozenset from Different Types of Lists
print("\n2. FROZENSET FROM DIFFERENT TYPES OF LISTS")
print("-" * 40)

# String list
string_list = ["apple", "banana", "cherry", "date"]
frozenset_strings = frozenset(string_list)
print(f"String list: {string_list}")
print(f"Frozenset from strings: {frozenset_strings}")

# Mixed data type list
mixed_list = [1, "hello", 3.14, True, "world"]
frozenset_mixed = frozenset(mixed_list)
print(f"Mixed list: {mixed_list}")
print(f"Frozenset from mixed: {frozenset_mixed}")

# 3. Handling Duplicates in Lists
print("\n3. HANDLING DUPLICATES IN LISTS")
print("-" * 40)

# List with duplicates
duplicate_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
frozenset_no_duplicates = frozenset(duplicate_list)
print(f"List with duplicates: {duplicate_list}")
print(f"Frozenset (duplicates removed): {frozenset_no_duplicates}")
print(f"Original list length: {len(duplicate_list)}")
print(f"Frozenset length: {len(frozenset_no_duplicates)}")

# 4. Empty List to Frozenset
print("\n4. EMPTY LIST TO FROZENSET")
print("-" * 40)

empty_list = []
frozenset_empty = frozenset(empty_list)
print(f"Empty list: {empty_list}")
print(f"Frozenset from empty list: {frozenset_empty}")
print(f"Is empty frozenset: {len(frozenset_empty) == 0}")

# 5. Nested Lists (Note: This will cause an error)
print("\n5. NESTED LISTS (ERROR DEMONSTRATION)")
print("-" * 40)

nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"Nested list: {nested_list}")
try:
    frozenset_nested = frozenset(nested_list)
    print(f"Frozenset from nested list: {frozenset_nested}")
except TypeError as e:
    print(f"Error: {e}")
    print("Solution: Convert inner lists to tuples")
    nested_tuples = [(1, 2), (3, 4), (5, 6)]
    frozenset_nested_fixed = frozenset(nested_tuples)
    print(f"Fixed with tuples: {frozenset_nested_fixed}")

# 6. Operations with Frozensets from Lists
print("\n6. OPERATIONS WITH FROZENSETS FROM LISTS")
print("-" * 40)

# Create frozensets from different lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [1, 3, 5, 7, 9]

fs1 = frozenset(list1)
fs2 = frozenset(list2)
fs3 = frozenset(list3)

print(f"List 1: {list1} -> Frozenset 1: {fs1}")
print(f"List 2: {list2} -> Frozenset 2: {fs2}")
print(f"List 3: {list3} -> Frozenset 3: {fs3}")

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

# 7. Membership Testing
print("\n7. MEMBERSHIP TESTING")
print("-" * 40)

test_list = [10, 20, 30, 40, 50]
test_frozenset = frozenset(test_list)
print(f"Test frozenset: {test_frozenset}")

# Test membership
test_values = [10, 25, 30, 60]
for value in test_values:
    if value in test_frozenset:
        print(f"{value} is in the frozenset")
    else:
        print(f"{value} is NOT in the frozenset")

# 8. Comparison Operations
print("\n8. COMPARISON OPERATIONS")
print("-" * 40)

small_list = [1, 2, 3]
large_list = [1, 2, 3, 4, 5, 6]
different_list = [7, 8, 9]

small_fs = frozenset(small_list)
large_fs = frozenset(large_list)
different_fs = frozenset(different_list)

print(f"Small frozenset: {small_fs}")
print(f"Large frozenset: {large_fs}")
print(f"Different frozenset: {different_fs}")

# Subset and superset
print(f"Is small_fs subset of large_fs? {small_fs.issubset(large_fs)}")
print(f"Is large_fs superset of small_fs? {large_fs.issuperset(small_fs)}")
print(f"Are small_fs and different_fs disjoint? {small_fs.isdisjoint(different_fs)}")

# 9. Practical Examples
print("\n9. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Valid file extensions
valid_extensions = ['.txt', '.pdf', '.doc', '.docx', '.py', '.java']
valid_extensions_fs = frozenset(valid_extensions)
print(f"Valid file extensions: {valid_extensions_fs}")

# Check if a file extension is valid
test_files = ['document.txt', 'image.jpg', 'script.py', 'data.csv']
for file in test_files:
    extension = '.' + file.split('.')[-1]
    if extension in valid_extensions_fs:
        print(f"✓ {file} has a valid extension")
    else:
        print(f"✗ {file} has an invalid extension")

# Example 2: User permissions
admin_permissions = ['read', 'write', 'delete', 'execute', 'admin']
user_permissions = ['read', 'write']
guest_permissions = ['read']

admin_fs = frozenset(admin_permissions)
user_fs = frozenset(user_permissions)
guest_fs = frozenset(guest_permissions)

print(f"\nAdmin permissions: {admin_fs}")
print(f"User permissions: {user_fs}")
print(f"Guest permissions: {guest_fs}")

# Check permission hierarchy
print(f"User is subset of Admin: {user_fs.issubset(admin_fs)}")
print(f"Guest is subset of User: {guest_fs.issubset(user_fs)}")

# Example 3: Data analysis - finding common elements
survey1_responses = [1, 2, 3, 4, 5, 3, 2, 1, 4, 5]
survey2_responses = [3, 4, 5, 6, 7, 4, 3, 5, 6, 7]

unique_survey1 = frozenset(survey1_responses)
unique_survey2 = frozenset(survey2_responses)

print(f"\nSurvey 1 unique responses: {unique_survey1}")
print(f"Survey 2 unique responses: {unique_survey2}")
print(f"Common responses: {unique_survey1.intersection(unique_survey2)}")
print(f"Responses only in survey 1: {unique_survey1.difference(unique_survey2)}")
print(f"Responses only in survey 2: {unique_survey2.difference(unique_survey1)}")

# 10. Converting Back to List
print("\n10. CONVERTING FROZENSET BACK TO LIST")
print("-" * 40)

original_list = [5, 3, 8, 1, 9, 2, 7, 4, 6]
fs_from_list = frozenset(original_list)
back_to_list = list(fs_from_list)
sorted_list = sorted(back_to_list)

print(f"Original list: {original_list}")
print(f"Frozenset: {fs_from_list}")
print(f"Back to list: {back_to_list}")
print(f"Sorted list: {sorted_list}")

# 11. Performance Comparison
print("\n11. PERFORMANCE COMPARISON")
print("-" * 40)

import time

# Create a large list
large_list = list(range(1000000))
print(f"Testing with {len(large_list)} elements...")

# Time list creation
start_time = time.time()
test_list = large_list.copy()
list_time = time.time() - start_time

# Time frozenset creation
start_time = time.time()
test_frozenset = frozenset(large_list)
frozenset_time = time.time() - start_time

# Time membership testing
test_value = 500000

start_time = time.time()
result_list = test_value in test_list
list_membership_time = time.time() - start_time

start_time = time.time()
result_frozenset = test_value in test_frozenset
frozenset_membership_time = time.time() - start_time

print(f"List creation time: {list_time:.6f} seconds")
print(f"Frozenset creation time: {frozenset_time:.6f} seconds")
print(f"List membership test time: {list_membership_time:.6f} seconds")
print(f"Frozenset membership test time: {frozenset_membership_time:.6f} seconds")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)
