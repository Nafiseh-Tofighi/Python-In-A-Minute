
"""
File: 016-ComparisonOperators-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script provides an overview of comparison operators in Python along with their explanations and examples.

Usage:
- Review the table to understand each comparison operator's symbol and explanation.
- Run the script to see examples of comparison operations using these operators.
"""


"""

| Operator               | Symbol | Explanation                                       |
|------------------------|--------|---------------------------------------------------|
| Equal                  |   ==   | Returns True if the operands are equal.           |
| Not Equal              |   !=   | Returns True if the operands are not equal.       |
| Greater Than           |   >    | Returns True if the left operand is greater than the right operand. |
| Less Than              |   <    | Returns True if the left operand is less than the right operand.    |
| Greater Than or Equal To | >=  | Returns True if the left operand is greater than or equal to the right operand. |
| Less Than or Equal To  |  <=   | Returns True if the left operand is less than or equal to the right operand. |
"""

a = 2
b = 4

c = 7
d = 7

result = a == b
print(result)

# Output: False

result = c == d
print(result)

# Output: True

result = a != b
print(result)

# Output: True

result = c != d
print(result)

# Output: False

result = a < b
print(result)

# Output: True

result = c < d
print(result)

# Output: False

result = c <= d
print(result)

# Output: True