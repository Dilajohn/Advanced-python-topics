""" LAMBDAS IN PYTHON """

""" Definition
A lambda function is a small, anonymous function defined using the lambda keyword. 
It can have multiple arguments but only one expression, which is evaluated and returned. 
Lambda functions are often used for short, simple tasks and are written in a single line. """

""" Syntax

lambda arguments: expression
arguments: A comma-separated list of inputs to the function.
expression: A single expression that is evaluated and returned. """

""" Examples
1-Basic Example """

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

""" 2-Single Argument """

square = lambda x: x * x
print(square(4))  # Output: 16

""" 3-No Arguments """

greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

""" 4-Conditional Expression """

is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(5))  # Output: Odd

""" Common Use Cases
1-In Built-in Functions"""

""" map() """

numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]

""" filter() """

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

""" reduce() """

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

""" 2-Sorting with key Parameter """

items = [("apple", 10), ("banana", 5), ("cherry", 8)]
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)  # Output: [('banana', 5), ('cherry', 8), ('apple', 10)]

""" 3-Inline Functions """

def apply_function(f, x):
    return f(x)

result = apply_function(lambda x: x ** 2, 5)
print(result)  # Output: 25

""" Lambdas vs Regular Functions

Feature	        Lambda Functions                    	    Regular Functions

Syntax	        Single-line, concise	                    Multi-line, more descriptive
Name	          Anonymous	                                Named (via def)
Complexity	    Simple operations	                        Suitable for complex logic
Usage	          Quick, throwaway functions	              Reusable, longer-term logic
Readability   	Less readable for complex expressions	    More readable for complex expressions
    
Advantages of Lambdas

1-Conciseness: Compact and easy to define.
2-Anonymous: No need to define a named function for simple operations.
3-Versatility: Works seamlessly with higher-order functions like map, filter, and reduce.

Limitations of Lambdas

1-Single Expression: Can only contain one expression (no statements or multi-line logic).
2-Debugging: Errors in lambdas can be harder to trace because they are anonymous.
3-Readability: Complex lambdas can be difficult to read and understand.

Best Practices

1-Keep Lambdas Simple: Use them for short, one-line functions.
2-Avoid Complex Logic: If the logic is complex, use a regular function for better readability.
3-Combine with Higher-Order Functions: Use lambdas effectively with map, filter, and similar functions.
    
Lambdas are a powerful feature in Python, ideal for concise, inline operations and often used in 
functional programming scenarios. """