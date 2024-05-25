"""
File: 025-Pep8-Code-Layout-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 25May2024

Description:
This script demonstrates Python code structuring and styling guidelines, focusing on class definitions, function definitions,
method organization inside classes, line length considerations, and line breaking techniques.

Best Practices Covered:
1. Surround method definitions inside classes with a single blank line.
2. Use blank lines sparingly inside functions to show clear steps.
3. Maximum line length and appropriate line breaking.

Usage:
- Run the script to understand and apply Python's recommended practices for code structure and styling.
"""

class FirstClass:
    pass


class SecondClass:
    pass


def top_level_function():
    return None

"""**Surround method definitions inside classes with a single blank line**"""

class ClassWithMethods:
    def first_method(self):
        return None

    def second_method(self):
        return None

"""**Use blank lines sparingly inside functions to show clear steps.**"""

def calculate_variance(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers = sum_numbers + number
    mean = sum_numbers / len(numbers)

    sum_squares = 0
    for number in numbers:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(numbers)

    return mean_squares - mean**2

"""**Maximum Line Length and Line Breaking**

- PEP 8 suggests lines should be limited to 79 characters.
"""

def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one

# Python will assume line continuation if code is contained within parentheses, brackets, or braces:

from package import example1, \
    example2, example3

# If it’s impossible to use implied continuation, then you can use backslashes (\) to break lines instead

total = (first_variable
         + second_variable
         - third_variable)

# total = (first_variable +
#          second_variable -
#          third_variable)

# If you need to break a line around binary operators, like + and *, then you should do so before the operator.

# source: https://realpython.com/python-pep8/

