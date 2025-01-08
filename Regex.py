""" Regular Expressions (regex) in Python

Definition
A regular expression (regex) is a sequence of characters that defines a search pattern. 
It is used for matching, extracting, and manipulating strings based on specific patterns.

Key Features

.Powerful string searching and pattern matching.
.Flexible text manipulation (e.g., validation, replacement, extraction).
.Supported via Python's re module."""

""" Common Operations with re Module
1-Importing the Module """

import re

""" Common Functions 
re.match(): Matches the pattern at the start of the string.
re.search(): Searches the entire string for a match.
re.findall(): Returns all occurrences of the pattern as a list.
re.finditer(): Returns an iterator yielding match objects.
re.sub(): Replaces matched patterns with a specified string.
re.split(): Splits a string by occurrences of the pattern."""

#Syntax and Examples
""" 1-Matching a Pattern """
import re
pattern = r"hello"
text = "hello world"
match = re.match(pattern, text)
if match:
    print("Match found!")  # Output: Match found!

""" 2-Searching Anywhere in the String"""
search = re.search(r"world", text)
if search:
    print("Found:", search.group())  # Output: Found: world

""" 3-Finding All Matches """
numbers = re.findall(r"\\d+", "There are 3 apples and 5 oranges.")
print(numbers)  # Output: ['3', '5']

""" 4-Replacing Patterns """
result = re.sub(r"apples", "bananas", "I like apples and apples.")
print(result)  # Output: I like bananas and bananas.

""" 5-Splitting Strings """
result = re.split(r"\\s+", "Split this sentence by spaces")
print(result)  # Output: ['Split', 'this', 'sentence', 'by', 'spaces']

""" Regex Syntax and Examples

Pattern	    Matches	                                Example                        	Example Match
.	          Any character except newline	          a.b	                            Matches acb, a*b
\\d	        Any digit (0-9)	                        \\d+	                          Matches 123
\\w	        Any word character (letters, digits, _)	\\w+	                          Matches word_123
\\s	        Any whitespace	                        \\s+	                          Matches ,\\t
^	          Start of string	                        ^Hello	                        Matches Hello
$	          End of string                         	world$	                        Matches world
[]	        Any character in brackets               [aeiou]	                        Matches a, e
[^]	        Any character not in brackets	          [^aeiou]	                      Matches b, c
(pattern)	  Capturing group	                        (\\d+)-(\\d+)	                  Matches 123-456
`	`	                                                Logical OR	                    `cat
*	          0 or more repetitions	                  a*	                            Matches aaa, ``
+	          1 or more repetitions                 	a+	                            Matches aaa
?         	0 or 1 repetition	                      a?	                            Matches a, ``
{n}	        Exactly n repetitions	                  a{3}	                          Matches aaa
{n,}	      n or more repetitions	                  a{2,}	                          Matches aaa
{n,m}	      Between n and m repetitions             a{1,3}	                        Matches a, aa
"""
"""special Functions
1-Compiling Patterns For efficiency when reusing patterns."""

pattern = re.compile(r"\\d+")
result = pattern.findall("123 apples and 456 bananas")
print(result)  # Output: ['123', '456']

""" 2-Using Match Objects Match objects provide detailed information about the match. """
match = re.search(r"(\\d+)-(\\d+)", "Phone: 123-456")
if match:
    print(match.group(0))  # Output: 123-456
    print(match.group(1))  # Output: 123
    print(match.group(2))  # Output: 456
    
""" 3-Flags for Pattern Matching Flags modify the behavior of the regex engine. """
pattern = re.compile(r"hello", re.IGNORECASE)
match = pattern.match("HELLO")
if match:
    print("Match found!")  # Output: Match found!

""" 4-Backreferences in Substitution Patterns """
result = re.sub(r"(\\w+) (\\w+)", r"\\2, \\1", "Alice Smith")
print(result)  # Output: Smith, Alice

""" 5-Verbose Patterns for Readability """
pattern = re.compile(r"""\d+  # Match numbers\n     [a-z]+  # Match lowercase letters\n  
                                           """, re.VERBOSE)
result = pattern.match("123abc")
if result:
    print("Match found!")  # Output: Match found!

"""  
Applications

Validation: Check email addresses, phone numbers, or passwords.\n python\n def 
is_valid_email(email):\n pattern = r\"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0
-9-.]+$\"\n return re.match(pattern, email) is not None\n\n 
print(is_valid_email(\"example@test.com\")) # Output: True\n \n- Web Scraping: Extract
 data like URLs or tags from HTML.\n python\n urls = re.findall(r\"https?://[\\w./]+\",
   \"Visit https://example.com and http://test.com.\")\n print(urls) # Output:
     ['https://example.com', 'http://test.com']\n \n- Data Parsing: Extract meaningful data
       from logs or files.\n\n---\n\n#### Tips\n1. Use raw strings (r\"pattern\") to avoid issues with
         backslashes.\n2. Test patterns interactively with tools like regex101.\n3. For complex patterns,
           break them into multiple steps or use comments (re.VERBOSE).\n python\n pattern =
             re.compile(r\"\"\"\n ^[a-zA-Z0-9_.+-]+ # Username\n @ # @ symbol\n [a-zA-Z0-9-]+ #
               Domain name\n \\.[a-zA-Z0-9-.]+$ # Top-level domain\n \"\"\", re.VERBOSE)\n \n\nRegular
                 expressions in Python are an essential tool for text processing, offering immense power and flexibility."
"""
