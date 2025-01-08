""" PARADIGMS IN PYTHON 
Python is a versatile and powerful language that supports multiple programming paradigms.
These paradigms offer different approaches to solving problems and structuring code.
Below are the main paradigms supported by Python: """

""" 1. Imperative Programming
Definition: Focuses on how a program operates, using statements to change a program's state.
Features: Explicit step-by-step instructions. """
# Example:

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)  # Output: 15

""" 2. Procedural Programming
Definition: A subset of imperative programming where code is organized into procedures or functions.
Features: Emphasis on code reuse through functions. """

# Example:

def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))  # Output: 8

""" 3. Object-Oriented Programming (OOP)
Definition: Organizes code using objects, which bundle data (attributes) and behavior (methods).

Key Concepts:
.Class: Blueprint for creating objects.
.Object: Instance of a class.
.Encapsulation: Restrict access to certain parts of an object.
.Inheritance: Create new classes from existing ones.
.Polymorphism: Methods can perform differently based on the object. """

# Example:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!

""" 4. Functional Programming
Definition: Focuses on functions as the primary building blocks and avoids mutable state and side effects.

Key Concepts:
.Higher-Order Functions: Functions that take other functions as arguments or return them.
.Pure Functions: No side effects and consistent outputs for the same inputs.
.Immutability: Data structures should not be changed. """

# Example:
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

""" 5. Declarative Programming
Definition: Focuses on what the program should accomplish rather than how it does so.

Subtypes:
.Logic Programming: Defines rules and facts, leaving the logic engine to infer results.
.Database Queries: SQL-like syntax in Python (e.g., with SQLAlchemy)."""
# Example (Declarative Style):


even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

""" 6. Event-Driven Programming
Definition: Focuses on responding to events (e.g., user inputs, messages, or sensor outputs).

Use Cases: GUI applications, games, and asynchronous programming. """

# Example (Using tkinter):

import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()
root.mainloop()

"""7. Concurrent Programming
Definition: Enables multiple parts of a program to run independently or simultaneously.

Key Concepts:
.Multithreading: Multiple threads within the same process.
.Multiprocessing: Running multiple processes simultaneously.
.Asynchronous Programming: Non-blocking tasks using async and await."""

# Example (AsyncIO):

import asyncio

async def greet():
    print("Hello!")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(greet())

""" 8. Scripting
Definition: Writing small, task-specific scripts for automation or system administration."""
# Example:

import os

files = os.listdir(".")
print(files)  # Lists files in the current directory

""" 9. Meta-Programming
Definition: Writing programs that manipulate code (like generating code or altering class behavior).
Use Cases: Dynamic class creation, decorators, and altering methods."""
# Example (Decorator):

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(2, 3))  # Output: Calling add with (2, 3), {} | 5

"""Why Use Multiple Paradigms in Python?
Flexibility: Use the best paradigm for the problem at hand.
Readable Code: Different paradigms make your code expressive and easier to understand.
Rich Ecosystem: Python libraries often leverage different paradigms.
Let me know if you'd like to dive deeper into any specific paradigm!"""