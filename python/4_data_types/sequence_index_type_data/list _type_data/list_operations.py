#!/usr/bin/env python3
"""
List Operations Program
This program demonstrates various list operations in Python with examples.
"""

def list_creation_operations():
    """Demonstrate different ways to create lists."""
    
    print("=" * 50)
    print("LIST CREATION OPERATIONS")
    print("=" * 50)
    
    # 1. Empty list creation
    empty_list1 = []
    empty_list2 = list()
    print("1. Empty list creation:")
    print(f"   Using []: {empty_list1}")
    print(f"   Using list(): {empty_list2}")
    
    # 2. List with initial values
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "cherry"]
    mixed = [1, "hello", 3.14, True, None]
    print("\n2. Lists with initial values:")
    print(f"   Numbers: {numbers}")
    print(f"   Fruits: {fruits}")
    print(f"   Mixed types: {mixed}")
    
    # 3. List from string
    char_list = list("hello")
    print(f"\n3. List from string: {char_list}")
    
    # 4. List from range
    range_list = list(range(5))
    range_list2 = list(range(2, 10, 2))
    print(f"\n4. List from range:")
    print(f"   range(5): {range_list}")
    print(f"   range(2, 10, 2): {range_list2}")
    
    # 5. List repetition
    repeated = [0] * 5
    pattern = [1, 2] * 3
    print(f"\n5. List repetition:")
    print(f"   [0] * 5: {repeated}")
    print(f"   [1, 2] * 3: {pattern}")
    
    # 6. List comprehension
    squares = [x**2 for x in range(5)]
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"\n6. List comprehension:")
    print(f"   Squares: {squares}")
    print(f"   Even numbers: {evens}")

def list_access_operations():
    """Demonstrate list access operations."""
    
    print("\n" + "=" * 50)
    print("LIST ACCESS OPERATIONS")
    print("=" * 50)
    
    colors = ["red", "green", "blue", "yellow", "purple"]
    print(f"Original list: {colors}")
    
    # 1. Positive indexing
    print("\n1. Positive indexing:")
    print(f"   First element (index 0): {colors[0]}")
    print(f"   Second element (index 1): {colors[1]}")
    print(f"   Last element (index {len(colors)-1}): {colors[len(colors)-1]}")
    
    # 2. Negative indexing
    print("\n2. Negative indexing:")
    print(f"   Last element (index -1): {colors[-1]}")
    print(f"   Second last (index -2): {colors[-2]}")
    print(f"   First element (index -{len(colors)}): {colors[-len(colors)]}")
    
    # 3. Index bounds checking
    print("\n3. Index bounds checking:")
    try:
        print(f"   Accessing index 10: {colors[10]}")
    except IndexError as e:
        print(f"   Error accessing index 10: {e}")
    
    # 4. Using get-like functionality with slicing
    def safe_get(lst, index, default=None):
        """Safely get element at index with default value."""
        try:
            return lst[index]
        except IndexError:
            return default
    
    print(f"   Safe access index 10: {safe_get(colors, 10, 'Not found')}")
    print(f"   Safe access index 2: {safe_get(colors, 2, 'Not found')}")

def list_slicing_operations():
    """Demonstrate list slicing operations."""
    
    print("\n" + "=" * 50)
    print("LIST SLICING OPERATIONS")
    print("=" * 50)
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Original list: {numbers}")
    
    # 1. Basic slicing
    print("\n1. Basic slicing [start:end]:")
    print(f"   numbers[2:5]: {numbers[2:5]}")
    print(f"   numbers[0:3]: {numbers[0:3]}")
    print(f"   numbers[5:]: {numbers[5:]}")
    print(f"   numbers[:4]: {numbers[:4]}")
    print(f"   numbers[:]: {numbers[:]}")
    
    # 2. Negative slicing
    print("\n2. Negative slicing:")
    print(f"   numbers[-3:]: {numbers[-3:]}")
    print(f"   numbers[:-2]: {numbers[:-2]}")
    print(f"   numbers[-5:-2]: {numbers[-5:-2]}")
    
    # 3. Step slicing
    print("\n3. Step slicing [start:end:step]:")
    print(f"   numbers[::2]: {numbers[::2]}")
    print(f"   numbers[1::2]: {numbers[1::2]}")
    print(f"   numbers[::3]: {numbers[::3]}")
    print(f"   numbers[::-1]: {numbers[::-1]}")
    print(f"   numbers[8:2:-1]: {numbers[8:2:-1]}")
    
    # 4. Slice assignment
    print("\n4. Slice assignment:")
    temp_list = numbers.copy()
    temp_list[2:5] = [20, 30, 40]
    print(f"   After temp_list[2:5] = [20, 30, 40]: {temp_list}")
    
    temp_list = numbers.copy()
    temp_list[1:4] = [100]
    print(f"   After temp_list[1:4] = [100]: {temp_list}")

