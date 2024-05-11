
"""
File: 021-BitwiseOperators-Xor-Not-Shift-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script continues the overview of bitwise operators in Python with additional examples.

Usage:
- Review the table to understand each bitwise operator's symbol and explanation.
- Run the script to see additional examples of bitwise operations using these operators.
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

# Bitwise XOR
result_xor = x ^ y
print("\nBitwise XOR (^):")
print("Binary format of x:", bin(x))    # Output: 0b0101
print("Binary format of y:", bin(y))    # Output: 0b0011
print("Binary result:", bin(result_xor))# Output: 0b0110
print("Decimal result:", result_xor)    # Output: 6

# Bitwise NOT (Unary)
result_not_x = ~x
print("\nBitwise NOT (~x):")
print("Binary format of x:", bin(x))     # Output: 0b0101
print("Binary result:", bin(result_not_x))# Output: -0b110
print("Decimal result:", result_not_x)   # Output: -6

# Bitwise Left Shift
result_left_shift = x << 1
print("\nBitwise Left Shift (<<):")
print("Binary format of x:", bin(x))      # Output: 0b0101
print("Binary result:", bin(result_left_shift))# Output: 0b1010
print("Decimal result:", result_left_shift)    # Output: 10

# Bitwise Right Shift
result_right_shift = y >> 1
print("\nBitwise Right Shift (>>):")
print("Binary format of y:", bin(y))       # Output: 0b0011
print("Binary result:", bin(result_right_shift)) # Output: 0b0001
print("Decimal result:", result_right_shift)     # Output: 1

