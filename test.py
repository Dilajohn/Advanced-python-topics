""" list comprehension """
# squares = [x**2 for x in range(10)]
# print(squares)

# even_numbers = [x for x in range(20) if x % 2 == 0]
# print(even_numbers)

# words = ["hello","world", "python" ]
# capitalized = [word.upper() for word in words]
# print(capitalized)

# pairs = [(x,y) for x in range(3) for y in range(3)]
# print(pairs)

# processed = [x if x % 2 == 0 else -x for x in range(10)]
# print(processed)

# nested_list = [[1,2],[3,4],[5,6]]
# flat_list = [item for sublist in nested_list for item in sublist]
# print(flat_list)

""" generators """

# def count_up_to(n):
  # count = 1
  # while count <= n:
    # yield count
    # count += 1

# for num in count_up_to(5):
  # print(num)

# gen = (x**2 for x in range(5))
# for value in gen:
  # print(value)

# def infinite_numbers(start=0):
  # while True:
    # yield start
    # start += 1 

# gen = (x for x in range(3)) 
# print(next(gen)) 
# print(next(gen)) 
# print(next(gen)) 

# def fibonacci(limit):
  # a,b = 0,1
  # while a < limit: 
    # yield a
    # a, b = b, a + b

# for num in fibonacci(10):
  # print(num)   

""" expressions """  
# a = True
# b = False
# result = a and b
# print(result)

# greeting = "Hello" + " " + "World"
# repeat = "Hi" * 3
# print(greeting)
# print(repeat)

# ist = [1,2,3]
# result = ist + [4,5]
# print (result)

# unique_numbers = {1,2,3} | {3,4,5}
# print(unique_numbers)

# age = 18
# result = "Adult" if age >= 18 else "Minor"
# print(result)

# lambda expressions -a way to define , anonymous functions
# square = lambda x: x**2
# result = square(5)
# print(result)

# Function Calls: Any call to a function is also an expression because it returns a value
# def add(a, b):
  # return a + b

# result = add(2, 3)
# print(result)

# Assignment Expressions (Walrus Operator :=): Introduced in Python 3.8, the walrus operator allows you to assign
#  a value to a variable as part of an expression.

# if (n:=len("Hello"))> 3:
  # print(n)

""" closures """

# def outer_function(x):
  # def inner_function(y):
    # return x + y
  # return inner_function

# add_five = outer_function(5)
# print(add_five(5))
# print(add_five(3))
# print(add_five(10))

# Inspecting free variables
# print(add_five.__code__.co_freevars)
# print(add_five.__closure__[0].cell_contents)

# def multiplier(factor):
  # def multiply_by_factor(x):
    # return x * factor
  # return multiply_by_factor

# double = multiplier(2)
# triple = multiplier(3)

# print(double(5))
# print(triple(5))

# Stateful Functions: Retain state between function calls

# def counter():
  # count = 0
  # def increment(): 
    # nonlocal count 
    # count += 1
    # return count
  # return increment

# counter_instance = counter()
# print(counter_instance())
# print(counter_instance())
# print(counter_instance())

# Mutable Variables: Closures with mutable free variables can behave unexpectedly.
# def  create_accumulator():
  # functions = []
  # for i in range(5):
    # def  accumulator():
      # return i
    # functions.append(accumulator)
  # return functions

# accs = create_accumulator()
# print(accs[0]()) 

#Solution: Bind variables immediately.
# def create_accumulator():
  # functions = []
  # for i in range(5):
    # def accumulator(i = i):
      # return i
    # functions.append(accumulator)
  # return functions  

# accs = create_accumulator()
# print(accs[0]())

""" Decorators """
# basic syntax

# def decorator_function(original_function):
  # def wrapper_function(*args, **kwargs):
    # print(f"Wrapper executed before {original_function.__name__}")
    # result  = original_function(*args, **kwargs)
    # print(f"Wrapper executed after {original_function.__name__}")
    # return result
  # return wrapper_function

# @decorator_function
# def display():
  # print("Display function executed.")

# display()

# logging
# def log_decorator(func):
  # def wrapper(*args, **kwargs):
    # print(f"Calling {func.__name__} with {args} and {kwargs}")
    # result = func(*args, **kwargs)
    # print(f"{func.__name__} returned {result}")
    # return result
  # return wrapper

# @log_decorator
# def add(a,b):
  # return a + b

# add(3,5)

# Access control
'''
def require_login(func):
  def wrapper(user):
    if not user.get("logged_in"):
      raise PermissionError("User not logged in")
    return func(user)
  return wrapper

@require_login
def view_dashboard(user):
  return "Welcome to the DashBoard"

user = {"username": "johnathan", "logged_in":True}
print(view_dashboard(user))
'''

# performance management 
"""
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
  print("Function Complete")

slow_function() """

# Chaining Multiple Decorators
"""
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

greet()  """

# class based decorators
# class DecoratorClass:
  # def __init__(self,func):
    # self.func = func

  # def __call__(self, *args, **kwargs):
    # print(f"Class based decorator called for {self.func.__name_}")
    # return self.func(*args, **kwargs)
  
# @DecoratorClass
# def say_hello():
  # print("Hello, world!") 

# say_hello()  
""" needto fix the attribute error on line  258"""

""" iterators """

# my_list = [1,2,3]
# iterator = iter(my_list)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# Custom Iterator Class You can create a custom iterator by defining the __iter__() and __next__() methods
"""
class MyIterator:
  def __init__(self,start,end):
    self.current = start
    self.end = end

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.current > self.end:
      raise StopIteration
    self.current += 1
    return self.current - 1
  
for num in MyIterator(1,5):
  print(num)

"""

