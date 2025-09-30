#!/usr/bin/env python3
"""
Dictionary Operations Program
============================

This program demonstrates comprehensive dictionary operations including:
1. Dictionary Creation
2. Basic Operations (CRUD)
3. Advanced Operations
4. Dictionary Methods
5. Error Handling
6. Best Practices

Author: Python Learning Series
"""

import copy
from collections import namedtuple


def print_separator(title):
    """Print a formatted separator for different sections."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def dictionary_creation():
    """Demonstrate different ways to create dictionaries."""
    print_separator("DICTIONARY CREATION")
    
    # Method 1: Using curly braces
    print("1. Using Curly Braces:")
    empty_dict = {}
    student = {'name': 'John', 'age': 20, 'grade': 'A'}
    mixed_dict = {'name': 'Alice', 'scores': [85, 92, 78], 'passed': True}
    nested_dict = {
        'person': {
            'name': 'Bob',
            'address': {'city': 'New York', 'zip': '10001'}
        }
    }
    
    print(f"Empty dictionary: {empty_dict}")
    print(f"Student dictionary: {student}")
    print(f"Mixed data types: {mixed_dict}")
    print(f"Nested dictionary: {nested_dict}")
    
    # Method 2: Using dict() constructor
    print("\n2. Using dict() Constructor:")
    d1 = dict(name='John', age=25, city='Boston')
    d2 = dict([('a', 1), ('b', 2), ('c', 3)])
    d3 = dict({'x': 10, 'y': 20})
    
    keys = ['name', 'age', 'city']
    values = ['Alice', 30, 'Seattle']
    d4 = dict(zip(keys, values))
    
    print(f"From keyword arguments: {d1}")
    print(f"From key-value pairs: {d2}")
    print(f"From another dictionary: {d3}")
    print(f"From zip of lists: {d4}")
    
    # Method 3: Dictionary comprehension
    print("\n3. Dictionary Comprehension:")
    squares = {x: x**2 for x in range(1, 6)}
    even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    char_count = {char: 'hello'.count(char) for char in set('hello')}
    
    print(f"Squares: {squares}")
    print(f"Even squares: {even_squares}")
    print(f"Character count: {char_count}")


def basic_operations():
    """Demonstrate basic dictionary operations."""
    print_separator("BASIC DICTIONARY OPERATIONS")
    
    # Initialize student dictionary
    student = {'name': 'John', 'age': 20}
    print(f"Initial student: {student}")
    
    # Adding elements
    print("\n1. Adding Elements:")
    student['grade'] = 'A'
    student['subjects'] = ['Math', 'Physics', 'Chemistry']
    student['gpa'] = 3.8
    print(f"After adding elements: {student}")
    
    # Accessing elements
    print("\n2. Accessing Elements:")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Subjects: {student['subjects']}")
    
    # Safe access using get()
    print(f"Grade (using get): {student.get('grade')}")
    print(f"Phone (using get with default): {student.get('phone', 'Not provided')}")
    
    # Updating elements
    print("\n3. Updating Elements:")
    student['age'] = 21
    student['grade'] = 'A+'
    print(f"After updating age and grade: {student}")
    
    # Multiple updates
    student.update({'gpa': 3.9, 'semester': 'Fall 2024'})
    print(f"After multiple updates: {student}")
    
    # Removing elements
    print("\n4. Removing Elements:")
    original_student = student.copy()
    
    # Remove using del
    del student['semester']
    print(f"After deleting semester: {student}")
    
    # Remove using pop() - returns value
    removed_gpa = student.pop('gpa')
    print(f"Removed GPA: {removed_gpa}")
    print(f"After popping GPA: {student}")
    
    # Remove with default value
    phone = student.pop('phone', 'No phone found')
    print(f"Phone removal result: {phone}")
    
    # Remove last inserted item
    last_item = student.popitem()
    print(f"Last item removed: {last_item}")
    print(f"After popitem(): {student}")


def advanced_operations():
    """Demonstrate advanced dictionary operations."""
    print_separator("ADVANCED DICTIONARY OPERATIONS")
    
    # Merging dictionaries
    print("1. Merging Dictionaries:")
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'e': 5, 'f': 6}
    
    # Using update()
    merged1 = dict1.copy()
    merged1.update(dict2)
    print(f"Using update(): {merged1}")
    
    # Using ** operator (Python 3.5+)
    merged2 = {**dict1, **dict2, **dict3}
    print(f"Using ** operator: {merged2}")
    
    # Using | operator (Python 3.9+)
    try:
        merged3 = dict1 | dict2
        print(f"Using | operator: {merged3}")
    except TypeError:
        print("| operator not supported in this Python version")
    
    # Handle key conflicts
    print("\n2. Handling Key Conflicts:")
    person1 = {'name': 'John', 'age': 25, 'city': 'Boston'}
    person2 = {'name': 'Jane', 'age': 30, 'country': 'USA'}
    
    merged_person = {**person1, **person2}
    print(f"Merged (person2 overwrites): {merged_person}")
    
    # Copying dictionaries
    print("\n3. Copying Dictionaries:")
    original = {'a': 1, 'b': [2, 3], 'c': {'nested': 'value'}}
    
    # Shallow copy
    shallow_copy1 = original.copy()
    shallow_copy2 = dict(original)
    
    # Deep copy
    deep_copy = copy.deepcopy(original)
    
    print(f"Original: {original}")
    
    # Modify nested structure
    original['b'].append(4)
    original['c']['nested'] = 'modified'
    
    print(f"After modifying original:")
    print(f"  Original: {original}")
    print(f"  Shallow copy: {shallow_copy1}")
    print(f"  Deep copy: {deep_copy}")
    
    # Dictionary filtering
    print("\n4. Dictionary Filtering:")
    grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96, 'Eve': 81}
    
    # Filter high grades
    high_grades = {name: grade for name, grade in grades.items() if grade >= 90}
    print(f"High grades (>=90): {high_grades}")
    
    # Filter by name length
    short_names = {name: grade for name, grade in grades.items() if len(name) <= 5}
    print(f"Short names (<=5 chars): {short_names}")


def dictionary_methods():
    """Demonstrate all dictionary methods."""
    print_separator("DICTIONARY METHODS")
    
    student = {'name': 'John', 'age': 20, 'grade': 'A', 'subjects': ['Math', 'Physics']}
    
    # 1. keys() method
    print("1. keys() method:")
    keys = student.keys()
    print(f"Keys: {list(keys)}")
    print(f"Keys type: {type(keys)}")
    
    # 2. values() method
    print("\n2. values() method:")
    values = student.values()
    print(f"Values: {list(values)}")
    
    # 3. items() method
    print("\n3. items() method:")
    items = student.items()
    print(f"Items: {list(items)}")
    
    # Iteration examples
    print("\n4. Iteration Examples:")
    print("Iterating through keys:")
    for key in student.keys():
        print(f"  {key}")
    
    print("Iterating through values:")
    for value in student.values():
        print(f"  {value}")
    
    print("Iterating through key-value pairs:")
    for key, value in student.items():
        print(f"  {key}: {value}")
    
    # 5. get() method
    print("\n5. get() method:")
    print(f"Name: {student.get('name')}")
    print(f"Phone: {student.get('phone')}")
    print(f"Phone with default: {student.get('phone', 'Not available')}")
    
    # 6. setdefault() method
    print("\n6. setdefault() method:")
    original_student = student.copy()
    
    # Key exists
    name = student.setdefault('name', 'Unknown')
    print(f"Name (exists): {name}")
    
    # Key doesn't exist
    phone = student.setdefault('phone', '123-456-7890')
    print(f"Phone (new): {phone}")
    print(f"Updated student: {student}")
    
    # 7. fromkeys() method
    print("\n7. fromkeys() method:")
    template_keys = ['name', 'age', 'grade', 'gpa']
    template = dict.fromkeys(template_keys, 'Unknown')
    print(f"Template: {template}")
    
    scores_template = dict.fromkeys(['math', 'science', 'english'], 0)
    print(f"Scores template: {scores_template}")
    
    # 8. clear() method
    print("\n8. clear() method:")
    temp_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f"Before clear: {temp_dict}")
    temp_dict.clear()
    print(f"After clear: {temp_dict}")


def error_handling():
    """Demonstrate common dictionary errors and their solutions."""
    print_separator("ERROR HANDLING")
    
    student = {'name': 'John', 'age': 20}
    
    # 1. KeyError handling
    print("1. KeyError Handling:")
    try:
        print(student['grade'])  # This will raise KeyError
    except KeyError as e:
        print(f"KeyError caught: {e}")
    
    # Safe alternatives
    print("Safe alternatives:")
    print(f"  Using get(): {student.get('grade', 'Not assigned')}")
    print(f"  Using 'in' operator: {'grade' in student}")
    
    # 2. TypeError with mutable keys
    print("\n2. TypeError with Mutable Keys:")
    try:
        mutable_key = [1, 2]
        invalid_dict = {mutable_key: 'value'}  # Lists are mutable  # type: ignore
    except TypeError as e:
        print(f"TypeError caught: {e}")
    
    # Valid key types
    valid_dict = {
        'string': 'value1',
        42: 'value2',
        (1, 2): 'value3',  # Tuples are immutable
        True: 'value4'
    }
    print(f"Valid dictionary: {valid_dict}")
    
    # 3. Modifying dictionary while iterating
    print("\n3. Safe Dictionary Modification:")
    grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}
    
    # Wrong way (can cause issues)
    print("Removing failing grades (safe way):")
    to_remove = []
    for name, grade in grades.items():
        if grade < 80:
            to_remove.append(name)
    
    for name in to_remove:
        del grades[name]
    
    print(f"After removing: {grades}")
    
    # Better way using dictionary comprehension
    original_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}
    passing_grades = {name: grade for name, grade in original_grades.items() if grade >= 80}
    print(f"Passing grades: {passing_grades}")


def practical_examples():
    """Demonstrate practical dictionary usage examples."""
    print_separator("PRACTICAL EXAMPLES")
    
    # 1. Student grade management
    print("1. Student Grade Management System:")
    
    class GradeManager:
        def __init__(self):
            self.students = {}
        
        def add_student(self, name, grades=None):
            if grades is None:
                grades = {}
            self.students[name] = grades
        
        def add_grade(self, name, subject, grade):
            if name not in self.students:
                self.students[name] = {}
            self.students[name][subject] = grade
        
        def get_average(self, name):
            if name in self.students and self.students[name]:
                grades = self.students[name].values()
                return sum(grades) / len(grades)
            return 0
        
        def get_student_info(self, name):
            return self.students.get(name, {})
        
        def display_all(self):
            for name, grades in self.students.items():
                avg = self.get_average(name)
                print(f"  {name}: {grades} (Average: {avg:.2f})")
    
    # Use the grade manager
    gm = GradeManager()
    gm.add_student('Alice')
    gm.add_grade('Alice', 'Math', 85)
    gm.add_grade('Alice', 'Science', 92)
    gm.add_grade('Alice', 'English', 78)
    
    gm.add_student('Bob')
    gm.add_grade('Bob', 'Math', 90)
    gm.add_grade('Bob', 'Science', 88)
    
    gm.display_all()
    
    # 2. Word frequency counter
    print("\n2. Word Frequency Counter:")
    text = "python is great and python is powerful and python is fun"
    words = text.split()
    
    # Method 1: Using setdefault
    freq1 = {}
    for word in words:
        freq1.setdefault(word, 0)
        freq1[word] += 1
    
    # Method 2: Using get
    freq2 = {}
    for word in words:
        freq2[word] = freq2.get(word, 0) + 1
    
    print(f"Word frequencies: {freq1}")
    
    # 3. Grouping data
    print("\n3. Grouping Students by Grade:")
    students_data = [
        {'name': 'Alice', 'grade': 'A', 'age': 20},
        {'name': 'Bob', 'grade': 'B', 'age': 21},
        {'name': 'Charlie', 'grade': 'A', 'age': 19},
        {'name': 'Diana', 'grade': 'B', 'age': 20},
        {'name': 'Eve', 'grade': 'A', 'age': 22}
    ]
    
    grouped = {}
    for student in students_data:
        grade = student['grade']
        if grade not in grouped:
            grouped[grade] = []
        grouped[grade].append(student['name'])
    
    for grade, names in grouped.items():
        print(f"  Grade {grade}: {names}")
    
    # 4. Configuration management
    print("\n4. Configuration Management:")
    default_config = {
        'host': 'localhost',
        'port': 8080,
        'debug': False,
        'timeout': 30
    }
    
    user_config = {
        'port': 9000,
        'debug': True
    }
    
    # Merge configurations
    final_config = {**default_config, **user_config}
    print(f"Final configuration: {final_config}")


def performance_tips():
    """Demonstrate performance optimization tips."""
    print_separator("PERFORMANCE TIPS")
    
    # 1. Membership testing
    print("1. Fast Membership Testing:")
    large_dict = {f'key_{i}': f'value_{i}' for i in range(1000)}
    
    # Fast O(1) lookup
    if 'key_500' in large_dict:
        print("  Key found using 'in' operator (O(1))")
    
    # 2. Efficient iteration
    print("\n2. Efficient Iteration:")
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    
    # Good: Direct iteration over items
    print("  Iterating over items:")
    for key, value in sample_dict.items():
        print(f"    {key}: {value}")
    
    # 3. Batch operations
    print("\n3. Batch Operations:")
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    
    # Good: Use update for multiple additions
    dict1.update(dict2)
    print(f"  After batch update: {dict1}")
    
    # 4. Dictionary comprehension vs loops
    print("\n4. Dictionary Comprehension Performance:")
    
    # Comprehension (faster)
    squares_comp = {x: x**2 for x in range(100)}
    
    # Loop (slower)
    squares_loop = {}
    for x in range(100):
        squares_loop[x] = x**2
    
    print(f"  Both methods created {len(squares_comp)} items")


def main():
    """Main function to run all dictionary operation examples."""
    print("🐍 COMPREHENSIVE DICTIONARY OPERATIONS PROGRAM 🐍")
    print("=" * 60)
    
    # Run all demonstration functions
    dictionary_creation()
    basic_operations()
    advanced_operations()
    dictionary_methods()
    error_handling()
    practical_examples()
    performance_tips()
    
    print_separator("PROGRAM COMPLETED")
    print("All dictionary operations have been demonstrated!")
    print("Review the output above to understand different dictionary concepts.")


if __name__ == "__main__":
    main()
