#!/usr/bin/env python3
"""
Python Advanced Functions Program

This program demonstrates all concepts from Advanced_Functions_Documentation.md including:
- Lambda functions, filter, map, reduce
- Decorators and generators
- Modules, packages, and iterators
- Common errors and best practices

Author: Generated from Advanced_Functions_Documentation.md
"""

import sys
import time
import itertools
from functools import reduce, wraps, lru_cache, partial
from typing import List, Callable, Any, Iterator, Generator


def main():
    """Main function to run all demonstrations"""
    print("=" * 80)
    print("PYTHON ADVANCED FUNCTIONS DEMONSTRATION")
    print("=" * 80)
    
    # Section 1: Definitions and Characteristics
    print("\n1. DEFINITIONS AND CHARACTERISTICS")
    print("-" * 60)
    demonstrate_lambda_basics()
    demonstrate_filter_basics()
    demonstrate_map_basics()
    demonstrate_reduce_basics()
    demonstrate_decorator_basics()
    demonstrate_generator_basics()
    demonstrate_iterator_basics()
    
    # Section 2: Operations
    print("\n2. OPERATIONS")
    print("-" * 60)
    demonstrate_lambda_operations()
    demonstrate_filter_operations()
    demonstrate_map_operations()
    demonstrate_functional_operations()
    
    # Section 3: Advanced Methods
    print("\n3. ADVANCED METHODS")
    print("-" * 60)
    demonstrate_advanced_techniques()
    demonstrate_functional_patterns()
    demonstrate_performance_optimization()
    
    # Section 4: Common Errors and Best Practices
    print("\n4. COMMON ERRORS AND BEST PRACTICES")
    print("-" * 60)
    demonstrate_common_errors()
    demonstrate_best_practices()
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)


# Section 1: Definitions and Characteristics

def demonstrate_lambda_basics():
    """Demonstrate basic lambda function concepts"""
    print("\n1.1 Lambda Functions")
    
    # Basic lambda examples
    square = lambda x: x ** 2
    add = lambda x, y: x + y
    max_val = lambda x, y: x if x > y else y
    
    print(f"  Square of 5: {square(5)}")
    print(f"  Add 3 + 4: {add(3, 4)}")
    print(f"  Max of 10, 7: {max_val(10, 7)}")
    
    # Lambda with closures
    def create_multiplier(n):
        return lambda x: x * n
    
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"  Double 4: {double(4)}")
    print(f"  Triple 4: {triple(4)}")
    
    # Lambda vs regular function
    def regular_cube(x):
        return x ** 3
    
    lambda_cube = lambda x: x ** 3
    
    print(f"  Regular cube(3): {regular_cube(3)}")
    print(f"  Lambda cube(3): {lambda_cube(3)}")
    print(f"  Function name: {regular_cube.__name__}")
    print(f"  Lambda name: {lambda_cube.__name__}")


def demonstrate_filter_basics():
    """Demonstrate basic filter function concepts"""
    print("\n1.2 Filter Function")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Basic filtering
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 == 1, numbers))
    greater_than_5 = list(filter(lambda x: x > 5, numbers))
    
    print(f"  Original: {numbers}")
    print(f"  Even numbers: {evens}")
    print(f"  Odd numbers: {odds}")
    print(f"  Greater than 5: {greater_than_5}")
    
    # Filter with None (removes falsy values)
    mixed_values = [0, 1, False, True, '', 'hello', [], [1, 2], None]
    truthy_values = list(filter(None, mixed_values))
    print(f"  Mixed values: {mixed_values}")
    print(f"  Truthy values: {truthy_values}")
    
    # Filter strings
    words = ['apple', 'banana', 'cherry', 'date']
    long_words = list(filter(lambda word: len(word) > 5, words))
    print(f"  Words: {words}")
    print(f"  Long words (>5 chars): {long_words}")


