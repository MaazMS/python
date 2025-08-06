#!/usr/bin/env python3
"""
Python Global and Local Variables - Comprehensive Demo
This script demonstrates all concepts related to global and local variable scope in Python
"""

print("=" * 70)
print("PYTHON GLOBAL AND LOCAL VARIABLES - COMPREHENSIVE DEMO")
print("=" * 70)

# ============================================================================
# 1. BASIC GLOBAL VARIABLES
# ============================================================================
print("\n1. BASIC GLOBAL VARIABLES")
print("-" * 40)

# Global variables (defined outside any function)
global_counter = 0
global_message = "Hello from Global Scope"
global_list = [1, 2, 3]
global_dict = {"name": "Global", "type": "variable"}

print(f"Global counter: {global_counter}")
print(f"Global message: {global_message}")
print(f"Global list: {global_list}")
print(f"Global dict: {global_dict}")

def show_global_access():
    """Demonstrate accessing global variables from inside functions"""
    print(f"\nInside function - accessing global variables:")
    print(f"  global_counter: {global_counter}")
    print(f"  global_message: {global_message}")
    print(f"  global_list: {global_list}")
    print(f"  global_dict: {global_dict}")

show_global_access()

# ============================================================================
# 2. BASIC LOCAL VARIABLES
# ============================================================================
print("\n" + "=" * 70)
print("2. BASIC LOCAL VARIABLES")
print("-" * 40)

def demonstrate_local_variables():
    """Demonstrate local variables and their scope"""
    local_counter = 100
    local_message = "Hello from Local Scope"
    local_list = [10, 20, 30]
    local_dict = {"name": "Local", "type": "variable"}
    
    print(f"Inside function - local variables:")
    print(f"  local_counter: {local_counter}")
    print(f"  local_message: {local_message}")
    print(f"  local_list: {local_list}")
    print(f"  local_dict: {local_dict}")
    
    return local_counter, local_message

result = demonstrate_local_variables()
print(f"Returned from function: {result}")

# Trying to access local variables outside function would cause NameError
# print(local_counter)  # This would raise NameError

# ============================================================================
# 3. VARIABLE SHADOWING (Same Names)
# ============================================================================
print("\n" + "=" * 70)
print("3. VARIABLE SHADOWING (Same Names)")
print("-" * 40)

# Global variable
shadowed_variable = "I am GLOBAL"

def demonstrate_shadowing():
    """Demonstrate how local variables shadow global variables with same name"""
    # First access global variable explicitly
    print(f"Global variable (using globals()): {globals()['shadowed_variable']}")
    
    # This creates a local variable that shadows the global one
    shadowed_variable = "I am LOCAL"
    print(f"Local variable (shadows global): {shadowed_variable}")

print(f"Global variable before function: {shadowed_variable}")
demonstrate_shadowing()
print(f"Global variable after function: {shadowed_variable}")

def access_global_when_shadowed():
    """Demonstrate accessing global variable when local has same name"""
    shadowed_variable = "I am LOCAL in this function"
    print(f"Local variable: {shadowed_variable}")
    print(f"Global variable (using globals()): {globals()['shadowed_variable']}")

print(f"\nDemonstrating access to global when shadowed:")
access_global_when_shadowed()

# ============================================================================
# 4. GLOBAL KEYWORD - MODIFYING GLOBAL VARIABLES
# ============================================================================
print("\n" + "=" * 70)
print("4. GLOBAL KEYWORD - MODIFYING GLOBAL VARIABLES")
print("-" * 40)

modification_counter = 0
modification_message = "Original Message"

print(f"Initial values:")
print(f"  modification_counter: {modification_counter}")
print(f"  modification_message: {modification_message}")

def modify_global_variables():
    """Demonstrate using global keyword to modify global variables"""
    global modification_counter, modification_message
    
    print(f"\nInside function - before modification:")
    print(f"  modification_counter: {modification_counter}")
    print(f"  modification_message: {modification_message}")
    
    # Now we can modify global variables
    modification_counter += 10
    modification_message = "Modified by function"
    
    print(f"\nInside function - after modification:")
    print(f"  modification_counter: {modification_counter}")
    print(f"  modification_message: {modification_message}")