def list_concatenation_operations():
    """Demonstrate list concatenation and repetition operations."""
    
    print("\n" + "=" * 50)
    print("LIST CONCATENATION & REPETITION")
    print("=" * 50)
    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = ["a", "b", "c"]
    
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"List 3: {list3}")
    
    # 1. Concatenation with +
    print("\n1. Concatenation with + operator:")
    result1 = list1 + list2
    result2 = list1 + list3
    print(f"   list1 + list2: {result1}")
    print(f"   list1 + list3: {result2}")
    
    # 2. Multiple concatenation
    print("\n2. Multiple concatenation:")
    result3 = list1 + list2 + list3
    print(f"   list1 + list2 + list3: {result3}")
    
    # 3. Repetition with *
    print("\n3. Repetition with * operator:")
    repeated1 = list1 * 3
    repeated2 = [0] * 5
    print(f"   list1 * 3: {repeated1}")
    print(f"   [0] * 5: {repeated2}")
    
    # 4. In-place concatenation with +=
    print("\n4. In-place concatenation with +=:")
    temp_list = list1.copy()
    print(f"   Before: {temp_list}")
    temp_list += list2
    print(f"   After temp_list += list2: {temp_list}")
    
    # 5. In-place repetition with *=
    print("\n5. In-place repetition with *=:")
    temp_list = [1, 2]
    print(f"   Before: {temp_list}")
    temp_list *= 3
    print(f"   After temp_list *= 3: {temp_list}")

def list_comparison_operations():
    """Demonstrate list comparison operations."""
    
    print("\n" + "=" * 50)
    print("LIST COMPARISON OPERATIONS")
    print("=" * 50)
    
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    list4 = [1, 2, 3, 4]
    
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"List 3: {list3}")
    print(f"List 4: {list4}")
    
    # 1. Equality comparison
    print("\n1. Equality comparison:")
    print(f"   list1 == list2: {list1 == list2}")
    print(f"   list1 == list3: {list1 == list3}")
    print(f"   list1 != list3: {list1 != list3}")
    
    # 2. Lexicographic comparison
    print("\n2. Lexicographic comparison:")
    print(f"   list1 < list3: {list1 < list3}")
    print(f"   list1 > list3: {list1 > list3}")
    print(f"   list1 < list4: {list1 < list4}")
    print(f"   list1 <= list2: {list1 <= list2}")
    
    # 3. Identity comparison
    print("\n3. Identity comparison:")
    list5 = list1
    list6 = list1.copy()
    print(f"   list1 is list5: {list1 is list5}")
    print(f"   list1 is list6: {list1 is list6}")
    print(f"   list1 == list6: {list1 == list6}")

def list_membership_operations():
    """Demonstrate membership operations."""
    
    print("\n" + "=" * 50)
    print("LIST MEMBERSHIP OPERATIONS")
    print("=" * 50)
    
    fruits = ["apple", "banana", "cherry", "date"]
    numbers = [1, 2, 3, 4, 5]
    
    print(f"Fruits: {fruits}")
    print(f"Numbers: {numbers}")
    
    # 1. in operator
    print("\n1. 'in' operator:")
    print(f"   'banana' in fruits: {'banana' in fruits}")
    print(f"   'grape' in fruits: {'grape' in fruits}")
    print(f"   3 in numbers: {3 in numbers}")
    print(f"   10 in numbers: {10 in numbers}")
    
    # 2. not in operator
    print("\n2. 'not in' operator:")
    print(f"   'grape' not in fruits: {'grape' not in fruits}")
    print(f"   'apple' not in fruits: {'apple' not in fruits}")
    print(f"   10 not in numbers: {10 not in numbers}")
    
    # 3. Membership with sublists
    nested = [[1, 2], [3, 4], [5, 6]]
    print(f"\n3. Membership with sublists:")
    print(f"   Nested list: {nested}")
    print(f"   [1, 2] in nested: {[1, 2] in nested}")
    print(f"   [1, 3] in nested: {[1, 3] in nested}")

