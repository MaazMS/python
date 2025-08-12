# Python Advanced Functions Documentation

## 1. Lambda, Functional Programming, and Advanced Concepts - Definition and Characteristics

### 1.1 Lambda Functions

**Definition**: Lambda functions are anonymous functions defined using the `lambda` keyword. They can have any number of arguments but can only have one expression.

#### Characteristics
- Anonymous (no name required)
- Single expression only
- Returns a function object
- Often used with higher-order functions
- More concise than regular functions for simple operations

#### Basic Lambda Structure

```python
def lambda_definition_examples():
    """Demonstrate basic lambda function definitions"""
    
    # Basic lambda syntax
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with multiple arguments
    add = lambda x, y: x + y
    print(f"Add 3 + 4: {add(3, 4)}")
    
    # Lambda with default arguments
    multiply = lambda x, y=2: x * y
    print(f"Multiply 5 (default): {multiply(5)}")
    print(f"Multiply 5 * 3: {multiply(5, 3)}")
    
    # Lambda with conditional expression
    max_val = lambda x, y: x if x > y else y
    print(f"Max of 10, 7: {max_val(10, 7)}")
    
    # Lambda returning another lambda (closure)
    multiplier = lambda n: lambda x: x * n
    double = multiplier(2)
    triple = multiplier(3)
    print(f"Double 4: {double(4)}")
    print(f"Triple 4: {triple(4)}")

lambda_definition_examples()
```

#### Lambda vs Regular Functions

```python
def lambda_vs_function_comparison():
    """Compare lambda functions with regular functions"""
    
    # Regular function
    def regular_cube(x):
        """Calculate cube of x"""
        return x ** 3
    
    # Lambda equivalent
    lambda_cube = lambda x: x ** 3
    
    # Complex regular function
    def regular_process(x, y):
        """Process two numbers with validation"""
        if x < 0 or y < 0:
            return 0
        return (x + y) * 2
    
    # Lambda equivalent (limited)
    lambda_process = lambda x, y: (x + y) * 2 if x >= 0 and y >= 0 else 0
    
    print("Regular vs Lambda Comparison:")
    print(f"Regular cube(3): {regular_cube(3)}")
    print(f"Lambda cube(3): {lambda_cube(3)}")
    print(f"Regular process(3, 4): {regular_process(3, 4)}")
    print(f"Lambda process(3, 4): {lambda_process(3, 4)}")
    
    # Differences
    print(f"\nFunction name: {regular_cube.__name__}")
    print(f"Lambda name: {lambda_cube.__name__}")
    print(f"Function docstring: {regular_cube.__doc__}")
    print(f"Lambda docstring: {lambda_cube.__doc__}")

lambda_vs_function_comparison()
```

### 1.2 Filter Function

**Definition**: `filter()` creates an iterator from elements of an iterable for which a function returns True.

#### Characteristics
- Returns a filter object (iterator)
- Filters elements based on a condition
- First argument: function that returns True/False
- Second argument: iterable to filter
- Lazy evaluation (computed on demand)

```python
def filter_characteristics():
    """Demonstrate filter function characteristics"""
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Basic filtering
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Filter with None (removes falsy values)
    mixed_values = [0, 1, False, True, '', 'hello', [], [1, 2], None]
    truthy_values = list(filter(None, mixed_values))
    print(f"Truthy values: {truthy_values}")
    
    # Filter strings
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    long_words = list(filter(lambda word: len(word) > 5, words))
    print(f"Long words: {long_words}")
    
    # Filter with custom function
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = list(filter(is_prime, range(1, 21)))
    print(f"Prime numbers 1-20: {primes}")
    
    # Filter objects
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person('{self.name}', {self.age})"
    
    people = [
        Person('Alice', 25),
        Person('Bob', 17),
        Person('Charlie', 30),
        Person('Diana', 16)
    ]
    
    adults = list(filter(lambda person: person.age >= 18, people))
    print(f"Adults: {adults}")

filter_characteristics()
```

### 1.3 Map Function

**Definition**: `map()` applies a function to every item of an iterable and returns an iterator.

#### Characteristics
- Returns a map object (iterator)
- Applies function to each element
- Can work with multiple iterables
- Length determined by shortest iterable
- Lazy evaluation

