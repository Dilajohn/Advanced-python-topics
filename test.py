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
def create_accumulator():
  functions = []
  for i in range(5):
    def accumulator(i = i):
      return i
    functions.append(accumulator)
  return functions  

accs = create_accumulator()
print(accs[0]())





