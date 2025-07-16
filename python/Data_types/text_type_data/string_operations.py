#!/usr/bin/env python3
"""
String Operations Program
This program demonstrates various string operations in Python
"""

def string_creation_demo():
    """Demonstrate different ways to create strings"""
    print("=" * 50)
    print("1. STRING CREATION METHODS")
    print("=" * 50)
    
    # Single quotes
    single_quote = 'Hello World'
    print(f"Single quotes: {single_quote}")
    
    # Double quotes
    double_quote = "Python Programming"
    print(f"Double quotes: {double_quote}")
    
    # Triple quotes (multiline)
    multiline = """This is a
multiline string
example"""
    print(f"Multiline string:\n{multiline}")
    
    # Raw strings
    raw_string = r"C:\Users\Name\Documents"
    print(f"Raw string: {raw_string}")
    
    # f-strings
    name = "Maaz"
    age = 25
    f_string = f"My name is {name} and I'm {age} years old"
    print(f"F-string: {f_string}")
    
    print()

def string_concatenation_demo():
    """Demonstrate string concatenation"""
    print("=" * 50)
    print("2. STRING CONCATENATION")
    print("=" * 50)
    
    first_name = "Maaz"
    last_name = "Shaikh"
    
    # Using + operator
    full_name = first_name + " " + last_name
    print(f"Using + operator: {full_name}")
    
    # Using join method
    words = ["Python", "is", "awesome"]
    sentence = " ".join(words)
    print(f"Using join(): {sentence}")
    
    # Using format method
    formatted = "Hello {} {}".format(first_name, last_name)
    print(f"Using format(): {formatted}")
    
    # Using f-strings
    f_formatted = f"Hello {first_name} {last_name}"
    print(f"Using f-string: {f_formatted}")
    
    print()

def string_repetition_demo():
    """Demonstrate string repetition"""
    print("=" * 50)
    print("3. STRING REPETITION")
    print("=" * 50)
    
    # Basic repetition
    text = "Hello! "
    repeated = text * 3
    print(f"'{text}' * 3 = {repeated}")
    
    # Creating separators
    separator = "-" * 30
    print(f"Separator: {separator}")
    
    # Pattern creation
    pattern = "* " * 10
    print(f"Pattern: {pattern}")
    
    print()

def string_indexing_demo():
    """Demonstrate string indexing"""
    print("=" * 50)
    print("4. STRING INDEXING")
    print("=" * 50)
    
    text = "Python"
    print(f"String: '{text}'")
    print(f"Length: {len(text)}")
    
    # Positive indexing
    print("\nPositive indexing:")
    for i in range(len(text)):
        print(f"text[{i}] = '{text[i]}'")
    
    # Negative indexing
    print("\nNegative indexing:")
    for i in range(-len(text), 0):
        print(f"text[{i}] = '{text[i]}'")
    
    print()

def string_slicing_demo():
    """Demonstrate string slicing"""
    print("=" * 50)
    print("5. STRING SLICING")
    print("=" * 50)
    
    text = "Programming"
    print(f"Original string: '{text}'")
    
    # Basic slicing
    print(f"text[0:4] = '{text[0:4]}'")
    print(f"text[4:] = '{text[4:]}'")
    print(f"text[:4] = '{text[:4]}'")
    print(f"text[-4:] = '{text[-4:]}'")
    
    # Step slicing
    print(f"text[::2] = '{text[::2]}'")  # Every 2nd character
    print(f"text[1::2] = '{text[1::2]}'")  # Every 2nd character starting from index 1
    print(f"text[::-1] = '{text[::-1]}'")  # Reverse string
    
    print()

def string_membership_demo():
    """Demonstrate string membership testing"""
    print("=" * 50)
    print("6. STRING MEMBERSHIP TESTING")
    print("=" * 50)
    
    text = "Python Programming Language"
    print(f"String: '{text}'")
    
    # Test various substrings
    test_cases = ["Python", "Java", "Program", "language", "Lang"]
    
    for test in test_cases:
        in_result = test in text
        not_in_result = test not in text
        print(f"'{test}' in text: {in_result}")
        print(f"'{test}' not in text: {not_in_result}")
        print()

