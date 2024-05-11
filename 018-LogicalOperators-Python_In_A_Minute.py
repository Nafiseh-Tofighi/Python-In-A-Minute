"""
File: 018-LogicalOperators-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script provides an overview of logical operators in Python along with their explanations and examples.

Usage:
- Review the table to understand each logical operator's symbol and explanation.
- Run the script to see examples of logical operations using these operators.
"""



"""

| Operator | Example  | Explanation                                       |
|----------|----------|---------------------------------------------------|
| and      | x and y  | Returns True if both x and y are true.           |
| or       | x or y   | Returns True if either x or y is true.           |
| not      | not x    | Returns True if x is false, and vice versa.      |

| x     | y     | x and y | x or y  |
|-------|-------|---------|---------|
| True  | True  |  True   |  True   |
| True  | False |  False  |  True   |
| False | True  |  False  |  True   |
| False | False |  False  |  False  |

| x     | not x |
|-------|-------|
| True  | False |
| False | True  |
"""

x = True
y = False

# and Operator
result_and = x and y
print("and Operator:", result_and)  # Output: False

# or Operator
result_or = x or y
print("or Operator:", result_or)  # Output: True

# not Operator
result_not_x = not x
result_not_y = not y
print("not Operator for x:", result_not_x)  # Output: False
print("not Operator for y:", result_not_y)  # Output: True

print(1 < 2 and 6 < 5)

# Output: False

print(1 < 2 or 6 < 5)

# Output: True