```python
def map_characteristics():
    """Demonstrate map function characteristics"""
    
    numbers = [1, 2, 3, 4, 5]
    
    # Basic mapping
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Squares: {squares}")
    
    # Map with multiple iterables
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40, 50]  # Extra element ignored
    sums = list(map(lambda x, y: x + y, list1, list2))
    print(f"Element-wise sum: {sums}")
    
    # Map with built-in functions
    str_numbers = ['1', '2', '3', '4', '5']
    integers = list(map(int, str_numbers))
    print(f"String to int: {integers}")
    
    # Map with string operations
    words = ['hello', 'world', 'python', 'programming']
    upper_words = list(map(str.upper, words))
    print(f"Uppercase: {upper_words}")
    
    # Map vs list comprehension comparison
    # Using map
    cubes_map = list(map(lambda x: x ** 3, numbers))
    
    # Using list comprehension
    cubes_comp = [x ** 3 for x in numbers]
    
    print(f"Cubes (map): {cubes_map}")
    print(f"Cubes (comprehension): {cubes_comp}")
    
    # Map with complex transformations
    data = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78}
    ]
    
    names = list(map(lambda person: person['name'], data))
    grades = list(map(lambda person: 'A' if person['score'] >= 90 else 'B' if person['score'] >= 80 else 'C', data))
    
    print(f"Names: {names}")
    print(f"Grades: {grades}")

map_characteristics()
```

---

## 2. Operations with Lambda, Filter, Map, and Advanced Concepts

### 2.1 Lambda Operations

```python
def lambda_operations():
    """Demonstrate various lambda operations"""
    
    # Arithmetic operations
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else None,
        'power': lambda x, y: x ** y,
        'modulo': lambda x, y: x % y if y != 0 else None
    }
    
    print("=== Lambda Arithmetic Operations ===")
    for op_name, op_func in operations.items():
        result = op_func(10, 3)
        print(f"{op_name}(10, 3) = {result}")
    
    # String operations
    string_ops = {
        'concat': lambda s1, s2: s1 + s2,
        'repeat': lambda s, n: s * n,
        'upper': lambda s: s.upper(),
        'reverse': lambda s: s[::-1],
        'first_char': lambda s: s[0] if s else '',
        'last_char': lambda s: s[-1] if s else ''
    }
    
    print("\n=== Lambda String Operations ===")
    test_string = "hello"
    for op_name, op_func in string_ops.items():
        if op_name in ['concat']:
            result = op_func(test_string, " world")
        elif op_name in ['repeat']:
            result = op_func(test_string, 2)
        else:
            result = op_func(test_string)
        print(f"{op_name}('{test_string}'): {result}")
    
    # List operations
    list_ops = {
        'sum_list': lambda lst: sum(lst),
        'max_list': lambda lst: max(lst) if lst else None,
        'min_list': lambda lst: min(lst) if lst else None,
        'length': lambda lst: len(lst),
        'reverse': lambda lst: lst[::-1],
        'sort': lambda lst: sorted(lst)
    }
    
    print("\n=== Lambda List Operations ===")
    test_list = [3, 1, 4, 1, 5, 9, 2, 6]
    for op_name, op_func in list_ops.items():
        result = op_func(test_list)
        print(f"{op_name}({test_list}): {result}")
    
    # Conditional operations
    conditional_ops = {
        'is_even': lambda x: x % 2 == 0,
        'is_positive': lambda x: x > 0,
        'is_in_range': lambda x, low, high: low <= x <= high,
        'max_of_three': lambda x, y, z: max(x, y, z),
        'clamp': lambda x, low, high: max(low, min(x, high))
    }
    
    print("\n=== Lambda Conditional Operations ===")
    for op_name, op_func in conditional_ops.items():
        if op_name in ['is_in_range']:
            result = op_func(5, 1, 10)
            print(f"{op_name}(5, 1, 10): {result}")
        elif op_name in ['max_of_three']:
            result = op_func(3, 7, 5)
            print(f"{op_name}(3, 7, 5): {result}")
        elif op_name in ['clamp']:
            result = op_func(15, 1, 10)
            print(f"{op_name}(15, 1, 10): {result}")
        else:
            result = op_func(6)
            print(f"{op_name}(6): {result}")

lambda_operations()
```

### 2.2 Filter Operations