modify_global_variables()

print(f"\nAfter function execution:")
print(f"  modification_counter: {modification_counter}")
print(f"  modification_message: {modification_message}")

# ============================================================================
# 5. CREATING GLOBAL VARIABLES INSIDE FUNCTIONS
# ============================================================================
print("\n" + "=" * 70)
print("5. CREATING GLOBAL VARIABLES INSIDE FUNCTIONS")
print("-" * 40)

def create_global_variable():
    """Demonstrate creating global variables inside functions"""
    global new_global_var
    global dynamic_global
    
    new_global_var = "Created inside function"
    dynamic_global = {"created": "inside function", "value": 42}
    
    print(f"Created global variables inside function:")
    print(f"  new_global_var: {new_global_var}")
    print(f"  dynamic_global: {dynamic_global}")

# Before calling function, these variables don't exist
print("Before calling function:")
try:
    print(f"new_global_var: {new_global_var}")
except NameError:
    print("new_global_var: Not defined yet")

create_global_variable()

print(f"\nAfter calling function:")
print(f"new_global_var: {new_global_var}")
print(f"dynamic_global: {dynamic_global}")

# ============================================================================
# 6. NESTED FUNCTIONS AND NONLOCAL KEYWORD
# ============================================================================
print("\n" + "=" * 70)
print("6. NESTED FUNCTIONS AND NONLOCAL KEYWORD")
print("-" * 40)

def outer_function():
    """Demonstrate nested functions and nonlocal keyword"""
    outer_variable = "I am in outer function"
    outer_counter = 100
    
    print(f"Outer function variable: {outer_variable}")
    print(f"Outer function counter: {outer_counter}")
    
    def inner_function_read():
        """Inner function that only reads outer variable"""
        print(f"  Inner function reading: {outer_variable}")
        print(f"  Inner function reading counter: {outer_counter}")
    
    def inner_function_modify():
        """Inner function that modifies outer variable using nonlocal"""
        nonlocal outer_variable, outer_counter
        outer_variable = "Modified by inner function"
        outer_counter += 50
        print(f"  Inner function modified: {outer_variable}")
        print(f"  Inner function modified counter: {outer_counter}")
    
    print("\nCalling inner function (read only):")
    inner_function_read()
    
    print(f"\nOuter variables before modification: {outer_variable}, {outer_counter}")
    print("Calling inner function (with nonlocal modification):")
    inner_function_modify()
    
    print(f"Outer variables after modification: {outer_variable}, {outer_counter}")

outer_function()

# ============================================================================
# 7. VARIABLE SCOPE HIERARCHY
# ============================================================================
print("\n" + "=" * 70)
print("7. VARIABLE SCOPE HIERARCHY (LEGB Rule)")
print("-" * 40)

# Global scope
legb_variable = "GLOBAL scope"

def demonstrate_legb_rule():
    """Demonstrate LEGB rule: Local -> Enclosing -> Global -> Built-in"""
    # Enclosing scope
    legb_variable = "ENCLOSING scope"
    
    def inner_function():
        # Local scope
        legb_variable = "LOCAL scope"
        print(f"  Local scope: {legb_variable}")
        
        # Access different scopes
        print(f"  Built-in scope example: {len([1, 2, 3])}")  # len is built-in
    
    def inner_function_no_local():
        # No local variable, will use enclosing
        print(f"  Enclosing scope (no local): {legb_variable}")
    
    print(f"Enclosing scope: {legb_variable}")
    inner_function()
    inner_function_no_local()

demonstrate_legb_rule()
print(f"Global scope: {legb_variable}")

# ============================================================================
# 8. GLOBALS() AND LOCALS() FUNCTIONS
# ============================================================================
print("\n" + "=" * 70)
print("8. GLOBALS() AND LOCALS() FUNCTIONS")
print("-" * 40)

inspection_global = "Global for inspection"

