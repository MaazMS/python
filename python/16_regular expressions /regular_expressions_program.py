#!/usr/bin/env python3
"""
Regular Expressions Program
Comprehensive examples demonstrating all regex concepts from the documentation
"""

import re

def main():
    print("=" * 80)
    print("REGULAR EXPRESSIONS COMPREHENSIVE EXAMPLES")
    print("=" * 80)
    
    # 1. BASIC REGULAR EXPRESSIONS AND PATTERN MATCHING
    print("\n1. BASIC PATTERN MATCHING")
    print("-" * 40)
    
    # Email validation example
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    emails = ["user@example.com", "invalid.email", "test@domain.org", "bad@"]
    
    print("Email validation:")
    for email in emails:
        if re.match(email_pattern, email):
            print(f"✓ {email} is valid")
        else:
            print(f"✗ {email} is invalid")
    
    # 2. SEQUENCE CHARACTERS
    print("\n\n2. SEQUENCE CHARACTERS")
    print("-" * 40)
    
    text = "Hello World 123! @#$"
    print(f"Text: '{text}'")
    
    # Find all digits
    digits = re.findall(r'\d', text)
    print(f"Digits (\\d): {digits}")
    
    # Find all non-digits
    non_digits = re.findall(r'\D', text)
    print(f"Non-digits (\\D): {non_digits}")
    
    # Find all word characters
    words = re.findall(r'\w+', text)
    print(f"Word characters (\\w+): {words}")
    
    # Find all non-word characters
    non_words = re.findall(r'\W', text)
    print(f"Non-word characters (\\W): {non_words}")
    
    # Find whitespace
    spaces = re.findall(r'\s', text)
    print(f"Whitespace (\\s): {spaces}")
    
    # Find non-whitespace
    non_spaces = re.findall(r'\S+', text)
    print(f"Non-whitespace (\\S+): {non_spaces}")
    
    # 3. SEARCH OPERATIONS
    print("\n\n3. SEARCH OPERATIONS")
    print("-" * 40)
    
    price_text = "The price is $25.99 and tax is $3.75"
    print(f"Text: '{price_text}'")
    
    # Basic search - finds first match
    price_match = re.search(r'\$\d+\.\d{2}', price_text)
    if price_match:
        print(f"First price found: {price_match.group()}")
        print(f"Position: {price_match.start()}-{price_match.end()}")
    
    # Case-insensitive search
    text2 = "HELLO world"
    match = re.search(r'hello', text2, re.IGNORECASE)
    if match:
        print(f"Case-insensitive match: '{match.group()}' in '{text2}'")
    
    # Multiple patterns
    contact_text = "Contact: john@email.com or call 555-123-4567"
    email_or_phone = re.search(r'(\w+@\w+\.\w+|\d{3}-\d{3}-\d{4})', contact_text)
    if email_or_phone:
        print(f"Contact info found: {email_or_phone.group()}")
    
    # 4. GROUP OPERATIONS
    print("\n\n4. GROUP OPERATIONS")
    print("-" * 40)
    
    date_text = "Born on 1990-05-15 in New York"
    print(f"Text: '{date_text}'")
    
    date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_text)
    if date_match:
        print(f"Full match: {date_match.group()}")
        print(f"Year: {date_match.group(1)}")
        print(f"Month: {date_match.group(2)}")
        print(f"Day: {date_match.group(3)}")
        print(f"All groups: {date_match.groups()}")
    
    # 5. FINDALL OPERATIONS
    print("\n\n5. FINDALL OPERATIONS")
    print("-" * 40)
    
    log_text = """
    2023-01-15 ERROR: Database connection failed
    2023-01-15 INFO: Server started
    2023-01-16 WARNING: Low disk space
    2023-01-16 ERROR: Authentication failed
    """
    
    print("Log text analysis:")
    
    # Find all dates
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', log_text)
    print(f"Dates found: {dates}")
    
    # Find all log levels
    levels = re.findall(r'(ERROR|INFO|WARNING)', log_text)
    print(f"Log levels: {levels}")
    
    # Find complete log entries
    entries = re.findall(r'(\d{4}-\d{2}-\d{2}) (\w+): (.+)', log_text)
    print("Complete log entries:")
    for date, level, message in entries:
        print(f"  {date} [{level}] {message.strip()}")
    
    # 6. MATCH OPERATIONS
    print("\n\n6. MATCH OPERATIONS")
    print("-" * 40)
    
    # Match only at beginning of string
    text1 = "Hello World"
    text2 = "Say Hello World"
    
    match1 = re.match(r'Hello', text1)
    match2 = re.match(r'Hello', text2)
    
    print(f"'{text1}' starts with 'Hello': {match1 is not None}")
    print(f"'{text2}' starts with 'Hello': {match2 is not None}")
    
    # Using match with groups
    email = "user@domain.com"
    email_match = re.match(r'(\w+)@(\w+)\.(\w+)', email)
    if email_match:
        print(f"Email parts:")
        print(f"  Username: {email_match.group(1)}")
        print(f"  Domain: {email_match.group(2)}")
        print(f"  Extension: {email_match.group(3)}")
    
    # 7. SPLIT OPERATIONS
    print("\n\n7. SPLIT OPERATIONS")
    print("-" * 40)
    
    # Split on multiple delimiters
    fruit_text = "apple,banana;orange:grape|mango"
    fruits = re.split(r'[,;:|]', fruit_text)
    print(f"Fruits: {fruits}")
    
    # Split on whitespace (including multiple spaces)
    sentence = "This   has    irregular     spacing"
    words = re.split(r'\s+', sentence)
    print(f"Words: {words}")
    
    # Split and keep delimiters
    section_text = "Section1::Section2::Section3"
    parts = re.split(r'(::)', section_text)
    print(f"Sections with delimiters: {parts}")
    
    # Limit splits
    chain_text = "a-b-c-d-e"
    limited = re.split(r'-', chain_text, maxsplit=2)
    print(f"Limited split: {limited}")
    
    # 8. SUBSTITUTION OPERATIONS
    print("\n\n8. SUBSTITUTION OPERATIONS")
    print("-" * 40)
    
    # Basic substitution
    text = "I have 5 apples and 3 oranges"
    result = re.sub(r'\d+', 'many', text)
    print(f"Original: {text}")
    print(f"Substituted: {result}")
    
    # Advanced substitution with groups
    phone = "Call me at (555) 123-4567"
    formatted = re.sub(r'\((\d{3})\) (\d{3})-(\d{4})', r'\1-\2-\3', phone)
    print(f"Phone formatting: {phone} -> {formatted}")
    
    # Conditional substitution with function
    def replace_numbers(match):
        num = int(match.group())
        return "small" if num < 10 else "large"
    
    text2 = "I have 5 cats and 15 dogs"
    result2 = re.sub(r'\d+', replace_numbers, text2)
    print(f"Conditional: {text2} -> {result2}")
    
    # Count replacements
    text3 = "red red red blue"
    result3, count = re.subn(r'red', 'green', text3)
    print(f"Replace count: {text3} -> {result3} ({count} replacements)")
    
    # 9. QUANTIFIERS
    print("\n\n9. QUANTIFIERS")
    print("-" * 40)
    
    phone_text = "Phone: 123-456-7890, Code: 12345, Emergency: 911"
    print(f"Text: '{phone_text}'")
    
    # Find phone number pattern (exactly 3-3-4 digits)
    phone_pattern = re.search(r'\d{3}-\d{3}-\d{4}', phone_text)
    if phone_pattern:
        print(f"Phone number: {phone_pattern.group()}")
    
    # Find any sequence of digits (one or more)
    all_numbers = re.findall(r'\d+', phone_text)
    print(f"All number sequences: {all_numbers}")
    
    # Optional area code pattern
    phone_texts = ["555-123-4567", "(555) 123-4567", "123-4567"]
    pattern = r'\(?(\d{3})?\)?\s?-?(\d{3})-?(\d{4})'
    
    print("Phone number variations:")
    for phone in phone_texts:
        match = re.search(pattern, phone)
        if match:
            area, prefix, number = match.groups()
            area = area or "N/A"
            print(f"  {phone}: Area={area}, Prefix={prefix}, Number={number}")
    
    # 10. SPECIAL CHARACTERS
    print("\n\n10. SPECIAL CHARACTERS")
    print("-" * 40)
    
    web_text = "Visit www.example.com or https://test.org for more info."
    print(f"Text: '{web_text}'")
    
    # Match any website
    websites = re.findall(r'www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', web_text)
    print(f"Websites: {websites}")
    
    # Match start of string
    starts_with = re.match(r'^Visit', web_text)
    print(f"Starts with 'Visit': {starts_with is not None}")
    
    # Match end of string
    ends_with = re.search(r'info\.$', web_text)
    print(f"Ends with 'info.': {ends_with is not None}")
    
    # Character sets
    vowels = re.findall(r'[aeiou]', web_text.lower())
    print(f"Vowels found: {len(vowels)} - {set(vowels)}")
    
    consonants = re.findall(r'[^aeiou\s\W]', web_text.lower())
    print(f"Consonants: {len(consonants)} unique - {set(consonants)}")
    
    # 11. COMPILED PATTERNS
    print("\n\n11. COMPILED PATTERNS")
    print("-" * 40)
    
    # Compile pattern once, use multiple times
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    test_emails = ["user@example.com", "invalid.email", "test@domain.org", "admin@site.co.uk"]
    print("Compiled pattern email validation:")
    for email in test_emails:
        if email_pattern.match(email):
            print(f"✓ {email}")
        else:
            print(f"✗ {email}")
    
    # 12. MATCH OBJECT METHODS
    print("\n\n12. MATCH OBJECT METHODS")
    print("-" * 40)
    
    contact_text = "Contact: john.doe@email.com, Phone: 123-456-7890"
    pattern = r'(\w+)\.(\w+)@(\w+)\.(\w+)'
    match = re.search(pattern, contact_text)
    
    if match:
        print("Match object methods:")
        print(f"  Full match: {match.group()}")
        print(f"  First name: {match.group(1)}")
        print(f"  Last name: {match.group(2)}")
        print(f"  Domain: {match.group(3)}")
        print(f"  Extension: {match.group(4)}")
        print(f"  Start position: {match.start()}")
        print(f"  End position: {match.end()}")
        print(f"  Span: {match.span()}")
        print(f"  All groups: {match.groups()}")
    
    # 13. FINDITER METHOD
    print("\n\n13. FINDITER METHOD")
    print("-" * 40)
    
    price_text = "Prices: $10.50, $25.99, $5.00, $100.00"
    pattern = r'\$(\d+)\.(\d{2})'
    
    print("Using finditer for detailed price analysis:")
    total = 0
    for i, match in enumerate(re.finditer(pattern, price_text), 1):
        dollars = int(match.group(1))
        cents = int(match.group(2))
        price = dollars + cents/100
        total += price
        print(f"  Price {i}: ${dollars}.{match.group(2)} at position {match.start()}-{match.end()}")
    
    print(f"Total: ${total:.2f}")
    
    # 14. NAMED GROUPS
    print("\n\n14. NAMED GROUPS")
    print("-" * 40)
    
    # Define pattern with named groups
    log_pattern = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>\w+): (?P<message>.+)')
    log_entries = [
        "2023-01-15 ERROR: Database connection failed",
        "2023-01-15 INFO: Server started successfully",
        "2023-01-16 WARNING: Low disk space detected"
    ]
    
    print("Named groups log parsing:")
    for entry in log_entries:
        match = log_pattern.match(entry.strip())
        if match:
            print(f"  Date: {match.group('date')}")
            print(f"  Level: {match.group('level')}")
            print(f"  Message: {match.group('message')}")
            print(f"  All groups: {match.groupdict()}")
            print()
    
    # 15. FLAGS AND MODIFIERS
    print("\n\n15. FLAGS AND MODIFIERS")
    print("-" * 40)
    
    multiline_text = """First Line
    Second LINE
    Third line"""
    
    print("Text:")
    print(multiline_text)
    print()
    
    # Case insensitive
    matches1 = re.findall(r'line', multiline_text, re.IGNORECASE)
    print(f"Case insensitive 'line': {matches1}")
    
    # Multiline mode (^ and $ match line boundaries)
    matches2 = re.findall(r'^.*LINE.*$', multiline_text, re.MULTILINE)
    print(f"Multiline mode - lines with 'LINE': {matches2}")
    
    # Dot matches newline
    matches3 = re.findall(r'First.*Third', multiline_text, re.DOTALL)
    print(f"DOTALL - First to Third: {matches3}")
    
    # 16. COMMON ERRORS DEMONSTRATION
    print("\n\n16. COMMON ERRORS DEMONSTRATION")
    print("-" * 40)
    
    # Error 1: Forgetting to escape special characters
    price_text = "Price: $25.99"
    
    # Wrong way (won't work)
    try:
        wrong = re.search(r'$25.99', price_text)
        print(f"Wrong pattern result: {wrong}")
    except:
        print("Wrong pattern failed as expected")
    
    # Correct way
    correct = re.search(r'\$25\.99', price_text)
    print(f"Correct pattern result: {correct.group() if correct else 'No match'}")
    
    # Using re.escape()
    literal_price = "$25.99"
    escaped_price = re.escape(literal_price)
    pattern = re.compile(escaped_price)
    match = pattern.search(price_text)
    print(f"Using re.escape(): {match.group() if match else 'No match'}")
    
    # Error 2: Greedy vs Non-Greedy
    html = '<div>Content 1</div><div>Content 2</div>'
    
    greedy = re.search(r'<div>.*</div>', html)
    print(f"Greedy matching: {greedy.group() if greedy else 'No match'}")
    
    non_greedy = re.search(r'<div>.*?</div>', html)
    print(f"Non-greedy matching: {non_greedy.group() if non_greedy else 'No match'}")
    
    # Error 3: Not handling None results
    no_numbers_text = "No numbers here"
    
    # Safe way to handle potential None
    result = re.search(r'\d+', no_numbers_text)
    if result:
        print(f"Found number: {result.group()}")
    else:
        print("No numbers found (handled safely)")
    
    # Using walrus operator (Python 3.8+)
    if (result := re.search(r'\d+', "Found 123 here")):
        print(f"Using walrus operator - found: {result.group()}")
    else:
        print("No match with walrus operator")
    
    print("\n" + "=" * 80)
    print("REGULAR EXPRESSIONS EXAMPLES COMPLETED")
    print("=" * 80)

