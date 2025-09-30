#!/usr/bin/env python3
"""
List Comprehensions Program
Based on List_comprehensions_documentation.md

This program demonstrates all aspects of list comprehensions in Python:
1. Basic definitions and characteristics
2. Various operations (arithmetic, string, nested, conditional)
3. Methods and functions usage
4. Common errors and their solutions
5. Best practices and performance considerations
"""

import time
import math

def print_section(title):
    """Helper function to print section headers"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def print_example(description, code_result=None):
    """Helper function to print examples"""
    print(f"\n--- {description} ---")
    if code_result:
        print(f"Result: {code_result}")

# =============================================================================
# 1. LIST COMPREHENSION DEFINITION AND CHARACTERISTICS
# =============================================================================

def basic_list_comprehensions():
    print_section("1. BASIC LIST COMPREHENSIONS")
    
    print_example("Basic list comprehension")
    numbers = [x for x in range(10)]
    print(f"numbers = [x for x in range(10)]")
    print(f"Result: {numbers}")
    
    print_example("List comprehension with condition")
    even_numbers = [x for x in range(10) if x % 2 == 0]
    print(f"even_numbers = [x for x in range(10) if x % 2 == 0]")
    print(f"Result: {even_numbers}")
    
    print_example("List comprehension with transformation")
    squares = [x**2 for x in range(5)]
    print(f"squares = [x**2 for x in range(5)]")
    print(f"Result: {squares}")
    
    print_example("Traditional vs List Comprehension comparison")
    # Traditional way
    traditional_squares = []
    for x in range(5):
        traditional_squares.append(x**2)
    
    # List comprehension way
    lc_squares = [x**2 for x in range(5)]
    
    print(f"Traditional: {traditional_squares}")
    print(f"List Comp:   {lc_squares}")
    print(f"Both equal:  {traditional_squares == lc_squares}")

# =============================================================================
# 2. LIST COMPREHENSIONS OPERATIONS
# =============================================================================

def arithmetic_operations():
    print_section("2. ARITHMETIC OPERATIONS")
    
    numbers = [1, 2, 3, 4, 5]
    print(f"Base numbers: {numbers}")
    
    print_example("Addition operations")
    add_ten = [x + 10 for x in numbers]
    print(f"Add 10: {add_ten}")
    
    print_example("Multiplication operations")
    multiply_by_two = [x * 2 for x in numbers]
    print(f"Multiply by 2: {multiply_by_two}")
    
    print_example("Power operations")
    powers_of_two = [2**x for x in range(5)]
    print(f"Powers of 2: {powers_of_two}")
    
    print_example("Complex arithmetic")
    complex_calc = [x**2 + 2*x + 1 for x in range(5)]
    print(f"x² + 2x + 1: {complex_calc}")

def string_operations():
    print_section("3. STRING OPERATIONS")
    
    words = ['hello', 'world', 'python']
    print(f"Base words: {words}")
    
    print_example("String transformation")
    uppercase_words = [word.upper() for word in words]
    print(f"Uppercase: {uppercase_words}")
    
    lowercase_words = [word.lower() for word in words]
    print(f"Lowercase: {lowercase_words}")
    
    capitalized_words = [word.capitalize() for word in words]
    print(f"Capitalized: {capitalized_words}")
    
    print_example("String length operations")
    word_lengths = [len(word) for word in words]
    print(f"Word lengths: {word_lengths}")
    
    print_example("String filtering")
    long_words = [word for word in words if len(word) > 5]
    print(f"Words > 5 chars: {long_words}")
    
    short_words = [word for word in words if len(word) <= 5]
    print(f"Words <= 5 chars: {short_words}")

def nested_list_operations():
    print_section("4. NESTED LIST OPERATIONS")
    
    print_example("Flattening nested lists")
    nested_list = [[1, 2], [3, 4], [5, 6]]
    print(f"Nested list: {nested_list}")
    flattened = [item for sublist in nested_list for item in sublist]
    print(f"Flattened: {flattened}")
    
    print_example("Matrix operations")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original matrix:")
    for row in matrix:
        print(f"  {row}")
    
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print("Transposed matrix:")
    for row in transposed:
        print(f"  {row}")
    
    print_example("Nested filtering")
    nested_numbers = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    even_from_nested = [[num for num in sublist if num % 2 == 0] for sublist in nested_numbers]
    print(f"Even numbers from nested: {even_from_nested}")

def conditional_operations():
    print_section("5. CONDITIONAL OPERATIONS")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Numbers: {numbers}")
    
    print_example("If-else in list comprehension")
    result = ['even' if x % 2 == 0 else 'odd' for x in numbers]
    print(f"Even/Odd: {result}")
    
    print_example("Multiple conditions")
    filtered_numbers = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
    print(f"Divisible by 2 AND 3: {filtered_numbers}")
    
    print_example("Complex conditional logic")
    categorized = ['small' if x < 3 else 'medium' if x < 7 else 'large' for x in numbers]
    print(f"Categorized: {categorized}")
    
    print_example("Filtering with multiple OR conditions")
    special_numbers = [x for x in range(20) if x % 3 == 0 or x % 5 == 0]
    print(f"Divisible by 3 OR 5: {special_numbers}")

# =============================================================================
# 3. LIST COMPREHENSIONS METHODS
# =============================================================================

def builtin_functions():
    print_section("6. BUILT-IN FUNCTIONS")
    
    print_example("Using abs() function")
    numbers = [-5, -3, 0, 3, 5]
    absolute_values = [abs(x) for x in numbers]
    print(f"Original: {numbers}")
    print(f"Absolute: {absolute_values}")
    
    print_example("Using round() function")
    decimals = [3.14159, 2.71828, 1.41421]
    rounded = [round(x, 2) for x in decimals]
    print(f"Original: {decimals}")
    print(f"Rounded:  {rounded}")
    
    print_example("Using str() function")
    numbers = [1, 2, 3, 4, 5]
    string_numbers = [str(x) for x in numbers]
    print(f"Numbers: {numbers}")
    print(f"Strings: {string_numbers}")
    
    print_example("Using math functions")
    angles = [0, 30, 45, 60, 90]
    radians = [math.radians(x) for x in angles]
    sines = [round(math.sin(math.radians(x)), 3) for x in angles]
    print(f"Angles: {angles}")
    print(f"Sines:  {sines}")

def string_methods():
    print_section("7. STRING METHODS")
    
    print_example("Using string methods")
    words = ['  hello  ', '  world  ', '  python  ']
    cleaned_words = [word.strip().title() for word in words]
    print(f"Original: {words}")
    print(f"Cleaned:  {cleaned_words}")
    
    print_example("Using split() method")
    sentences = ['hello world', 'python programming', 'list comprehension']
    word_lists = [sentence.split() for sentence in sentences]
    print(f"Sentences: {sentences}")
    print(f"Split:     {word_lists}")
    
    print_example("Using replace() method")
    texts = ['hello world', 'good morning', 'nice day']
    replaced_texts = [text.replace(' ', '_') for text in texts]
    print(f"Original: {texts}")
    print(f"Replaced: {replaced_texts}")
    
    print_example("Using join() method")
    word_pairs = [['hello', 'world'], ['good', 'morning'], ['nice', 'day']]
    joined_texts = [' '.join(pair) for pair in word_pairs]
    print(f"Pairs:  {word_pairs}")
    print(f"Joined: {joined_texts}")

def custom_functions():
    print_section("8. CUSTOM FUNCTIONS")
    
    def is_prime(n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def fibonacci(n):
        """Generate nth Fibonacci number"""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    print_example("Finding prime numbers")
    primes = [x for x in range(2, 20) if is_prime(x)]
    print(f"Primes 2-19: {primes}")
    
    print_example("Using lambda functions")
    numbers = [1, 2, 3, 4, 5]
    squared = [(lambda x: x**2)(x) for x in numbers]
    print(f"Lambda squares: {squared}")
    
    print_example("Fibonacci sequence")
    fib_sequence = [fibonacci(x) for x in range(10)]
    print(f"Fibonacci 0-9: {fib_sequence}")
    
    print_example("Custom string processing")
    def process_name(name):
        return name.strip().title().replace(' ', '_')
    
    names = ['  john doe  ', '  jane smith  ', '  bob johnson  ']
    processed_names = [process_name(name) for name in names]
    print(f"Original: {names}")
    print(f"Processed: {processed_names}")

def dictionary_operations():
    print_section("9. DICTIONARY OPERATIONS")
    
    student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'Diana': 92, 'Eve': 88}
    print(f"Student grades: {student_grades}")
    
    print_example("Dictionary values to list")
    grades_list = [grade for grade in student_grades.values()]
    print(f"All grades: {grades_list}")
    
    print_example("Dictionary keys to list")
    names_list = [name.upper() for name in student_grades.keys()]
    print(f"Student names: {names_list}")
    
    print_example("Dictionary items with conditions")
    high_performers = [name for name, grade in student_grades.items() if grade >= 85]
    print(f"High performers (>=85): {high_performers}")
    
    low_performers = [name for name, grade in student_grades.items() if grade < 80]
    print(f"Need improvement (<80): {low_performers}")
    
    print_example("Creating new dictionary from comprehension")
    grade_letters = {name: 'A' if grade >= 90 else 'B' if grade >= 80 else 'C' 
                    for name, grade in student_grades.items()}
    print(f"Letter grades: {grade_letters}")

# =============================================================================
# 4. COMMON ERRORS AND SOLUTIONS
# =============================================================================

def common_errors_examples():
    print_section("10. COMMON ERRORS AND SOLUTIONS")
    
    print_example("1. Syntax Errors - Correct Examples")
    # Correct syntax
    numbers = [x for x in range(5)]
    result = [x * 2 for x in range(5)]
    print(f"Correct basic: {numbers}")
    print(f"Correct with operation: {result}")
    
    print_example("2. Variable Scope - Correct Usage")
    y = 10
    result = [x * y for x in range(5)]
    print(f"With defined variable y={y}: {result}")
    
    print_example("3. Type Handling")
    mixed_list = [1, '2', 3.0, '4', 5]
    # Safe type conversion
    safe_numbers = [int(x) for x in mixed_list if str(x).isdigit()]
    print(f"Mixed list: {mixed_list}")
    print(f"Safe conversion: {safe_numbers}")
    
    # Filter by type
    numbers_only = [x for x in mixed_list if isinstance(x, (int, float))]
    print(f"Numbers only: {numbers_only}")
    
    print_example("4. Avoiding Complex Nested Comprehensions")
    # Instead of complex nested comprehension, break it down
    lists = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    filtered_lists = [x for x in lists if len(x) > 3]
    result = [[y for y in x if y % 2 == 0] for x in filtered_lists]
    print(f"Original lists: {lists}")
    print(f"Even numbers from each: {result}")
    
    print_example("5. Safe List Operations")
    original_list = [1, 2, 3, 4, 5]
    # Work with a copy to avoid mutation issues
    filtered_copy = [x for x in original_list.copy() if x % 2 == 0]
    print(f"Original: {original_list}")
    print(f"Filtered copy: {filtered_copy}")

# =============================================================================
# 5. PERFORMANCE AND BEST PRACTICES
# =============================================================================

def performance_examples():
    print_section("11. PERFORMANCE AND BEST PRACTICES")
    
    print_example("List Comprehension vs Traditional Loop Performance")
    
    # Timing list comprehension
    start_time = time.time()
    lc_result = [x**2 for x in range(10000)]
    lc_time = time.time() - start_time
    
    # Timing traditional loop
    start_time = time.time()
    loop_result = []
    for x in range(10000):
        loop_result.append(x**2)
    loop_time = time.time() - start_time
    
    print(f"List comprehension time: {lc_time:.6f} seconds")
    print(f"Traditional loop time:   {loop_time:.6f} seconds")
    print(f"List comprehension is {loop_time/lc_time:.2f}x faster")
    
    print_example("Generator vs List for Large Datasets")
    
    # Generator expression (memory efficient)
    large_gen = (x**2 for x in range(1000000))
    print(f"Generator created: {large_gen}")
    print(f"Generator size in memory: minimal")
    
    # Convert small portion to demonstrate
    first_ten = [next(large_gen) for _ in range(10)]
    print(f"First 10 values: {first_ten}")
    
    print_example("Efficient Filtering")
    # Using walrus operator for efficiency (Python 3.8+)
    def expensive_operation(x):
        return x ** 3 + 2 * x ** 2 + x + 1
    
    # Efficient: calculate once, use twice
    try:
        # This uses the walrus operator (:=) available in Python 3.8+
        efficient_result = [result for x in range(10) 
                          if (result := expensive_operation(x)) > 50]
        print(f"Efficient filtering result: {efficient_result}")
    except SyntaxError:
        # Fallback for older Python versions
        print("Walrus operator not available in this Python version")
        # Alternative approach
        temp_results = [(x, expensive_operation(x)) for x in range(10)]
        efficient_result = [result for x, result in temp_results if result > 50]
        print(f"Efficient filtering result: {efficient_result}")

def best_practices_summary():
    print_section("12. BEST PRACTICES SUMMARY")
    
    practices = [
        "1. Keep list comprehensions simple and readable",
        "2. Use traditional loops for complex logic",
        "3. Be mindful of memory usage with large datasets",
        "4. Handle type errors gracefully",
        "5. Avoid side effects within comprehensions",
        "6. Use meaningful variable names",
        "7. Consider generator expressions for large datasets",
        "8. Break down complex nested comprehensions",
        "9. Use appropriate built-in functions",
        "10. Test performance for critical code paths"
    ]
    
    for practice in practices:
        print(f"✅ {practice}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main function to run all examples"""
    print("🐍 LIST COMPREHENSIONS COMPREHENSIVE EXAMPLES")
    print("=" * 60)
    print("This program demonstrates all aspects of Python list comprehensions")
    print("based on the comprehensive documentation.")
    
    try:
        # Basic examples
        basic_list_comprehensions()
        
        # Operations
        arithmetic_operations()
        string_operations()
        nested_list_operations()
        conditional_operations()
        
        # Methods and functions
        builtin_functions()
        string_methods()
        custom_functions()
        dictionary_operations()
        
        # Error handling and best practices
        common_errors_examples()
        performance_examples()
        best_practices_summary()
        
        print(f"\n{'='*60}")
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("📚 Check the documentation for detailed explanations.")
        print(f"{'='*60}")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        print("Please check your Python version and try again.")

if __name__ == "__main__":
    main()
