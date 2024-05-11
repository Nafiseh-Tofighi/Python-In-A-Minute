"""
File: 023-OperatorPrecedence-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script demonstrates the operator precedence in Python along with examples.

Usage:
- Run the script to see how operator precedence affects the evaluation of expressions.
"""


"""

| Precedence | Operators                       | Example                     | Explanation                                       |
|------------|---------------------------------|-----------------------------|---------------------------------------------------|
| 1          | Parentheses                     | ( ), [ ]                    | Grouping expressions, overriding default precedence |
| 2          | Exponentiation                  | **                          | Highest precedence, exponentiation                |
| 3          | Unary Arithmetic                | +x, -x                      | Unary plus and minus                              |
| 4          | Multiplication, Division, Modulus | *, /, //, %               | Multiplication, division, floor division, modulus |
| 5          | Addition, Subtraction           | +, -                        | Addition and subtraction                         |
| 6          | Bitwise Shifts                  | <<, >>                      | Bitwise left shift, bitwise right shift           |
| 7          | Bitwise AND                     | &                           | Bitwise AND                                       |
| 8          | Bitwise XOR                     | ^                           | Bitwise XOR                                       |
| 9          | Bitwise OR                      | \|                          | Bitwise OR                                        |
| 10         | Comparison                      | <, <=, >, >=, ==, !=        | Comparison operators                              |
| 11         | Boolean NOT                     | not                         | Logical NOT                                       |
| 12         | Boolean AND                     | and                         | Logical AND                                       |
| 13         | Boolean OR                      | or                          | Logical OR                                        |
"""

result = 2 + 3 * 4 ** 2 / 2 - 1
print(result)  # Output: 25.0

result_with_parentheses = ((2 + 3) * 4) ** (2 / 2) - 1
print(result_with_parentheses)  # Output: 19.0

