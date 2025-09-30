#!/usr/bin/env python3
"""
Set Type Data Operations Program
================================

This program demonstrates various set operations in Python including:
1. Mathematical Operations (Union, Intersection, Difference, Symmetric Difference)
2. Membership Testing
3. Subset and Superset Operations
4. Method vs Operator syntax comparison

Author: Python Learning Series
"""

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"{title:^60}")
    print(f"{'='*60}")

def print_subsection(title):
    """Print a formatted subsection header"""
    print(f"\n{'-'*40}")
    print(f"{title}")
    print(f"{'-'*40}")

def demonstrate_mathematical_operations():
    """Demonstrate mathematical set operations"""
    print_section("MATHEMATICAL SET OPERATIONS")
    
    # Sample sets for demonstration
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {1, 2, 3}
    set4 = {9, 10, 11}
    
    print("Sample Sets:")
    print(f"set1 = {set1}")
    print(f"set2 = {set2}")
    print(f"set3 = {set3}")
    print(f"set4 = {set4}")
    
    # Union Operation
    print_subsection("1. UNION OPERATION")
    print("Union combines all unique elements from both sets")
    print(f"set1.union(set2) = {set1.union(set2)}")
    print(f"set1 | set2 = {set1 | set2}")
    print(f"set1.union(set2, set3) = {set1.union(set2, set3)}")
    
    # Intersection Operation
    print_subsection("2. INTERSECTION OPERATION")
    print("Intersection returns elements common to both sets")
    print(f"set1.intersection(set2) = {set1.intersection(set2)}")
    print(f"set1 & set2 = {set1 & set2}")
    print(f"set1.intersection(set3) = {set1.intersection(set3)}")
    print(f"set1 & set3 = {set1 & set3}")
    
    # Difference Operation
    print_subsection("3. DIFFERENCE OPERATION")
    print("Difference returns elements in first set but not in second")
    print(f"set1.difference(set2) = {set1.difference(set2)}")
    print(f"set1 - set2 = {set1 - set2}")
    print(f"set2.difference(set1) = {set2.difference(set1)}")
    print(f"set2 - set1 = {set2 - set1}")
    
    # Symmetric Difference Operation
    print_subsection("4. SYMMETRIC DIFFERENCE OPERATION")
    print("Symmetric difference returns elements in either set, but not both")
    print(f"set1.symmetric_difference(set2) = {set1.symmetric_difference(set2)}")
    print(f"set1 ^ set2 = {set1 ^ set2}")
    print(f"set1.symmetric_difference(set4) = {set1.symmetric_difference(set4)}")
    print(f"set1 ^ set4 = {set1 ^ set4}")

def demonstrate_membership_testing():
    """Demonstrate membership testing operations"""
    print_section("MEMBERSHIP TESTING")
    
    fruits = {'apple', 'banana', 'orange', 'grape', 'kiwi'}
    print(f"fruits = {fruits}")
    
    # Test various elements
    test_items = ['apple', 'mango', 'banana', 'pear', 'orange']
    
    print(f"\nTesting membership for items: {test_items}")
    print("-" * 50)
    
    for item in test_items:
        in_set = item in fruits
        not_in_set = item not in fruits
        print(f"'{item}' in fruits: {in_set}")
        print(f"'{item}' not in fruits: {not_in_set}")
        print()

