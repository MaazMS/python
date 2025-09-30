#!/usr/bin/env python3
"""
Tuple Methods Program
=====================

This program demonstrates all tuple methods and related built-in functions:

Tuple Methods:
- count() - Count occurrences of an element
- index() - Find first occurrence index

Built-in Functions with Tuples:
- len() - Get tuple length
- min() - Find minimum value
- max() - Find maximum value
- sum() - Sum numeric elements
- sorted() - Return sorted list
- any() - Boolean OR operation
- all() - Boolean AND operation
- enumerate() - Get index-value pairs
- zip() - Combine tuples
- reversed() - Reverse iteration
"""

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"{title:^60}")
    print('='*60)

def print_subsection(title):
    """Print a formatted subsection header"""
    print(f"\n{'-'*50}")
    print(f"{title}")
    print('-'*50)

def demonstrate_count_method():
    """Demonstrate the count() method with various examples"""
    print_section("TUPLE count() METHOD")
    
    print("The count() method returns the number of times a specified value appears in the tuple.")
    print("Syntax: tuple.count(value)")
    
    # Basic count examples
    print_subsection("1. Basic Count Examples")
    
    numbers = (1, 2, 3, 2, 1, 4, 2, 5, 1, 2)
    print(f"Numbers tuple: {numbers}")
    print(f"Count of 1: {numbers.count(1)}")
    print(f"Count of 2: {numbers.count(2)}")
    print(f"Count of 3: {numbers.count(3)}")
    print(f"Count of 6: {numbers.count(6)} (not in tuple)")
    
    # String count examples
    print_subsection("2. String Count Examples")
    
    letters = ('a', 'b', 'c', 'a', 'b', 'a', 'd', 'a')
    print(f"Letters tuple: {letters}")
    print(f"Count of 'a': {letters.count('a')}")
    print(f"Count of 'b': {letters.count('b')}")
    print(f"Count of 'z': {letters.count('z')} (not in tuple)")
    
    # Mixed data type count
    print_subsection("3. Mixed Data Type Count")
    
    mixed = (1, 'hello', 3.14, 'hello', True, 1, 'hello', False)
    print(f"Mixed tuple: {mixed}")
    print(f"Count of 'hello': {mixed.count('hello')}")
    print(f"Count of 1: {mixed.count(1)}")
    print(f"Count of True: {mixed.count(True)}")  # Note: True == 1 in Python
    print(f"Count of 3.14: {mixed.count(3.14)}")
    
    # Nested tuple count
    print_subsection("4. Nested Tuple Count")
    
    nested = ((1, 2), (3, 4), (1, 2), (5, 6), (1, 2))
    print(f"Nested tuple: {nested}")
    print(f"Count of (1, 2): {nested.count((1, 2))}")
    print(f"Count of (3, 4): {nested.count((3, 4))}")
    print(f"Count of (7, 8): {nested.count((7, 8))}")
    
    # Practical example: Grade counting
    print_subsection("5. Practical Example: Grade Counting")
    
    grades = ('A', 'B', 'C', 'A', 'B', 'A', 'C', 'B', 'A', 'C', 'A')
    print(f"Student grades: {grades}")
    print(f"A grades: {grades.count('A')}")
    print(f"B grades: {grades.count('B')}")
    print(f"C grades: {grades.count('C')}")
    print(f"Total grades: {len(grades)}")
    
    # Calculate grade percentages
    total = len(grades)
    a_percent = (grades.count('A') / total) * 100
    b_percent = (grades.count('B') / total) * 100
    c_percent = (grades.count('C') / total) * 100
    
    print(f"\nGrade Distribution:")
    print(f"A: {a_percent:.1f}%")
    print(f"B: {b_percent:.1f}%")
    print(f"C: {c_percent:.1f}%")