```python
def filter_operations():
    """Demonstrate various filter operations"""
    
    # Numeric filtering
    numbers = list(range(1, 21))
    
    print("=== Numeric Filter Operations ===")
    print(f"Original numbers: {numbers}")
    
    # Basic filters
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 == 1, numbers))
    multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
    greater_than_10 = list(filter(lambda x: x > 10, numbers))
    
    print(f"Even numbers: {evens}")
    print(f"Odd numbers: {odds}")
    print(f"Multiples of 3: {multiples_of_3}")
    print(f"Greater than 10: {greater_than_10}")
    
    # Complex numeric filters
    def is_perfect_square(n):
        return int(n ** 0.5) ** 2 == n
    
    perfect_squares = list(filter(is_perfect_square, numbers))
    prime_numbers = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)), numbers))
    
    print(f"Perfect squares: {perfect_squares}")
    print(f"Prime numbers: {prime_numbers}")
    
    # String filtering
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
    
    print("\n=== String Filter Operations ===")
    print(f"Original words: {words}")
    
    short_words = list(filter(lambda word: len(word) <= 5, words))
    words_with_e = list(filter(lambda word: 'e' in word, words))
    words_starting_vowel = list(filter(lambda word: word[0].lower() in 'aeiou', words))
    
    print(f"Short words (≤5 chars): {short_words}")
    print(f"Words with 'e': {words_with_e}")
    print(f"Starting with vowel: {words_starting_vowel}")
    
    # Object filtering
    class Student:
        def __init__(self, name, age, grade):
            self.name = name
            self.age = age
            self.grade = grade
        
        def __repr__(self):
            return f"Student('{self.name}', {self.age}, {self.grade})"
    
    students = [
        Student('Alice', 20, 85),
        Student('Bob', 19, 92),
        Student('Charlie', 21, 78),
        Student('Diana', 18, 95),
        Student('Eve', 22, 67)
    ]
    
    print("\n=== Object Filter Operations ===")
    print(f"All students: {students}")
    
    high_achievers = list(filter(lambda s: s.grade >= 90, students))
    young_students = list(filter(lambda s: s.age < 20, students))
    names_with_a = list(filter(lambda s: 'a' in s.name.lower(), students))
    
    print(f"High achievers (≥90): {high_achievers}")
    print(f"Young students (<20): {young_students}")
    print(f"Names with 'a': {names_with_a}")
    
    # Advanced filtering with multiple conditions
    excellent_young = list(filter(lambda s: s.grade >= 90 and s.age < 21, students))
    print(f"Excellent young students: {excellent_young}")

filter_operations()
```

### 2.3 Map Operations

```python
def map_operations():
    """Demonstrate various map operations"""
    
    # Basic transformations
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("=== Basic Map Operations ===")
    print(f"Original numbers: {numbers}")
    
    squares = list(map(lambda x: x ** 2, numbers))
    cubes = list(map(lambda x: x ** 3, numbers))
    doubled = list(map(lambda x: x * 2, numbers))
    reciprocals = list(map(lambda x: 1/x, numbers))
    
    print(f"Squares: {squares}")
    print(f"Cubes: {cubes}")
    print(f"Doubled: {doubled}")
    print(f"Reciprocals: {reciprocals[:5]}...")  # Show first 5
    
    # String transformations
    words = ['hello', 'world', 'python', 'programming']
    
    print("\n=== String Map Operations ===")
    print(f"Original words: {words}")
    
    uppercase = list(map(str.upper, words))
    capitalized = list(map(str.capitalize, words))
    lengths = list(map(len, words))
    reversed_words = list(map(lambda s: s[::-1], words))
    
    print(f"Uppercase: {uppercase}")
    print(f"Capitalized: {capitalized}")
    print(f"Lengths: {lengths}")
    print(f"Reversed: {reversed_words}")
    
    # Multiple iterables
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50]
    list3 = [100, 200, 300, 400, 500]
    
    print("\n=== Multiple Iterable Map Operations ===")
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"List 3: {list3}")
    
    sums = list(map(lambda x, y: x + y, list1, list2))
    products = list(map(lambda x, y, z: x * y * z, list1, list2, list3))
    averages = list(map(lambda x, y, z: (x + y + z) / 3, list1, list2, list3))
    
    print(f"Element-wise sums: {sums}")
    print(f"Triple products: {products}")
    print(f"Averages: {averages}")
    
    # Complex object transformations
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person('{self.name}', {self.age})"
    
    people = [
        Person('Alice', 25),
        Person('Bob', 30),
        Person('Charlie', 35),
        Person('Diana', 28)
    ]
    
    print("\n=== Object Map Operations ===")
    print(f"People: {people}")
    
    names = list(map(lambda p: p.name, people))
    ages = list(map(lambda p: p.age, people))
    descriptions = list(map(lambda p: f"{p.name} is {p.age} years old", people))
    age_categories = list(map(lambda p: "Young" if p.age < 30 else "Mature", people))
    
    print(f"Names: {names}")
    print(f"Ages: {ages}")
    print(f"Descriptions: {descriptions}")
    print(f"Age categories: {age_categories}")
    
    # Data structure transformations
    data = [
        {'name': 'Alice', 'score': 85, 'subject': 'Math'},
        {'name': 'Bob', 'score': 92, 'subject': 'Science'},
        {'name': 'Charlie', 'score': 78, 'subject': 'English'}
    ]
    
    print("\n=== Data Structure Map Operations ===")
    print(f"Original data: {data}")
    
    student_names = list(map(lambda d: d['name'], data))
    letter_grades = list(map(lambda d: 'A' if d['score'] >= 90 else 'B' if d['score'] >= 80 else 'C', data))
    formatted_results = list(map(lambda d: f"{d['name']}: {d['score']} in {d['subject']}", data))
    
    print(f"Student names: {student_names}")
    print(f"Letter grades: {letter_grades}")
    print(f"Formatted results: {formatted_results}")

map_operations()
```