def demonstrate_map_basics():
    """Demonstrate basic map function concepts"""
    print("\n1.3 Map Function")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Basic mapping
    squares = list(map(lambda x: x ** 2, numbers))
    doubled = list(map(lambda x: x * 2, numbers))
    
    print(f"  Original: {numbers}")
    print(f"  Squares: {squares}")
    print(f"  Doubled: {doubled}")
    
    # Map with multiple iterables
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    sums = list(map(lambda x, y: x + y, list1, list2))
    
    print(f"  List 1: {list1}")
    print(f"  List 2: {list2}")
    print(f"  Element-wise sum: {sums}")
    
    # Map with built-in functions
    str_numbers = ['1', '2', '3', '4', '5']
    integers = list(map(int, str_numbers))
    
    print(f"  String numbers: {str_numbers}")
    print(f"  Converted to int: {integers}")
    
    # Map with strings
    words = ['hello', 'world', 'python']
    uppercase = list(map(str.upper, words))
    lengths = list(map(len, words))
    
    print(f"  Words: {words}")
    print(f"  Uppercase: {uppercase}")
    print(f"  Lengths: {lengths}")


def demonstrate_reduce_basics():
    """Demonstrate basic reduce function concepts"""
    print("\n1.4 Reduce Function")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Basic reductions
    total = reduce(lambda x, y: x + y, numbers)
    product = reduce(lambda x, y: x * y, numbers)
    maximum = reduce(lambda x, y: x if x > y else y, numbers)
    
    print(f"  Numbers: {numbers}")
    print(f"  Sum: {total}")
    print(f"  Product: {product}")
    print(f"  Maximum: {maximum}")
    
    # Reduce with initial value
    total_with_initial = reduce(lambda x, y: x + y, numbers, 100)
    print(f"  Sum with initial 100: {total_with_initial}")
    
    # String concatenation
    words = ['Python', 'is', 'awesome']
    sentence = reduce(lambda x, y: x + ' ' + y, words)
    print(f"  Words: {words}")
    print(f"  Sentence: {sentence}")
    
    # Flattening lists
    nested_lists = [[1, 2], [3, 4], [5, 6]]
    flattened = reduce(lambda x, y: x + y, nested_lists)
    print(f"  Nested: {nested_lists}")
    print(f"  Flattened: {flattened}")


def demonstrate_decorator_basics():
    """Demonstrate basic decorator concepts"""
    print("\n1.5 Decorators")
    
    # Simple decorator
    def simple_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"    Before calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"    After calling {func.__name__}")
            return result
        return wrapper
    
    # Timing decorator
    def timing_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"    {func.__name__} took {end_time - start_time:.6f} seconds")
            return result
        return wrapper
    
    # Apply decorators
    @simple_decorator
    def greet(name):
        return f"Hello, {name}!"
    
    @timing_decorator
    def slow_function():
        time.sleep(0.01)  # Simulate work
        return "Done"
    
    print("  Testing simple decorator:")
    result = greet("Alice")
    print(f"    Result: {result}")
    
    print("  Testing timing decorator:")
    slow_function()
    
    # Parameterized decorator
    def repeat(times):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for _ in range(times):
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator
    
    @repeat(3)
    def get_number():
        return 42
    
    print("  Testing parameterized decorator:")
    results = get_number()
    print(f"    Results: {results}")


def demonstrate_generator_basics():
    """Demonstrate basic generator concepts"""
    print("\n1.6 Generators")
    
    # Simple generator
    def simple_generator():
        yield 1
        yield 2
        yield 3
    
    print("  Simple generator:")
    for value in simple_generator():
        print(f"    Generated: {value}")
    
    # Generator with loop
    def count_up_to(n):
        count = 1
        while count <= n:
            yield count
            count += 1
    
    print("  Count up to 5:")
    for num in count_up_to(5):
        print(f"    Count: {num}")
    
    # Fibonacci generator
    def fibonacci_generator(limit=10):
        a, b = 0, 1
        count = 0
        while count < limit:
            yield a
            a, b = b, a + b
            count += 1
    
    print("  Fibonacci sequence (first 8):")
    fib_numbers = list(fibonacci_generator(8))
    print(f"    {fib_numbers}")
    
    # Generator expression
    squares_gen = (x**2 for x in range(1, 6))
    print("  Generator expression (squares):")
    print(f"    {list(squares_gen)}")
    
    # Generator with send()
    def echo_generator():
        while True:
            received = yield
            if received is not None:
                yield f"Echo: {received}"
    
    print("  Generator with send():")
    gen = echo_generator()
    next(gen)  # Prime the generator
    print(f"    {gen.send('Hello')}")
    print(f"    {next(gen)}")


