#!/usr/bin/env python3
"""
Python For Loop and Range Program
Demonstrates comprehensive examples of for loops and range functions
Based on for_or_range_documentation.md
"""

import datetime
import math

def main():
    print("=== Python For Loop and Range Demonstrations ===\n")
    
    # Example 1: Basic for loop with lists
    print("1. Basic For Loop - Iterating Over Lists:")
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print("My favorite fruits:")
    for fruit in fruits:
        print(f"  🍎 {fruit.capitalize()}")
    
    # Calculate total characters
    total_chars = 0
    for fruit in fruits:
        total_chars += len(fruit)
    print(f"Total characters in all fruit names: {total_chars}\n")
    
    # Example 2: For loop with strings
    print("2. For Loop with Strings - Character Analysis:")
    message = "Hello Python World!"
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    print(f"Message: '{message}'")
    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
    print(f"Characters breakdown:")
    for i, char in enumerate(message):
        print(f"  Position {i:2d}: '{char}' - {'Vowel' if char in vowels else 'Consonant' if char.isalpha() else 'Special'}")
    print()
    
    # Example 3: Range function demonstrations
    print("3. Range Function Examples:")
    
    # Basic range
    print("a) Basic range(5):")
    for i in range(5):
        print(f"  Count: {i}")
    
    # Range with start and stop
    print("\nb) Range with start and stop - range(3, 8):")
    for i in range(3, 8):
        print(f"  Number: {i}")
    
    # Range with step
    print("\nc) Range with step - range(0, 20, 3):")
    for i in range(0, 20, 3):
        print(f"  Step by 3: {i}")
    
    # Reverse range
    print("\nd) Reverse range - range(10, 0, -2):")
    for i in range(10, 0, -2):
        print(f"  Countdown: {i}")
    print()
    
    # Example 4: Mathematical operations with range
    print("4. Mathematical Operations:")
    
    # Multiplication table
    number = 7
    print(f"a) Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"  {number} × {i:2d} = {result:2d}")
    
    # Calculate factorial
    n = 6
    factorial = 1
    print(f"\nb) Calculating factorial of {n}:")
    for i in range(1, n + 1):
        factorial *= i
        print(f"  Step {i}: {factorial}")
    print(f"  {n}! = {factorial}")
    
    # Generate Fibonacci sequence
    print(f"\nc) Fibonacci sequence (first 10 numbers):")
    fib_sequence = [0, 1]
    for i in range(2, 10):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    for i, fib_num in enumerate(fib_sequence):
        print(f"  F({i}) = {fib_num}")
    print()
    
    # Example 5: Dictionary iteration
    print("5. Dictionary Iteration:")
    student_grades = {
        "Alice": 95,
        "Bob": 87,
        "Charlie": 92,
        "Diana": 88,
        "Eve": 96
    }
    
    print("a) Iterating over keys:")
    for name in student_grades:
        print(f"  Student: {name}")
    
    print("\nb) Iterating over values:")
    for grade in student_grades.values():
        print(f"  Grade: {grade}%")
    
    print("\nc) Iterating over key-value pairs:")
    total_grade = 0
    for name, grade in student_grades.items():
        print(f"  {name}: {grade}%")
        total_grade += grade
    
    average = total_grade / len(student_grades)
    print(f"  Class Average: {average:.1f}%\n")
    
    # Example 6: Nested loops - Pattern printing
    print("6. Nested Loops - Pattern Printing:")
    
    print("a) Right triangle pattern:")
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print()
    
    print("\nb) Number pyramid:")
    for i in range(1, 6):
        # Print spaces
        for j in range(5 - i):
            print(" ", end="")
        # Print numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Print reverse numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
    
    print("\nc) Multiplication table grid:")
    print("   ", end="")
    for i in range(1, 6):
        print(f"{i:3d}", end="")
    print()
    
    for i in range(1, 6):
        print(f"{i}: ", end="")
        for j in range(1, 6):
            print(f"{i*j:3d}", end="")
        print()
    print()
    
    # Example 7: Using enumerate and zip
    print("7. Advanced Iteration with enumerate() and zip():")
    
    # Enumerate example
    colors = ["red", "green", "blue", "yellow", "purple"]
    print("a) Using enumerate():")
    for index, color in enumerate(colors, start=1):
        print(f"  Color #{index}: {color}")
    
    # Zip example
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["New York", "London", "Tokyo"]
    
    print("\nb) Using zip() to combine multiple lists:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name} is {age} years old and lives in {city}")
    print()
    
    # Example 8: Loop control with break and continue
    print("8. Loop Control - break and continue:")
    
    # Using break
    print("a) Finding first number divisible by 7:")
    numbers = [12, 15, 21, 28, 33, 35, 42]
    for num in numbers:
        if num % 7 == 0:
            print(f"  First number divisible by 7: {num}")
            break
        print(f"  Checking {num}... not divisible by 7")
    
    # Using continue
    print("\nb) Processing only positive numbers:")
    data = [5, -2, 8, -1, 12, 0, -7, 15]
    positive_sum = 0
    for num in data:
        if num <= 0:
            print(f"  Skipping {num} (not positive)")
            continue
        positive_sum += num
        print(f"  Adding {num}, running sum: {positive_sum}")
    print(f"  Total of positive numbers: {positive_sum}")
    
    # For-else example
    print("\nc) Using for-else clause:")
    target = 50
    search_list = [10, 20, 30, 40, 60, 70]
    for num in search_list:
        if num == target:
            print(f"  Found {target} in the list!")
            break
        print(f"  Checking {num}...")
    else:
        print(f"  {target} was not found in the list")
    print()
    
    # Example 9: List comprehensions (advanced)
    print("9. List Comprehensions (Advanced For Loop Usage):")
    
    # Traditional for loop
    squares_traditional = []
    for i in range(1, 6):
        squares_traditional.append(i ** 2)
    print(f"a) Traditional loop - squares: {squares_traditional}")
    
    # List comprehension
    squares_comprehension = [i ** 2 for i in range(1, 6)]
    print(f"b) List comprehension - squares: {squares_comprehension}")
    
    # Conditional list comprehension
    even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
    print(f"c) Even squares (1-10): {even_squares}")
    
    # Complex list comprehension
    word_lengths = [len(word) for word in ["python", "programming", "is", "awesome"]]
    print(f"d) Word lengths: {word_lengths}\n")
    
    # Example 10: Practical application - Calendar display (improved version)
    print("10. Practical Application - Monthly Calendar:")
    
    year = 2024
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2024 is leap year
    
    # Display first quarter
    for month_index in range(3):  # First 3 months
        month_name = month_names[month_index]
        days = days_in_month[month_index]
        
        print(f"\n{month_name} {year}")
        print("Mo Tu We Th Fr Sa Su")
        print("-" * 21)
        
        # Simple calendar layout (starting Monday = 1)
        start_day = (month_index * 30) % 7  # Simplified calculation
        
        # Print leading spaces
        for _ in range(start_day):
            print("   ", end="")
        
        # Print days
        for day in range(1, days + 1):
            print(f"{day:2d} ", end="")
            if (day + start_day) % 7 == 0:  # New line after Sunday
                print()
        print()
    
    print("\n=== Program completed successfully! ===")

def demonstrate_range_properties():
    """Demonstrate range object properties and methods."""
    print("\n--- Range Properties Demo ---")
    
    r = range(5, 20, 3)
    print(f"Range object: {r}")
    print(f"Start: {r.start}")
    print(f"Stop: {r.stop}")
    print(f"Step: {r.step}")
    print(f"Length: {len(r)}")
    print(f"As list: {list(r)}")
    
    # Check membership
    print(f"Is 11 in range? {11 in r}")
    print(f"Is 12 in range? {12 in r}")

if __name__ == "__main__":
    main()
    demonstrate_range_properties()