def string_comparison_demo():
    """Demonstrate string comparison"""
    print("=" * 50)
    print("7. STRING COMPARISON")
    print("=" * 50)
    
    strings = ["apple", "banana", "Apple", "APPLE"]
    
    print("Lexicographical comparison:")
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1, str2 = strings[i], strings[j]
            print(f"'{str1}' < '{str2}': {str1 < str2}")
            print(f"'{str1}' > '{str2}': {str1 > str2}")
            print(f"'{str1}' == '{str2}': {str1 == str2}")
            print()

def string_methods_demo():
    """Demonstrate common string methods"""
    print("=" * 50)
    print("8. STRING METHODS")
    print("=" * 50)
    
    text = "  Hello World, Python Programming  "
    print(f"Original: '{text}'")
    
    # Case methods
    print(f"upper(): '{text.upper()}'")
    print(f"lower(): '{text.lower()}'")
    print(f"title(): '{text.title()}'")
    print(f"capitalize(): '{text.capitalize()}'")
    print(f"swapcase(): '{text.swapcase()}'")
    
    # Whitespace methods
    print(f"strip(): '{text.strip()}'")
    print(f"lstrip(): '{text.lstrip()}'")
    print(f"rstrip(): '{text.rstrip()}'")
    
    # Search methods
    print(f"find('World'): {text.find('World')}")
    print(f"count('l'): {text.count('l')}")
    print(f"startswith('  Hello'): {text.startswith('  Hello')}")
    print(f"endswith('  '): {text.endswith('  ')}")
    
    # Replace and split
    print(f"replace('World', 'Universe'): '{text.replace('World', 'Universe')}'")
    words = text.strip().split()
    print(f"split(): {words}")
    
    print()

def string_validation_demo():
    """Demonstrate string validation methods"""
    print("=" * 50)
    print("9. STRING VALIDATION METHODS")
    print("=" * 50)
    
    test_strings = ["Hello123", "Hello", "123", "hello world", "HELLO", "   ", "_variable", "123.45"]
    
    for test_str in test_strings:
        print(f"String: '{test_str}'")
        print(f"  isalnum(): {test_str.isalnum()}")
        print(f"  isalpha(): {test_str.isalpha()}")
        print(f"  isdigit(): {test_str.isdigit()}")
        print(f"  islower(): {test_str.islower()}")
        print(f"  isupper(): {test_str.isupper()}")
        print(f"  isspace(): {test_str.isspace()}")
        print(f"  isidentifier(): {test_str.isidentifier()}")
        print()

def interactive_string_operations():
    """Interactive string operations"""
    print("=" * 50)
    print("10. INTERACTIVE STRING OPERATIONS")
    print("=" * 50)
    
    while True:
        print("\nChoose an operation:")
        print("1. String length")
        print("2. String reversal")
        print("3. Count characters")
        print("4. Find substring")
        print("5. Replace text")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '6':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice! Please try again.")
            continue
        
        text = input("Enter a string: ").strip()
        
        if choice == '1':
            print(f"Length of '{text}': {len(text)}")
        
        elif choice == '2':
            reversed_text = text[::-1]
            print(f"Reversed: '{reversed_text}'")
        
        elif choice == '3':
            char = input("Enter character to count: ").strip()
            count = text.count(char)
            print(f"'{char}' appears {count} times in '{text}'")
        
        elif choice == '4':
            substring = input("Enter substring to find: ").strip()
            index = text.find(substring)
            if index != -1:
                print(f"'{substring}' found at index {index}")
            else:
                print(f"'{substring}' not found in '{text}'")
        
        elif choice == '5':
            old_text = input("Enter text to replace: ").strip()
            new_text = input("Enter replacement text: ").strip()
            result = text.replace(old_text, new_text)
            print(f"Result: '{result}'")

def main():
    """Main function to run all string operation demonstrations"""
    print("STRING OPERATIONS PROGRAM")
    print("=" * 50)
    
    # Run all demonstrations
    string_creation_demo()
    string_concatenation_demo()
    string_repetition_demo()
    string_indexing_demo()
    string_slicing_demo()
    string_membership_demo()
    string_comparison_demo()
    string_methods_demo()
    string_validation_demo()
    
    # Interactive section
    interactive_string_operations()

if __name__ == "__main__":
    main()