---

## 3. Methods and Advanced Techniques

### 3.1 Advanced Lambda Methods

```python
def advanced_lambda_methods():
    """Demonstrate advanced lambda methods and techniques"""
    
    # Higher-order functions with lambdas
    def create_multiplier(n):
        return lambda x: x * n
    
    def create_validator(condition):
        return lambda x: condition(x)
    
    def create_transformer(transform_func):
        return lambda data: [transform_func(item) for item in data]
    
    print("=== Higher-Order Lambda Functions ===")
    
    # Create specialized functions
    double = create_multiplier(2)
    triple = create_multiplier(3)
    is_positive = create_validator(lambda x: x > 0)
    is_even = create_validator(lambda x: x % 2 == 0)
    square_all = create_transformer(lambda x: x ** 2)
    
    print(f"Double 5: {double(5)}")
    print(f"Triple 4: {triple(4)}")
    print(f"Is 7 positive: {is_positive(7)}")
    print(f"Is 8 even: {is_even(8)}")
    print(f"Square all [1,2,3,4]: {square_all([1, 2, 3, 4])}")
    
    # Lambda with closures
    def create_counter():
        count = 0
        return lambda: globals().update(count=globals().get('count', 0) + 1) or globals()['count']
    
    # Partial application with lambdas
    def partial_apply(func, *args):
        return lambda *remaining_args: func(*(args + remaining_args))
    
    add_three = lambda x, y, z: x + y + z
    add_10_and = partial_apply(add_three, 10)
    
    print(f"Add 10 + 5 + 3: {add_10_and(5, 3)}")
    
    # Lambda composition
    def compose(*functions):
        return lambda x: x if not functions else functions[0](compose(*functions[1:])(x))
    
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    composed_func = compose(square, multiply_by_two, add_one)
    print(f"Compose (square ∘ *2 ∘ +1)(3): {composed_func(3)}")  # ((3+1)*2)^2 = 64
    
    # Lambda with error handling
    safe_divide = lambda x, y: x / y if y != 0 else float('inf')
    safe_sqrt = lambda x: x ** 0.5 if x >= 0 else complex(0, (-x) ** 0.5)
    
    print(f"Safe divide 10/0: {safe_divide(10, 0)}")
    print(f"Safe sqrt of -4: {safe_sqrt(-4)}")

advanced_lambda_methods()
```

### 3.2 Functional Programming Patterns

```python
from functools import reduce, partial
from operator import add, mul, and_, or_

def functional_programming_patterns():
    """Demonstrate functional programming patterns"""
    
    # Currying
    def curry(func):
        def curried(*args, **kwargs):
            if len(args) + len(kwargs) >= func.__code__.co_argcount:
                return func(*args, **kwargs)
            return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
        return curried
    
    @curry
    def add_three_numbers(x, y, z):
        return x + y + z
    
    print("=== Currying Pattern ===")
    add_5 = add_three_numbers(5)
    add_5_and_3 = add_5(3)
    result = add_5_and_3(2)
    print(f"Curried addition 5+3+2: {result}")
    
    # Map-Reduce patterns
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("\n=== Map-Reduce Patterns ===")
    
    # Sum of squares
    sum_of_squares = reduce(add, map(lambda x: x ** 2, numbers))
    print(f"Sum of squares: {sum_of_squares}")
    
    # Product of evens
    evens = filter(lambda x: x % 2 == 0, numbers)
    product_of_evens = reduce(mul, evens, 1)
    print(f"Product of evens: {product_of_evens}")
    
    # All/any patterns
    all_positive = reduce(and_, map(lambda x: x > 0, numbers))
    any_greater_than_5 = reduce(or_, map(lambda x: x > 5, numbers))
    print(f"All positive: {all_positive}")
    print(f"Any greater than 5: {any_greater_than_5}")
    
    # Pipeline pattern
    def pipeline(*functions):
        return lambda x: reduce(lambda acc, func: func(acc), functions, x)
    
    process_text = pipeline(
        str.lower,
        lambda s: s.replace(' ', '_'),
        lambda s: s + '_processed'
    )
    
    result = process_text("Hello World")
    print(f"Pipeline result: {result}")
    
    # Monadic patterns (simplified)
    class Maybe:
        def __init__(self, value):
            self._value = value
        
        def bind(self, func):
            return Maybe(func(self._value)) if self._value is not None else Maybe(None)
        
        def value(self):
            return self._value
        
        @staticmethod
        def of(value):
            return Maybe(value)
    
    print("\n=== Maybe Monad Pattern ===")
    result = (Maybe.of(10)
              .bind(lambda x: x * 2)
              .bind(lambda x: x + 5)
              .bind(lambda x: x / 5)
              .value())
    print(f"Maybe monad result: {result}")
    
    # Null handling
    null_result = (Maybe.of(None)
                   .bind(lambda x: x * 2)
                   .bind(lambda x: x + 5)
                   .value())
    print(f"Maybe monad with None: {null_result}")

functional_programming_patterns()
```

