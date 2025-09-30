#!/usr/bin/env python3
"""
Dictionary Methods Program
=========================

This program demonstrates all built-in dictionary methods with detailed examples:
1. get() - Safe value retrieval
2. keys() - Get dictionary keys
3. values() - Get dictionary values  
4. items() - Get key-value pairs
5. pop() - Remove and return value
6. popitem() - Remove and return last item
7. clear() - Remove all items
8. update() - Update dictionary
9. setdefault() - Set default value
10. fromkeys() - Create dict from keys
11. copy() - Create shallow copy

Author: Python Learning Series
"""

import copy


def print_header(title):
    """Print a formatted header for method demonstrations."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}")


def print_method_header(method_name, description):
    """Print a formatted header for individual methods."""
    print(f"\n{'-'*50}")
    print(f"  {method_name} - {description}")
    print(f"{'-'*50}")


def demonstrate_get_method():
    """Demonstrate the get() method for safe value retrieval."""
    print_method_header("get(key, default=None)", "Safe value retrieval")
    
    student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
    print(f"Student dictionary: {student}")
    
    # Basic usage
    print(f"\n1. Basic Usage:")
    print(f"   student.get('name') = {student.get('name')}")
    print(f"   student.get('age') = {student.get('age')}")
    
    # Non-existent key
    print(f"\n2. Non-existent Key:")
    print(f"   student.get('phone') = {student.get('phone')}")
    print(f"   student.get('email') = {student.get('email')}")
    
    # With default value
    print(f"\n3. With Default Value:")
    print(f"   student.get('phone', 'Not provided') = {student.get('phone', 'Not provided')}")
    print(f"   student.get('gpa', 0.0) = {student.get('gpa', 0.0)}")
    print(f"   student.get('active', True) = {student.get('active', True)}")
    
    # Comparison with direct access
    print(f"\n4. Comparison with Direct Access:")
    try:
        print(f"   student['phone'] would raise KeyError")
    except KeyError as e:
        print(f"   KeyError: {e}")
    
    print(f"   student.get('phone') safely returns: {student.get('phone')}")


def demonstrate_keys_method():
    """Demonstrate the keys() method."""
    print_method_header("keys()", "Get dictionary keys")
    
    inventory = {'apples': 50, 'bananas': 30, 'oranges': 25, 'grapes': 40}
    print(f"Inventory: {inventory}")
    
    # Get keys
    keys = inventory.keys()
    print(f"\n1. Get Keys:")
    print(f"   inventory.keys() = {keys}")
    print(f"   Type: {type(keys)}")
    print(f"   List of keys: {list(keys)}")
    
    # Iterate through keys
    print(f"\n2. Iterate Through Keys:")
    for item in inventory.keys():
        print(f"   Item: {item}")
    
    # Check if key exists
    print(f"\n3. Check Key Existence:")
    print(f"   'apples' in inventory.keys() = {'apples' in inventory.keys()}")
    print(f"   'mangoes' in inventory.keys() = {'mangoes' in inventory.keys()}")
    
    # Keys are dynamic (view object)
    print(f"\n4. Dynamic Nature of Keys:")
    print(f"   Before adding: {list(inventory.keys())}")
    inventory['mangoes'] = 15
    print(f"   After adding mangoes: {list(keys)}")  # Same keys object updates


def demonstrate_values_method():
    """Demonstrate the values() method."""
    print_method_header("values()", "Get dictionary values")
    
    grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}
    print(f"Grades: {grades}")
    
    # Get values
    values = grades.values()
    print(f"\n1. Get Values:")
    print(f"   grades.values() = {values}")
    print(f"   Type: {type(values)}")
    print(f"   List of values: {list(values)}")
    
    # Iterate through values
    print(f"\n2. Iterate Through Values:")
    for grade in grades.values():
        print(f"   Grade: {grade}")
    
    # Statistical operations
    print(f"\n3. Statistical Operations:")
    print(f"   Total: {sum(grades.values())}")
    print(f"   Average: {sum(grades.values()) / len(grades.values()):.2f}")
    print(f"   Highest: {max(grades.values())}")
    print(f"   Lowest: {min(grades.values())}")
    
    # Count occurrences
    print(f"\n4. Count Specific Values:")
    print(f"   Grades above 90: {sum(1 for grade in grades.values() if grade > 90)}")
    print(f"   Failing grades (<60): {sum(1 for grade in grades.values() if grade < 60)}")


def demonstrate_items_method():
    """Demonstrate the items() method."""
    print_method_header("items()", "Get key-value pairs")
    
    employee = {'name': 'John', 'position': 'Developer', 'salary': 75000, 'department': 'IT'}
    print(f"Employee: {employee}")
    
    # Get items
    items = employee.items()
    print(f"\n1. Get Items:")
    print(f"   employee.items() = {items}")
    print(f"   Type: {type(items)}")
    print(f"   List of items: {list(items)}")
    
    # Iterate through items
    print(f"\n2. Iterate Through Items:")
    for key, value in employee.items():
        print(f"   {key}: {value}")
    
    # Formatted display
    print(f"\n3. Formatted Display:")
    for key, value in employee.items():
        print(f"   {key.capitalize()}: {value}")
    
    # Filtering items
    print(f"\n4. Filtering Items:")
    print("   String values:")
    for key, value in employee.items():
        if isinstance(value, str):
            print(f"     {key}: {value}")
    
    print("   Numeric values:")
    for key, value in employee.items():
        if isinstance(value, (int, float)):
            print(f"     {key}: {value}")


def demonstrate_pop_method():
    """Demonstrate the pop() method."""
    print_method_header("pop(key, default)", "Remove and return value")
    
    settings = {'theme': 'dark', 'language': 'en', 'notifications': True, 'auto_save': True}
    print(f"Settings: {settings}")
    
    # Basic pop
    print(f"\n1. Basic Pop:")
    theme = settings.pop('theme')
    print(f"   Removed theme: {theme}")
    print(f"   Updated settings: {settings}")
    
    # Pop with default
    print(f"\n2. Pop with Default:")
    timeout = settings.pop('timeout', 30)
    print(f"   Timeout (with default): {timeout}")
    print(f"   Settings unchanged: {settings}")
    
    # Pop without default (KeyError)
    print(f"\n3. Pop Non-existent Key:")
    try:
        settings.pop('unknown_key')
    except KeyError as e:
        print(f"   KeyError: {e}")
    
    # Safe pop with default
    result = settings.pop('unknown_key', 'Not found')
    print(f"   Safe pop result: {result}")
    
    # Practical example: removing temporary settings
    print(f"\n4. Practical Example - Cleanup:")
    temp_settings = settings.copy()
    temp_settings.update({'temp_file': '/tmp/data', 'debug_mode': True})
    print(f"   With temp settings: {temp_settings}")
    
    # Clean up temporary settings
    temp_file = temp_settings.pop('temp_file', None)
    debug_mode = temp_settings.pop('debug_mode', False)
    print(f"   Removed temp_file: {temp_file}")
    print(f"   Removed debug_mode: {debug_mode}")
    print(f"   Clean settings: {temp_settings}")


def demonstrate_popitem_method():
    """Demonstrate the popitem() method."""
    print_method_header("popitem()", "Remove and return last item")
    
    stack = {'item1': 'first', 'item2': 'second', 'item3': 'third', 'item4': 'fourth'}
    print(f"Stack: {stack}")
    
    # Basic popitem
    print(f"\n1. Basic Popitem (LIFO - Last In, First Out):")
    while stack:
        item = stack.popitem()
        print(f"   Removed: {item}")
        print(f"   Remaining: {stack}")
    
    # Popitem on empty dictionary
    print(f"\n2. Popitem on Empty Dictionary:")
    try:
        stack.popitem()
    except KeyError as e:
        print(f"   KeyError: {e}")
    
    # Practical example: Undo functionality
    print(f"\n3. Practical Example - Undo Stack:")
    actions = {}
    
    def add_action(action, data):
        actions[len(actions)] = {'action': action, 'data': data}
        print(f"   Added action: {action}")
    
    def undo_last_action():
        if actions:
            last_action = actions.popitem()
            print(f"   Undoing: {last_action[1]}")
            return last_action[1]
        else:
            print("   No actions to undo")
            return None
    
    # Simulate some actions
    add_action('create_file', 'document.txt')
    add_action('edit_file', 'added line 1')
    add_action('edit_file', 'added line 2')
    print(f"   Current actions: {actions}")
    
    # Undo actions
    undo_last_action()
    undo_last_action()
    print(f"   Actions after undo: {actions}")


def demonstrate_clear_method():
    """Demonstrate the clear() method."""
    print_method_header("clear()", "Remove all items")
    
    data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(f"Original data: {data}")
    
    # Basic clear
    print(f"\n1. Basic Clear:")
    print(f"   Before clear: {data}")
    data.clear()
    print(f"   After clear: {data}")
    print(f"   Length: {len(data)}")
    print(f"   Is empty: {len(data) == 0}")
    
    # Clear vs reassignment
    print(f"\n2. Clear vs Reassignment:")
    dict1 = {'x': 1, 'y': 2}
    dict2 = dict1  # Same object reference
    
    print(f"   dict1: {dict1}")
    print(f"   dict2: {dict2}")
    print(f"   Same object: {dict1 is dict2}")
    
    # Clear affects all references
    dict1.clear()
    print(f"   After dict1.clear():")
    print(f"   dict1: {dict1}")
    print(f"   dict2: {dict2}")
    
    # Reassignment only affects one reference
    dict3 = {'x': 1, 'y': 2}
    dict4 = dict3
    dict3 = {}  # Reassignment
    print(f"   After dict3 = {{}}:")
    print(f"   dict3: {dict3}")
    print(f"   dict4: {dict4}")
    
    # Practical example: Reset configuration
    print(f"\n3. Practical Example - Reset Configuration:")
    config = {'host': 'localhost', 'port': 8080, 'debug': True}
    print(f"   Config before reset: {config}")
    config.clear()
    print(f"   Config after reset: {config}")


def demonstrate_update_method():
    """Demonstrate the update() method."""
    print_method_header("update(other)", "Update dictionary")
    
    user_profile = {'name': 'Alice', 'age': 25}
    print(f"User profile: {user_profile}")
    
    # Update with another dictionary
    print(f"\n1. Update with Dictionary:")
    additional_info = {'city': 'New York', 'occupation': 'Engineer'}
    user_profile.update(additional_info)
    print(f"   After update: {user_profile}")
    
    # Update with keyword arguments
    print(f"\n2. Update with Keyword Arguments:")
    user_profile.update(email='alice@email.com', phone='123-456-7890')
    print(f"   After keyword update: {user_profile}")
    
    # Update with iterable of pairs
    print(f"\n3. Update with Iterable of Pairs:")
    preferences = [('theme', 'dark'), ('language', 'en')]
    user_profile.update(preferences)
    print(f"   After iterable update: {user_profile}")
    
    # Update with mixed arguments
    print(f"\n4. Update with Mixed Arguments:")
    user_profile.update({'active': True}, notifications=False, auto_save=True)
    print(f"   After mixed update: {user_profile}")
    
    # Overwriting existing keys
    print(f"\n5. Overwriting Existing Keys:")
    print(f"   Before: age = {user_profile['age']}")
    user_profile.update({'age': 26})
    print(f"   After: age = {user_profile['age']}")
    
    # Practical example: Merging configurations
    print(f"\n6. Practical Example - Merging Configurations:")
    default_config = {'timeout': 30, 'retries': 3, 'debug': False}
    user_config = {'timeout': 60, 'api_key': 'secret123'}
    
    final_config = default_config.copy()
    final_config.update(user_config)
    print(f"   Default config: {default_config}")
    print(f"   User config: {user_config}")
    print(f"   Final config: {final_config}")


def demonstrate_setdefault_method():
    """Demonstrate the setdefault() method."""
    print_method_header("setdefault(key, default=None)", "Set default value")
    
    inventory = {'apples': 50, 'bananas': 30}
    print(f"Inventory: {inventory}")
    
    # Key exists
    print(f"\n1. Key Exists:")
    result = inventory.setdefault('apples', 0)
    print(f"   setdefault('apples', 0) = {result}")
    print(f"   Inventory: {inventory}")
    
    # Key doesn't exist
    print(f"\n2. Key Doesn't Exist:")
    result = inventory.setdefault('oranges', 25)
    print(f"   setdefault('oranges', 25) = {result}")
    print(f"   Inventory: {inventory}")
    
    # Default value is None
    print(f"\n3. Default Value is None:")
    result = inventory.setdefault('grapes', 0)
    print(f"   setdefault('grapes') = {result}")
    print(f"   Inventory: {inventory}")
    
    # Practical example: Counting occurrences
    print(f"\n4. Practical Example - Counting Occurrences:")
    text = "hello world hello python world"
    word_count = {}
    
    for word in text.split():
        word_count.setdefault(word, 0)
        word_count[word] += 1
    
    print(f"   Word count: {word_count}")
    
    # Grouping data
    print(f"\n5. Practical Example - Grouping Data:")
    students = [
        {'name': 'Alice', 'grade': 'A'},
        {'name': 'Bob', 'grade': 'B'},
        {'name': 'Charlie', 'grade': 'A'},
        {'name': 'Diana', 'grade': 'B'}
    ]
    
    grouped = {}
    for student in students:
        grade = student['grade']
        grouped.setdefault(grade, []).append(student['name'])
    
    print(f"   Grouped by grade: {grouped}")


def demonstrate_fromkeys_method():
    """Demonstrate the fromkeys() class method."""
    print_method_header("fromkeys(iterable, value=None)", "Create dict from keys")
    
    # Basic usage
    print(f"\n1. Basic Usage:")
    keys = ['name', 'age', 'city']
    template = dict.fromkeys(keys)
    print(f"   Keys: {keys}")
    print(f"   Template: {template}")
    
    # With specific default value
    print(f"\n2. With Specific Default Value:")
    settings = dict.fromkeys(['theme', 'language', 'notifications'], 'default')
    print(f"   Settings: {settings}")
    
    # Different default values
    print(f"\n3. Different Default Values:")
    scores = dict.fromkeys(['math', 'science', 'english'], 0)
    flags = dict.fromkeys(['active', 'verified', 'premium'], False)
    print(f"   Scores: {scores}")
    print(f"   Flags: {flags}")
    
    # From string (each character as key)
    print(f"\n4. From String:")
    char_dict = dict.fromkeys('hello', 0)
    print(f"   Character dict: {char_dict}")
    
    # Practical example: Initialize user permissions
    print(f"\n5. Practical Example - User Permissions:")
    permissions = ['read', 'write', 'delete', 'admin']
    user_permissions = dict.fromkeys(permissions, False)
    print(f"   Default permissions: {user_permissions}")
    
    # Grant specific permissions
    user_permissions.update({'read': True, 'write': True})
    print(f"   Updated permissions: {user_permissions}")
    
    # Warning: Mutable default values
    print(f"\n6. Warning - Mutable Default Values:")
    # This creates the same list object for all keys
    bad_example = dict.fromkeys(['user1', 'user2'], [])
    print(f"   Bad example: {bad_example}")
    
    # Modifying one affects all
    bad_example['user1'].append('item1')
    print(f"   After adding to user1: {bad_example}")
    
    # Better approach for mutable defaults
    users = ['user1', 'user2', 'user3']
    good_example = {user: [] for user in users}
    print(f"   Good example: {good_example}")
    
    good_example['user1'].append('item1')
    print(f"   After adding to user1: {good_example}")


def demonstrate_copy_method():
    """Demonstrate the copy() method."""
    print_method_header("copy()", "Create shallow copy")
    
    original = {'name': 'Alice', 'scores': [85, 92, 78], 'info': {'age': 25}}
    print(f"Original: {original}")
    
    # Create copy
    print(f"\n1. Create Copy:")
    copied = original.copy()
    print(f"   Copied: {copied}")
    print(f"   Same object: {original is copied}")
    print(f"   Equal content: {original == copied}")
    
    # Modify top-level key
    print(f"\n2. Modify Top-level Key:")
    copied['name'] = 'Bob'
    print(f"   Original: {original}")
    print(f"   Copied: {copied}")
    
    # Modify nested mutable object (shallow copy behavior)
    print(f"\n3. Modify Nested Mutable Object:")
    original['scores'].append(95)
    print(f"   Original: {original}")
    print(f"   Copied: {copied}")  # Also affected!
    
    # Demonstrate deep copy
    print(f"\n4. Deep Copy Comparison:")
    import copy as copy_module
    
    original2 = {'name': 'Charlie', 'scores': [80, 85], 'info': {'age': 30}}
    shallow_copy = original2.copy()
    deep_copy = copy_module.deepcopy(original2)
    
    print(f"   Original: {original2}")
    print(f"   Shallow copy: {shallow_copy}")
    print(f"   Deep copy: {deep_copy}")
    
    # Modify nested structure
    original2['scores'].append(90)
    original2['info']['age'] = 31
    
    print(f"\n   After modifying original:")
    print(f"   Original: {original2}")
    print(f"   Shallow copy: {shallow_copy}")  # Nested objects affected
    print(f"   Deep copy: {deep_copy}")       # Unaffected
    
    # Practical example: Template copying
    print(f"\n5. Practical Example - Template Copying:")
    user_template = {
        'name': '',
        'permissions': ['read'],
        'settings': {'theme': 'light', 'notifications': True}
    }
    
    # Create users from template
    user1 = user_template.copy()
    user1['name'] = 'John'
    user1['permissions'].append('write')  # This affects the template!
    
    user2 = user_template.copy()
    user2['name'] = 'Jane'
    
    print(f"   Template after user1: {user_template}")
    print(f"   User1: {user1}")
    print(f"   User2: {user2}")  # Jane also has 'write' permission!


def main():
    """Main function to demonstrate all dictionary methods."""
    print_header("DICTIONARY METHODS DEMONSTRATION")
    
    # Demonstrate each method
    demonstrate_get_method()
    demonstrate_keys_method()
    demonstrate_values_method()
    demonstrate_items_method()
    demonstrate_pop_method()
    demonstrate_popitem_method()
    demonstrate_clear_method()
    demonstrate_update_method()
    demonstrate_setdefault_method()
    demonstrate_fromkeys_method()
    demonstrate_copy_method()
    
    print_header("SUMMARY")
    print("""
Dictionary Methods Summary:
==========================
1. get(key, default)      - Safe value retrieval
2. keys()                 - View of dictionary keys
3. values()               - View of dictionary values
4. items()                - View of key-value pairs
5. pop(key, default)      - Remove and return value
6. popitem()              - Remove and return last item
7. clear()                - Remove all items
8. update(other)          - Update with another dict/iterable
9. setdefault(key, default) - Set value if key doesn't exist
10. fromkeys(keys, value)  - Create dict from keys (class method)
11. copy()                 - Create shallow copy

Tips:
- Use get() instead of direct access for safety
- Use setdefault() for counting and grouping
- Be careful with mutable objects in copy() and fromkeys()
- update() can accept dicts, iterables, or keyword arguments
- popitem() is useful for LIFO operations
    """)


if __name__ == "__main__":
    main()
