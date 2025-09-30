#!/usr/bin/env python3
"""
Tuple Operations Program
========================

This program demonstrates various tuple operations including:
- Tuple creation methods
- Accessing elements
- Tuple unpacking
- Concatenation and repetition
- Membership testing
- Iteration
- Tuple methods
- Built-in functions with tuples
"""

def separator(title):
    """Print a formatted separator with title"""
    print(f"\n{'='*50}")
    print(f"{title:^50}")
    print('='*50)

def demonstrate_tuple_creation():
    """Demonstrate various ways to create tuples"""
    separator("TUPLE CREATION METHODS")
    
    # Method 1: Using parentheses
    print("1. Using Parentheses:")
    fruits = ("apple", "banana", "orange")
    numbers = (1, 2, 3, 4, 5)
    mixed = ("Alice", 20, 3.8, True)
    
    print(f"   Fruits: {fruits}")
    print(f"   Numbers: {numbers}")
    print(f"   Mixed data: {mixed}")
    
    # Method 2: Without parentheses (tuple packing)
    print("\n2. Tuple Packing (without parentheses):")
    colors = "red", "green", "blue"
    coordinates = 10, 20
    
    print(f"   Colors: {colors}")
    print(f"   Coordinates: {coordinates}")
    print(f"   Type: {type(colors)}")
    
    # Method 3: Using tuple() constructor
    print("\n3. Using tuple() Constructor:")
    from_list = tuple([1, 2, 3, 4])
    from_string = tuple("hello")
    from_range = tuple(range(5))
    
    print(f"   From list: {from_list}")
    print(f"   From string: {from_string}")
    print(f"   From range: {from_range}")
    
    # Special cases
    print("\n4. Special Cases:")
    empty_tuple = ()
    single_element = (42,)  # Comma is crucial!
    
    print(f"   Empty tuple: {empty_tuple}")
    print(f"   Single element: {single_element}")
    print(f"   Type check: {type(single_element)}")

def demonstrate_accessing_elements():
    """Demonstrate various ways to access tuple elements"""
    separator("ACCESSING TUPLE ELEMENTS")
    
    student = ("Alice", 20, "Computer Science", 3.8, "Senior")
    print(f"Student tuple: {student}")
    
    # Index access
    print("\n1. Index Access:")
    print(f"   First element (index 0): {student[0]}")
    print(f"   Last element (index -1): {student[-1]}")
    print(f"   Second element: {student[1]}")
    
    # Slicing
    print("\n2. Slicing:")
    print(f"   First 3 elements: {student[:3]}")
    print(f"   Last 2 elements: {student[-2:]}")
    print(f"   Middle elements: {student[1:4]}")
    print(f"   Every 2nd element: {student[::2]}")
    
    # Nested tuple access
    print("\n3. Nested Tuple Access:")
    nested = (("John", "Doe"), (25, "Engineer"), ("City", "Country"))
    print(f"   Nested tuple: {nested}")
    print(f"   First name: {nested[0][0]}")
    print(f"   Last name: {nested[0][1]}")
    print(f"   Age: {nested[1][0]}")