### 3.3 Generator and Iterator Methods

```python
def generator_iterator_methods():
    """Demonstrate advanced generator and iterator methods"""
    
    # Generator expressions
    squares_gen = (x**2 for x in range(10))
    evens_gen = (x for x in range(20) if x % 2 == 0)
    
    print("=== Generator Expressions ===")
    print(f"Squares: {list(squares_gen)}")
    print(f"Evens: {list(evens_gen)}")
    
    # Generator with send() method
    def accumulator():
        total = 0
        while True:
            value = yield total
            if value is not None:
                total += value
    
    print("\n=== Generator with send() ===")
    acc = accumulator()
    next(acc)  # Prime the generator
    print(f"Send 5: {acc.send(5)}")
    print(f"Send 10: {acc.send(10)}")
    print(f"Send 3: {acc.send(3)}")
    
    # Generator with throw() and close()
    def error_handling_generator():
        try:
            while True:
                value = yield
                if value < 0:
                    raise ValueError("Negative value not allowed")
                print(f"Received: {value}")
        except ValueError as e:
            print(f"Caught error: {e}")
            yield "Error handled"
        finally:
            print("Generator closed")
    
    print("\n=== Generator Error Handling ===")
    gen = error_handling_generator()
    next(gen)
    gen.send(5)
    try:
        gen.throw(ValueError, "Manual error")
        next(gen)
    except StopIteration:
        pass
    gen.close()
    
    # Infinite generators with itertools
    import itertools
    
    print("\n=== Infinite Generators ===")
    
    # Fibonacci generator
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    fib_gen = fibonacci()
    first_10_fib = [next(fib_gen) for _ in range(10)]
    print(f"First 10 Fibonacci: {first_10_fib}")
    
    # Cycle through values
    colors = itertools.cycle(['red', 'green', 'blue'])
    color_sequence = [next(colors) for _ in range(8)]
    print(f"Color cycle: {color_sequence}")
    
    # Count with step
    counter = itertools.count(start=10, step=3)
    count_sequence = [next(counter) for _ in range(6)]
    print(f"Count sequence: {count_sequence}")
    
    # Chain generators
    gen1 = (x for x in range(3))
    gen2 = (x for x in range(3, 6))
    chained = itertools.chain(gen1, gen2)
    print(f"Chained generators: {list(chained)}")
    
    # Generator pipeline
    def numbers():
        for i in range(1, 11):
            yield i
    
    def squares(iterable):
        for x in iterable:
            yield x ** 2
    
    def evens_only(iterable):
        for x in iterable:
            if x % 2 == 0:
                yield x
    
    pipeline = evens_only(squares(numbers()))
    print(f"Pipeline result: {list(pipeline)}")

generator_iterator_methods()
```

---

## 4. Common Errors and Best Practices

### 4.1 Lambda Function Errors

```python
def lambda_common_errors():
    """Demonstrate common lambda function errors"""
    
    print("=== Lambda Common Errors ===")
    
    # Error 1: Multiple statements in lambda
    print("Error 1: Multiple statements (NOT ALLOWED)")
    print("# WRONG: lambda x: print(x); return x * 2")
    print("# CORRECT: Use regular function for multiple statements")
    
    def correct_multiple_statements(x):
        print(x)
        return x * 2
    
    result = correct_multiple_statements(5)
    print(f"Correct approach result: {result}")
    
    # Error 2: Lambda variable capture (late binding)
    print("\nError 2: Late binding closure")
    
    # Wrong way - all lambdas capture the same variable
    wrong_multipliers = []
    for i in range(3):
        wrong_multipliers.append(lambda x: x * i)
    
    print("Wrong multipliers (all use i=2):")
    for j, mult in enumerate(wrong_multipliers):
        print(f"  Multiplier {j}(5) = {mult(5)}")
    
    # Correct way - capture value at creation time
    correct_multipliers = []
    for i in range(3):
        correct_multipliers.append(lambda x, i=i: x * i)
    
    print("Correct multipliers:")
    for j, mult in enumerate(correct_multipliers):
        print(f"  Multiplier {j}(5) = {mult(5)}")
    
    # Error 3: Complex expressions that should be functions
    print("\nError 3: Overly complex lambdas")
    
    # Wrong - too complex for lambda
    complex_lambda = lambda x: x**2 + 2*x + 1 if x > 0 else -x**2 + 2*x - 1 if x < 0 else 0
    
    # Better - use regular function
    def complex_function(x):
        """Calculate complex expression based on x value"""
        if x > 0:
            return x**2 + 2*x + 1
        elif x < 0:
            return -x**2 + 2*x - 1
        else:
            return 0
    
    test_values = [-2, 0, 3]
    for val in test_values:
        lambda_result = complex_lambda(val)
        function_result = complex_function(val)
        print(f"  f({val}): lambda={lambda_result}, function={function_result}")
    
    # Error 4: Assignment in lambda (not allowed)
    print("\nError 4: Assignment in lambda")
    print("# WRONG: lambda x: (y := x * 2)  # Walrus operator works in Python 3.8+")
    print("# WRONG: lambda x: x = x * 2     # Direct assignment not allowed")
    print("# CORRECT: Use regular function for assignments")
    
    # Error 5: Debugging difficulties
    print("\nError 5: Debugging difficulties")
    
    # Hard to debug lambda
    data = [1, 2, 3, 4, 5]
    try:
        result = list(map(lambda x: x / (x - 3), data))  # Will cause error
    except ZeroDivisionError as e:
        print(f"Lambda error (hard to debug): {e}")
    
    # Easier to debug function
    def safe_divide_by_diff(x):
        """Divide x by (x-3) with error handling"""
        if x == 3:
            return float('inf')  # or handle as needed
        return x / (x - 3)
    
    result = list(map(safe_divide_by_diff, data))
    print(f"Safe function result: {result}")

lambda_common_errors()
```

