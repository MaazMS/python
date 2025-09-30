# Frozenset with Text/String Program
# This program demonstrates various ways to create and work with frozensets from text/string data

from __future__ import annotations
import re
import string

print("=" * 60)
print("FROZENSET WITH TEXT/STRING PROGRAM")
print("=" * 60)

# 1. Basic Frozenset Creation from Strings
print("\n1. BASIC FROZENSET CREATION FROM STRINGS")
print("-" * 40)

# Creating frozenset from string characters
sample_text = "hello world"
frozenset_chars = frozenset(sample_text)
print(f"Original string: '{sample_text}'")
print(f"Frozenset from string: {frozenset_chars}")
print(f"Type: {type(frozenset_chars)}")

# String with duplicates
duplicate_text = "programming"
frozenset_duplicate_chars = frozenset(duplicate_text)
print(f"\nString with duplicates: '{duplicate_text}'")
print(f"Frozenset (unique chars): {frozenset_duplicate_chars}")
print(f"Original length: {len(duplicate_text)}")
print(f"Unique characters: {len(frozenset_duplicate_chars)}")

# Case sensitivity
mixed_case = "Hello World"
frozenset_mixed = frozenset(mixed_case)
frozenset_lower = frozenset(mixed_case.lower())
print(f"\nMixed case: '{mixed_case}'")
print(f"Frozenset (case-sensitive): {frozenset_mixed}")
print(f"Frozenset (lowercase): {frozenset_lower}")

# 2. Frozenset from Words in Text
print("\n2. FROZENSET FROM WORDS IN TEXT")
print("-" * 40)

# Split text into words
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
frozenset_words = frozenset(words)
print(f"Original sentence: '{sentence}'")
print(f"Words list: {words}")
print(f"Frozenset from words: {frozenset_words}")
print(f"Total words: {len(words)}")
print(f"Unique words: {len(frozenset_words)}")

# More complex text processing
complex_text = "Python is great! Python is powerful. Python is fun!"
words_complex = complex_text.lower().replace('!', '').replace('.', '').split()
frozenset_complex_words = frozenset(words_complex)
print(f"\nComplex text: '{complex_text}'")
print(f"Processed words: {words_complex}")
print(f"Unique words frozenset: {frozenset_complex_words}")

# 3. Character Analysis with Frozensets
print("\n3. CHARACTER ANALYSIS WITH FROZENSETS")
print("-" * 40)

text_analysis = "Data Science and Machine Learning"
chars_fs = frozenset(text_analysis)
letters_fs = frozenset(text_analysis.replace(' ', ''))
alphabetic_fs = frozenset(char for char in text_analysis if char.isalpha())
numeric_fs = frozenset(char for char in text_analysis if char.isdigit())
special_fs = frozenset(char for char in text_analysis if not char.isalnum())

print(f"Text: '{text_analysis}'")
print(f"All characters: {chars_fs}")
print(f"Letters only (no spaces): {letters_fs}")
print(f"Alphabetic characters: {alphabetic_fs}")
print(f"Numeric characters: {numeric_fs}")
print(f"Special characters: {special_fs}")

# Vowels and consonants
vowels = "aeiouAEIOU"
vowels_fs = frozenset(vowels)
text_vowels = frozenset(char for char in text_analysis if char in vowels_fs)
text_consonants = frozenset(char for char in text_analysis if char.isalpha() and char not in vowels_fs)

print(f"\nVowels in text: {text_vowels}")
print(f"Consonants in text: {text_consonants}")

# 4. Text Processing with Multiple Strings
print("\n4. TEXT PROCESSING WITH MULTIPLE STRINGS")
print("-" * 40)

# Different texts for comparison
text1 = "artificial intelligence"
text2 = "machine learning"
text3 = "deep learning"

# Character-level comparison
chars1: frozenset[str] = frozenset(text1)
chars2: frozenset[str] = frozenset(text2)
chars3: frozenset[str] = frozenset(text3)

print(f"Text 1: '{text1}' → {chars1}")
print(f"Text 2: '{text2}' → {chars2}")
print(f"Text 3: '{text3}' → {chars3}")

