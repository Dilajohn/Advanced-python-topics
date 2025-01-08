""" Generators in Python

Definition

A generator is a special type of iterable in Python that allows you to yield values one
at a time using the yield keyword instead of returning them all at once. Generators produce items 
lazily, meaning values are computed and provided only when requested."""

"""Key Characteristics

1-Lazy Evaluation: Values are generated on-demand, which is memory-efficient, especially for large datasets.
2-State Retention: Generators retain their state between calls, allowing them to resume execution where they left off.
3-Single Iteration: Generators can be iterated over only once. They are not reusable like lists.

Creating Generators

1-Using yield in a function: A function becomes a generator when it contains the yield keyword.
2-Using generator expressions: Similar to list comprehensions but with parentheses."""

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

#Output:
1
2
3
4
5

""" Using Generator Expressions: Similar to list comprehensions but with parentheses."""

gen = (x**2 for x in range(5))
for value in gen:
    print(value)

#Output:
0
1
4
9
16

""" Advantages
Memory Efficiency: Unlike lists, generators don’t store all values in memory. They compute each value on demand.
Infinite Sequences: Generators can produce values indefinitely without running out of memory."""


def infinite_numbers(start=0):
    while True:
        yield start
        start += 1

"""Methods of Generators
1-__next__(): Retrieves the next value from the generator."""

gen = (x for x in range(3))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

""" 2-send(value): Resumes the generator and sends a value to it.
    3-close(): Stops the generator.

Applications

1-Streaming Data: Handle large files or infinite streams of data.
2-Pipelines: Process data step-by-step in stages.
3-Custom Iterables: Create your own iterable logic.

Comparison with Iterators
Generators are a type of iterator, but they are implemented differently in Python."""

"""
Feature   	    Generators	                                       Iterators
Creation  	    Defined with yield or generator expressions	       Implemented using __iter__ and __next__
State           Retention	Built-in	                           Must manage manually
Memory	        Very efficient	                                   Can be less efficient  for large datasets
efficiency
Reusability	    Not reusable	                                   Reusable with __iter__ and __next__
Applications    Streaming data, pipelines, custom iterables	       Custom iterators, data processing """

"""Example: Custom Range Function"""
"""Example: Fibonacci Sequence"""

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
    
#Output:
0
1
1
2
3
5
8

"""Generators provide a powerful way to manage and process data efficiently in Python programs."""