def demonstrate_subset_superset_operations():
    """Demonstrate subset and superset operations"""
    print_section("SUBSET AND SUPERSET OPERATIONS")
    
    # Create sample sets with clear relationships
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_numbers = {2, 4, 6, 8, 10}
    odd_numbers = {1, 3, 5, 7, 9}
    small_numbers = {1, 2, 3}
    separate_numbers = {11, 12, 13}
    
    print("Sample Sets:")
    print(f"numbers = {numbers}")
    print(f"even_numbers = {even_numbers}")
    print(f"odd_numbers = {odd_numbers}")
    print(f"small_numbers = {small_numbers}")
    print(f"separate_numbers = {separate_numbers}")
    
    # Subset Operations
    print_subsection("SUBSET OPERATIONS")
    print("A subset contains only elements that are also in the superset")
    print(f"even_numbers.issubset(numbers) = {even_numbers.issubset(numbers)}")
    print(f"even_numbers <= numbers = {even_numbers <= numbers}")
    print(f"small_numbers.issubset(numbers) = {small_numbers.issubset(numbers)}")
    print(f"small_numbers <= numbers = {small_numbers <= numbers}")
    print(f"separate_numbers.issubset(numbers) = {separate_numbers.issubset(numbers)}")
    print(f"separate_numbers <= numbers = {separate_numbers <= numbers}")
    
    # Superset Operations
    print_subsection("SUPERSET OPERATIONS")
    print("A superset contains all elements of the subset")
    print(f"numbers.issuperset(even_numbers) = {numbers.issuperset(even_numbers)}")
    print(f"numbers >= even_numbers = {numbers >= even_numbers}")
    print(f"numbers.issuperset(small_numbers) = {numbers.issuperset(small_numbers)}")
    print(f"numbers >= small_numbers = {numbers >= small_numbers}")
    print(f"even_numbers.issuperset(numbers) = {even_numbers.issuperset(numbers)}")
    print(f"even_numbers >= numbers = {even_numbers >= numbers}")
    
    # Disjoint Operations
    print_subsection("DISJOINT OPERATIONS")
    print("Disjoint sets have no common elements")
    print(f"even_numbers.isdisjoint(odd_numbers) = {even_numbers.isdisjoint(odd_numbers)}")
    print(f"even_numbers.isdisjoint(small_numbers) = {even_numbers.isdisjoint(small_numbers)}")
    print(f"numbers.isdisjoint(separate_numbers) = {numbers.isdisjoint(separate_numbers)}")

def demonstrate_complex_operations():
    """Demonstrate complex set operations with real-world examples"""
    print_section("COMPLEX SET OPERATIONS - REAL WORLD EXAMPLES")
    
    # Example 1: Student courses
    print_subsection("Example 1: Student Course Analysis")
    alice_courses = {'Math', 'Physics', 'Chemistry', 'Biology'}
    bob_courses = {'Math', 'Chemistry', 'English', 'History'}
    charlie_courses = {'Physics', 'Biology', 'English', 'Art'}
    
    print(f"Alice's courses: {alice_courses}")
    print(f"Bob's courses: {bob_courses}")
    print(f"Charlie's courses: {charlie_courses}")
    
    # Common courses between Alice and Bob
    common_alice_bob = alice_courses & bob_courses
    print(f"\nCommon courses (Alice & Bob): {common_alice_bob}")
    
    # All courses taken by at least one student
    all_courses = alice_courses | bob_courses | charlie_courses
    print(f"All courses: {all_courses}")
    
    # Courses only Alice takes
    alice_only = alice_courses - bob_courses - charlie_courses
    print(f"Courses only Alice takes: {alice_only}")
    
    # Courses taken by exactly two students
    alice_bob_only = (alice_courses & bob_courses) - charlie_courses
    alice_charlie_only = (alice_courses & charlie_courses) - bob_courses
    bob_charlie_only = (bob_courses & charlie_courses) - alice_courses
    
    print(f"Courses taken by Alice & Bob only: {alice_bob_only}")
    print(f"Courses taken by Alice & Charlie only: {alice_charlie_only}")
    print(f"Courses taken by Bob & Charlie only: {bob_charlie_only}")
    
    # Example 2: Programming languages
    print_subsection("Example 2: Programming Language Skills")
    frontend_languages = {'JavaScript', 'TypeScript', 'HTML', 'CSS'}
    backend_languages = {'Python', 'Java', 'JavaScript', 'C++', 'Go'}
    mobile_languages = {'Swift', 'Kotlin', 'JavaScript', 'Dart'}
    
    print(f"Frontend languages: {frontend_languages}")
    print(f"Backend languages: {backend_languages}")
    print(f"Mobile languages: {mobile_languages}")
    
    # Cross-platform languages
    cross_platform = frontend_languages & backend_languages & mobile_languages
    print(f"\nCross-platform languages: {cross_platform}")
    
    # Web development languages
    web_languages = frontend_languages | backend_languages
    print(f"Web development languages: {web_languages}")
    
    # Languages unique to each domain
    frontend_only = frontend_languages - backend_languages - mobile_languages
    backend_only = backend_languages - frontend_languages - mobile_languages
    mobile_only = mobile_languages - frontend_languages - backend_languages
    
    print(f"Frontend-only languages: {frontend_only}")
    print(f"Backend-only languages: {backend_only}")
    print(f"Mobile-only languages: {mobile_only}")