### 4.2 Filter and Map Errors

```python
def filter_map_common_errors():
    """Demonstrate common filter and map errors"""
    
    print("=== Filter and Map Common Errors ===")
    
    # Error 1: Forgetting that filter/map return iterators
    print("Error 1: Iterator vs List confusion")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Wrong - treating iterator as list
    evens_iter = filter(lambda x: x % 2 == 0, numbers)
    print(f"Filter iterator: {evens_iter}")
    print(f"First iteration: {list(evens_iter)}")
    print(f"Second iteration (empty): {list(evens_iter)}")  # Empty!
    
    # Correct - convert to list if needed multiple times
    evens_list = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Filter list: {evens_list}")
    print(f"Can use multiple times: {evens_list}")
    
    # Error 2: Wrong function signature for filter
    print("\nError 2: Wrong filter function signature")
    
    try:
        # Wrong - filter function should return bool, not transformed value
        wrong_filter = list(filter(lambda x: x * 2, numbers))
        print(f"Wrong filter (returns values): {wrong_filter}")
    except:
        print("Filter with non-boolean function can be confusing")
    
    # Correct - filter returns boolean
    correct_filter = list(filter(lambda x: x > 2, numbers))
    print(f"Correct filter (returns bool): {correct_filter}")
    
    # Error 3: Map with different length iterables
    print("\nError 3: Map with different length iterables")
    
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20]  # Shorter list
    
    # Map stops at shortest iterable
    result = list(map(lambda x, y: x + y, list1, list2))
    print(f"Map with different lengths: {result}")  # Only 2 elements
    print("Note: Remaining elements of longer list are ignored")
    
    # Error 4: Modifying original data during iteration
    print("\nError 4: Modifying data during iteration")
    
    data = [1, 2, 3, 4, 5]
    original_data = data.copy()
    
    # Dangerous - modifying list during iteration
    try:
        result = []
        for item in data:
            if item % 2 == 0:
                data.remove(item)  # Modifying during iteration
            result.append(item)
        print(f"Modified during iteration: {result}")
        print(f"Original data changed: {data}")
    except:
        print("Error occurred during modification")
    
    # Correct - use filter/map without modifying original
    data = original_data.copy()
    filtered_data = list(filter(lambda x: x % 2 != 0, data))
    print(f"Correct filtering: {filtered_data}")
    print(f"Original data unchanged: {data}")
    
    # Error 5: Performance issues with large datasets
    print("\nError 5: Performance considerations")
    
    # Inefficient - multiple passes through data
    large_numbers = list(range(1000000))
    
    # Wrong approach - multiple iterations
    import time
    start_time = time.time()
    evens = list(filter(lambda x: x % 2 == 0, large_numbers))
    squares = list(map(lambda x: x ** 2, evens))
    large_squares = list(filter(lambda x: x > 1000, squares))
    end_time = time.time()
    
    print(f"Multiple passes time: {end_time - start_time:.4f}s")
    print(f"Result length: {len(large_squares)}")
    
    # Better approach - generator pipeline
    start_time = time.time()
    result = [x ** 2 for x in large_numbers if x % 2 == 0 and x ** 2 > 1000]
    end_time = time.time()
    
    print(f"Single pass time: {end_time - start_time:.4f}s")
    print(f"Result length: {len(result)}")

filter_map_common_errors()
```

### 4.3 Generator and Iterator Errors

