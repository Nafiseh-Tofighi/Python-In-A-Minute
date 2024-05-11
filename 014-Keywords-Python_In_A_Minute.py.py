"""
File: 014-Keywords-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script demonstrates the usage of Python keywords and the keyword module.

Usage:
- Use the help('keywords') command to get a list of Python keywords and more help.
- Check if a string is a Python keyword using the keyword.iskeyword() function.
- Determine the total number of Python keywords using the len(keyword.kwlist) function.
"""

help('keywords')

# Output:
# Here is a list of the Python keywords.  Enter any keyword to get more help.

# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not

import keyword

print(keyword.iskeyword('in'))

# Output: True

print(keyword.iskeyword('In'))

# Output: False

print(len(keyword.kwlist))

# Output: 35