def demonstrate_inspection_functions():
    """Demonstrate globals() and locals() functions"""
    inspection_local = "Local for inspection"
    another_local = 42
    
    print("LOCAL VARIABLES (using locals()):")
    local_vars = locals()
    for name, value in local_vars.items():
        print(f"  {name}: {value}")
    
    print(f"\nNumber of local variables: {len(local_vars)}")
    
    print("\nSome GLOBAL VARIABLES (using globals()):")
    global_vars = globals()
    
    # Show some specific global variables
    relevant_globals = {k: v for k, v in global_vars.items() 
                       if not k.startswith('__') and 'inspection' in k}
    
    for name, value in relevant_globals.items():
        print(f"  {name}: {value}")
    
    print(f"\nTotal number of global variables: {len(global_vars)}")
    
    # Modify global variable using globals()
    globals()['inspection_global'] = "Modified through globals()"
    print(f"\nModified global through globals(): {globals()['inspection_global']}")

demonstrate_inspection_functions()
print(f"Global variable after function: {inspection_global}")

# ============================================================================
# 9. VARIABLE SCOPE WITH DIFFERENT DATA TYPES
# ============================================================================
print("\n" + "=" * 70)
print("9. VARIABLE SCOPE WITH DIFFERENT DATA TYPES")
print("-" * 40)

# Global collections
global_list_demo = [1, 2, 3]
global_dict_demo = {"key": "value"}
global_set_demo = {10, 20, 30}

def demonstrate_mutable_globals():
    """Demonstrate working with mutable global objects"""
    print(f"Original global list: {global_list_demo}")
    print(f"Original global dict: {global_dict_demo}")
    print(f"Original global set: {global_set_demo}")
    
    # Modifying mutable objects (no global keyword needed)
    global_list_demo.append(4)
    global_dict_demo["new_key"] = "new_value"
    global_set_demo.add(40)
    
    print(f"\nAfter modification (no global keyword needed):")
    print(f"Modified global list: {global_list_demo}")
    print(f"Modified global dict: {global_dict_demo}")
    print(f"Modified global set: {global_set_demo}")

def reassign_global_collections():
    """Demonstrate reassigning global collections (needs global keyword)"""
    global global_list_demo, global_dict_demo
    
    print(f"\nBefore reassignment:")
    print(f"Global list: {global_list_demo}")
    print(f"Global dict: {global_dict_demo}")
    
    # Reassigning requires global keyword
    global_list_demo = [100, 200, 300]
    global_dict_demo = {"reassigned": True}
    
    print(f"\nAfter reassignment (with global keyword):")
    print(f"Global list: {global_list_demo}")
    print(f"Global dict: {global_dict_demo}")

demonstrate_mutable_globals()
reassign_global_collections()

# ============================================================================
# 10. BEST PRACTICES AND COMMON PITFALLS
# ============================================================================
print("\n" + "=" * 70)
print("10. BEST PRACTICES AND COMMON PITFALLS")
print("-" * 40)

# Example of common pitfall
pitfall_counter = 0

def pitfall_example():
    """Demonstrate common UnboundLocalError pitfall"""
    print(f"This will cause UnboundLocalError if uncommented:")
    print("# print(pitfall_counter)  # This line...")
    print("# pitfall_counter += 1     # ...combined with this line causes error")
    print("\nReason: Python sees assignment and treats variable as local,")
    print("but tries to read it before assignment.")

def correct_approach():
    """Demonstrate correct approach to avoid pitfall"""
    global pitfall_counter
    print(f"Current counter: {pitfall_counter}")
    pitfall_counter += 1
    print(f"Updated counter: {pitfall_counter}")

pitfall_example()
print(f"\nCorrect approach:")
correct_approach()

# Best practices demonstration
print(f"\nBEST PRACTICES:")

# 1. Use constants for global configuration
MAX_CONNECTIONS = 100  # Global constant (convention: UPPER_CASE)
DEBUG_MODE = True

def demonstrate_constants():
    """Show proper use of global constants"""
    print(f"  Using global constants:")
    print(f"    MAX_CONNECTIONS: {MAX_CONNECTIONS}")
    print(f"    DEBUG_MODE: {DEBUG_MODE}")