def demonstrate_practical_examples():
    """Additional practical examples for real-world usage"""
    print("\n\nBONUS: PRACTICAL REAL-WORLD EXAMPLES")
    print("=" * 50)
    
    # Phone number validation
    def validate_phone(phone):
        patterns = [
            r'^\(\d{3}\) \d{3}-\d{4}$',  # (123) 456-7890
            r'^\d{3}-\d{3}-\d{4}$',      # 123-456-7890
            r'^\d{10}$',                 # 1234567890
        ]
        return any(re.match(pattern, phone) for pattern in patterns)
    
    phones = ["(555) 123-4567", "555-123-4567", "5551234567", "invalid-phone"]
    print("Phone validation:")
    for phone in phones:
        print(f"  {phone}: {'✓' if validate_phone(phone) else '✗'}")
    
    # Extract information from text
    text = """
    John Doe (john.doe@email.com) - Phone: (555) 123-4567
    Jane Smith (jane@company.org) - Phone: 555-987-6543
    Bob Wilson (bob.wilson@test.net) - Phone: 5551112222
    """
    
    # Extract all contact information
    contact_pattern = r'(\w+ \w+) \(([^)]+)\) - Phone: ([\d\s\(\)-]+)'
    contacts = re.findall(contact_pattern, text)
    
    print("\nExtracted contacts:")
    for name, email, phone in contacts:
        print(f"  Name: {name}")
        print(f"  Email: {email}")
        print(f"  Phone: {phone.strip()}")
        print()
    
    # Clean and format data
    messy_data = "Price:$25.99,Quantity:5,Date:2023-01-15,Status:ACTIVE"
    
    # Parse key-value pairs
    pairs = re.findall(r'(\w+):([^,]+)', messy_data)
    cleaned_data = {key: value for key, value in pairs}
    
    print("Cleaned data:")
    for key, value in cleaned_data.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
    demonstrate_practical_examples()
