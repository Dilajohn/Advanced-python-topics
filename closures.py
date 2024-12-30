""" Closures in Python
Definition
A closure in Python is a function that retains access to variables from its enclosing scope, even after the outer function has finished executing. Closures enable you to encapsulate behavior and maintain state.

How Closures Work
. An inner function is defined inside an outer function.
. The inner function references variables from the outer function.
. The outer function returns the inner function.
. The returned function retains the environment of the variables it referenced from the outer scope."""

""" Syntax and Example"""
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

""" Create a closure"""
add_five = outer_function(5)
print(add_five(3))  # Output: 8
print(add_five(10)) # Output: 15

"""Here, add_five is a closure. It retains access to x = 5 from the outer function,
even though outer_function has finished executing.

Components of a Closure

1-Free Variables: Variables from the enclosing scope that are referenced by the inner function.
2-Inner Function: The function that uses the free variables.
3-Environment: The saved state of the free variables."""

""" Inspecting free variables"""
print(add_five.__code__.co_freevars)  # Output: ('x',)
print(add_five.__closure__[0].cell_contents)  # Output: 5

""" #Use Cases
1-Data Encapsulation: Hide data and only expose controlled behavior.
2-Function Factory: Create customized functions dynamically.
3-Stateful Functions: Retain state between function calls."""

def multiplier(factor):
    def multiply_by_factor(x):
        return x * factor
    return multiply_by_factor

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

"""Stateful Functions: Retain state between function calls."""

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter_instance = counter()
print(counter_instance())  # Output: 1
print(counter_instance())  # Output: 2
print(counter_instance())  # Output: 3

"""
Advantages
1-Encapsulation: Closures help in encapsulating variables and making them private to the inner function.
2-Higher-Order Functions: Useful for writing functions that return other functions dynamically.
3-Flexibility: Enable functional programming patterns, such as currying and decorators.
4-Stateful Behavior: Retain state between function calls.
5-Data Hiding: Hide data from the global scope and expose only necessary behavior.
6-Code Reusability: Create reusable functions that can be customized with different parameters.
7-Functional Programming: Implement functional programming concepts such as partial application and currying.
8-Callback Functions: Pass functions as arguments to other functions.

Comparison with Regular Functions

Feature	                        Regular Function	                                     Closure
Access to Outer Scope	          Limited to global variables	           Can access variables from enclosing scope
State Retention	                No	                                   Yes
Encapsulation	                  No	                                   Yes
"""

""" Caveats

1-Memory Overhead: If closures are not used carefully, they can lead to memory retention issues.
2-Mutable Variables: Closures with mutable free variables can behave unexpectedly."""

def create_accumulators():
    functions = []
    for i in range(5):
        def accumulator():
            return i
        functions.append(accumulator)
    return functions

accs = create_accumulators()
print(accs[0]())  # Output: 4 (not 0)
#Solution: Bind variables immediately.
def create_accumulators():
    functions = []
    for i in range(5):
        def accumulator(i=i):
            return i
        functions.append(accumulator)
    return functions

""" Closures are a powerful feature in Python for creating dynamic, encapsulated, and stateful behavior in your programs."""