def demonstrate_iterator_basics():
    """Demonstrate basic iterator concepts"""
    print("\n1.7 Iterators")
    
    # Custom iterator class
    class CountDown:
        def __init__(self, start):
            self.start = start
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.start <= 0:
                raise StopIteration
            self.start -= 1
            return self.start + 1
    
    print("  Custom CountDown iterator:")
    countdown = CountDown(5)
    for num in countdown:
        print(f"    Countdown: {num}")
    
    # Range-like iterator
    class Range:
        def __init__(self, start, stop, step=1):
            self.start = start
            self.stop = stop
            self.step = step
            self.current = start
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if (self.step > 0 and self.current >= self.stop) or \
               (self.step < 0 and self.current <= self.stop):
                raise StopIteration
            result = self.current
            self.current += self.step
            return result
    
    print("  Custom Range iterator (0 to 10, step 2):")
    custom_range = Range(0, 10, 2)
    range_values = list(custom_range)
    print(f"    {range_values}")
    
    # Built-in iterators
    print("  Built-in iterators:")
    text = "Hello"
    text_iter = iter(text)
    print(f"    String iteration: {list(text_iter)}")
    
    numbers = [1, 2, 3, 4, 5]
    num_iter = iter(numbers)
    print(f"    First element: {next(num_iter)}")
    print(f"    Remaining: {list(num_iter)}")


# Section 2: Operations

def demonstrate_lambda_operations():
    """Demonstrate various lambda operations"""
    print("\n2.1 Lambda Operations")
    
    # Arithmetic operations
    operations = {
        'add': lambda x, y: x + y,
        'multiply': lambda x, y: x * y,
        'power': lambda x, y: x ** y,
        'max': lambda x, y: x if x > y else y
    }
    
    print("  Arithmetic operations:")
    for op_name, op_func in operations.items():
        result = op_func(5, 3)
        print(f"    {op_name}(5, 3) = {result}")
    
    # String operations
    string_ops = {
        'concat': lambda s1, s2: s1 + s2,
        'repeat': lambda s, n: s * n,
        'reverse': lambda s: s[::-1]
    }
    
    print("  String operations:")
    for op_name, op_func in string_ops.items():
        if op_name == 'concat':
            result = op_func("Hello", " World")
        elif op_name == 'repeat':
            result = op_func("Hi", 3)
        else:
            result = op_func("Hello")
        print(f"    {op_name}: {result}")
    
    # Conditional operations
    is_even = lambda x: x % 2 == 0
    clamp = lambda x, low, high: max(low, min(x, high))
    
    print("  Conditional operations:")
    print(f"    is_even(6): {is_even(6)}")
    print(f"    is_even(7): {is_even(7)}")
    print(f"    clamp(15, 1, 10): {clamp(15, 1, 10)}")


def demonstrate_filter_operations():
    """Demonstrate various filter operations"""
    print("\n2.2 Filter Operations")
    
    numbers = list(range(1, 21))
    
    # Numeric filtering
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
    greater_than_10 = list(filter(lambda x: x > 10, numbers))
    
    print("  Numeric filtering:")
    print(f"    Numbers: {numbers}")
    print(f"    Evens: {evens}")
    print(f"    Multiples of 3: {multiples_of_3}")
    print(f"    Greater than 10: {greater_than_10}")
    
    # String filtering
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    short_words = list(filter(lambda word: len(word) <= 5, words))
    words_with_e = list(filter(lambda word: 'e' in word, words))
    
    print("  String filtering:")
    print(f"    Words: {words}")
    print(f"    Short words (≤5): {short_words}")
    print(f"    Words with 'e': {words_with_e}")
    
    # Complex filtering
    def is_prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    
    primes = list(filter(is_prime, numbers))
    print(f"    Prime numbers: {primes}")