def demonstrate_tuple_unpacking():
    """Demonstrate tuple unpacking operations"""
    separator("TUPLE UNPACKING")
    
    # Basic unpacking
    print("1. Basic Unpacking:")
    student = ("Bob", 22, "Mathematics")
    name, age, major = student
    print(f"   Student: {student}")
    print(f"   Name: {name}, Age: {age}, Major: {major}")
    
    # Partial unpacking with *
    print("\n2. Partial Unpacking with *:")
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    first, second, *middle, last = numbers
    print(f"   Numbers: {numbers}")
    print(f"   First: {first}")
    print(f"   Second: {second}")
    print(f"   Middle: {middle}")
    print(f"   Last: {last}")
    
    # Swapping variables
    print("\n3. Variable Swapping:")
    a, b = 10, 20
    print(f"   Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"   After swap: a={a}, b={b}")
    
    # Unpacking in function calls
    print("\n4. Unpacking in Function Calls:")
    def display_info(name, age, city):
        return f"Name: {name}, Age: {age}, City: {city}"
    
    person = ("Charlie", 30, "New York")
    result = display_info(*person)
    print(f"   Person tuple: {person}")
    print(f"   Function result: {result}")

def demonstrate_concatenation_repetition():
    """Demonstrate tuple concatenation and repetition"""
    separator("CONCATENATION AND REPETITION")
    
    # Concatenation
    print("1. Tuple Concatenation:")
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    tuple3 = ("a", "b", "c")
    
    combined = tuple1 + tuple2
    all_combined = tuple1 + tuple2 + tuple3
    
    print(f"   Tuple 1: {tuple1}")
    print(f"   Tuple 2: {tuple2}")
    print(f"   Tuple 3: {tuple3}")
    print(f"   Combined (1+2): {combined}")
    print(f"   All combined: {all_combined}")
    
    # Repetition
    print("\n2. Tuple Repetition:")
    pattern = ("x", "o")
    repeated = pattern * 5
    
    print(f"   Pattern: {pattern}")
    print(f"   Repeated 5 times: {repeated}")
    
    # Building tuples incrementally
    print("\n3. Building Tuples Incrementally:")
    result = ()
    for i in range(5):
        result = result + (i**2,)
        print(f"   Step {i+1}: {result}")

def demonstrate_membership_testing():
    """Demonstrate membership testing operations"""
    separator("MEMBERSHIP TESTING")
    
    fruits = ("apple", "banana", "orange", "grape", "mango")
    print(f"Fruits tuple: {fruits}")
    
    # Basic membership testing
    print("\n1. Basic Membership Testing:")
    test_items = ["apple", "cherry", "banana", "kiwi"]
    
    for item in test_items:
        if item in fruits:
            print(f"   ✓ '{item}' is in the tuple")
        else:
            print(f"   ✗ '{item}' is NOT in the tuple")
    
    # Using not in
    print("\n2. Using 'not in' operator:")
    for item in test_items:
        if item not in fruits:
            print(f"   '{item}' is not available")
    
    # Membership with numbers
    print("\n3. Membership with Numbers:")
    numbers = (1, 3, 5, 7, 9, 11, 13, 15)
    print(f"   Numbers: {numbers}")
    
    for num in [5, 8, 13, 20]:
        status = "found" if num in numbers else "not found"
        print(f"   {num}: {status}")

def demonstrate_iteration():
    """Demonstrate various iteration methods"""
    separator("TUPLE ITERATION")
    
    colors = ("red", "green", "blue", "yellow", "purple")
    print(f"Colors tuple: {colors}")
    
    # Basic iteration
    print("\n1. Basic Iteration:")
    for color in colors:
        print(f"   Color: {color}")
    
    # Iteration with index using enumerate
    print("\n2. Iteration with Index (enumerate):")
    for index, color in enumerate(colors):
        print(f"   Index {index}: {color}")
    
    # Iteration with custom start index
    print("\n3. Iteration with Custom Start Index:")
    for index, color in enumerate(colors, start=1):
        print(f"   Position {index}: {color}")
    
    # Iteration with range and len
    print("\n4. Iteration using Range and Len:")
    for i in range(len(colors)):
        print(f"   colors[{i}] = {colors[i]}")
    
    # Iteration over nested tuples
    print("\n5. Iteration over Nested Tuples:")
    students = (
        ("Alice", 20, "CS"),
        ("Bob", 22, "Math"),
        ("Charlie", 21, "Physics")
    )
    
    for student in students:
        name, age, major = student
        print(f"   {name} is {age} years old, studying {major}")

def demonstrate_tuple_methods():
    """Demonstrate tuple methods: count() and index()"""
    separator("TUPLE METHODS")
    
    # count() method
    print("1. count() Method:")
    numbers = (1, 2, 3, 2, 1, 4, 2, 5, 1)
    letters = ('a', 'b', 'c', 'a', 'b', 'a')
    
    print(f"   Numbers: {numbers}")
    print(f"   Count of 1: {numbers.count(1)}")
    print(f"   Count of 2: {numbers.count(2)}")
    print(f"   Count of 6: {numbers.count(6)}")
    
    print(f"\n   Letters: {letters}")
    print(f"   Count of 'a': {letters.count('a')}")
    print(f"   Count of 'b': {letters.count('b')}")
    
    # index() method
    print("\n2. index() Method:")
    fruits = ("apple", "banana", "orange", "banana", "grape")
    print(f"   Fruits: {fruits}")
    
    try:
        print(f"   First 'banana' at index: {fruits.index('banana')}")
        print(f"   'orange' at index: {fruits.index('orange')}")
        print(f"   'banana' from index 2: {fruits.index('banana', 2)}")
    except ValueError as e:
        print(f"   Error: {e}")
    
    # Safe index finding
    print("\n3. Safe Index Finding:")
    search_items = ["apple", "mango", "banana"]
    
    for item in search_items:
        if item in fruits:
            index = fruits.index(item)
            print(f"   '{item}' found at index {index}")
        else:
            print(f"   '{item}' not found in tuple")

def demonstrate_builtin_functions():
    """Demonstrate built-in functions with tuples"""
    separator("BUILT-IN FUNCTIONS WITH TUPLES")
    
    numbers = (5, 2, 8, 1, 9, 3, 7, 4, 6)
    print(f"Numbers: {numbers}")
    
    # Basic functions
    print("\n1. Basic Functions:")
    print(f"   Length: {len(numbers)}")
    print(f"   Minimum: {min(numbers)}")
    print(f"   Maximum: {max(numbers)}")
    print(f"   Sum: {sum(numbers)}")
    
    # Sorted function
    print("\n2. Sorted Function:")
    print(f"   Sorted (ascending): {sorted(numbers)}")
    print(f"   Sorted (descending): {sorted(numbers, reverse=True)}")
    
    # String tuple operations
    print("\n3. String Tuple Operations:")
    words = ("python", "java", "javascript", "c++", "go")
    print(f"   Words: {words}")
    print(f"   Alphabetically first: {min(words)}")
    print(f"   Alphabetically last: {max(words)}")
    print(f"   Sorted: {sorted(words)}")
    
    # Boolean operations
    print("\n4. Boolean Operations:")
    bool_tuple1 = (True, False, True, True)
    bool_tuple2 = (True, True, True, True)
    bool_tuple3 = (False, False, False)
    
    print(f"   Tuple 1: {bool_tuple1}")
    print(f"   any(): {any(bool_tuple1)} (at least one True)")
    print(f"   all(): {all(bool_tuple1)} (all True)")
    
    print(f"\n   Tuple 2: {bool_tuple2}")
    print(f"   any(): {any(bool_tuple2)}")
    print(f"   all(): {all(bool_tuple2)}")
    
    print(f"\n   Tuple 3: {bool_tuple3}")
    print(f"   any(): {any(bool_tuple3)}")
    print(f"   all(): {all(bool_tuple3)}")

def demonstrate_practical_examples():
    """Demonstrate practical tuple usage examples"""
    separator("PRACTICAL EXAMPLES")
    
    # Example 1: Coordinate system
    print("1. Coordinate System:")
    points = ((0, 0), (3, 4), (1, 2), (5, 5))
    print(f"   Points: {points}")
    
    # Calculate distances from origin
    distances = []
    for point in points:
        x, y = point
        distance = (x**2 + y**2)**0.5
        distances.append((point, distance))
    
    for point, distance in distances:
        print(f"   Distance from origin to {point}: {distance:.2f}")
    
    # Example 2: Student records
    print("\n2. Student Records:")
    students = (
        ("Alice", 85, 90, 88),
        ("Bob", 78, 82, 85),
        ("Charlie", 92, 88, 91)
    )
    
    print("   Student Report Cards:")
    for student in students:
        name, math, science, english = student
        average = (math + science + english) / 3
        print(f"   {name}: Math={math}, Science={science}, English={english}, Average={average:.1f}")
    
    # Example 3: Menu system
    print("\n3. Menu System:")
    menu_items = (
        ("Pizza", 12.99),
        ("Burger", 8.99),
        ("Salad", 7.99),
        ("Pasta", 10.99)
    )
    
    print("   Restaurant Menu:")
    total = 0
    for item, price in menu_items:
        print(f"   {item}: ${price}")
        total += price
    
    print(f"   Total menu value: ${total:.2f}")
    
    # Example 4: RGB color palette
    print("\n4. RGB Color Palette:")
    colors = (
        ("Red", (255, 0, 0)),
        ("Green", (0, 255, 0)),
        ("Blue", (0, 0, 255)),
        ("Yellow", (255, 255, 0)),
        ("Purple", (128, 0, 128))
    )
    
    print("   Color Palette:")
    for color_name, rgb in colors:
        r, g, b = rgb
        print(f"   {color_name}: RGB({r}, {g}, {b})")

def main():
    """Main function to run all demonstrations"""
    print("TUPLE OPERATIONS DEMONSTRATION")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_tuple_creation()
    demonstrate_accessing_elements()
    demonstrate_tuple_unpacking()
    demonstrate_concatenation_repetition()
    demonstrate_membership_testing()
    demonstrate_iteration()
    demonstrate_tuple_methods()
    demonstrate_builtin_functions()
    demonstrate_practical_examples()
    
    separator("PROGRAM COMPLETED")
    print("All tuple operations have been demonstrated!")

if __name__ == "__main__":
    main()
