#!/usr/bin/env python3
"""
Set Type Data Methods Program
=============================

This program demonstrates all set methods in Python including:
1. Adding Elements (add, update)
2. Removing Elements (remove, discard, pop, clear)
3. Other Useful Methods (copy, len)
4. Error handling and best practices

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

def demonstrate_adding_methods():
    """Demonstrate methods for adding elements to sets"""
    print_section("ADDING ELEMENTS TO SETS")
    
    # add() method demonstration
    print_subsection("1. add() METHOD")
    print("The add() method adds a single element to the set")
    
    fruits = {'apple', 'banana'}
    print(f"Original set: {fruits}")
    
    # Adding new element
    fruits.add('orange')
    print(f"After fruits.add('orange'): {fruits}")
    
    # Adding duplicate element (no effect)
    fruits.add('apple')
    print(f"After fruits.add('apple') [duplicate]: {fruits}")
    
    # Adding different data types
    mixed_set: set = {1, 2, 3}  # Explicit type annotation allows mixed types
    print(f"\nMixed set: {mixed_set}")
    mixed_set.add('hello')
    print(f"After mixed_set.add('hello'): {mixed_set}")
    mixed_set.add(3.14)
    print(f"After mixed_set.add(3.14): {mixed_set}")
    mixed_set.add(True)
    print(f"After mixed_set.add(True): {mixed_set}")
    
    # update() method demonstration
    print_subsection("2. update() METHOD")
    print("The update() method adds multiple elements from any iterable")
    
    numbers = {1, 2, 3}
    print(f"Original set: {numbers}")
    
    # Update with list
    numbers.update([4, 5, 6])
    print(f"After numbers.update([4, 5, 6]): {numbers}")
    
    # Update with tuple
    numbers.update((7, 8, 9))
    print(f"After numbers.update((7, 8, 9)): {numbers}")
    
    # Update with string (adds each character)
    letters = {'a', 'b'}
    print(f"\nLetters set: {letters}")
    letters.update('cde')
    print(f"After letters.update('cde'): {letters}")
    
    # Update with multiple iterables
    colors = {'red', 'green'}
    print(f"\nColors set: {colors}")
    colors.update(['blue', 'yellow'], {'purple', 'orange'}, ('black', 'white'))
    print(f"After updating with multiple iterables: {colors}")
    
    # Update with another set
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    print(f"\nset1: {set1}")
    print(f"set2: {set2}")
    set1.update(set2)
    print(f"After set1.update(set2): {set1}")

def demonstrate_removing_methods():
    """Demonstrate methods for removing elements from sets"""
    print_section("REMOVING ELEMENTS FROM SETS")
    
    # remove() method demonstration
    print_subsection("1. remove() METHOD")
    print("The remove() method removes a specified element (raises KeyError if not found)")
    
    fruits = {'apple', 'banana', 'orange', 'grape'}
    print(f"Original set: {fruits}")
    
    # Remove existing element
    fruits.remove('banana')
    print(f"After fruits.remove('banana'): {fruits}")
    
    # Demonstrate error handling
    print(f"\nTrying to remove 'mango' (not in set):")
    try:
        fruits.remove('mango')
    except KeyError as e:
        print(f"KeyError caught: {e}")
    
    print(f"Set remains unchanged: {fruits}")
    
    # discard() method demonstration
    print_subsection("2. discard() METHOD")
    print("The discard() method removes a specified element (no error if not found)")
    
    animals = {'cat', 'dog', 'bird', 'fish'}
    print(f"Original set: {animals}")
    
    # Discard existing element
    animals.discard('bird')
    print(f"After animals.discard('bird'): {animals}")
    
    # Discard non-existent element (no error)
    animals.discard('elephant')
    print(f"After animals.discard('elephant') [not in set]: {animals}")
    
    # pop() method demonstration
    print_subsection("3. pop() METHOD")
    print("The pop() method removes and returns an arbitrary element")
    
    numbers = {1, 2, 3, 4, 5}
    print(f"Original set: {numbers}")
    
    # Pop elements one by one
    for i in range(3):
        popped = numbers.pop()
        print(f"Popped element: {popped}, Remaining set: {numbers}")
    
    # Demonstrate error with empty set
    empty_set = set()
    print(f"\nTrying to pop from empty set:")
    try:
        empty_set.pop()
    except KeyError as e:
        print(f"KeyError caught: {e}")
    
    # clear() method demonstration
    print_subsection("4. clear() METHOD")
    print("The clear() method removes all elements from the set")
    
    languages = {'Python', 'Java', 'C++', 'JavaScript'}
    print(f"Original set: {languages}")
    print(f"Set length: {len(languages)}")
    
    languages.clear()
    print(f"After languages.clear(): {languages}")
    print(f"Set length after clear: {len(languages)}")

def demonstrate_other_methods():
    """Demonstrate other useful set methods"""
    print_section("OTHER USEFUL SET METHODS")
    
    # copy() method demonstration
    print_subsection("1. copy() METHOD")
    print("The copy() method creates a shallow copy of the set")
    
    original = {1, 2, 3, 4, 5}
    copied = original.copy()
    
    print(f"Original set: {original}")
    print(f"Copied set: {copied}")
    print(f"Are they the same object? {original is copied}")
    print(f"Are they equal? {original == copied}")
    
    # Modify original to show they're independent
    original.add(6)
    print(f"After adding 6 to original: {original}")
    print(f"Copied set remains unchanged: {copied}")
    
    # len() function demonstration
    print_subsection("2. len() FUNCTION")
    print("The len() function returns the number of elements in the set")
    
    test_sets = [
        set(),
        {1},
        {1, 2, 3},
        {'a', 'b', 'c', 'd', 'e'},
        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    ]
    
    for i, test_set in enumerate(test_sets):
        print(f"Set {i+1}: {test_set}")
        print(f"Length: {len(test_set)}")
        print()

def demonstrate_method_chaining():
    """Demonstrate method chaining and combining operations"""
    print_section("METHOD CHAINING AND COMBINATIONS")
    
    print("Demonstrating various method combinations and patterns")
    
    # Building a set step by step
    print_subsection("Building a Set Step by Step")
    my_set = set()
    print(f"Start with empty set: {my_set}")
    
    # Add individual elements
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    print(f"After adding 1, 2, 3: {my_set}")
    
    # Update with multiple elements
    my_set.update([4, 5, 6])
    print(f"After updating with [4, 5, 6]: {my_set}")
    
    # Remove some elements
    my_set.discard(2)
    my_set.discard(5)
    print(f"After discarding 2 and 5: {my_set}")
    
    # Copy and modify
    copy_set = my_set.copy()
    copy_set.update([10, 11, 12])
    print(f"Original set: {my_set}")
    print(f"Modified copy: {copy_set}")

def demonstrate_practical_examples():
    """Demonstrate practical real-world examples"""
    print_section("PRACTICAL REAL-WORLD EXAMPLES")
    
    # Example 1: Managing a shopping cart
    print_subsection("Example 1: Shopping Cart Management")
    cart = set()
    
    # Add items to cart
    cart.add('milk')
    cart.add('bread')
    cart.add('eggs')
    print(f"Initial cart: {cart}")
    
    # Add more items
    cart.update(['butter', 'cheese', 'yogurt'])
    print(f"After adding dairy products: {cart}")
    
    # Remove an item (customer changed mind)
    cart.discard('yogurt')
    print(f"After removing yogurt: {cart}")
    
    # Try to remove item that might not be there
    cart.discard('chocolate')  # Safe removal
    print(f"After trying to remove chocolate: {cart}")
    
    print(f"Final cart has {len(cart)} items")
    
    # Example 2: Managing user permissions
    print_subsection("Example 2: User Permission Management")
    user_permissions = set()
    
    # Add basic permissions
    user_permissions.update(['read', 'write'])
    print(f"Basic permissions: {user_permissions}")
    
    # Promote user - add admin permissions
    admin_permissions = {'delete', 'modify_users', 'system_config'}
    user_permissions.update(admin_permissions)
    print(f"After promotion: {user_permissions}")
    
    # Revoke specific permission
    user_permissions.discard('system_config')
    print(f"After revoking system_config: {user_permissions}")
    
    # Check permission count
    print(f"User has {len(user_permissions)} permissions")
    
    # Example 3: Unique visitor tracking
    print_subsection("Example 3: Unique Visitor Tracking")
    visitors = set()
    
    # Simulate visitors (IDs)
    daily_visits = [101, 102, 103, 101, 104, 102, 105, 103, 106]
    
    for visitor_id in daily_visits:
        visitors.add(visitor_id)
        print(f"Visitor {visitor_id} visited. Unique visitors: {len(visitors)}")
    
    print(f"Final unique visitors: {visitors}")
    print(f"Total unique visitors today: {len(visitors)}")

def demonstrate_error_handling():
    """Demonstrate proper error handling with set methods"""
    print_section("ERROR HANDLING AND BEST PRACTICES")
    
    print_subsection("Safe Remove Operations")
    
    my_set = {1, 2, 3, 4, 5}
    items_to_remove = [2, 6, 4, 8, 1]
    
    print(f"Original set: {my_set}")
    print(f"Items to remove: {items_to_remove}")
    
    # Method 1: Using discard() (safe)
    print("\nMethod 1: Using discard() - Safe approach")
    temp_set = my_set.copy()
    for item in items_to_remove:
        temp_set.discard(item)
        print(f"Attempted to remove {item}: {temp_set}")
    
    # Method 2: Using remove() with error handling
    print("\nMethod 2: Using remove() with try-except")
    temp_set = my_set.copy()
    for item in items_to_remove:
        try:
            temp_set.remove(item)
            print(f"Successfully removed {item}: {temp_set}")
        except KeyError:
            print(f"Item {item} not found in set: {temp_set}")
    
    # Method 3: Check membership first
    print("\nMethod 3: Check membership before removing")
    temp_set = my_set.copy()
    for item in items_to_remove:
        if item in temp_set:
            temp_set.remove(item)
            print(f"Removed {item}: {temp_set}")
        else:
            print(f"Item {item} not in set: {temp_set}")
    
    print_subsection("Handling Immutable Elements")
    
    # Demonstrate adding tuples (immutable) vs lists (mutable)
    valid_set = set()
    
    # Valid: adding tuples (immutable)
    valid_set.add((1, 2, 3))
    valid_set.add((4, 5, 6))
    print(f"Set with tuples: {valid_set}")
    
    # Invalid: trying to add lists (mutable)
    print("\nTrying to add mutable objects:")
    try:
        valid_set.add([1, 2, 3])
    except TypeError as e:
        print(f"TypeError caught: {e}")
    
    print("Solution: Convert list to tuple")
    my_list = [7, 8, 9]
    valid_set.add(tuple(my_list))
    print(f"After adding tuple(my_list): {valid_set}")

def demonstrate_performance_tips():
    """Demonstrate performance tips for set methods"""
    print_section("PERFORMANCE TIPS")
    
    import time
    
    # Tip 1: Use update() instead of multiple add() calls
    print_subsection("Tip 1: update() vs multiple add() calls")
    
    data = list(range(1000))
    
    # Method 1: Multiple add() calls
    start_time = time.time()
    set1 = set()
    for item in data:
        set1.add(item)
    time1 = time.time() - start_time
    
    # Method 2: Single update() call
    start_time = time.time()
    set2 = set()
    set2.update(data)
    time2 = time.time() - start_time
    
    print(f"Multiple add() calls: {time1:.6f} seconds")
    print(f"Single update() call: {time2:.6f} seconds")
    print(f"update() is {time1/time2:.2f}x faster")
    
    # Tip 2: Use discard() for safe removal
    print_subsection("Tip 2: discard() vs remove() with error handling")
    
    test_set = set(range(100))
    items_to_remove = [50, 150, 75, 200, 25]  # Some exist, some don't
    
    # Method 1: Using discard()
    start_time = time.time()
    temp_set1 = test_set.copy()
    for item in items_to_remove:
        temp_set1.discard(item)
    time1 = time.time() - start_time
    
    # Method 2: Using remove() with try-except
    start_time = time.time()
    temp_set2 = test_set.copy()
    for item in items_to_remove:
        try:
            temp_set2.remove(item)
        except KeyError:
            pass
    time2 = time.time() - start_time
    
    print(f"discard() method: {time1:.6f} seconds")
    print(f"remove() with try-except: {time2:.6f} seconds")
    print(f"discard() is {time2/time1:.2f}x faster")

def main():
    """Main function to run all demonstrations"""
    print("SET TYPE DATA METHODS PROGRAM")
    print("=" * 60)
    print("This program demonstrates all set methods in Python")
    
    # Run all demonstrations
    demonstrate_adding_methods()
    demonstrate_removing_methods()
    demonstrate_other_methods()
    demonstrate_method_chaining()
    demonstrate_practical_examples()
    demonstrate_error_handling()
    demonstrate_performance_tips()
    
    print_section("PROGRAM COMPLETED")
    print("All set methods have been demonstrated!")
    print("Key takeaways:")
    print("• Use add() for single elements, update() for multiple elements")
    print("• Use discard() for safe removal, remove() when you're sure element exists")
    print("• Use pop() to remove arbitrary elements, clear() to empty the set")
    print("• Always handle KeyError when using remove() or pop() on potentially empty sets")
    print("• Sets only accept immutable elements (strings, numbers, tuples)")

if __name__ == "__main__":
    main() 