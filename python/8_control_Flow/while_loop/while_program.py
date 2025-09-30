#!/usr/bin/env python3
"""
Python While Loop Program
Demonstrates comprehensive examples of while loops
Based on while_documentation.md
"""

import random

def main():
    print("=== Python While Loop Demonstrations ===\n")
    
    # Example 1: Basic While Loop - Multiplication Table (Enhanced)
    print("1. Basic While Loop - Multiplication Table:")
    while True:
        try:
            number = int(input("Enter a number for multiplication table (1-20): "))
            if 1 <= number <= 20:
                break
            else:
                print("Please enter a number between 1 and 20")
        except ValueError:
            print("Please enter a valid integer")
    
    print(f"\nMultiplication Table for {number}:")
    print("-" * 25)
    start = 1
    while start <= 10:
        result = number * start
        print(f"{number} × {start:2d} = {result:3d}")
        start += 1
    print()
    
    # Example 2: Countdown Timer
    print("2. Countdown Timer:")
    try:
        countdown = int(input("Enter countdown start (1-10): "))
        if 1 <= countdown <= 10:
            print("Starting countdown...")
            while countdown > 0:
                print(f"⏰ {countdown}")
                countdown -= 1
            print("🚀 Blast off! Time's up!")
        else:
            print("Using default countdown of 5")
            countdown = 5
            while countdown > 0:
                print(f"⏰ {countdown}")
                countdown -= 1
            print("🚀 Blast off!")
    except ValueError:
        print("Invalid input, skipping countdown demo")
    print()
    
    # Example 3: Sum Calculation
    print("3. Sum Calculation - Add numbers until 0 is entered:")
    total = 0
    count = 0
    
    while True:
        try:
            num = float(input("Enter a number (0 to stop): "))
            if num == 0:
                break
            total += num
            count += 1
            print(f"Running total: {total}")
        except ValueError:
            print("Please enter a valid number")
    
    if count > 0:
        average = total / count
        print(f"📊 Final Results:")
        print(f"   Numbers entered: {count}")
        print(f"   Total sum: {total}")
        print(f"   Average: {average:.2f}")
    else:
        print("No numbers were entered")
    print()
    
    # Example 4: Number Guessing Game
    print("4. Number Guessing Game:")
    play_guessing_game()
    print()
    
    # Example 5: Menu-Driven Calculator
    print("5. Menu-Driven Calculator:")
    calculator_menu()
    print()
    
    # Example 6: String Processing
    print("6. String Processing - Character Analysis:")
    text = input("Enter a sentence: ")
    if text:
        analyze_string(text)
    print()
    
    # Example 7: Fibonacci Sequence Generator
    print("7. Fibonacci Sequence Generator:")
    generate_fibonacci()
    print()
    
    # Example 8: Input Validation Demo
    print("8. Input Validation - Age Verification:")
    validate_age()
    print()
    
    print("\n=== Program completed successfully! ===")

def play_guessing_game():
    """Number guessing game using while loop."""
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    
    print(f"🎮 I'm thinking of a number between 1 and 50!")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed {secret_number} correctly in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
                
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts remaining.")
                
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input as attempt
    else:
        print(f"😞 Game over! The secret number was {secret_number}")

def calculator_menu():
    """Menu-driven calculator using while loop."""
    def show_menu():
        print("\n=== Simple Calculator ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Exit")
    
    running = True
    calculation_count = 0
    
    while running:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print(f"Thank you for using the calculator! You performed {calculation_count} calculations.")
            running = False
        elif choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                
                if choice == '1':
                    result = a + b
                    operation = f"{a} + {b}"
                elif choice == '2':
                    result = a - b
                    operation = f"{a} - {b}"
                elif choice == '3':
                    result = a * b
                    operation = f"{a} × {b}"
                elif choice == '4':
                    if b != 0:
                        result = a / b
                        operation = f"{a} ÷ {b}"
                    else:
                        print("❌ Error: Division by zero!")
                        continue
                
                print(f"✅ Result: {operation} = {result}")
                calculation_count += 1
                
            except ValueError:
                print("❌ Error: Please enter valid numbers!")
        else:
            print("❌ Invalid choice! Please select 1-5.")

