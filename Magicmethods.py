""" MAGIC METHODS IN PYTHON """

""" Magic methods in Python, also known as dunder methods (short for "double underscore"),
are special methods with double underscores (__) at the beginning and end of their names.
 These methods enable custom behavior for your objects and allow you to define or override the
     behavior of Python operators, built-in functions, and other standard features."""

# Commonly Used Magic Methods
""" 1-Initialization and Representation """
'''
__init__(self, ...): Initializes a new object.
__str__(self): Defines the string representation of an object (used by str() or print()).
__repr__(self): Defines a more formal string representation (used in debugging, or by repr()).'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Alice", 30)
print(str(p))  # Alice, 30 years old
print(repr(p)) # Person(name=Alice, age=30)

""" 2-Arithmetic Operators These methods define custom behavior for arithmetic operations:"""

"""__add__(self, other): Implements +.
__sub__(self, other): Implements -.
__mul__(self, other): Implements *.
__truediv__(self, other): Implements /.
__floordiv__(self, other): Implements //.
__mod__(self, other): Implements %.
__pow__(self, other): Implements **. """


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)

""" 3-Comparison Operators :Define behavior for comparison operators:

__eq__(self, other): Implements ==.
__ne__(self, other): Implements !=.
__lt__(self, other): Implements <.
__le__(self, other): Implements <=.
__gt__(self, other): Implements >.
__ge__(self, other): Implements >=. """



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age

p1 = Person("Alice", 30)
p2 = Person("Bob", 30)
print(p1 == p2)  # True

""" 4-Container-Like Behavior These methods allow your objects to behave like containers (lists, dictionaries, etc.):

__len__(self): Returns the length (used by len()).
__getitem__(self, key): Retrieves an item using obj[key].
__setitem__(self, key, value): Sets an item using obj[key] = value.
__delitem__(self, key): Deletes an item using del obj[key].
__contains__(self, item): Implements the in operator. """


class CustomList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]

cl = CustomList([1, 2, 3])
print(len(cl))    # 3
print(cl[1])      # 2

""" 5-Callable Objects

__call__(self, *args, **kwargs): Makes an instance callable like a function. """


class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"

greet = Greeter()
print(greet("Alice"))  # Hello, Alice!

""" 6-Attribute Access

__getattr__(self, name): Called when accessing an attribute that doesn't exist.
__getattribute__(self, name): Called for every attribute access.
__setattr__(self, name, value): Called when setting an attribute.
__delattr__(self, name): Called when deleting an attribute. """


class DynamicAttributes:
    def __getattr__(self, name):
        return f"Attribute {name} not found"

obj = DynamicAttributes()
print(obj.some_attr)  # Attribute some_attr not found

""" 7-Context Managers

__enter__(self): Defines setup logic for with statements.
__exit__(self, exc_type, exc_value, traceback): Defines teardown logic for with."""

class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager("test.txt") as f:
    f.write("Hello, World!")

""" Benefits of Magic Methods
Allow you to create objects that behave like built-in types.
Enable operator overloading for custom classes.
Enhance readability and usability of your classes. """