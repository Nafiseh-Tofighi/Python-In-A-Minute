
"""
File: 020-BitwiseOperators-And-Or-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script provides an overview of bitwise operators in Python along with their explanations and examples.

Usage:
- Review the table to understand each bitwise operator's symbol and explanation.
- Run the script to see examples of bitwise operations using these operators.
"""


"""
| Operator | Example | Explanation                                                         |
|----------|---------|---------------------------------------------------------------------|
| &        | x & y   | Bitwise AND: Returns 1 if both bits at the same position are 1.     |
| \|        | x \| y   | Bitwise OR: Returns 1 if at least one bit at the same position is 1. |
| ^        | x ^ y   | Bitwise XOR: Returns 1 if the bits at the same position are different. |
| ~        | ~x      | Bitwise NOT: Flips the bits.                                      |
| <<       | x << n  | Left Shift: Shifts the bits of x to the left by n positions.       |
| >>       | x >> n  | Right Shift: Shifts the bits of x to the right by n positions.     |
"""

# Example Values
x = 5  # Binary representation: 0b0101
y = 3  # Binary representation: 0b0011

# Bitwise AND
result_and = x & y
print("Bitwise AND (&):")
print("Binary format of x:", bin(x))    # Output: 0b0101
print("Binary format of y:", bin(y))    # Output: 0b0011
print("Binary result:", bin(result_and))# Output: 0b0001
print("Decimal result:", result_and)    # Output: 1

# Bitwise OR
result_or = x | y
print("\nBitwise OR (|):")
print("Binary format of x:", bin(x))    # Output: 0b0101
print("Binary format of y:", bin(y))    # Output: 0b0011
print("Binary result:", bin(result_or)) # Output: 0b0111
print("Decimal result:", result_or)     # Output: 7