def analyze_string(text):
    """Analyze string characters using while loop."""
    index = 0
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_count = 0
    
    print(f"Analyzing: '{text}'")
    print("Character breakdown:")
    
    while index < len(text):
        char = text[index]
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
                char_type = "Vowel"
            else:
                consonant_count += 1
                char_type = "Consonant"
        elif char.isdigit():
            digit_count += 1
            char_type = "Digit"
        elif char.isspace():
            char_type = "Space"
        else:
            special_count += 1
            char_type = "Special"
        
        print(f"  Position {index:2d}: '{char}' - {char_type}")
        index += 1
    
    print(f"\n📊 Summary:")
    print(f"   Total characters: {len(text)}")
    print(f"   Vowels: {vowel_count}")
    print(f"   Consonants: {consonant_count}")
    print(f"   Digits: {digit_count}")
    print(f"   Special characters: {special_count}")

def generate_fibonacci():
    """Generate Fibonacci sequence using while loop."""
    try:
        limit = int(input("Enter the maximum value for Fibonacci sequence: "))
        if limit < 0:
            print("Please enter a positive number")
            return
    except ValueError:
        print("Invalid input, using default limit of 100")
        limit = 100
    
    print(f"Fibonacci sequence up to {limit}:")
    
    a, b = 0, 1
    fibonacci_numbers = []
    
    # Add first two numbers if they're within limit
    if a <= limit:
        fibonacci_numbers.append(a)
        print(f"F(0) = {a}")
    
    if b <= limit:
        fibonacci_numbers.append(b)
        print(f"F(1) = {b}")
    
    position = 2
    while True:
        next_fib = a + b
        if next_fib > limit:
            break
        fibonacci_numbers.append(next_fib)
        print(f"F({position}) = {next_fib}")
        a, b = b, next_fib
        position += 1
    
    print(f"\nGenerated {len(fibonacci_numbers)} Fibonacci numbers: {fibonacci_numbers}")

def validate_age():
    """Demonstrate input validation using while loop."""
    max_attempts = 3
    attempt_count = 0
    valid_age = None
    
    while attempt_count < max_attempts and valid_age is None:
        try:
            age_input = input(f"Enter your age (Attempt {attempt_count + 1}/{max_attempts}): ")
            
            # Check for exit condition
            if age_input.lower() in ['quit', 'exit']:
                print("Operation cancelled by user.")
                return
            
            age = int(age_input)
            
            if 0 <= age <= 120:
                valid_age = age
                print(f"✅ Valid age entered: {age}")
                
                # Age category
                if age < 13:
                    category = "Child"
                elif age < 20:
                    category = "Teenager"
                elif age < 60:
                    category = "Adult"
                else:
                    category = "Senior"
                
                print(f"Age category: {category}")
            else:
                print("❌ Age must be between 0 and 120")
                
        except ValueError:
            print("❌ Please enter a valid number")
        
        attempt_count += 1
        
        if valid_age is None and attempt_count < max_attempts:
            remaining = max_attempts - attempt_count
            print(f"You have {remaining} attempts remaining.")
    
    if valid_age is None:
        print("❌ Maximum attempts exceeded. Age validation failed.")

def demonstrate_loop_control():
    """Demonstrate break, continue, and else in while loops."""
    print("\n--- Loop Control Demonstration ---")
    
    # Break example
    print("1. Using 'break' - Find first number divisible by 7:")
    numbers = [12, 15, 21, 28, 33, 35, 42]
    i = 0
    while i < len(numbers):
        if numbers[i] % 7 == 0:
            print(f"   First number divisible by 7: {numbers[i]}")
            break
        print(f"   Checking {numbers[i]}... not divisible by 7")
        i += 1
    
    # Continue example
    print("\n2. Using 'continue' - Process only positive numbers:")
    data = [5, -2, 8, -1, 12, 0, -7, 15]
    i = 0
    positive_sum = 0
    while i < len(data):
        if data[i] <= 0:
            print(f"   Skipping {data[i]} (not positive)")
            i += 1
            continue
        positive_sum += data[i]
        print(f"   Adding {data[i]}, running sum: {positive_sum}")
        i += 1
    print(f"   Total of positive numbers: {positive_sum}")
    
    # While-else example
    print("\n3. Using 'while-else' - Search for target:")
    target = 50
    search_list = [10, 20, 30, 40, 60, 70]
    i = 0
    while i < len(search_list):
        if search_list[i] == target:
            print(f"   Found {target} in the list!")
            break
        print(f"   Checking {search_list[i]}...")
        i += 1
    else:
        print(f"   {target} was not found in the list")

if __name__ == "__main__":
    main()
    
    # Additional demonstration
    demonstrate_loop_control()
