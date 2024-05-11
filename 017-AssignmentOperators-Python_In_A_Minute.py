"""
File: 017-AssignmentOperators-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script provides an overview of assignment operators in Python along with their explanations and examples.

Usage:
- Review the table to understand each assignment operator's symbol, equivalent expression, and explanation.
- Run the script to see examples of assignment operations using these operators.
"""



"""

| Operator   | Example   | Equivalent to      | Explanation                                       |
|------------|-----------|---------------------|---------------------------------------------------|
| =          | x = 5     | x = 5               | Assigns the value of the right operand to the left operand. |
| +=         | x += 5    | x = x + 5           | Adds the value of the right operand to the variable and assigns the result to the variable. |
| -=         | x -= 5    | x = x - 5           | Subtracts the value of the right operand from the variable and assigns the result to the variable. |
| *=         | x *= 5    | x = x * 5           | Multiplies the variable by the value of the right operand and assigns the result to the variable. |
| /=         | x /= 5    | x = x / 5           | Divides the variable by the value of the right operand and assigns the result to the variable. |
| //=        | x //= 5   | x = x // 5          | Performs floor division on the variable by the value of the right operand and assigns the result to the variable. |
| %=         | x %= 5    | x = x % 5           | Computes the modulus of the variable with the value of the right operand and assigns the result to the variable. |
| **=        | x **= 5   | x = x ** 5          | Raises the variable to the power of the value of the right operand and assigns the result to the variable. |
"""

a = 3

a += 5

print(a)

# Output: 8

a /= 2

print(a)

# Output: 4.0

a **= 2

print(a)

# Output: 16.0