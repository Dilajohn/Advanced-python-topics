""" FUNCTIONAL PROGRAMMING IN PYTHON """

""" Definition

Functional programming (FP) is a programming paradigm focused on using functions to build programs.
It treats computation as the evaluation of mathematical functions and avoids changing state or mutable data.

Python supports functional programming features while still being a multi-paradigm language.

***Key Concepts in Functional Programming***
1-First-Class Functions: Functions are treated as first-class citizens. They can be:

. Assigned to variables
. Passed as arguments to other functions
. Returned as values from other functions

2-Pure Functions: A function is pure if:

. Its output depends only on its inputs.
. It produces no side effects (e.g., modifying global variables).

3-Immutability: Data does not change after it is created.

4-Higher-Order Functions: Functions that take other functions as arguments or return functions as results.

5-Recursion: Functions call themselves to solve smaller instances of a problem.

6-Function Composition: Combining simple functions to build more complex ones. """

""" Functional Constructs in Python

1- map() Applies a function to each item in an iterable and returns a map object (an iterator)."""

numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))  # Output: [1, 4, 9, 16]

""" 2-filter() Filters elements in an iterable based on a predicate (a function returning True or False). """

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

""" 3-reduce() Applies a function cumulatively to the items in an iterable, reducing it to a single value.
Requires importing from functools."""

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

""" 4-lambda Functions Short, anonymous functions for quick operations."""

multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

""" Higher-Order Functions
Functions that operate on other functions. """

""" 1-Passing Functions as Arguments """

def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x ** 2, 5)
print(result)  # Output: 25

""" 2-Returning Functions """

def multiplier(factor):
    return lambda x: x * factor

double = multiplier(2)
print(double(5))  # Output: 10

""" Functional Features in itertools """
""" 1-itertools.accumulate() Accumulates results of a binary function (e.g., sum or product) applied iteratively."""

from itertools import accumulate
numbers = [1, 2, 3, 4]
cumulative_sum = accumulate(numbers)
print(list(cumulative_sum))  # Output: [1, 3, 6, 10]

""" 2-itertools.chain() Combines multiple iterables into one."""

from itertools import chain
combined = chain([1, 2], [3, 4])
print(list(combined))  # Output: [1, 2, 3, 4]

""" Immutability in Python
While Python does not enforce immutability, you can emulate it using:

. Tuples instead of lists.
. Frozensets instead of sets. """

immutable_tuple = (1, 2, 3)
immutable_set = frozenset([1, 2, 3])

""" Recursive Functions
Functional programming often relies on recursion. """

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

""" Benefits of Functional Programming

1-Simplicity: Focus on pure functions makes programs easier to reason about.
2-Modularity: Small, reusable functions promote cleaner code.
3-Concurrency: Immutable data structures avoid race conditions in multi-threaded programs.
4-Testability: Pure functions are easier to test and debug.

Challenges of Functional Programming

1-Performance: Recursion can be less efficient compared to loops in Python due to the lack of tail-call optimization.
2-Readability: Extensive use of lambdas and higher-order functions can make code harder to read for beginners.
3-State Management: Managing state in a purely functional style can be more complex.

When to Use Functional Programming in Python

1-Data Transformation: Use map, filter, and reduce for clean and efficient data processing.
2-Immutable Data: Functional programming shines when immutability is crucial, such as in concurrent applications.
3-Composability: When you want to combine simple functions into more complex ones. """

""" Combining FP with Other Paradigms   
Python allows mixing functional programming with object-oriented or procedural paradigms. For example:"""

class Calculator:
    def __init__(self):
        self.operations = []

    def add_operation(self, func):
        self.operations.append(func)

    def calculate(self, value):
        for operation in self.operations:
            value = operation(value)
        return value

calc = Calculator()
calc.add_operation(lambda x: x + 10)
calc.add_operation(lambda x: x * 2)
print(calc.calculate(5))  # Output: 30

""" Python's functional programming features allow developers to write concise, readable, and powerful code
while maintaining flexibility. """