# Character operations
common_chars = chars1.intersection(chars2)
all_chars = chars1.union(chars2)
unique_to_text1 = chars1.difference(chars2)

print(f"\nCommon characters (text1 ∩ text2): {common_chars}")
print(f"All characters (text1 ∪ text2): {all_chars}")
print(f"Characters unique to text1: {unique_to_text1}")

# Word-level comparison
words1: frozenset[str] = frozenset(text1.split())
words2: frozenset[str] = frozenset(text2.split())
words3: frozenset[str] = frozenset(text3.split())

print(f"\nWords in text1: {words1}")
print(f"Words in text2: {words2}")
print(f"Words in text3: {words3}")

common_words = words1.intersection(words2)
all_words = words1.union(words2, words3)
print(f"Common words: {common_words}")
print(f"All unique words: {all_words}")

# 5. Regular Expressions with Frozensets
print("\n5. REGULAR EXPRESSIONS WITH FROZENSETS")
print("-" * 40)

email_text = "Contact us at john@example.com or support@company.org for help"
phone_text = "Call us at 123-456-7890 or 987.654.3210 for assistance"

# Extract emails
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email_text)
frozenset_emails = frozenset(emails)
print(f"Email text: '{email_text}'")
print(f"Extracted emails: {frozenset_emails}")

# Extract phone numbers
phones = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', phone_text)
frozenset_phones = frozenset(phones)
print(f"\nPhone text: '{phone_text}'")
print(f"Extracted phones: {frozenset_phones}")

# Extract words of specific length
long_words = re.findall(r'\b\w{6,}\b', email_text + " " + phone_text)
frozenset_long_words = frozenset(long_words)
print(f"Long words (6+ chars): {frozenset_long_words}")

# 6. File-like Text Processing
print("\n6. FILE-LIKE TEXT PROCESSING")
print("-" * 40)

# Simulate file content
file_content = """Python is a programming language.
It is easy to learn and powerful.
Python supports multiple programming paradigms.
Object-oriented programming is one of them."""

# Process line by line
lines = file_content.strip().split('\n')
print(f"File content ({len(lines)} lines):")
for i, line in enumerate(lines, 1):
    print(f"  {i}: {line}")

# Create frozensets from different aspects
all_words_from_file = []
for line in lines:
    # Clean and extract words
    clean_line = re.sub(r'[^\w\s]', '', line.lower())
    words = clean_line.split()
    all_words_from_file.extend(words)

unique_words_fs = frozenset(all_words_from_file)
print(f"\nAll words from file: {len(all_words_from_file)}")
print(f"Unique words: {len(unique_words_fs)}")
print(f"Unique words frozenset: {unique_words_fs}")

# Line-specific analysis
line_chars = [frozenset(line.lower()) for line in lines]
common_chars_all_lines = frozenset.intersection(*line_chars)
print(f"Characters common to all lines: {common_chars_all_lines}")

# 7. Text Statistics with Frozensets
print("\n7. TEXT STATISTICS WITH FROZENSETS")
print("-" * 40)

sample_paragraph = """Machine learning is a subset of artificial intelligence that focuses on 
algorithms that can learn from data. It includes supervised learning, unsupervised learning, 
and reinforcement learning approaches."""

# Clean text
clean_paragraph = re.sub(r'[^\w\s]', '', sample_paragraph.lower())
words_in_paragraph = clean_paragraph.split()
chars_in_paragraph = clean_paragraph.replace(' ', '')

# Create frozensets
words_fs = frozenset(words_in_paragraph)
chars_fs = frozenset(chars_in_paragraph)

print(f"Sample paragraph word count: {len(words_in_paragraph)}")
print(f"Unique words: {len(words_fs)}")
print(f"Total characters (no spaces): {len(chars_in_paragraph)}")
print(f"Unique characters: {len(chars_fs)}")

# Calculate text diversity
word_diversity = len(words_fs) / len(words_in_paragraph)
char_diversity = len(chars_fs) / len(chars_in_paragraph)

print(f"Word diversity: {word_diversity:.2%}")
print(f"Character diversity: {char_diversity:.2%}")