def demonstrate_map_operations():
    """Demonstrate various map operations"""
    print("\n2.3 Map Operations")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Basic transformations
    squares = list(map(lambda x: x ** 2, numbers))
    cubes = list(map(lambda x: x ** 3, numbers))
    
    print("  Basic transformations:")
    print(f"    Numbers: {numbers}")
    print(f"    Squares: {squares}")
    print(f"    Cubes: {cubes}")
    
    # String transformations
    words = ['hello', 'world', 'python']
    uppercase = list(map(str.upper, words))
    lengths = list(map(len, words))
    reversed_words = list(map(lambda s: s[::-1], words))
    
    print("  String transformations:")
    print(f"    Words: {words}")
    print(f"    Uppercase: {uppercase}")
    print(f"    Lengths: {lengths}")
    print(f"    Reversed: {reversed_words}")
    
    # Multiple iterables
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    sums = list(map(lambda x, y: x + y, list1, list2))
    products = list(map(lambda x, y: x * y, list1, list2))
    
    print("  Multiple iterables:")
    print(f"    List 1: {list1}")
    print(f"    List 2: {list2}")
    print(f"    Sums: {sums}")
    print(f"    Products: {products}")


def demonstrate_functional_operations():
    """Demonstrate functional programming operations"""
    print("\n2.4 Functional Programming Operations")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Chaining operations
    # Get sum of squares of even numbers
    evens = filter(lambda x: x % 2 == 0, numbers)
    squares = map(lambda x: x ** 2, evens)
    sum_of_squares = reduce(lambda x, y: x + y, squares)
    
    print("  Chained operations (sum of squares of evens):")
    print(f"    Numbers: {numbers}")
    print(f"    Result: {sum_of_squares}")
    
    # One-liner equivalent
    result = reduce(lambda x, y: x + y, 
                   map(lambda x: x ** 2, 
                       filter(lambda x: x % 2 == 0, numbers)))
    print(f"    One-liner result: {result}")
    
    # List comprehension equivalent
    result_comp = sum(x**2 for x in numbers if x % 2 == 0)
    print(f"    List comprehension: {result_comp}")
    
    # Complex data processing
    students = [
        {'name': 'Alice', 'scores': [85, 92, 78]},
        {'name': 'Bob', 'scores': [92, 88, 94]},
        {'name': 'Charlie', 'scores': [78, 85, 82]}
    ]
    
    # Calculate average scores
    avg_scores = list(map(lambda s: {
        'name': s['name'], 
        'average': sum(s['scores']) / len(s['scores'])
    }, students))
    
    print("  Complex data processing:")
    print(f"    Students with averages: {avg_scores}")
    
    # Filter high achievers (average >= 85)
    high_achievers = list(filter(lambda s: s['average'] >= 85, avg_scores))
    print(f"    High achievers: {high_achievers}")


# Section 3: Advanced Methods

def demonstrate_advanced_techniques():
    """Demonstrate advanced functional programming techniques"""
    print("\n3.1 Advanced Techniques")
    
    # Currying
    def curry(func):
        def curried(*args, **kwargs):
            if len(args) + len(kwargs) >= func.__code__.co_argcount:
                return func(*args, **kwargs)
            return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
        return curried
    
    @curry
    def add_three(x, y, z):
        return x + y + z
    
    print("  Currying:")
    add_5 = add_three(5)
    add_5_and_3 = add_5(3)
    result = add_5_and_3(2)
    print(f"    Curried addition 5+3+2: {result}")
    
    # Function composition
    def compose(*functions):
        return lambda x: reduce(lambda acc, func: func(acc), functions, x)
    
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    composed = compose(square, multiply_by_two, add_one)
    result = composed(3)  # ((3+1)*2)^2 = 64
    print(f"    Composed function result: {result}")
    
    # Partial application
    multiply = lambda x, y: x * y
    double = partial(multiply, 2)
    triple = partial(multiply, 3)
    
    print("  Partial application:")
    print(f"    Double 5: {double(5)}")
    print(f"    Triple 4: {triple(4)}")
    
    # Memoization decorator
    def memoize(func):
        cache = {}
        @wraps(func)
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        wrapper.cache = cache
        return wrapper
    
    @memoize
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    print("  Memoization:")
    result = fibonacci(10)
    print(f"    Fibonacci(10): {result}")
    print(f"    Cache size: {len(fibonacci.cache)}")