def demonstrate_index_method():
    """Demonstrate the index() method with various examples"""
    print_section("TUPLE index() METHOD")
    
    print("The index() method returns the index of the first occurrence of a specified value.")
    print("Syntax: tuple.index(value, start, end)")
    print("Raises ValueError if the value is not found.")
    
    # Basic index examples
    print_subsection("1. Basic Index Examples")
    
    fruits = ('apple', 'banana', 'orange', 'banana', 'grape', 'banana')
    print(f"Fruits tuple: {fruits}")
    
    try:
        print(f"Index of 'banana': {fruits.index('banana')}")
        print(f"Index of 'orange': {fruits.index('orange')}")
        print(f"Index of 'apple': {fruits.index('apple')}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Index with start parameter
    print_subsection("2. Index with Start Parameter")
    
    print(f"Fruits tuple: {fruits}")
    print(f"First 'banana' from index 0: {fruits.index('banana', 0)}")
    print(f"Next 'banana' from index 2: {fruits.index('banana', 2)}")
    print(f"Last 'banana' from index 4: {fruits.index('banana', 4)}")
    
    # Index with start and end parameters
    print_subsection("3. Index with Start and End Parameters")
    
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 6, 7)
    print(f"Numbers tuple: {numbers}")
    
    try:
        print(f"Index of 5 in range [0:10]: {numbers.index(5, 0, 10)}")
        print(f"Index of 5 in range [6:13]: {numbers.index(5, 6, 13)}")
        print(f"Index of 7 in range [0:8]: {numbers.index(7, 0, 8)}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Error handling
    print_subsection("4. Error Handling")
    
    colors = ('red', 'green', 'blue', 'yellow')
    print(f"Colors tuple: {colors}")
    
    # Safe index finding
    search_items = ['red', 'purple', 'blue', 'orange', 'green']
    
    for item in search_items:
        try:
            index = colors.index(item)
            print(f"✓ '{item}' found at index {index}")
        except ValueError:
            print(f"✗ '{item}' not found in tuple")
    
    # Safe index function
    print_subsection("5. Safe Index Function")
    
    def safe_index(tuple_obj, value, default=-1):
        """Safely find index of value, return default if not found"""
        try:
            return tuple_obj.index(value)
        except ValueError:
            return default
    
    test_tuple = ('a', 'b', 'c', 'd', 'e')
    print(f"Test tuple: {test_tuple}")
    print(f"Safe index of 'c': {safe_index(test_tuple, 'c')}")
    print(f"Safe index of 'z': {safe_index(test_tuple, 'z')}")
    print(f"Safe index of 'z' (custom default): {safe_index(test_tuple, 'z', -999)}")
    
    # Practical example: Finding student position
    print_subsection("6. Practical Example: Student Rankings")
    
    students = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank')
    print(f"Student ranking: {students}")
    
    for i, student in enumerate(students):
        position = i + 1
        print(f"{student} is at position {position}")
    
    # Find specific student
    search_student = 'Charlie'
    try:
        position = students.index(search_student) + 1
        print(f"\n{search_student} is ranked #{position}")
    except ValueError:
        print(f"\n{search_student} is not in the ranking")

def demonstrate_len_function():
    """Demonstrate the len() function with tuples"""
    print_section("len() FUNCTION WITH TUPLES")
    
    print("The len() function returns the number of items in a tuple.")
    print("Syntax: len(tuple)")
    
    # Basic len examples
    print_subsection("1. Basic Length Examples")
    
    empty_tuple = ()
    single_tuple = (42,)
    small_tuple = (1, 2, 3)
    large_tuple = tuple(range(100))
    
    print(f"Empty tuple: {empty_tuple}")
    print(f"Length: {len(empty_tuple)}")
    
    print(f"\nSingle element: {single_tuple}")
    print(f"Length: {len(single_tuple)}")
    
    print(f"\nSmall tuple: {small_tuple}")
    print(f"Length: {len(small_tuple)}")
    
    print(f"\nLarge tuple: (0, 1, 2, ..., 99)")
    print(f"Length: {len(large_tuple)}")
    
    # Nested tuple length
    print_subsection("2. Nested Tuple Length")
    
    nested = ((1, 2), (3, 4, 5), (6, 7, 8, 9))
    print(f"Nested tuple: {nested}")
    print(f"Outer length: {len(nested)}")
    
    for i, inner_tuple in enumerate(nested):
        print(f"Inner tuple {i}: {inner_tuple}, length: {len(inner_tuple)}")
    
    # Practical example: Data validation
    print_subsection("3. Practical Example: Data Validation")
    
    def validate_record(record, expected_length):
        """Validate that a record has the expected number of fields"""
        if len(record) == expected_length:
            return True, "Valid record"
        else:
            return False, f"Expected {expected_length} fields, got {len(record)}"
    
    # Student records should have 4 fields: name, age, grade, gpa
    student_records = [
        ('Alice', 20, 'A', 3.8),
        ('Bob', 22, 'B'),  # Missing GPA
        ('Charlie', 21, 'A', 3.9, 'Extra'),  # Extra field
        ('David', 19, 'B', 3.5),
    ]
    
    print("Validating student records (expected 4 fields):")
    for record in student_records:
        is_valid, message = validate_record(record, 4)
        status = "✓" if is_valid else "✗"
        print(f"{status} {record} - {message}")

def demonstrate_min_max_functions():
    """Demonstrate min() and max() functions with tuples"""
    print_section("min() AND max() FUNCTIONS WITH TUPLES")
    
    print("The min() function returns the smallest item in a tuple.")
    print("The max() function returns the largest item in a tuple.")
    
    # Numeric min/max
    print_subsection("1. Numeric Min/Max")
    
    numbers = (5, 2, 8, 1, 9, 3, 7, 4, 6)
    print(f"Numbers: {numbers}")
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")
    
    # String min/max (alphabetical)
    print_subsection("2. String Min/Max (Alphabetical)")
    
    words = ('python', 'java', 'javascript', 'c++', 'go', 'rust')
    print(f"Words: {words}")
    print(f"Alphabetically first: {min(words)}")
    print(f"Alphabetically last: {max(words)}")
    
    # Custom key function
    print_subsection("3. Custom Key Function")
    
    students = (('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 96))
    print(f"Students (name, score): {students}")
    
    # Find student with min/max score
    min_student = min(students, key=lambda x: x[1])
    max_student = max(students, key=lambda x: x[1])
    
    print(f"Lowest score: {min_student[0]} with {min_student[1]}")
    print(f"Highest score: {max_student[0]} with {max_student[1]}")
    
    # String length min/max
    print_subsection("4. String Length Min/Max")
    
    fruits = ('apple', 'banana', 'orange', 'kiwi', 'strawberry')
    print(f"Fruits: {fruits}")
    
    shortest = min(fruits, key=len)
    longest = max(fruits, key=len)
    
    print(f"Shortest name: '{shortest}' ({len(shortest)} characters)")
    print(f"Longest name: '{longest}' ({len(longest)} characters)")
    
    # Practical example: Temperature analysis
    print_subsection("5. Practical Example: Temperature Analysis")
    
    temperatures = (23.5, 18.2, 31.7, 15.9, 28.3, 19.8, 25.1)
    print(f"Weekly temperatures (°C): {temperatures}")
    print(f"Minimum temperature: {min(temperatures)}°C")
    print(f"Maximum temperature: {max(temperatures)}°C")
    print(f"Temperature range: {max(temperatures) - min(temperatures):.1f}°C")

def demonstrate_sum_function():
    """Demonstrate the sum() function with tuples"""
    print_section("sum() FUNCTION WITH TUPLES")
    
    print("The sum() function returns the sum of all numeric items in a tuple.")
    print("Syntax: sum(tuple, start=0)")
    
    # Basic sum
    print_subsection("1. Basic Sum Examples")
    
    numbers = (1, 2, 3, 4, 5)
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    
    # Sum with start value
    print_subsection("2. Sum with Start Value")
    
    scores = (85, 92, 78, 96, 88)
    print(f"Scores: {scores}")
    print(f"Sum: {sum(scores)}")
    print(f"Sum with bonus (start=10): {sum(scores, 10)}")
    
    # Float sum
    print_subsection("3. Float Sum")
    
    prices = (12.99, 8.50, 15.75, 6.25, 23.99)
    print(f"Prices: {prices}")
    print(f"Total: ${sum(prices):.2f}")
    
    # Practical examples
    print_subsection("4. Practical Examples")
    
    # Calculate average
    def calculate_average(numbers):
        if len(numbers) == 0:
            return 0
        return sum(numbers) / len(numbers)
    
    test_scores = (78, 85, 92, 88, 76, 94, 82)
    print(f"Test scores: {test_scores}")
    print(f"Total points: {sum(test_scores)}")
    print(f"Average score: {calculate_average(test_scores):.1f}")
    
    # Shopping cart total
    cart_items = (
        ('Apple', 2.99),
        ('Banana', 1.50),
        ('Orange', 3.25),
        ('Grape', 4.99)
    )
    
    print(f"\nShopping cart:")
    for item, price in cart_items:
        print(f"  {item}: ${price}")
    
    total = sum(price for item, price in cart_items)
    print(f"Total: ${total:.2f}")

def demonstrate_sorted_function():
    """Demonstrate the sorted() function with tuples"""
    print_section("sorted() FUNCTION WITH TUPLES")
    
    print("The sorted() function returns a new sorted list from the items in a tuple.")
    print("Syntax: sorted(tuple, key=None, reverse=False)")
    
    # Basic sorting
    print_subsection("1. Basic Sorting")
    
    numbers = (5, 2, 8, 1, 9, 3, 7, 4, 6)
    print(f"Original: {numbers}")
    print(f"Sorted (ascending): {sorted(numbers)}")
    print(f"Sorted (descending): {sorted(numbers, reverse=True)}")
    
    # String sorting
    print_subsection("2. String Sorting")
    
    fruits = ('banana', 'apple', 'cherry', 'date', 'elderberry')
    print(f"Original: {fruits}")
    print(f"Alphabetical: {sorted(fruits)}")
    print(f"Reverse alphabetical: {sorted(fruits, reverse=True)}")
    
    # Sort by length
    print_subsection("3. Sort by Length")
    
    words = ('python', 'java', 'c', 'javascript', 'go', 'rust')
    print(f"Original: {words}")
    print(f"By length: {sorted(words, key=len)}")
    print(f"By length (desc): {sorted(words, key=len, reverse=True)}")
    
    # Sort tuples
    print_subsection("4. Sort Tuples")
    
    students = (('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 96))
    print(f"Original: {students}")
    print(f"By name: {sorted(students)}")
    print(f"By score: {sorted(students, key=lambda x: x[1])}")
    print(f"By score (desc): {sorted(students, key=lambda x: x[1], reverse=True)}")
    
    # Practical example: Leaderboard
    print_subsection("5. Practical Example: Game Leaderboard")
    
    players = (
        ('Alice', 1250),
        ('Bob', 980),
        ('Charlie', 1450),
        ('David', 1100),
        ('Eve', 1380)
    )
    
    print("Player scores:")
    for player, score in players:
        print(f"  {player}: {score} points")
    
    leaderboard = sorted(players, key=lambda x: x[1], reverse=True)
    print(f"\nLeaderboard (highest to lowest):")
    for rank, (player, score) in enumerate(leaderboard, 1):
        print(f"  {rank}. {player}: {score} points")

def demonstrate_any_all_functions():
    """Demonstrate any() and all() functions with tuples"""
    print_section("any() AND all() FUNCTIONS WITH TUPLES")
    
    print("any() returns True if any element in the tuple is True")
    print("all() returns True if all elements in the tuple are True")
    
    # Boolean tuples
    print_subsection("1. Boolean Tuples")
    
    test_cases = [
        (True, True, True),
        (True, False, True),
        (False, False, False),
        (True,),
        (False,),
        ()  # Empty tuple
    ]
    
    for test_tuple in test_cases:
        print(f"Tuple: {test_tuple}")
        print(f"  any(): {any(test_tuple)}")
        print(f"  all(): {all(test_tuple)}")
        print()
    
    # Numeric tuples
    print_subsection("2. Numeric Tuples")
    
    numbers1 = (1, 2, 3, 4, 5)  # All truthy
    numbers2 = (0, 1, 2, 3)     # Contains 0 (falsy)
    numbers3 = (0, 0, 0)        # All falsy
    
    for name, nums in [('numbers1', numbers1), ('numbers2', numbers2), ('numbers3', numbers3)]:
        print(f"{name}: {nums}")
        print(f"  any(): {any(nums)} (at least one non-zero)")
        print(f"  all(): {all(nums)} (all non-zero)")
        print()
    
    # String tuples
    print_subsection("3. String Tuples")
    
    strings1 = ('hello', 'world', 'python')  # All non-empty
    strings2 = ('hello', '', 'world')        # Contains empty string
    strings3 = ('', '', '')                  # All empty
    
    for name, strs in [('strings1', strings1), ('strings2', strings2), ('strings3', strings3)]:
        print(f"{name}: {strs}")
        print(f"  any(): {any(strs)} (at least one non-empty)")
        print(f"  all(): {all(strs)} (all non-empty)")
        print()
    
    # Practical examples
    print_subsection("4. Practical Examples")
    
    # Check if all students passed
    grades = (85, 92, 78, 96, 88)
    passing_grade = 70
    
    passed = tuple(grade >= passing_grade for grade in grades)
    print(f"Grades: {grades}")
    print(f"Passing status: {passed}")
    print(f"All passed: {all(passed)}")
    print(f"Any passed: {any(passed)}")
    
    # Check if any item is on sale
    prices = (12.99, 8.50, 15.75, 6.25, 23.99)
    sale_threshold = 10.00
    
    on_sale = tuple(price < sale_threshold for price in prices)
    print(f"\nPrices: {prices}")
    print(f"On sale status: {on_sale}")
    print(f"Any on sale: {any(on_sale)}")
    print(f"All on sale: {all(on_sale)}")

def demonstrate_enumerate_function():
    """Demonstrate the enumerate() function with tuples"""
    print_section("enumerate() FUNCTION WITH TUPLES")
    
    print("The enumerate() function returns an enumerate object with index-value pairs.")
    print("Syntax: enumerate(tuple, start=0)")
    
    # Basic enumerate
    print_subsection("1. Basic Enumerate")
    
    fruits = ('apple', 'banana', 'cherry', 'date')
    print(f"Fruits: {fruits}")
    print("Enumerated:")
    
    for index, fruit in enumerate(fruits):
        print(f"  Index {index}: {fruit}")
    
    # Enumerate with custom start
    print_subsection("2. Enumerate with Custom Start")
    
    students = ('Alice', 'Bob', 'Charlie', 'David')
    print(f"Students: {students}")
    print("Class roster (starting from 1):")
    
    for number, student in enumerate(students, start=1):
        print(f"  Student #{number}: {student}")
    
    # Convert to list/tuple
    print_subsection("3. Convert Enumerate to List/Tuple")
    
    colors = ('red', 'green', 'blue')
    print(f"Colors: {colors}")
    
    enumerated_list = list(enumerate(colors))
    enumerated_tuple = tuple(enumerate(colors))
    
    print(f"As list: {enumerated_list}")
    print(f"As tuple: {enumerated_tuple}")
    
    # Practical example: Menu system
    print_subsection("4. Practical Example: Menu System")
    
    menu_items = ('Pizza', 'Burger', 'Salad', 'Pasta', 'Soup')
    print("Restaurant Menu:")
    
    for index, item in enumerate(menu_items, start=1):
        print(f"  {index}. {item}")
    
    # Create lookup dictionary
    menu_dict = {index: item for index, item in enumerate(menu_items, start=1)}
    print(f"\nMenu dictionary: {menu_dict}")
    
    # Simulate user selection
    user_choice = 3
    if user_choice in menu_dict:
        print(f"You selected: {menu_dict[user_choice]}")

def demonstrate_zip_function():
    """Demonstrate the zip() function with tuples"""
    print_section("zip() FUNCTION WITH TUPLES")
    
    print("The zip() function combines multiple iterables element-wise.")
    print("Syntax: zip(iterable1, iterable2, ...)")
    
    # Basic zip
    print_subsection("1. Basic Zip")
    
    names = ('Alice', 'Bob', 'Charlie')
    ages = (25, 30, 35)
    
    print(f"Names: {names}")
    print(f"Ages: {ages}")
    print("Zipped:")
    
    for name, age in zip(names, ages):
        print(f"  {name} is {age} years old")
    
    # Zip multiple tuples
    print_subsection("2. Zip Multiple Tuples")
    
    students = ('Alice', 'Bob', 'Charlie')
    subjects = ('Math', 'Science', 'English')
    scores = (85, 92, 78)
    
    print(f"Students: {students}")
    print(f"Subjects: {subjects}")
    print(f"Scores: {scores}")
    print("Combined:")
    
    for student, subject, score in zip(students, subjects, scores):
        print(f"  {student} scored {score} in {subject}")
    
    # Zip with different lengths
    print_subsection("3. Zip with Different Lengths")
    
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = ('a', 'b', 'c')
    
    print(f"Tuple 1: {tuple1}")
    print(f"Tuple 2: {tuple2}")
    print("Zipped (stops at shortest):")
    
    zipped = list(zip(tuple1, tuple2))
    print(f"  Result: {zipped}")
    
    # Create dictionary from zip
    print_subsection("4. Create Dictionary from Zip")
    
    keys = ('name', 'age', 'city', 'country')
    values = ('John', 28, 'New York', 'USA')
    
    print(f"Keys: {keys}")
    print(f"Values: {values}")
    
    person_dict = dict(zip(keys, values))
    print(f"Dictionary: {person_dict}")
    
    # Practical example: Data processing
    print_subsection("5. Practical Example: Sales Data")
    
    products = ('Laptop', 'Mouse', 'Keyboard', 'Monitor')
    prices = (999.99, 25.99, 79.99, 299.99)
    quantities = (5, 20, 15, 8)
    
    print("Sales Report:")
    total_revenue = 0
    
    for product, price, qty in zip(products, prices, quantities):
        revenue = price * qty
        total_revenue += revenue
        print(f"  {product}: ${price} x {qty} = ${revenue:.2f}")
    
    print(f"\nTotal Revenue: ${total_revenue:.2f}")

def demonstrate_reversed_function():
    """Demonstrate the reversed() function with tuples"""
    print_section("reversed() FUNCTION WITH TUPLES")
    
    print("The reversed() function returns a reverse iterator.")
    print("Syntax: reversed(tuple)")
    
    # Basic reversed
    print_subsection("1. Basic Reversed")
    
    numbers = (1, 2, 3, 4, 5)
    print(f"Original: {numbers}")
    print(f"Reversed: {tuple(reversed(numbers))}")
    
    # Iterate through reversed
    print_subsection("2. Iterate Through Reversed")
    
    fruits = ('apple', 'banana', 'cherry', 'date')
    print(f"Original order: {fruits}")
    print("Reversed order:")
    
    for fruit in reversed(fruits):
        print(f"  {fruit}")
    
    # Reversed with enumerate
    print_subsection("3. Reversed with Enumerate")
    
    students = ('Alice', 'Bob', 'Charlie', 'David')
    print(f"Students: {students}")
    print("Reverse class roster:")
    
    for index, student in enumerate(reversed(students), start=1):
        print(f"  {index}. {student}")
    
    # Practical example: Undo system
    print_subsection("4. Practical Example: Command History")
    
    commands = ('open file.txt', 'edit line 5', 'save file.txt', 'close file.txt')
    print(f"Command history: {commands}")
    print("Undo sequence (reverse order):")
    
    for step, command in enumerate(reversed(commands), start=1):
        print(f"  Step {step}: Undo '{command}'")

def main():
    """Main function to run all method demonstrations"""
    print("TUPLE METHODS DEMONSTRATION")
    print("="*60)
    print("This program demonstrates all tuple methods and related functions.")
    
    # Tuple-specific methods
    demonstrate_count_method()
    demonstrate_index_method()
    
    # Built-in functions commonly used with tuples
    demonstrate_len_function()
    demonstrate_min_max_functions()
    demonstrate_sum_function()
    demonstrate_sorted_function()
    demonstrate_any_all_functions()
    demonstrate_enumerate_function()
    demonstrate_zip_function()
    demonstrate_reversed_function()
    
    print_section("PROGRAM COMPLETED")
    print("All tuple methods and functions have been demonstrated!")
    print("\nSUMMARY:")
    print("- Tuple methods: count(), index()")
    print("- Built-in functions: len(), min(), max(), sum(), sorted(),")
    print("  any(), all(), enumerate(), zip(), reversed()")

if __name__ == "__main__":
    main()
