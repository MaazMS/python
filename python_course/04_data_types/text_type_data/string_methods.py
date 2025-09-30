#!/usr/bin/env python3
"""
String Methods Program
This program demonstrates various string methods in Python
"""

def case_conversion_methods():
    """Demonstrate string case conversion methods"""
    print("=" * 60)
    print("1. CASE CONVERSION METHODS")
    print("=" * 60)
    
    text = "hello world python programming"
    print(f"Original text: '{text}'")
    print()
    
    # Basic case conversions
    print("Basic Case Conversions:")
    print(f"upper():      '{text.upper()}'")
    print(f"lower():      '{text.lower()}'")
    print(f"capitalize(): '{text.capitalize()}'")
    print(f"title():      '{text.title()}'")
    print(f"swapcase():   '{text.swapcase()}'")
    print()
    
    # Case folding (more aggressive than lower())
    mixed_case = "HELLO WoRlD PyThOn"
    print(f"Mixed case: '{mixed_case}'")
    print(f"casefold(): '{mixed_case.casefold()}'")
    print(f"lower():    '{mixed_case.lower()}'")
    print()

def search_and_count_methods():
    """Demonstrate string search and count methods"""
    print("=" * 60)
    print("2. SEARCH AND COUNT METHODS")
    print("=" * 60)
    
    text = "Hello World, Hello Python, Hello Everyone"
    print(f"Text: '{text}'")
    print()
    
    # Count methods
    print("Count Methods:")
    print(f"count('Hello'):     {text.count('Hello')}")
    print(f"count('l'):         {text.count('l')}")
    print(f"count('o'):         {text.count('o')}")
    print(f"count('World'):     {text.count('World')}")
    print()
    
    # Find methods
    print("Find Methods:")
    print(f"find('World'):      {text.find('World')}")
    print(f"find('Python'):     {text.find('Python')}")
    print(f"find('Java'):       {text.find('Java')}")  # Returns -1 if not found
    print(f"rfind('Hello'):     {text.rfind('Hello')}")  # Find from right
    print()
    
    # Index methods (similar to find but raises exception if not found)
    print("Index Methods:")
    print(f"index('World'):     {text.index('World')}")
    print(f"rindex('Hello'):    {text.rindex('Hello')}")
    print()
    
    # Start and end methods
    print("Start/End Methods:")
    print(f"startswith('Hello'):     {text.startswith('Hello')}")
    print(f"startswith('Hi'):        {text.startswith('Hi')}")
    print(f"endswith('Everyone'):    {text.endswith('Everyone')}")
    print(f"endswith('World'):       {text.endswith('World')}")
    print()

def string_validation_methods():
    """Demonstrate string validation methods"""
    print("=" * 60)
    print("3. STRING VALIDATION METHODS")
    print("=" * 60)
    
    test_strings = [
        "Hello123",     # alphanumeric
        "Hello",        # alphabetic
        "123",          # numeric
        "hello world",  # contains space
        "HELLO",        # uppercase
        "hello",        # lowercase
        "Hello World",  # title case
        "   ",          # whitespace
        "_variable",    # identifier
        "123.45",       # decimal
        "",             # empty
        "Hello\nWorld"  # contains newline
    ]
    
    print("String Validation Results:")
    print(f"{'String':<15} {'isalnum':<8} {'isalpha':<8} {'isdigit':<8} {'islower':<8} {'isupper':<8} {'istitle':<8} {'isspace':<8} {'isidentifier':<12}")
    print("-" * 100)
    
    for test_str in test_strings:
        display_str = repr(test_str)[:15]
        print(f"{display_str:<15} {str(test_str.isalnum()):<8} {str(test_str.isalpha()):<8} {str(test_str.isdigit()):<8} "
              f"{str(test_str.islower()):<8} {str(test_str.isupper()):<8} {str(test_str.istitle()):<8} "
              f"{str(test_str.isspace()):<8} {str(test_str.isidentifier()):<12}")
    
    print()
    
    # Additional validation methods
    print("Additional Validation Methods:")
    print(f"'123'.isdecimal():     {'123'.isdecimal()}")
    print(f"'123'.isnumeric():     {'123'.isnumeric()}")
    print(f"'hello'.isprintable(): {'hello'.isprintable()}")
    newline_text = 'hello\n'
    print(f"'hello\\n'.isprintable(): {newline_text.isprintable()}")
    print()