```python
def generator_iterator_errors():
    """Demonstrate common generator and iterator errors"""
    
    print("=== Generator and Iterator Common Errors ===")
    
    # Error 1: Generator exhaustion
    print("Error 1: Generator exhaustion")
    
    def simple_generator():
        yield 1
        yield 2
        yield 3
    
    gen = simple_generator()
    print(f"First consumption: {list(gen)}")
    print(f"Second consumption (empty): {list(gen)}")  # Empty!
    
    # Solution: Create new generator or use itertools.tee
    import itertools
    
    gen1, gen2 = itertools.tee(simple_generator(), 2)
    print(f"Tee generator 1: {list(gen1)}")
    print(f"Tee generator 2: {list(gen2)}")
    
    # Error 2: Forgetting to handle StopIteration
    print("\nError 2: StopIteration handling")
    
    gen = simple_generator()
    try:
        print(f"Value 1: {next(gen)}")
        print(f"Value 2: {next(gen)}")
        print(f"Value 3: {next(gen)}")
        print(f"Value 4: {next(gen)}")  # Will raise StopIteration
    except StopIteration:
        print("Generator exhausted - StopIteration caught")
    
    # Better - use default value
    gen = simple_generator()
    for i in range(5):
        value = next(gen, "No more values")
        print(f"Value {i+1}: {value}")
    
    # Error 3: Incorrect yield usage
    print("\nError 3: Incorrect yield usage")
    
    # Wrong - yield in wrong context
    def wrong_generator():
        values = []
        for i in range(3):
            values.append(yield i)  # Problematic yield usage
        return values  # This won't work as expected
    
    # Correct - proper yield usage
    def correct_generator():
        for i in range(3):
            received = yield i
            if received is not None:
                print(f"Received: {received}")
    
    print("Testing correct generator:")
    gen = correct_generator()
    print(f"First next: {next(gen)}")
    print(f"Send value: {gen.send('hello')}")
    print(f"Next value: {next(gen)}")
    
    # Error 4: Memory issues with large generators
    print("\nError 4: Memory considerations")
    
    # Wrong - creating large list in memory
    def memory_intensive():
        return [x**2 for x in range(1000000)]  # Large list in memory
    
    # Correct - generator for large datasets
    def memory_efficient():
        for x in range(1000000):
            yield x**2
    
    print("Memory efficient generator created (no memory allocated yet)")
    
    # Error 5: Mixing generators with functions expecting lists
    print("\nError 5: Generator/List compatibility")
    
    def process_data(data):
        """Function that expects a list-like object"""
        print(f"Data length: {len(data)}")  # Will fail with generator
        return sum(data)
    
    # Wrong - passing generator to function expecting list
    gen_data = (x for x in range(5))
    try:
        result = process_data(gen_data)
    except TypeError as e:
        print(f"Error with generator: {e}")
    
    # Correct - convert to list when needed
    list_data = list(x for x in range(5))
    result = process_data(list_data)
    print(f"Correct result: {result}")
    
    # Error 6: Infinite generator without proper control
    print("\nError 6: Infinite generator control")
    
    def infinite_numbers():
        n = 0
        while True:
            yield n
            n += 1
    
    # Wrong - no termination condition
    # for num in infinite_numbers():  # This would run forever!
    #     print(num)
    
    # Correct - proper termination
    infinite_gen = infinite_numbers()
    for _ in range(5):  # Limit iterations
        print(f"Infinite gen: {next(infinite_gen)}")
    
    # Or use takewhile from itertools
    from itertools import takewhile
    limited_gen = takewhile(lambda x: x < 5, infinite_numbers())
    print(f"Limited infinite gen: {list(limited_gen)}")

generator_iterator_errors()
```

### 4.4 Module and Package Errors