# Find repeated words
word_counts = {}
for word in words_in_paragraph:
    word_counts[word] = word_counts.get(word, 0) + 1

repeated_words = frozenset(word for word, count in word_counts.items() if count > 1)
print(f"Repeated words: {repeated_words}")

# 8. Language Analysis
print("\n8. LANGUAGE ANALYSIS")
print("-" * 40)

# Different language samples
english_text = "Hello world, how are you today?"
spanish_text = "Hola mundo, ¿cómo estás hoy?"
french_text = "Bonjour le monde, comment allez-vous aujourd'hui?"

# Character analysis
english_chars = frozenset(english_text.lower())
spanish_chars = frozenset(spanish_text.lower())
french_chars = frozenset(french_text.lower())

print(f"English chars: {english_chars}")
print(f"Spanish chars: {spanish_chars}")
print(f"French chars: {french_chars}")

# Find common characters
common_all_languages = english_chars.intersection(spanish_chars, french_chars)
print(f"Common characters across all languages: {common_all_languages}")

# Language-specific characters
spanish_specific = spanish_chars.difference(english_chars)
french_specific = french_chars.difference(english_chars)
print(f"Spanish-specific characters: {spanish_specific}")
print(f"French-specific characters: {french_specific}")

# 9. Practical Examples
print("\n9. PRACTICAL EXAMPLES")
print("-" * 40)

# Example 1: Password strength analysis
passwords = ["password123", "MySecureP@ssw0rd!", "12345", "Aa1!Bb2@Cc3#"]

def analyze_password_strength(password):
    chars = frozenset(password)
    lowercase = frozenset(string.ascii_lowercase)
    uppercase = frozenset(string.ascii_uppercase)
    digits = frozenset(string.digits)
    special = frozenset(string.punctuation)
    
    has_lower = bool(chars.intersection(lowercase))
    has_upper = bool(chars.intersection(uppercase))
    has_digit = bool(chars.intersection(digits))
    has_special = bool(chars.intersection(special))
    
    strength = sum([has_lower, has_upper, has_digit, has_special])
    return strength, chars

print("Password strength analysis:")
for pwd in passwords:
    strength, chars = analyze_password_strength(pwd)
    print(f"'{pwd}': Strength {strength}/4, Unique chars: {len(chars)}")

# Example 2: Text similarity
def text_similarity(text1, text2):
    chars1 = frozenset(text1.lower())
    chars2 = frozenset(text2.lower())
    
    intersection = chars1.intersection(chars2)
    union = chars1.union(chars2)
    
    # Jaccard similarity
    similarity = len(intersection) / len(union) if union else 0
    return similarity

texts_to_compare = [
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "computer vision"
]

print(f"\nText similarity analysis:")
for i, text1 in enumerate(texts_to_compare):
    for j, text2 in enumerate(texts_to_compare):
        if i < j:
            similarity = text_similarity(text1, text2)
            print(f"'{text1}' vs '{text2}': {similarity:.2%}")

# Example 3: Plagiarism detection (simplified)
original_text = "Python is a high-level programming language"
suspected_texts = [
    "Python is a high-level programming language",  # Exact match
    "Python is a powerful programming language",    # Similar
    "Java is a high-level programming language",    # Different
    "Machine learning uses Python extensively"      # Different
]

def simple_plagiarism_check(original, suspected):
    orig_words = frozenset(original.lower().split())
    susp_words = frozenset(suspected.lower().split())
    
    common_words = orig_words.intersection(susp_words)
    similarity = len(common_words) / len(orig_words) if orig_words else 0
    
    return similarity

print(f"\nSimple plagiarism detection:")
print(f"Original: '{original_text}'")
for i, suspected in enumerate(suspected_texts, 1):
    similarity = simple_plagiarism_check(original_text, suspected)
    status = "SUSPICIOUS" if similarity > 0.7 else "OK"
    print(f"Text {i}: {similarity:.2%} similar - {status}")

# 10. Performance Comparison
print("\n10. PERFORMANCE COMPARISON")
print("-" * 40)

import time

# Create large text
large_text = "Python programming " * 10000
print(f"Testing with text of {len(large_text)} characters...")

