""" ITERATORS IN PYTHON """

""" Definition
An iterator in Python is an object that allows you to traverse a sequence (like lists, tuples, or strings)
one element at a time. It implements two key methods:

__iter__(): Returns the iterator object itself.
__next__(): Returns the next value from the sequence or raises a StopIteration exception when no more elements
are available.

**Key Concepts**

Iterable: An object that can return an iterator using the iter() function (e.g., lists, tuples, sets, strings,
 dictionaries).

Iterator: An object that implements the __iter__() and __next__() methods. """

""" Creating an Iterator """

""" 1-Using Built-in Iterables """

my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3

"""2- Custom Iterator Class You can create a custom iterator by defining the __iter__() and __next__() methods."""

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

for num in MyIterator(1, 5):
    print(num)  # Output: 1, 2, 3, 4, 5


""" ***Built-in Iterators*** 

Python provides many built-in iterators for commonly used data types: """

""" Strings """

for char in "Python":
    print(char)  # Output: P y t h o n


""" Dictionaries """

for key, value in {"a": 1, "b": 2}.items():
    print(key, value)


""" Files """

with open("example.txt") as file:
    for line in file:
        print(line)


""" Iterating with Loops
1-For Loop: Simplifies iteration by handling the iterator internally. """

my_list = [10, 20, 30]
for value in my_list:
    print(value)


""" 2-While Loop: Explicitly uses iter() and next().""" 

iterator = iter(my_list)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
    
""" Difference Between Iterable and Iterator

Feature	                     Iterable	                                        Iterator

Definition	                 An object capable of returning an iterator.	    An object with a __next__() method.
Methods Required	           __iter__()	                                      __iter__() and __next__()
Examples	                 Lists, Tuples, Strings, Dictionaries	            File objects, Generator objects
Usage	                     Can be passed to iter() to get an iterator.	    Produces values one at a time.

"""

""" Use Cases
1-Efficient Data Handling Iterators are memory-efficient because they don’t require loading all elements at once.

2-Infinite Sequences Iterators can generate infinite sequences without exhausting memory."""

class InfiniteNumbers:
    def __init__(self, start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current - 1

infinite = iter(InfiniteNumbers(1))
for _ in range(5):
    print(next(infinite))  # Output: 1, 2, 3, 4, 5


""" 3-Chained Iteration Use libraries like itertools to combine or extend iterator functionalities."""

from itertools import cycle

for item in cycle(["A", "B", "C"]):
    print(item)


""" Custom Iterators Example """

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

fib = Fibonacci(10)
for num in fib:
    print(num)

""" Output:"""
0
1
1
2
3
5
8

"""
Advantages of Iterators
1-Lazy Evaluation: Compute values on demand, reducing memory usage.
2-Custom Behavior: Define how objects should be iterated over.
3-Simplified Code: Built-in support for loops and comprehensions.


Iterators are a core concept in Python, enabling efficient and flexible iteration over data."""