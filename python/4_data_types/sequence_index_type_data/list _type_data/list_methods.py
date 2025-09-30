#!/usr/bin/env python3
"""
List Methods Program
This program demonstrates various list methods in Python with examples.
"""

def demonstrate_list_methods():
    """Demonstrate various list methods with examples."""
    
    print("=" * 50)
    print("LIST METHODS DEMONSTRATION")
    print("=" * 50)
    
    # Initialize sample lists
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4, 5]
    mixed_list = [1, "hello", 3.14, True]
    
    print("\n1. APPEND METHOD - Add single element to end")
    print("Original fruits:", fruits)
    fruits.append("orange")
    print("After append('orange'):", fruits)
    
    print("\n2. EXTEND METHOD - Add multiple elements to end")
    print("Original fruits:", fruits)
    fruits.extend(["grape", "kiwi"])
    print("After extend(['grape', 'kiwi']):", fruits)
    
    print("\n3. INSERT METHOD - Add element at specific position")
    print("Original fruits:", fruits)
    fruits.insert(1, "mango")
    print("After insert(1, 'mango'):", fruits)
    
    print("\n4. REMOVE METHOD - Remove first occurrence of element")
    print("Original fruits:", fruits)
    fruits.remove("banana")
    print("After remove('banana'):", fruits)
    
    print("\n5. POP METHOD - Remove and return element at index")
    print("Original fruits:", fruits)
    popped_fruit = fruits.pop(2)
    print(f"Popped element at index 2: {popped_fruit}")
    print("After pop(2):", fruits)
    
    # Pop without index (removes last element)
    last_fruit = fruits.pop()
    print(f"Popped last element: {last_fruit}")
    print("After pop():", fruits)
    
    print("\n6. INDEX METHOD - Find index of element")
    print("Current fruits:", fruits)
    try:
        index = fruits.index("apple")
        print(f"Index of 'apple': {index}")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n7. COUNT METHOD - Count occurrences of element")
    sample_list = [1, 2, 2, 3, 2, 4, 2, 5]
    print("Sample list:", sample_list)
    count = sample_list.count(2)
    print(f"Count of 2: {count}")
    
    print("\n8. SORT METHOD - Sort list in ascending order")
    numbers_copy = [64, 34, 25, 12, 22, 11, 90]
    print("Original numbers:", numbers_copy)
    numbers_copy.sort()
    print("After sort():", numbers_copy)
    
    # Sort in descending order
    numbers_copy.sort(reverse=True)
    print("After sort(reverse=True):", numbers_copy)
    
    print("\n9. REVERSE METHOD - Reverse the order of elements")
    print("Original numbers:", numbers_copy)
    numbers_copy.reverse()
    print("After reverse():", numbers_copy)
    
    print("\n10. COPY METHOD - Create shallow copy of list")
    original = [1, 2, [3, 4], 5]
    copied = original.copy()
    print("Original list:", original)
    print("Copied list:", copied)
    print("Are they the same object?", original is copied)
    
    print("\n11. CLEAR METHOD - Remove all elements")
    temp_list = [1, 2, 3, 4, 5]
    print("Before clear():", temp_list)
    temp_list.clear()
    print("After clear():", temp_list)
    
    print("\n12. LEN FUNCTION - Get length of list")
    print("Length of fruits:", len(fruits))
    print("Length of numbers:", len(numbers))
    
    print("\n13. MIN and MAX FUNCTIONS")
    nums = [45, 23, 78, 12, 67, 89, 34]
    print("Numbers:", nums)
    print("Minimum:", min(nums))
    print("Maximum:", max(nums))
    
    print("\n14. SUM FUNCTION - Sum of numeric elements")
    print("Sum of numbers:", sum(nums))
    
    print("\n15. SORTED FUNCTION - Return sorted copy (doesn't modify original)")
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Original:", unsorted)
    print("Sorted copy:", sorted(unsorted))
    print("Original unchanged:", unsorted)

def list_comprehension_with_methods():
    """Demonstrate list methods with list comprehension."""
    
    print("\n" + "=" * 50)
    print("LIST METHODS WITH LIST COMPREHENSION")
    print("=" * 50)
    
    # Create list of squares
    squares = [x**2 for x in range(1, 6)]
    print("Squares:", squares)
    
    # Filter even numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [x for x in numbers if x % 2 == 0]
    print("Even numbers:", even_numbers)
    
    # String methods on list of strings
    words = ["hello", "world", "python", "programming"]
    uppercase_words = [word.upper() for word in words]
    print("Uppercase words:", uppercase_words)

def advanced_list_operations():
    """Demonstrate advanced list operations."""
    
    print("\n" + "=" * 50)
    print("ADVANCED LIST OPERATIONS")
    print("=" * 50)
    
    # List slicing
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Original:", numbers)
    print("First 5 elements:", numbers[:5])
    print("Last 5 elements:", numbers[-5:])
    print("Every second element:", numbers[::2])
    print("Reversed using slice:", numbers[::-1])
    
    # List multiplication
    repeated = [1, 2, 3] * 3
    print("List multiplication [1,2,3] * 3:", repeated)
    
    # List concatenation
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated = list1 + list2
    print("Concatenation [1,2,3] + [4,5,6]:", concatenated)
    
    # Membership testing
    print("Is 5 in numbers?", 5 in numbers)
    print("Is 15 not in numbers?", 15 not in numbers)

def practical_examples():
    """Practical examples using list methods."""
    
    print("\n" + "=" * 50)
    print("PRACTICAL EXAMPLES")
    print("=" * 50)
    
    # Example 1: Managing a shopping cart
    shopping_cart = []
    print("Shopping Cart Management:")
    shopping_cart.append("milk")
    shopping_cart.append("bread")
    shopping_cart.extend(["eggs", "cheese"])
    print("Cart after adding items:", shopping_cart)
    
    # Remove an item
    shopping_cart.remove("bread")
    print("Cart after removing bread:", shopping_cart)
    
    # Example 2: Student grades management
    grades = [85, 90, 78, 92, 88]
    print("\nGrades Management:")
    print("Original grades:", grades)
    grades.append(95)  # Add new grade
    print("After adding new grade:", grades)
    print("Average grade:", sum(grades) / len(grades))
    grades.sort(reverse=True)  # Sort in descending order
    print("Sorted grades (highest first):", grades)
    
    # Example 3: Removing duplicates while preserving order
    numbers_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4, 6]
    unique_numbers = []
    for num in numbers_with_duplicates:
        if num not in unique_numbers:
            unique_numbers.append(num)
    print("\nRemoving duplicates:")
    print("Original:", numbers_with_duplicates)
    print("Unique numbers:", unique_numbers)

def main():
    """Main function to run all demonstrations."""
    demonstrate_list_methods()
    list_comprehension_with_methods()
    advanced_list_operations()
    practical_examples()
    
    print("\n" + "=" * 50)
    print("PROGRAM COMPLETED SUCCESSFULLY!")
    print("=" * 50)

if __name__ == "__main__":
    main()