""" lambda function """
# add = lambda x, y:x + y
# print(add(3, 5))

# square = lambda x: x*x
# print(square(4))

# greet = lambda :"Hello, World!"
# print(greet())

# is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(is_even(5))

# numbers = [1,2,3,4]
# squared = map(lambda x: x ** 2, numbers)
# print(list(squared))

# numbers = [1, 2, 3, 4, 5]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))

"""from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x , y: x * y, numbers)
print(product)


items = [("apple",10), ("banana",5), ("cherry",8)]
sorted_items = sorted(items, key = lambda x: x[1])
print(sorted_items)

 Inline functions

def apply_function(f, x):
  return f(x)

result = apply_function(lambda x: x **2, 5)
print(result) """

""" THREADING """
import threading

# def print_numbers():
  # for i in range(5):
    # print(f"Number: {i}")

# thread = threading.Thread(target=print_numbers)
# thread.start()
# thread.join()
# print(" Thread finished")    

""" 2-using subclass """

# class MyThread(threading.Thread):
  # def run(self):
    # for i in range(5):
      # print(f"Thread is running: {i}")

# thread = MyThread()   
# thread.start()
# thread.join()  

""" Thread synchronization""" 
# 1-locks

# lock = threading.Lock()

# def safe_print():
  # with lock:
    # print("Safe access to shared resource")

# thread1 = threading.Thread(target=safe_print)
# thread2 = threading.Thread(target=safe_print)
# thread1.start()
# thread2.start()

# 2-Rlocks(reentrant locks)

# rlock = threading.RLock()

""" 3- Control access to a resource with a set limit."""
# allows up to 2 threads

# semaphore = threading.Semaphore(2)

# def limited_access():
  # with semaphore:
    # print("Accessing a resource")

# thread1 = threading.Thread(target=limited_access) 
# thread2 = threading.Thread(target=limited_access) 
# thread3 = threading.Thread(target=limited_access) 
# thread1.start()
# thread2.start()
# thread3.start()   

"""Thread Communication"""
""" 1-Event Threads can communicate using threading.Event. """

# event = threading.Event()

# def wait_for_event():
  # print("Waiting for event.....")
  # event.wait()
  # print("Event received!")

# thread = threading.Thread(target=wait_for_event)
# thread.start()

# event.set()

""" 2-Queue: Uses queue.Queue for thread-safe communication.""" 

# import queue

# q = queue.Queue()

# def producer():
  # for i in range(5):
    # q.put(i)
    # print(f"produced: {i}")

# def consumer():
  # while not q.empty():
    # item = q.get()
    # print(f"consumed: {item}")

# thread1 = threading.Thread(target=producer) 
# thread2 = threading.Thread(target=consumer) 
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()  

""" ***DEAMON THREADS *** 
A daemon thread runs in the background and is terminated when the main program exits."""

# def background_task():
  # while True:
    # print("Deamon  thread running....")

# thread = threading.Thread(target=background_task, daemon=True)
# thread.start()

""" Thread Pooling with concurrent.futures
The ThreadPoolExecutor simplifies managing a pool of threads. """

# from concurrent.futures import ThreadPoolExecutor

# def task(name):
  # print(f"Executing task {name}")

# with ThreadPoolExecutor(max_workers=3) as executor:
  # executor.submit(task, "Task 1")
  # executor.submit(task, "Task 2") 
  # executor.submit(task, "Task 3")  

""" MAGIC METHODS"""  

# class Person:
  # def __init__(self, name, age):
    # self.name = name
    # self.age = age

  # def __str__(self): 
    # return f"{self.name}, {self.age} years old"
  
  # def __repr__(self):
    # return f"Person(name={self.name}, age={self.age})"
  
# P = Person("Jonathan", 30) 
# print(str(P))
# print(repr(P))

""" 2-Arithmetic Operators"""     

# class Vector:
  # def __init__(self, x, y):
    # self.x = x
    # self.y = y

  # def __add__(self, other):
    # return Vector(self.x + other.x, self.y + other.y) 

  # def __repr__(self):
    # return f"Vector({self.x}, {self.y})"

# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print(v1 + v2)   

""" 3-Comparison Operators :Define behavior for comparison operators:"""
# class Person:
  # def __init__(self, name, age):
    # self.name = name
    # self.age = age

  # def __eq__(self, other):
    # return self.age == other.age  

# p1 = Person("Jonathan", 30)
# p2 = Person("Tina",30)
# print(p1 == p2)    

""" 4-Container-Like Behavior: These methods allow your objects to 
behave like containers (lists, dictionaries, etc.)"""

# class CustomList:
  # def __init__(self,items):
    # self.items = items

  # def __len__(self):
    # return len(self.items)
  
  # def __getitem__(self, index):
    # return self.items[index]
  
# cl = CustomList([1, 2, 3])
# print(len(cl)) 
# print(cl[1]) 

""" 5-Callable Objects
__call__(self, *args, **kwargs): Makes an instance callable like a function. """

# class Greeter:
  # def __call__(self, name):
    # return f"Hello, {name}!"
  
# greet = Greeter()
# print(greet("Jonathan"))

""" 6-Attribute Access """

# class DynamicAttributes:
  # def __getattr__(self, name):
    # return f"Attribute {name} not found"
  
# obj = DynamicAttributes()
# print(obj.some_attr)  

""" 7-Context Managers """

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w") 
        return self .file   
    
    def __exit__(self, exec_type, exec_value, traceback):
        self.file.close()


with FileManager("test.txt") as f:
    f.write("Hello, World!")
        


  

    

    


    


  