def list_iteration_operations():
    """Demonstrate list iteration operations."""
    
    print("\n" + "=" * 50)
    print("LIST ITERATION OPERATIONS")
    print("=" * 50)
    
    colors = ["red", "green", "blue", "yellow"]
    numbers = [10, 20, 30, 40, 50]
    
    # 1. Basic iteration
    print("1. Basic iteration:")
    print("   Colors:", end=" ")
    for color in colors:
        print(color, end=" ")
    print()
    
    # 2. Iteration with index using enumerate
    print("\n2. Iteration with index using enumerate:")
    for i, color in enumerate(colors):
        print(f"   Index {i}: {color}")
    
    # 3. Iteration with custom start index
    print("\n3. Iteration with custom start index:")
    for i, color in enumerate(colors, start=1):
        print(f"   Position {i}: {color}")
    
    # 4. Parallel iteration with zip
    print("\n4. Parallel iteration with zip:")
    for color, number in zip(colors, numbers):
        print(f"   {color} -> {number}")
    
    # 5. Iteration with range and len
    print("\n5. Iteration with range and len:")
    for i in range(len(colors)):
        print(f"   Index {i}: {colors[i]}")
    
    # 6. Reverse iteration
    print("\n6. Reverse iteration:")
    print("   Reversed colors:", end=" ")
    for color in reversed(colors):
        print(color, end=" ")
    print()

def list_unpacking_operations():
    """Demonstrate list unpacking operations."""
    
    print("\n" + "=" * 50)
    print("LIST UNPACKING OPERATIONS")
    print("=" * 50)
    
    # 1. Basic unpacking
    coordinates = [10, 20]
    x, y = coordinates
    print("1. Basic unpacking:")
    print(f"   Coordinates: {coordinates}")
    print(f"   x = {x}, y = {y}")
    
    # 2. Unpacking with more variables
    rgb = [255, 128, 0]
    red, green, blue = rgb
    print(f"\n2. RGB unpacking:")
    print(f"   RGB: {rgb}")
    print(f"   Red: {red}, Green: {green}, Blue: {blue}")
    
    # 3. Extended unpacking with *
    numbers = [1, 2, 3, 4, 5, 6]
    first, *middle, last = numbers
    print(f"\n3. Extended unpacking:")
    print(f"   Numbers: {numbers}")
    print(f"   First: {first}")
    print(f"   Middle: {middle}")
    print(f"   Last: {last}")
    
    # 4. Unpacking in function calls
    def print_coordinates(x, y, z):
        print(f"   Coordinates: x={x}, y={y}, z={z}")
    
    coords_3d = [100, 200, 300]
    print(f"\n4. Unpacking in function calls:")
    print(f"   3D Coordinates: {coords_3d}")
    print_coordinates(*coords_3d)

def nested_list_operations():
    """Demonstrate nested list operations."""
    
    print("\n" + "=" * 50)
    print("NESTED LIST OPERATIONS")
    print("=" * 50)
    
    # 1. Creating nested lists
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("1. 2D Matrix:")
    for row in matrix:
        print(f"   {row}")
    
    # 2. Accessing nested elements
    print(f"\n2. Accessing elements:")
    print(f"   matrix[0][1]: {matrix[0][1]}")
    print(f"   matrix[1][2]: {matrix[1][2]}")
    print(f"   matrix[2][0]: {matrix[2][0]}")
    
    # 3. Modifying nested elements
    print(f"\n3. Modifying elements:")
    matrix[1][1] = 50
    print(f"   After matrix[1][1] = 50:")
    for row in matrix:
        print(f"   {row}")
    
    # 4. Nested list comprehension
    print(f"\n4. Nested list comprehension:")
    squares_matrix = [[x**2 for x in range(3)] for _ in range(3)]
    print(f"   Squares matrix:")
    for row in squares_matrix:
        print(f"   {row}")
    
    # 5. Flattening nested lists
    print(f"\n5. Flattening nested lists:")
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = [item for sublist in nested for item in sublist]
    print(f"   Nested: {nested}")
    print(f"   Flattened: {flattened}")