def demonstrate_functional_patterns():
    """Demonstrate functional programming patterns"""
    print("\n3.2 Functional Patterns")
    
    # Pipeline pattern
    def pipeline(*functions):
        return lambda x: reduce(lambda acc, func: func(acc), functions, x)
    
    process_text = pipeline(
        str.lower,
        lambda s: s.replace(' ', '_'),
        lambda s: s + '_processed'
    )
    
    result = process_text("Hello World")
    print(f"  Pipeline result: {result}")
    
    # Map-reduce pattern for word counting
    text = "hello world hello python world"
    words = text.split()
    
    # Count words using map-reduce
    word_counts = reduce(
        lambda acc, word: {**acc, word: acc.get(word, 0) + 1},
        words,
        {}
    )
    
    print(f"  Word counting: {word_counts}")
    
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
    
    pipeline_result = list(evens_only(squares(numbers())))
    print(f"  Generator pipeline: {pipeline_result}")
    
    # Monadic pattern (Maybe)
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
    
    result = (Maybe.of(10)
              .bind(lambda x: x * 2)
              .bind(lambda x: x + 5)
              .bind(lambda x: x / 5)
              .value())
    
    print(f"  Maybe monad result: {result}")


def demonstrate_performance_optimization():
    """Demonstrate performance optimization techniques"""
    print("\n3.3 Performance Optimization")
    
    # Generator vs list performance
    def create_large_list():
        return [x**2 for x in range(100000)]
    
    def create_large_generator():
        return (x**2 for x in range(100000))
    
    print("  Memory efficiency:")
    
    # Time list creation
    start_time = time.time()
    large_list = create_large_list()
    list_time = time.time() - start_time
    
    # Time generator creation
    start_time = time.time()
    large_gen = create_large_generator()
    gen_time = time.time() - start_time
    
    print(f"    List creation time: {list_time:.6f}s")
    print(f"    Generator creation time: {gen_time:.6f}s")
    print(f"    Generator is {list_time/gen_time:.0f}x faster to create")
    
    # LRU Cache demonstration
    @lru_cache(maxsize=None)
    def expensive_fibonacci(n):
        if n <= 1:
            return n
        return expensive_fibonacci(n - 1) + expensive_fibonacci(n - 2)
    
    def naive_fibonacci(n):
        if n <= 1:
            return n
        return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)
    
    print("  Caching performance:")
    
    # Test cached version
    start_time = time.time()
    result_cached = expensive_fibonacci(30)
    cached_time = time.time() - start_time
    
    # Test naive version (smaller number to avoid long wait)
    start_time = time.time()
    result_naive = naive_fibonacci(25)
    naive_time = time.time() - start_time
    
    print(f"    Cached fib(30): {result_cached} in {cached_time:.6f}s")
    print(f"    Naive fib(25): {result_naive} in {naive_time:.6f}s")
    print(f"    Cache info: {expensive_fibonacci.cache_info()}")
    
    # Itertools for efficient iteration
    print("  Efficient iteration with itertools:")
    
    # Chain multiple iterables
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    chained = list(itertools.chain(list1, list2, list3))
    print(f"    Chained: {chained}")
    
    # Infinite counter
    counter = itertools.count(start=10, step=2)
    first_five = [next(counter) for _ in range(5)]
    print(f"    Infinite counter: {first_five}")
    
    # Combinations and permutations
    data = [1, 2, 3]
    combinations = list(itertools.combinations(data, 2))
    permutations = list(itertools.permutations(data, 2))
    print(f"    Combinations: {combinations}")
    print(f"    Permutations: {permutations}")


# Section 4: Common Errors and Best Practices