```python
def module_package_errors():
    """Demonstrate common module and package errors"""
    
    print("=== Module and Package Common Errors ===")
    
    # Error 1: Circular imports
    print("Error 1: Circular imports")
    print("""
    # module_a.py
    from module_b import function_b
    
    def function_a():
        return function_b()
    
    # module_b.py  
    from module_a import function_a  # Circular import!
    
    def function_b():
        return function_a()
    
    Solution: Restructure code or use local imports
    """)
    
    # Error 2: Import path issues
    print("\nError 2: Import path issues")
    
    import sys
    print(f"Python path: {sys.path[:3]}...")  # Show first 3 paths
    
    # Common issues:
    print("""
    Common import issues:
    1. Module not in PYTHONPATH
    2. Incorrect relative imports
    3. Missing __init__.py files
    4. Name conflicts with standard library
    """)
    
    # Error 3: Namespace pollution
    print("\nError 3: Namespace pollution")
    
    # Wrong - imports everything
    # from math import *  # Pollutes namespace
    
    # Better - specific imports
    from math import pi, sqrt, sin
    print(f"Specific imports: pi={pi:.3f}, sqrt(4)={sqrt(4)}")
    
    # Or use qualified imports
    import math
    print(f"Qualified import: math.cos(0)={math.cos(0)}")
    
    # Error 4: Module reloading issues
    print("\nError 4: Module reloading")
    
    print("""
    In interactive sessions, modules are cached:
    
    import my_module
    # Modify my_module.py
    import my_module  # Won't reload changes!
    
    Solutions:
    1. Restart Python interpreter
    2. Use importlib.reload() (Python 3.4+)
    3. Use IPython %autoreload magic
    """)
    
    # Error 5: Package structure issues
    print("\nError 5: Package structure")
    
    print("""
    Wrong package structure:
    mypackage/
        module1.py      # Missing __init__.py
        subpackage/
            module2.py  # Missing __init__.py
    
    Correct structure:
    mypackage/
        __init__.py     # Makes it a package
        module1.py
        subpackage/
            __init__.py # Makes it a sub-package
            module2.py
    """)
    
    # Error 6: Version compatibility
    print("\nError 6: Version compatibility")
    
    print("""
    Common version issues:
    1. Using Python 2 syntax in Python 3
    2. Using newer features in older Python versions
    3. Third-party package version conflicts
    
    Solutions:
    1. Use __future__ imports for compatibility
    2. Check Python version: sys.version_info
    3. Use virtual environments
    4. Pin package versions in requirements.txt
    """)
    
    # Check Python version
    print(f"Current Python version: {sys.version_info}")
    
    # Example of version checking
    if sys.version_info >= (3, 8):
        print("Python 3.8+ features available (walrus operator, etc.)")
    else:
        print("Using older Python version - some features unavailable")

module_package_errors()
```

### 4.5 Best Practices Summary

```python
def best_practices_summary():
    """Summary of best practices for all concepts"""
    
    print("=== BEST PRACTICES SUMMARY ===")
    
    print("""
    LAMBDA FUNCTIONS:
    ✓ Use for simple, single-expression functions
    ✓ Prefer regular functions for complex logic
    ✓ Be careful with variable capture in closures
    ✓ Don't use for functions that need debugging
    ✓ Consider readability over brevity
    
    FILTER AND MAP:
    ✓ Remember they return iterators, not lists
    ✓ Convert to list if multiple iterations needed
    ✓ Use generator expressions for better performance
    ✓ Consider list comprehensions for readability
    ✓ Handle different-length iterables carefully
    
    GENERATORS:
    ✓ Use for large datasets or infinite sequences
    ✓ Remember generators are consumed once
    ✓ Handle StopIteration exceptions properly
    ✓ Use yield for memory-efficient iteration
    ✓ Consider itertools for advanced patterns
    
    ITERATORS:
    ✓ Implement __iter__ and __next__ methods
    ✓ Raise StopIteration when exhausted
    ✓ Make iterators reusable when possible
    ✓ Use built-in functions like iter() and next()
    ✓ Handle edge cases gracefully
    
    DECORATORS:
    ✓ Use functools.wraps to preserve metadata
    ✓ Handle *args and **kwargs properly
    ✓ Consider performance impact
    ✓ Make decorators reusable and composable
    ✓ Document decorator behavior clearly
    
    MODULES AND PACKAGES:
    ✓ Avoid circular imports
    ✓ Use clear, descriptive names
    ✓ Include __init__.py in packages
    ✓ Handle import errors gracefully
    ✓ Use virtual environments for dependencies
    ✓ Document module interfaces
    
    GENERAL FUNCTIONAL PROGRAMMING:
    ✓ Prefer immutable data structures
    ✓ Use pure functions when possible
    ✓ Compose functions for complex operations
    ✓ Handle errors explicitly
    ✓ Consider performance implications
    ✓ Write tests for functional code
    """)
    
    # Practical example combining best practices
    print("\n=== PRACTICAL EXAMPLE ===")
    
    from functools import wraps
    from typing import List, Callable, Any
    
    def safe_operation(default_value=None):
        """Decorator for safe operations with error handling"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error in {func.__name__}: {e}")
                    return default_value
            return wrapper
        return decorator
    
    @safe_operation(default_value=[])
    def process_numbers(numbers: List[int]) -> List[int]:
        """Process numbers with functional operations"""
        # Chain operations using generator expressions
        evens = (x for x in numbers if x % 2 == 0)
        squares = (x ** 2 for x in evens)
        filtered = [x for x in squares if x < 100]
        return filtered
    
    # Test the example
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = process_numbers(test_data)
    print(f"Processed result: {result}")
    
    # Test error handling
    result_error = process_numbers("invalid")  # Will use default value
    print(f"Error case result: {result_error}")

best_practices_summary()
```