def string_formatting_methods():
    """Demonstrate string formatting methods"""
    print("=" * 60)
    print("4. STRING FORMATTING METHODS")
    print("=" * 60)
    
    # Basic format method
    print("Basic Format Method:")
    name = "Maaz"
    age = 25
    city = "Mumbai"
    
    formatted1 = "My name is {}, I am {} years old and live in {}".format(name, age, city)
    print(f"Positional: {formatted1}")
    
    formatted2 = "My name is {0}, I am {1} years old and live in {2}".format(name, age, city)
    print(f"Indexed: {formatted2}")
    
    formatted3 = "My name is {name}, I am {age} years old and live in {city}".format(name=name, age=age, city=city)
    print(f"Named: {formatted3}")
    print()
    
    # Format_map method
    print("Format_map Method:")
    person = {"name": "Maaz", "age": 25, "city": "Mumbai", "profession": "Developer"}
    formatted_map = "Hello {name}, you are {age} years old, live in {city} and work as a {profession}".format_map(person)
    print(f"format_map: {formatted_map}")
    print()
    
    # F-string formatting (Python 3.6+)
    print("F-string Formatting:")
    score = 85.67
    print(f"Basic f-string: My score is {score}")
    print(f"With precision: My score is {score:.2f}")
    print(f"Percentage: My score is {score:.1%}")
    print()
    
    # Advanced formatting
    print("Advanced Formatting:")
    number = 42
    print(f"Right align (10 chars): '{number:>10}'")
    print(f"Left align (10 chars):  '{number:<10}'")
    print(f"Center align (10 chars): '{number:^10}'")
    print(f"Zero padding (5 chars):  '{number:05}'")
    print(f"With separator (1000):   '{1000:,}'")
    print()

def string_modification_methods():
    """Demonstrate string modification methods"""
    print("=" * 60)
    print("5. STRING MODIFICATION METHODS")
    print("=" * 60)
    
    # Strip methods
    text_with_spaces = "   Hello World   "
    print("Strip Methods:")
    print(f"Original: '{text_with_spaces}'")
    print(f"strip():  '{text_with_spaces.strip()}'")
    print(f"lstrip(): '{text_with_spaces.lstrip()}'")
    print(f"rstrip(): '{text_with_spaces.rstrip()}'")
    print()
    
    # Replace method
    print("Replace Method:")
    message = "Hello World, Hello Python, Hello Everyone"
    print(f"Original: '{message}'")
    print(f"replace('Hello', 'Hi'): '{message.replace('Hello', 'Hi')}'")
    print(f"replace('Hello', 'Hi', 2): '{message.replace('Hello', 'Hi', 2)}'")  # Replace only first 2
    print()
    
    # Split methods
    print("Split Methods:")
    sentence = "Python,Java,JavaScript,C++,Go"
    print(f"Original: '{sentence}'")
    print(f"split(','): {sentence.split(',')}")
    print(f"split(',', 2): {sentence.split(',', 2)}")  # Split only first 2
    
    multiline = "Line 1\nLine 2\nLine 3"
    print(f"Multiline: {repr(multiline)}")
    print(f"splitlines(): {multiline.splitlines()}")
    print()
    
    # Join method
    print("Join Method:")
    words = ["Python", "is", "awesome", "language"]
    print(f"Words: {words}")
    print(f"' '.join(words): '{' '.join(words)}'")
    print(f"'-'.join(words): '{'-'.join(words)}'")
    print(f"''.join(words): '{' '.join(words)}'")
    print()
    
    # Partition methods
    print("Partition Methods:")
    email = "user@example.com"
    print(f"Email: '{email}'")
    print(f"partition('@'): {email.partition('@')}")
    print(f"rpartition('.'): {email.rpartition('.')}")
    print()

def string_alignment_methods():
    """Demonstrate string alignment methods"""
    print("=" * 60)
    print("6. STRING ALIGNMENT METHODS")
    print("=" * 60)
    
    text = "Python"
    width = 20
    
    print(f"Original text: '{text}'")
    print(f"Width: {width}")
    print()
    
    # Basic alignment
    print("Basic Alignment:")
    print(f"center({width}): '{text.center(width)}'")
    print(f"ljust({width}):  '{text.ljust(width)}'")
    print(f"rjust({width}):  '{text.rjust(width)}'")
    print()
    
    # Alignment with fill characters
    print("Alignment with Fill Characters:")
    print(f"center({width}, '-'): '{text.center(width, '-')}'")
    print(f"ljust({width}, '*'):  '{text.ljust(width, '*')}'")
    print(f"rjust({width}, '='):  '{text.rjust(width, '=')}'")
    print()
    
    # Zero fill
    print("Zero Fill:")
    numbers = ["42", "123", "7", "1000"]
    for num in numbers:
        print(f"'{num}'.zfill(5): '{num.zfill(5)}'")
    print()