def demonstrate_common_errors():
    """Demonstrate common errors and how to avoid them"""
    print("\n4.1 Common Errors")
    
    # Error 1: Lambda variable capture
    print("  Error 1: Lambda variable capture")
    
    # Wrong way - late binding
    wrong_multipliers = []
    for i in range(3):
        wrong_multipliers.append(lambda x: x * i)
    
    print("    Wrong (all use i=2):")
    for j, mult in enumerate(wrong_multipliers):
        print(f"      Multiplier {j}(5) = {mult(5)}")
    
    # Correct way - capture at creation
    correct_multipliers = []
    for i in range(3):
        correct_multipliers.append(lambda x, i=i: x * i)
    
    print("    Correct:")
    for j, mult in enumerate(correct_multipliers):
        print(f"      Multiplier {j}(5) = {mult(5)}")
    
    # Error 2: Generator exhaustion
    print("  Error 2: Generator exhaustion")
    
    def simple_gen():
        yield 1
        yield 2
        yield 3
    
    gen = simple_gen()
    print(f"    First consumption: {list(gen)}")
    print(f"    Second consumption: {list(gen)}")  # Empty!
    
    # Solution: Create new generator or use tee
    gen1, gen2 = itertools.tee(simple_gen(), 2)
    print(f"    Tee solution 1: {list(gen1)}")
    print(f"    Tee solution 2: {list(gen2)}")
    
    # Error 3: Filter/Map returning iterators
    print("  Error 3: Iterator vs List confusion")
    
    numbers = [1, 2, 3, 4, 5]
    evens_iter = filter(lambda x: x % 2 == 0, numbers)
    
    print(f"    First iteration: {list(evens_iter)}")
    print(f"    Second iteration: {list(evens_iter)}")  # Empty!
    
    # Solution: Convert to list if needed multiple times
    evens_list = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"    List solution: {evens_list} (reusable)")
    
    # Error 4: Overly complex lambdas
    print("  Error 4: Complex lambdas (hard to debug)")
    
    # Too complex for lambda
    complex_lambda = lambda x: x**2 + 2*x + 1 if x > 0 else -x**2 + 2*x - 1 if x < 0 else 0
    
    # Better as regular function
    def complex_function(x):
        """Calculate complex expression based on x value"""
        if x > 0:
            return x**2 + 2*x + 1
        elif x < 0:
            return -x**2 + 2*x - 1
        else:
            return 0
    
    test_val = 3
    print(f"    Lambda result: {complex_lambda(test_val)}")
    print(f"    Function result: {complex_function(test_val)}")
    print("    Function is more readable and debuggable")


def demonstrate_best_practices():
    """Demonstrate best practices for functional programming"""
    print("\n4.2 Best Practices")
    
    print("""
  LAMBDA FUNCTIONS:
  ✓ Use for simple, single-expression functions
  ✓ Prefer regular functions for complex logic
  ✓ Be careful with variable capture in closures
  ✓ Consider readability over brevity
  
  FILTER AND MAP:
  ✓ Remember they return iterators, not lists
  ✓ Convert to list if multiple iterations needed
  ✓ Consider list comprehensions for readability
  ✓ Handle different-length iterables carefully
  
  GENERATORS:
  ✓ Use for large datasets or infinite sequences
  ✓ Remember generators are consumed once
  ✓ Handle StopIteration exceptions properly
  ✓ Use yield for memory-efficient iteration
  
  DECORATORS:
  ✓ Use functools.wraps to preserve metadata
  ✓ Handle *args and **kwargs properly
  ✓ Consider performance impact
  ✓ Make decorators reusable and composable
  
  GENERAL:
  ✓ Prefer immutable data structures
  ✓ Use pure functions when possible
  ✓ Compose functions for complex operations
  ✓ Handle errors explicitly
  ✓ Write tests for functional code
    """)
    
    # Practical example combining best practices
    print("  Practical Example - Safe Data Processing:")
    
    def safe_operation(default_value=None):
        """Decorator for safe operations with error handling"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"      Error in {func.__name__}: {e}")
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
    print(f"    Processed result: {result}")
    
    # Test error handling
    result_error = process_numbers("invalid")  # Will use default
    print(f"    Error case result: {result_error}")
    
    # Performance-conscious example
    def efficient_data_pipeline(data):
        """Efficient data processing pipeline"""
        return [
            x * 2 
            for x in data 
            if x > 0 and x % 2 == 0
        ]
    
    large_data = list(range(-1000, 1001))
    start_time = time.time()
    result = efficient_data_pipeline(large_data)
    end_time = time.time()
    
    print(f"    Pipeline processed {len(large_data)} items")
    print(f"    Result length: {len(result)}")
    print(f"    Processing time: {end_time - start_time:.6f}s")


if __name__ == "__main__":
    main()