def demonstrate_method_vs_operator():
    """Demonstrate the difference between method and operator syntax"""
    print_section("METHOD VS OPERATOR SYNTAX")
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    list1 = [5, 6, 7, 8]
    
    print(f"set1 = {set1}")
    print(f"set2 = {set2}")
    print(f"list1 = {list1}")
    
    print_subsection("METHODS (Work with any iterable)")
    print(f"set1.union(set2) = {set1.union(set2)}")
    print(f"set1.union(list1) = {set1.union(list1)}")
    print(f"set1.intersection(set2) = {set1.intersection(set2)}")
    print(f"set1.intersection(list1) = {set1.intersection(list1)}")
    print(f"set1.difference(set2) = {set1.difference(set2)}")
    print(f"set1.difference(list1) = {set1.difference(list1)}")
    
    print_subsection("OPERATORS (Only work with sets)")
    print(f"set1 | set2 = {set1 | set2}")
    print(f"set1 & set2 = {set1 & set2}")
    print(f"set1 - set2 = {set1 - set2}")
    print(f"set1 ^ set2 = {set1 ^ set2}")
    
    print("\nNote: The following would raise TypeError:")
    print("# set1 | list1  # TypeError: unsupported operand type(s)")
    print("# set1 & list1  # TypeError: unsupported operand type(s)")

def demonstrate_performance_comparison():
    """Demonstrate performance differences in set operations"""
    print_section("PERFORMANCE DEMONSTRATION")
    
    import time
    
    # Create large sets for performance testing
    large_set1 = set(range(1, 10001))
    large_set2 = set(range(5000, 15001))
    large_list = list(range(5000, 15001))
    
    print(f"Testing with sets of size: {len(large_set1)} and {len(large_set2)}")
    
    # Test membership performance
    print_subsection("MEMBERSHIP TESTING PERFORMANCE")
    
    # Test with set
    start_time = time.time()
    for i in range(1000):
        result = 7500 in large_set1
    set_time = time.time() - start_time
    
    # Test with list
    start_time = time.time()
    for i in range(1000):
        result = 7500 in large_list
    list_time = time.time() - start_time
    
    print(f"Set membership test (1000 iterations): {set_time:.6f} seconds")
    print(f"List membership test (1000 iterations): {list_time:.6f} seconds")
    print(f"Set is {list_time/set_time:.2f}x faster than list for membership testing")
    
    # Test intersection performance
    print_subsection("INTERSECTION PERFORMANCE")
    
    start_time = time.time()
    intersection_result = large_set1 & large_set2
    intersection_time = time.time() - start_time
    
    print(f"Set intersection: {intersection_time:.6f} seconds")
    print(f"Intersection result size: {len(intersection_result)}")

def main():
    """Main function to run all demonstrations"""
    print("SET TYPE DATA OPERATIONS PROGRAM")
    print("=" * 60)
    print("This program demonstrates various set operations in Python")
    
    # Run all demonstrations
    demonstrate_mathematical_operations()
    demonstrate_membership_testing()
    demonstrate_subset_superset_operations()
    demonstrate_complex_operations()
    demonstrate_method_vs_operator()
    demonstrate_performance_comparison()
    
    print_section("PROGRAM COMPLETED")
    print("All set operations have been demonstrated!")
    print("Review the output above to understand set operations in Python.")

if __name__ == "__main__":
    main()
