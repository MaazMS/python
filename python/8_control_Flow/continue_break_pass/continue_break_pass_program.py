#!/usr/bin/env python3
"""
Python Loop Control Keywords Program
Demonstrates comprehensive examples of continue, break, and pass statements
Based on continue_break_pass_documentation.md
"""

import random

def main():
    print("=== Python Loop Control Keywords Demonstrations ===\n")
    
    # Example 1: continue Statement - Skip Even Numbers
    print("1. continue Statement - Print Only Odd Numbers:")
    print("Numbers 1-20, skipping even numbers:")
    for num in range(1, 21):
        if num % 2 == 0:  # If even number
            continue      # Skip to next iteration
        print(f"Odd number: {num}")
    print()
    
    # Example 2: continue with Data Filtering
    print("2. continue Statement - Data Filtering:")
    numbers = [5, -2, 8, -1, 12, 0, -7, 15, -3, 20]
    positive_sum = 0
    print(f"Original numbers: {numbers}")
    print("Processing only positive numbers:")
    
    for num in numbers:
        if num <= 0:
            print(f"  Skipping non-positive number: {num}")
            continue
        
        positive_sum += num
        print(f"  Added {num}, running sum: {positive_sum}")
    
    print(f"Total of positive numbers: {positive_sum}\n")
    
    # Example 3: continue with String Processing
    print("3. continue Statement - String Processing:")
    text = "Hello, World! 123 Python"
    letter_count = 0
    print(f"Analyzing text: '{text}'")
    print("Counting only alphabetic characters:")
    
    for i, char in enumerate(text):
        if not char.isalpha():
            print(f"  Position {i:2d}: '{char}' - Skipped (not a letter)")
            continue  # Skip non-alphabetic characters
        
        letter_count += 1
        print(f"  Position {i:2d}: '{char}' - Letter #{letter_count}")
    
    print(f"Total letters found: {letter_count}\n")
    
    # Example 4: break Statement - Search Operation
    print("4. break Statement - Search Operation:")
    students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    target_student = "Charlie"
    print(f"Student list: {students}")
    print(f"Searching for: {target_student}")
    
    for i, student in enumerate(students):
        print(f"  Checking student {i+1}: {student}")
        if student == target_student:
            print(f"  ✅ Found {target_student} at position {i+1}")
            break  # Exit loop after finding target
    else:
        print(f"  ❌ {target_student} not found in class list")
    print()
    
    # Example 5: break with Input Validation
    print("5. break Statement - Input Validation:")
    validate_user_input()
    print()
    
    # Example 6: break in Game Loop
    print("6. break Statement - Number Guessing Game:")
    play_guessing_game()
    print()
    
    # Example 7: pass Statement - Development Placeholder
    print("7. pass Statement - Development Placeholder:")
    demonstrate_pass_usage()
    print()
    
    # Example 8: pass in Exception Handling
    print("8. pass Statement - Exception Handling:")
    process_files_with_pass()
    print()
    
    # Example 9: Nested Loops with break and continue
    print("9. Nested Loops - break and continue:")
    demonstrate_nested_loops()
    print()
    
    # Example 10: Advanced Loop Control
    print("10. Advanced Loop Control - Email Validation:")
    validate_emails()
    
    print("\n=== Program completed successfully! ===")

def validate_user_input():
    """Demonstrate break with input validation."""
    max_attempts = 3
    attempt = 0
    
    print("Enter a valid age (0-120):")
    while attempt < max_attempts:
        try:
            age_input = input(f"  Attempt {attempt + 1}/{max_attempts}: ")
            
            # Check for exit condition
            if age_input.lower() in ['quit', 'exit']:
                print("  Operation cancelled by user.")
                break
            
            age = int(age_input)
            if 0 <= age <= 120:
                print(f"  ✅ Valid age entered: {age}")
                
                # Age category determination
                if age < 13:
                    category = "Child"
                elif age < 20:
                    category = "Teenager"
                elif age < 60:
                    category = "Adult"
                else:
                    category = "Senior"
                
                print(f"  Age category: {category}")
                break  # Exit loop on valid input
            else:
                print("  ❌ Age must be between 0 and 120")
                
        except ValueError:
            print("  ❌ Please enter a valid number")
        
        attempt += 1
    else:
        print("  ❌ Maximum attempts exceeded")

