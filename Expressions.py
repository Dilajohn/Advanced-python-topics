""" EXPRESSIONS IN PYTHON """

""" In Python, an expression is a combination of values, variables, operators, and function calls that are evaluated
to produce a result. Essentially, an expression is any piece of code that can be evaluated to a value. """

# Types of Expressions in Python

""" 1-Arithmetic Expressions: These involve mathematical operations. """
x = 5 + 3 * 2  # 5 + (3 * 2) = 11

""" 2-Comparison Expressions: These return a Boolean value (True or False)."""

result = 10 > 5  # True

""" 3-Logical Expressions: These combine Boolean values using logical operators."""

a = True
b = False
result = a and b  # False

""" 4-String Expressions: These involve operations with strings, like concatenation or repetition."""

greeting = "Hello" + " " + "World"  # "Hello World"
repeat = "Hi " * 3  # "Hi Hi Hi "

""" 5-List Expressions: Operations on lists can also be expressions."""

lst = [1, 2, 3]
result = lst + [4, 5]  # [1, 2, 3, 4, 5]

""" 6-Set and Dictionary Expressions:"""

""" Set expressions:"""
unique_nums = {1, 2, 3} | {3, 4, 5}  # {1, 2, 3, 4, 5}

""" Dictionary expressions:"""
user_info = {"name": "Alice", "age": 30}

""" Conditional Expressions (Ternary Operator): A compact if-else expression."""
age = 18
result = "Adult" if age >= 18 else "Minor"  # "Adult"

""" Lambda Expressions: A way to define anonymous functions. """
square = lambda x: x ** 2
result = square(5)  # 25

"""List Comprehensions: 
These are a type of expression that generates a list based on some condition or transformation."""

even_numbers = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

""" Function Calls: Any call to a function is also an expression because it returns a value."""

def add(a, b):
    return a + b

result = add(2, 3)  # 5

""" Assignment Expressions (Walrus Operator :=): Introduced in Python 3.8, the walrus operator allows you to assign
 a value to a variable as part of an expression."""

if (n := len("Hello")) > 3:
    print(n)  # 5

""" Evaluating Expressions
The evaluation of an expression follows a set of rules (precedence and associativity). """
# For example:
''' In arithmetic expressions, multiplication and division have higher precedence than addition and subtraction.'''

x = 5 + 3 * 2  # Result is 11 because multiplication has higher precedence.
""" Expressions in Conditionals and Loops
Expressions are commonly used in control structures such as if, while, or for loops."""
#  For example:
# If expression
if x > 10:
    print("x is greater than 10")

# While expression
while (n := len("Hello")) > 3:
    print(n)  # Prints 5
    break

""" Summary
Expressions in Python are everywhere, from simple arithmetic to more complex logical operations.
They are evaluated and produce a result that can be assigned to a variable, returned from a function,
or used in conditions and loops. """