# Time different operations
start_time = time.time()
char_frozenset = frozenset(large_text)
char_time = time.time() - start_time

start_time = time.time()
word_frozenset = frozenset(large_text.split())
word_time = time.time() - start_time

print(f"Character frozenset creation: {char_time:.6f} seconds")
print(f"Word frozenset creation: {word_time:.6f} seconds")
print(f"Character frozenset size: {len(char_frozenset)}")
print(f"Word frozenset size: {len(word_frozenset)}")

# Memory usage
import sys
print(f"\nMemory usage:")
print(f"Original text: {sys.getsizeof(large_text):,} bytes")
print(f"Character frozenset: {sys.getsizeof(char_frozenset):,} bytes")
print(f"Word frozenset: {sys.getsizeof(word_frozenset):,} bytes")

# 11. Text Cleaning and Normalization
print("\n11. TEXT CLEANING AND NORMALIZATION")
print("-" * 40)

messy_text = "  Hello,   WORLD!!!  How    are YOU today???  "
print(f"Original messy text: '{messy_text}'")

# Different cleaning approaches
cleaned_chars = frozenset(messy_text.strip().lower())
cleaned_words = frozenset(messy_text.strip().lower().split())
cleaned_alpha_only = frozenset(char for char in messy_text.lower() if char.isalpha())

print(f"Cleaned characters: {cleaned_chars}")
print(f"Cleaned words: {cleaned_words}")
print(f"Alphabetic only: {cleaned_alpha_only}")

# Text normalization
normalized_text = re.sub(r'[^\w\s]', '', messy_text.lower())
normalized_words = frozenset(normalized_text.split())
print(f"Normalized words: {normalized_words}")

# 12. Real-world Use Cases
print("\n12. REAL-WORLD USE CASES")
print("-" * 40)

# Use case 1: Content moderation
prohibited_words = frozenset([
    "spam", "scam", "fraud", "fake", "illegal", "harmful"
])

user_comments = [
    "This is a great product, highly recommended!",
    "Don't buy this, it's a total scam and fake!",
    "I love using this software for my work",
    "This website promotes illegal activities"
]

print("Content moderation:")
for i, comment in enumerate(user_comments, 1):
    comment_words = frozenset(comment.lower().split())
    violations = comment_words.intersection(prohibited_words)
    status = "FLAGGED" if violations else "APPROVED"
    print(f"Comment {i}: {status} {f'({violations})' if violations else ''}")

# Use case 2: SEO keyword analysis
target_keywords = frozenset([
    "python", "programming", "machine", "learning", "data", "science"
])

web_content = """
Python is a powerful programming language widely used in machine learning and data science.
Our Python programming courses cover everything from basics to advanced machine learning techniques.
Learn data science with Python and become a skilled data scientist.
"""

content_words = frozenset(web_content.lower().split())
keyword_matches = content_words.intersection(target_keywords)
keyword_coverage = len(keyword_matches) / len(target_keywords)

print(f"\nSEO keyword analysis:")
print(f"Target keywords: {target_keywords}")
print(f"Matched keywords: {keyword_matches}")
print(f"Keyword coverage: {keyword_coverage:.2%}")

# Use case 3: Document categorization
categories = {
    'technology': frozenset(['python', 'programming', 'software', 'computer', 'algorithm']),
    'business': frozenset(['marketing', 'sales', 'finance', 'management', 'strategy']),
    'science': frozenset(['research', 'experiment', 'analysis', 'data', 'hypothesis'])
}

documents = [
    "Python programming and software development",
    "Marketing strategy and sales management",
    "Data analysis and research methodology",
    "Computer algorithms and programming languages"
]

print(f"\nDocument categorization:")
for i, doc in enumerate(documents, 1):
    doc_words = frozenset(doc.lower().split())
    best_category = None
    best_score = 0
    
    for category, keywords in categories.items():
        matches = doc_words.intersection(keywords)
        score = len(matches) / len(keywords) if keywords else 0
        if score > best_score:
            best_score = score
            best_category = category
    
    print(f"Document {i}: '{doc}' → {best_category} ({best_score:.2%})")

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)
