"""
File: 026-pep8-Indentation-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 25May2024

Description:
This script illustrates Python indentation and line break guidelines as per PEP 8. It covers indentation using spaces,
preference for spaces over tabs, and various scenarios for line breaks, including alignment with opening delimiters,
hanging indents, and placing closing brackets.

Best Practices Covered:
1. Use four consecutive spaces for indentation.
2. Prefer spaces over tabs for indentation.
3. Indentation following line breaks, including alignment with opening delimiters and hanging indents.
4. Proper placement of closing brackets.

Usage:
- Review and apply the principles of indentation and line breaks to ensure code clarity and compliance with PEP 8 standards.
"""
"""
# Indentation


> There should be one—and preferably only one—obvious way to do it.

— The Zen of Python

**The key indentation rules laid out by PEP 8 are the following:**

* Use four consecutive spaces to indicate indentation.
* Prefer spaces over tabs.
"""

# You can adjust the settings in your text editor to output four spaces instead of a tab character when you press the Tab key.

"""**Indentation Following Line Breaks**

1. Alignment with the opening delimiter
2. Hanging indent

# Alignment with the opening delimiter
"""

def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one

"""N**ote that if you’re using a hanging indent, there must not be any arguments on the first line. The following example is not PEP 8 compliant:**


"""

# var = function(arg_one, arg_two,
#     arg_three, arg_four)

"""# Hanging indent"""

# def function(
#     arg_one, arg_two,
#     arg_three, arg_four):
#     return arg_one

def function(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_one

# double indent

"""**Where to Put the Closing Bracket?**"""

# Line up the closing bracket with the first non-whitespace character of the previous line:

list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]

# Line up the closing bracket with the first character of the line that starts the construct:

list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

# source: https://realpython.com/python-pep8/