def play_guessing_game():
    """Number guessing game demonstrating break usage."""
    secret = random.randint(1, 20)
    attempts = 0
    max_attempts = 5
    
    print(f"🎮 Guess the number between 1 and 20! You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"  Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1
            
            if guess == secret:
                print(f"  🎉 Correct! You guessed {secret} in {attempts} attempts!")
                break  # Exit game on correct guess
            elif guess < secret:
                print("  📈 Too low!")
            else:
                print("  📉 Too high!")
                
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"  You have {remaining} attempts left")
                
        except ValueError:
            print("  ❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input as attempt
    else:
        print(f"  😞 Game over! The number was {secret}")

def demonstrate_pass_usage():
    """Demonstrate pass statement as placeholder."""
    print("Processing different types of data:")
    
    data_items = ["INFO: System started", "ERROR: File not found", "WARNING: Low memory", 
                  "DEBUG: Connection established", "INFO: User logged in"]
    
    for item in data_items:
        print(f"  Processing: {item}")
        
        if item.startswith('ERROR'):
            print("    🔴 Error detected!")
            pass  # TODO: Implement error handling logic
        elif item.startswith('WARNING'):
            print("    🟡 Warning detected!")
            pass  # TODO: Implement warning processing
        elif item.startswith('DEBUG'):
            print("    🔵 Debug info detected!")
            pass  # TODO: Implement debug logging
        else:
            print("    ✅ Standard info processed")

def process_files_with_pass():
    """Demonstrate pass in exception handling."""
    files = ["data1.txt", "data2.txt", "missing.txt", "data3.txt"]
    processed_count = 0
    error_count = 0
    
    print("Attempting to process files:")
    for filename in files:
        try:
            # Simulate file processing
            print(f"  Processing {filename}...")
            
            if filename == "missing.txt":
                raise FileNotFoundError(f"File not found: {filename}")
            elif filename == "data3.txt":
                raise PermissionError(f"Permission denied: {filename}")
            
            # Simulate successful processing
            print(f"    ✅ Successfully processed {filename}")
            processed_count += 1
            
        except FileNotFoundError as e:
            print(f"    ❌ Warning: {e}")
            error_count += 1
            pass  # Continue processing other files
            
        except PermissionError as e:
            print(f"    ❌ Error: {e}")
            error_count += 1
            pass  # Continue with other files
            
        except Exception as e:
            print(f"    ❌ Unexpected error: {e}")
            error_count += 1
            pass  # Continue processing
    
    print(f"Summary: {processed_count} files processed, {error_count} errors encountered")

def demonstrate_nested_loops():
    """Demonstrate break and continue in nested loops."""
    print("Finding pairs of numbers that sum to 10:")
    
    numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    target = 10
    pairs_found = 0
    max_pairs = 3
    
    print(f"Numbers: {numbers}")
    print(f"Target sum: {target}")
    
    for i in range(len(numbers)):
        if pairs_found >= max_pairs:
            print(f"  Found maximum {max_pairs} pairs, stopping search")
            break  # Stop when we've found enough pairs
        
        for j in range(i + 1, len(numbers)):
            current_sum = numbers[i] + numbers[j]
            
            if current_sum < target:
                continue  # Skip pairs that sum to less than target
            elif current_sum == target:
                pairs_found += 1
                print(f"  Pair #{pairs_found}: {numbers[i]} + {numbers[j]} = {target}")
                break  # Found a pair, move to next i
            else:
                # Sum is greater than target, no point checking further j values
                break
    
    if pairs_found == 0:
        print("  No pairs found that sum to the target")

def validate_emails():
    """Advanced example combining continue, break, and pass."""
    print("Email validation system:")
    
    emails = [
        "user@example.com",
        "invalid-email",
        "test@domain.org",
        "",
        "admin@site.net",
        "another@test.co.uk",
        "bad@email",
        "good@email.edu"
    ]
    
    valid_emails = []
    max_valid_emails = 5
    
    print(f"Processing {len(emails)} email addresses:")
    print(f"Maximum valid emails to collect: {max_valid_emails}")
    
    for i, email in enumerate(emails, 1):
        print(f"\n  Email {i}: '{email}'")
        
        # Skip empty emails
        if not email:
            print("    ❌ Skipping empty email")
            continue
        
        # Basic email validation
        if "@" not in email:
            print("    ❌ Invalid: Missing @ symbol")
            continue
        
        if "." not in email:
            print("    ❌ Invalid: Missing domain extension")
            continue
        
        # Additional validation (placeholder for more complex logic)
        parts = email.split("@")
        if len(parts) != 2:
            print("    ❌ Invalid: Multiple @ symbols")
            continue
        
        username, domain = parts
        
        if not username:
            print("    ❌ Invalid: Empty username")
            continue
        
        if not domain:
            print("    ❌ Invalid: Empty domain")
            continue
        
        # Advanced domain validation (placeholder)
        if domain.count(".") < 1:
            print("    ❌ Invalid: Domain missing extension")
            continue
        
        # Email passed all validations
        valid_emails.append(email.lower().strip())
        print(f"    ✅ Valid email added: {email}")
        
        # Stop if we've collected enough valid emails
        if len(valid_emails) >= max_valid_emails:
            print(f"    Reached maximum of {max_valid_emails} valid emails")
            break
    
    print(f"\nValidation complete!")
    print(f"Valid emails collected ({len(valid_emails)}):")
    for i, email in enumerate(valid_emails, 1):
        print(f"  {i}. {email}")

def demonstrate_while_with_continue():
    """Demonstrate continue in while loop."""
    print("\n--- Bonus: continue in while loop ---")
    print("Processing numbers until we find 5 positive ones:")
    
    numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]
    positive_count = 0
    index = 0
    target_count = 5
    
    while positive_count < target_count and index < len(numbers):
        current_number = numbers[index]
        index += 1
        
        if current_number <= 0:
            print(f"  Skipping negative/zero: {current_number}")
            continue  # Skip to next iteration
        
        positive_count += 1
        print(f"  Found positive #{positive_count}: {current_number}")
    
    if positive_count == target_count:
        print(f"✅ Successfully found {target_count} positive numbers!")
    else:
        print(f"❌ Only found {positive_count} positive numbers")

def demonstrate_loop_else_with_break():
    """Demonstrate loop-else behavior with break."""
    print("\n--- Bonus: Loop-else with break ---")
    
    # Search for a prime number
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    start_num = 25
    search_range = 10
    
    print(f"Searching for first prime number from {start_num} to {start_num + search_range - 1}:")
    
    for num in range(start_num, start_num + search_range):
        print(f"  Checking {num}...")
        if is_prime(num):
            print(f"  ✅ Found prime number: {num}")
            break
    else:
        print(f"  ❌ No prime number found in range {start_num}-{start_num + search_range - 1}")

if __name__ == "__main__":
    main()
    
    # Additional demonstrations
    demonstrate_while_with_continue()
    demonstrate_loop_else_with_break()