def list_as_stack_queue():
    """Demonstrate using lists as stacks and queues."""
    
    print("\n" + "=" * 50)
    print("LIST AS STACK AND QUEUE")
    print("=" * 50)
    
    # 1. List as Stack (LIFO - Last In, First Out)
    print("1. List as Stack (LIFO):")
    stack = []
    print(f"   Initial stack: {stack}")
    
    # Push operations
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(f"   After pushing 1, 2, 3: {stack}")
    
    # Pop operations
    item = stack.pop()
    print(f"   Popped: {item}, Stack: {stack}")
    item = stack.pop()
    print(f"   Popped: {item}, Stack: {stack}")
    
    # 2. List as Queue (FIFO - First In, First Out)
    print(f"\n2. List as Queue (FIFO):")
    queue = []
    print(f"   Initial queue: {queue}")
    
    # Enqueue operations
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(f"   After enqueuing 1, 2, 3: {queue}")
    
    # Dequeue operations
    item = queue.pop(0)
    print(f"   Dequeued: {item}, Queue: {queue}")
    item = queue.pop(0)
    print(f"   Dequeued: {item}, Queue: {queue}")

def practical_list_operations():
    """Demonstrate practical list operations."""
    
    print("\n" + "=" * 50)
    print("PRACTICAL LIST OPERATIONS")
    print("=" * 50)
    
    # 1. Finding elements
    numbers = [10, 25, 30, 45, 50, 75, 80]
    print("1. Finding elements:")
    print(f"   Numbers: {numbers}")
    
    # Find maximum and minimum
    print(f"   Maximum: {max(numbers)}")
    print(f"   Minimum: {min(numbers)}")
    
    # Find index of specific value
    try:
        index = numbers.index(30)
        print(f"   Index of 30: {index}")
    except ValueError:
        print("   30 not found")
    
    # 2. Filtering lists
    print(f"\n2. Filtering operations:")
    evens = [x for x in numbers if x % 2 == 0]
    odds = [x for x in numbers if x % 2 != 0]
    greater_than_40 = [x for x in numbers if x > 40]
    
    print(f"   Even numbers: {evens}")
    print(f"   Odd numbers: {odds}")
    print(f"   Greater than 40: {greater_than_40}")
    
    # 3. Transforming lists
    print(f"\n3. Transforming operations:")
    squares = [x**2 for x in numbers]
    doubled = [x * 2 for x in numbers]
    
    print(f"   Squares: {squares}")
    print(f"   Doubled: {doubled}")
    
    # 4. Aggregating lists
    print(f"\n4. Aggregating operations:")
    total = sum(numbers)
    average = total / len(numbers)
    product = 1
    for num in numbers:
        product *= num
    
    print(f"   Sum: {total}")
    print(f"   Average: {average:.2f}")
    print(f"   Product: {product}")
    
    # 5. List statistics
    print(f"\n5. List statistics:")
    sorted_numbers = sorted(numbers)
    length = len(numbers)
    median = sorted_numbers[length // 2] if length % 2 == 1 else (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
    
    print(f"   Sorted: {sorted_numbers}")
    print(f"   Length: {length}")
    print(f"   Median: {median}")

def main():
    """Main function to run all demonstrations."""
    list_creation_operations()
    list_access_operations()
    list_slicing_operations()
    list_concatenation_operations()
    list_comparison_operations()
    list_membership_operations()
    list_iteration_operations()
    list_unpacking_operations()
    nested_list_operations()
    list_as_stack_queue()
    practical_list_operations()
    
    print("\n" + "=" * 50)
    print("PROGRAM COMPLETED SUCCESSFULLY!")
    print("=" * 50)

if __name__ == "__main__":
    main()
