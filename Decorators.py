""" DECORATORS IN PYTHON """

""" Definition
A decorator in Python is a higher-order function that modifies or enhances the behavior of another function or
method without changing its structure. Decorators are applied using the @decorator_name syntax.

How Decorators Work
.Functions as First-Class Citizens: Functions can be passed as arguments, returned from other functions, and 
assigned to variables.
.Closures: A decorator leverages closures to wrap a target function, altering its behavior."""

#Basic Syntax

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        result = original_function(*args, **kwargs)
        print(f"Wrapper executed after {original_function.__name__}")
        return result
    return wrapper_function

@decorator_function
def display():
    print("Display function executed.")

display()

""" Output:css

Wrapper executed before display
Display function executed.
Wrapper executed after display

Here, @decorator_function is syntactic sugar for display = decorator_function(display)."""

#Use Cases
""" 1-Logging """

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)

""" Output:csharp

Calling add with (3, 5) and {}
add returned 8 """

""" 2- Access Control """

def require_login(func):
    def wrapper(user):
        if not user.get("logged_in"):
            raise PermissionError("User not logged in")
        return func(user)
    return wrapper

@require_login
def view_dashboard(user):
    return "Welcome to the dashboard!"

user = {"username": "john", "logged_in": True}
print(view_dashboard(user))  # Output: Welcome to the dashboard!

""" 3-Performance Measurement """

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function complete")

slow_function()
""" Chaining Multiple Decorators """

def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One")
        return func(*args, **kwargs)
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two")
        return func(*args, **kwargs)
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Hello!")

greet()

""" Output:sql

Decorator One
Decorator Two
Hello!

The order of execution is bottom-to-top, meaning decorator_two is applied first. """

""" Class-Based Decorators
Instead of a function, you can use a class as a decorator by implementing the __call__ method. """

class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Class-based decorator called for {self.func.__name__}")
        return self.func(*args, **kwargs)

@DecoratorClass
def say_hello():
    print("Hello, world!")

say_hello()

""" Decorators with Arguments
To pass arguments to a decorator, create a decorator factory. """

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

greet()

""" #Output:
Hi!
Hi!
Hi! 
"""

""" Preserving Function Metadata
Decorators can overwrite the original function's metadata (e.g., name, docstring). To avoid this, use functools.wraps. """

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@decorator
def original_function():
    """Original function docstring."""
    pass

print(original_function.__name__)  # Output: original_function
print(original_function.__doc__)  # Output: Original function docstring.

"""Advantages of Decorators

1-Enhance code reusability and readability.
2-seful for cross-cutting concerns (e.g., logging, caching, validation).
3-Enable higher-order programming.

******-Decorators are a powerful and elegant feature in Python, ideal for extending
 or modifying the behavior of functions or methods dynamically.
 
"""