def string_encoding_methods():
    """Demonstrate string encoding methods"""
    print("=" * 60)
    print("7. STRING ENCODING METHODS")
    print("=" * 60)
    
    text = "Hello World"
    print(f"Original text: '{text}'")
    print()
    
    # Encoding
    print("Encoding:")
    utf8_bytes = text.encode('utf-8')
    ascii_bytes = text.encode('ascii')
    print(f"encode('utf-8'): {utf8_bytes}")
    print(f"encode('ascii'): {ascii_bytes}")
    print()
    
    # Decoding
    print("Decoding:")
    decoded_utf8 = utf8_bytes.decode('utf-8')
    decoded_ascii = ascii_bytes.decode('ascii')
    print(f"decode('utf-8'): '{decoded_utf8}'")
    print(f"decode('ascii'): '{decoded_ascii}'")
    print()
    
    # Special characters
    special_text = "café"
    print(f"Special text: '{special_text}'")
    print(f"encode('utf-8'): {special_text.encode('utf-8')}")
    print(f"encode('ascii', 'ignore'): {special_text.encode('ascii', 'ignore')}")
    print(f"encode('ascii', 'replace'): {special_text.encode('ascii', 'replace')}")
    print()

def interactive_string_methods():
    """Interactive string methods demonstration"""
    print("=" * 60)
    print("8. INTERACTIVE STRING METHODS")
    print("=" * 60)
    
    while True:
        print("\nChoose a string method to test:")
        print("1. Case conversion methods")
        print("2. Search and count methods")
        print("3. Validation methods")
        print("4. Formatting methods")
        print("5. Modification methods")
        print("6. Alignment methods")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '7':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please try again.")
            continue
        
        text = input("Enter a string: ").strip()
        
        if choice == '1':
            print(f"\nCase Conversion Results for '{text}':")
            print(f"upper():      '{text.upper()}'")
            print(f"lower():      '{text.lower()}'")
            print(f"capitalize(): '{text.capitalize()}'")
            print(f"title():      '{text.title()}'")
            print(f"swapcase():   '{text.swapcase()}'")
        
        elif choice == '2':
            substring = input("Enter substring to search: ").strip()
            print(f"\nSearch Results for '{substring}' in '{text}':")
            print(f"count(): {text.count(substring)}")
            print(f"find(): {text.find(substring)}")
            print(f"startswith(): {text.startswith(substring)}")
            print(f"endswith(): {text.endswith(substring)}")
        
        elif choice == '3':
            print(f"\nValidation Results for '{text}':")
            print(f"isalnum(): {text.isalnum()}")
            print(f"isalpha(): {text.isalpha()}")
            print(f"isdigit(): {text.isdigit()}")
            print(f"islower(): {text.islower()}")
            print(f"isupper(): {text.isupper()}")
            print(f"istitle(): {text.istitle()}")
            print(f"isspace(): {text.isspace()}")
        
        elif choice == '4':
            name = input("Enter name: ").strip()
            age = input("Enter age: ").strip()
            print(f"\nFormatting Results:")
            print(f"format(): 'My name is {{}} and I am {{}} years old'.format('{name}', '{age}')")
            print(f"Result: '{('My name is {} and I am {} years old'.format(name, age))}'")
        
        elif choice == '5':
            print(f"\nModification Results for '{text}':")
            print(f"strip(): '{text.strip()}'")
            print(f"split(): {text.split()}")
            old_text = input("Enter text to replace: ").strip()
            new_text = input("Enter replacement: ").strip()
            print(f"replace('{old_text}', '{new_text}'): '{text.replace(old_text, new_text)}'")
        
        elif choice == '6':
            width = int(input("Enter width for alignment: "))
            fill_char = input("Enter fill character (press Enter for space): ").strip()
            if not fill_char:
                fill_char = ' '
            print(f"\nAlignment Results for '{text}':")
            print(f"center({width}, '{fill_char}'): '{text.center(width, fill_char)}'")
            print(f"ljust({width}, '{fill_char}'): '{text.ljust(width, fill_char)}'")
            print(f"rjust({width}, '{fill_char}'): '{text.rjust(width, fill_char)}'")

def main():
    """Main function to run all string method demonstrations"""
    print("STRING METHODS PROGRAM")
    print("=" * 60)
    print("This program demonstrates various string methods in Python")
    print("=" * 60)
    
    # Run all method demonstrations
    case_conversion_methods()
    search_and_count_methods()
    string_validation_methods()
    string_formatting_methods()
    string_modification_methods()
    string_alignment_methods()
    string_encoding_methods()
    
    # Interactive section
    interactive_string_methods()

if __name__ == "__main__":
    main()
