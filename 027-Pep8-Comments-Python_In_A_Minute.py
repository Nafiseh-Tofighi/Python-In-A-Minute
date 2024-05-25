"""
File: 027-Pep8-Comments-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 25May2024

Description:
This script demonstrates best practices for writing comments in Python code, adhering to PEP 8 guidelines. It covers
block comments, inline comments, and docstrings. Comments are used to explain code logic, provide context, and
document important details.

Best Practices Covered:
1. Limit comment and docstring line length to 72 characters.
2. Use complete sentences starting with a capital letter.
3. Keep comments updated when code changes.

Usage:
- Review and apply the guidelines for writing effective comments in Python to enhance code readability and maintainability.
"""
"""
# Comments


> If the implementation is hard to explain, it’s a bad idea.

— The Zen of Python

1. Limit the line length of comments and docstrings to 72 characters.
2. Use complete sentences, starting with a capital letter.
3. Make sure to update comments if you change your code.
"""

# PEP 8 provides the following rules for writing block comments:

# Indent block comments to the same level as the code that they describe.
# Start each line with a # followed by a single space.
# Separate paragraphs by a line containing a single #.

for number in range(0, 10):
    # Loop over `number` ten times and print out the value of `number`
    # followed by a newline character.
    print(number, "\n")

# Calculate the solution to a quadratic equation using the quadratic
# formula.
#
# A quadratic equation has the following form:
# ax**2 + bx + c = 0
#
# There are always two solutions to a quadratic equation, x_1 and x_2.
x_1 = (-b + (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
x_2 = (-b - (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)

"""# Inline Comments
Inline comments explain a single statement in a piece of code.

* Use inline comments sparingly.
* Write inline comments on the same line as the statement they refer to.
* Separate inline comments from the statement by two or more spaces.
* Start inline comments with a # and a single space, like block comments.
* Don’t use them to explain the obvious.
"""

x = 5  # This is an inline comment

"""# Docstrings :)"""

# source: https://realpython.com/python-pep8/