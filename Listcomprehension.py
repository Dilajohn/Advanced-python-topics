""" LIST COMPREHENSION """

'''List comprehension in Python provides a concise way to create lists. 
It is often used to apply some operation to each element in an iterable or to filter elements 
from an iterable while constructing a list.'''

'''The general syntax is:'''
"""
[expression for item in iterable if condition] 

Key Components:
Expression: The operation to perform on each element (optional, can just be the element itself).
For item in iterable: The loop that iterates over an iterable.
If condition: (Optional) A filter to include only certain elements. """

#Examples:

""" 1-Basic List Comprehension: """

squares = [x**2 for x in range(10)]

""" 2-print(squares) """
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

""" 3-Using a Condition: """

even_numbers = [x for x in range(20) if x % 2 == 0]

""" 3-print(even_numbers) """
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

""" 4-Applying a Function:"""

words = ["hello", "world", "python"]
capitalized = [word.upper() for word in words]

"""5-print(capitalized) """
# Output: ['HELLO', 'WORLD', 'PYTHON']

""" 6-Nested Loops: """

pairs = [(x, y) for x in range(3) for y in range(3)]

""" 7-print(pairs) """
# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

""" 8-With if-else Condition: """

processed = [x if x % 2 == 0 else -x for x in range(10)]

""" 9-print(processed)"""
# Output: [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

""" 10-Flattening a Nested List: """

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]

""" 11-print(flat_list) 
Output: [1, 2, 3, 4, 5, 6] """

""" Benefits:
Conciseness: Combines loops and conditions in a single line.
Readability: Once familiar, it's often easier to read compared to traditional loops.
Efficiency: Faster than appending items in a loop due to optimized implementation.
Let me know if you'd like to explore more examples or related features! """