demonstrate_constants()

# 2. Minimize global variable usage
print(f"\n  Recommended: Minimize global variables")
print(f"  - Use function parameters and return values")
print(f"  - Use classes for state management")
print(f"  - Use global only when necessary")

# 3. Clear naming conventions
APP_CONFIG = {"version": "1.0", "debug": False}  # Global config

def get_app_version():
    """Return app version from global config"""
    return APP_CONFIG["version"]

print(f"  App version: {get_app_version()}")

# ============================================================================
# 11. PRACTICAL EXAMPLES
# ============================================================================
print("\n" + "=" * 70)
print("11. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Counter with global state
call_counter = 0

def increment_call_counter():
    """Increment global call counter"""
    global call_counter
    call_counter += 1
    return call_counter

print("Counter example:")
for i in range(3):
    count = increment_call_counter()
    print(f"  Call #{count}")

# Example 2: Configuration management
CONFIG = {
    "database_url": "localhost:5432",
    "api_key": "secret_key",
    "max_retries": 3
}

def get_config(key, default=None):
    """Get configuration value"""
    return CONFIG.get(key, default)

def update_config(key, value):
    """Update configuration value"""
    global CONFIG
    CONFIG[key] = value

print(f"\nConfiguration example:")
print(f"  Database URL: {get_config('database_url')}")
update_config('max_retries', 5)
print(f"  Updated max_retries: {get_config('max_retries')}")

# Example 3: State management with closures
def create_counter(initial_value=0):
    """Create a counter function with enclosing scope"""
    count = initial_value
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def get_count():
        return count
    
    def reset():
        nonlocal count
        count = initial_value
    
    return increment, get_count, reset

print(f"\nClosure example (alternative to global state):")
inc, get, reset = create_counter(10)
print(f"  Initial: {get()}")
print(f"  After increment: {inc()}")
print(f"  After increment: {inc()}")
reset()
print(f"  After reset: {get()}")

# ============================================================================
# 12. VARIABLE SCOPE INTROSPECTION
# ============================================================================
print("\n" + "=" * 70)
print("12. VARIABLE SCOPE INTROSPECTION")
print("-" * 40)

def scope_introspection():
    """Demonstrate various ways to inspect variable scope"""
    local_var = "Local variable"
    
    print("Scope introspection methods:")
    
    # Check if variable exists in different scopes
    print(f"  'local_var' in locals(): {'local_var' in locals()}")
    print(f"  'global_counter' in globals(): {'global_counter' in globals()}")
    print(f"  'len' in dir(__builtins__): {'len' in dir(__builtins__)}")
    
    # Get variable from specific scope
    local_value = locals().get('local_var', 'Not found')
    global_value = globals().get('global_counter', 'Not found')
    
    print(f"  Local variable value: {local_value}")
    print(f"  Global variable value: {global_value}")
    
    # Count variables in each scope
    print(f"  Number of local variables: {len(locals())}")
    print(f"  Number of global variables: {len([k for k in globals() if not k.startswith('__')])}")

scope_introspection()

print("\n" + "=" * 70)
print("GLOBAL AND LOCAL VARIABLES DEMO COMPLETED")
print("=" * 70)

# Summary of key concepts
print(f"\nKEY CONCEPTS SUMMARY:")
print(f"1. Global variables: Defined outside functions, accessible everywhere")
print(f"2. Local variables: Defined inside functions, only accessible within function")
print(f"3. Variable shadowing: Local variables hide global variables with same name")
print(f"4. global keyword: Required to modify global variables inside functions")
print(f"5. nonlocal keyword: Required to modify enclosing scope variables")
print(f"6. LEGB rule: Local -> Enclosing -> Global -> Built-in scope resolution")
print(f"7. globals() and locals(): Functions to access different scopes")
print(f"8. Mutable objects: Can be modified without global keyword")
print(f"9. Best practice: Minimize global variable usage, use parameters/returns")
print(f"10. Common pitfall: UnboundLocalError when reading then assigning")