"""
File: 022-WalrusOperator-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script demonstrates the usage of the Walrus operator in Python.

Usage:
- Run the script to see examples of how the Walrus operator (:=) can simplify code.
"""

# Example
x = 10

# Without Walrus Operator
if x > 5:
    y = x * 2
    print(y)

# With Walrus Operator
if (y := x * 2) > 5:
    print(y)

# Output:
# 20
# 20

# Example: Finding and Printing Even Numbers from a List

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without Walrus Operator
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Without Walrus Operator - Even Numbers:", even_numbers)

# With Walrus Operator
even_numbers_walrus = [num for num in numbers if (remainder := num % 2) == 0]


print("With Walrus Operator - Even Numbers:", even_numbers_walrus)
print("Last remainder calculated with Walrus Operator:", remainder)


# Output:
# Without Walrus Operator - Even Numbers: [2, 4, 6, 8, 10]
# With Walrus Operator - Even Numbers: [2, 4, 6, 8, 10]
# Last remainder calculated with Walrus Operator: 0

